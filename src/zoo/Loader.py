import csv

import pandas as pd
from loguru import logger
from PySide6 import QtCore as qtc
from tables import is_hdf5_file
from tables.exceptions import HDF5ExtError

from .utils import EXTENSIONS

THREADED = True  # TODO: Expose as command line option
DEFLATE_DATA = True  # TODO: Expose as command line option
COMMENT_CHARACTER = "#"
DEFAULT_COLUMNS = {0: "x1", 1: "x2", 2: "x3", 3: "material"}


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

        if df is None:
            logger.warning(f"Extracted no data from {self.filename}, rejecting...")
            self.rejected.emit()
            return

        self.df = df
        self.finished.emit()

    @staticmethod
    def read_as_h5(path):
        logger.info("Reading as hdf5...")
        try:
            df = pd.read_hdf(path, key="data", mode="r")
        except MemoryError as err:
            logger.critical(f"Out of memory: {path}")
            return None
        except HDF5ExtError as err:
            logger.warning(f"Failed to read HDF5: {path} - Possibly corrupted")
            return None
        except Exception as err:
            logger.warning(f"Error occured while reading: {path}")
            logger.opt(raw=True).warning(f"{err}")
            return None

        if DEFLATE_DATA:
            logger.info("Converting to categorical datasets...")
            _size_before = max(int(df.memory_usage(deep=True).sum() / 1e6), 1)

            eligible = df.nunique() < len(df) / 10
            eligible = list(eligible[eligible].index)
            df[eligible] = df[eligible].astype("category")

            _size_after = max(int(df.memory_usage(deep=True).sum() / 1e6), 1)
            _percent = int((1 - (_size_after / _size_before)) * 100)
            logger.debug(
                f"Size reduction: {_size_before}->{_size_after} MB ({_percent}% reduction)"
            )

        return df

    @staticmethod
    def read_as_grid_file(path):
        logger.info("Reading as csv...")
        skiprows, sep = Loader.preprocess_csv(path)
        try:
            grid = pd.read_csv(
                path,
                skiprows=skiprows,
                sep=sep,
                skipinitialspace=True,
                index_col=False,
                comment=COMMENT_CHARACTER,
                header=None,
            )
            if grid.isnull().values.any():
                logger.warning(f"Ignoring NaN values found in {path}")
                grid = grid.dropna(how="any")
        except Exception as err:
            raise err
        else:
            grid = Loader.postprocess_csv(grid)
            return grid

    @staticmethod
    def preprocess_csv(path):
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
        return skiprows, sep

    @staticmethod
    def postprocess_csv(grid):
        # Figure out headers
        if any(grid.iloc[0].apply(lambda x: isinstance(x, str))):
            logger.debug("Detected column headers. Converting...")
            grid = (
                grid[1:]
                .reset_index(drop=True)
                .rename(columns=grid.iloc[0])
                .astype(float)
            )
        else:
            logger.debug("No column headers. Assuming defaults...")
            grid = grid.rename(
                columns=lambda x: DEFAULT_COLUMNS[x]
                if x in DEFAULT_COLUMNS.keys()
                else str(x)
            )
        grid.columns = grid.columns.str.strip()
        logger.debug(grid.columns)
        # Add indices
        grid["iter"] = 0
        grid["m_global"] = grid.index
        grid.set_index(["iter", "m_global"], inplace=True)
        # Switch to required column names
        if {"x", "y", "z"}.issubset(set(grid.columns)):
            logger.debug("Converting x,y,z to x1,x2,x3")
            grid = grid.rename(columns={"x": "x1", "y": "x2", "z": "x3"})
        if {"ux", "uy", "uz"}.issubset(set(grid.columns)):
            logger.debug("Converting ux,uy,uz to u1,u2,u3")
            grid = grid.rename(columns={"ux": "u1", "uy": "u2", "uz": "u3"})
        # Add missing columns
        if not {"u1", "u2", "u3"}.issubset(set(grid.columns)):
            logger.debug("Adding dummy displacement columns")
            grid["u1"] = 0.0
            grid["u2"] = 0.0
            grid["u3"] = 0.0
        return grid
