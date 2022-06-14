import csv

import pandas as pd
from loguru import logger
from qtpy import QtCore as qtc
from tables import is_hdf5_file

from .utils import EXTENSIONS

THREADED = True
COMMENT_CHARACTER = "#"


class Loader(qtc.QObject):
    finished = qtc.Signal()
    rejected = qtc.Signal()
    progress = qtc.Signal(float)
    df: pd.DataFrame = None

    def __init__(self, filename) -> None:
        super().__init__()
        self.filename = filename

    def setup(self, parent) -> None:
        self.finished.connect(parent.extract)
        self.rejected.connect(parent.destroyed.emit)
        if not THREADED:
            self.load()
        else:
            self.thread = qtc.QThread()
            self.moveToThread(self.thread)
            self.thread.started.connect(self.load)

            self.finished.connect(self.thread.quit)
            self.finished.connect(self.deleteLater)

            self.rejected.connect(self.thread.quit)
            self.rejected.connect(self.deleteLater)

            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()

    def load(self) -> None:
        logger.info(f"Starting to load {self.filename}...")
        if self.filename.suffix in EXTENSIONS["h5"]:
            df = Loader.read_as_h5(self.filename)
        elif self.filename.suffix in EXTENSIONS["grid"]:
            df = Loader.read_as_grid_file(self.filename)
        elif self.filename.suffix in EXTENSIONS["known_bad"]:
            logger.debug(f"Ignoring {self.filename.suffix:5} file: {self.filename}")
            self.rejected.emit()
            return
        else:
            logger.warning(
                f"Unrecognized file extension: {self.filename.suffix} Checking directly..."
            )
            if is_hdf5_file(self.filename):
                df = Loader.read_as_h5(self.filename)
            else:
                try:  # Check if text file
                    with open(self.filename) as f:
                        f.readline()
                except Exception:
                    self.rejected.emit()
                    return
                else:
                    df = Loader.read_as_grid_file(self.filename)

        self.df = df
        self.finished.emit()

    @staticmethod
    def read_as_h5(path):
        logger.info("Reading as hdf5...")
        try:
            return pd.read_hdf(path, key="data", mode="r")
        except Exception as err:
            raise err

    @staticmethod
    def read_as_grid_file(path):
        logger.info("Reading as csv...")
        # Pre-determine delimiter and number of lines before data
        with open(path, mode="r") as f:
            skiprows = -1
            sep = "\s+"  # stackoverflow.com/a/59327911/13130795
            for i, line in enumerate(f):  # Find first data line
                skiprows += 1
                if line.strip().startswith(COMMENT_CHARACTER):
                    continue
                if line.strip().isdigit():  # Header of Emu grid file
                    logger.debug(f"Integer row found at {i}")
                    continue
                try:
                    sep = csv.Sniffer().sniff(line).delimiter
                except csv.Error:
                    continue
                else:
                    break
        logger.debug(f"Detected delimiter as {sep}")
        try:
            grid = pd.read_csv(
                path,
                skiprows=skiprows,
                sep=sep,
                skipinitialspace=True,
                index_col=False,
                comment=COMMENT_CHARACTER,
            )
            if any(grid.iloc[0].apply(lambda x: isinstance(x, str))):
                logger.debug("Detected column headers. Converting...")
                grid = grid[1:].reset_index(drop=True).rename(columns=grid.iloc[0])
            grid.columns = grid.columns.str.strip()
        except Exception as err:
            raise err
        else:
            grid["iter"] = 0
            grid["m_global"] = grid.index
            grid.set_index(["iter", "m_global"], inplace=True)
            logger.debug(grid.columns)
            if {"x", "y", "z"}.issubset(set(grid.columns)):
                logger.debug("Converting x,y,z to x1,x2,x3")
                grid = grid.rename(columns={"x": "x1", "y": "x2", "z": "x3"})
            if {"ux", "uy", "uz"}.issubset(set(grid.columns)):
                logger.debug("Converting ux,uy,uz to u1,u2,u3")
                grid = grid.rename(columns={"ux": "u1", "uy": "u2", "uz": "u3"})
            if not {"u1", "u2", "u3"}.issubset(set(grid.columns)):
                logger.debug("Adding dummy displacement columns")
                grid["u1"] = 0.0
                grid["u2"] = 0.0
                grid["u3"] = 0.0
            return grid
