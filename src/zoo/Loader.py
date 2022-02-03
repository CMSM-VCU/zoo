import pandas as pd
from loguru import logger
from qtpy import QtCore as qtc

from .utils import EXTENSIONS


class Loader(qtc.QObject):
    finished = qtc.Signal()
    rejected = qtc.Signal()
    progress = qtc.Signal(float)
    df: pd.DataFrame = None

    def __init__(self, filename) -> None:
        super().__init__()
        self.filename = filename

    def setup(self, parent) -> None:
        self.thread = qtc.QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.load)

        self.finished.connect(parent.extract)
        self.finished.connect(self.thread.quit)
        self.finished.connect(self.deleteLater)

        self.rejected.connect(self.thread.quit)
        self.rejected.connect(self.deleteLater)

        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

    def load(self) -> None:
        logger.info(f"Starting to load {self.filename}...")
        if self.filename.suffix in EXTENSIONS["h5"]:
            logger.info("Reading as hdf5...")
            try:
                df = pd.read_hdf(self.filename, key="data", mode="r")
            except Exception as err:
                raise err
        elif self.filename.suffix in EXTENSIONS["grid"]:
            logger.info("Reading as csv...")
            df = Loader.read_as_grid_file(self.filename)
        else:
            logger.warning(f"Unrecognized file extension: {self.filename.suffix}")
            self.rejected.emit()
            return

        self.df = df
        self.finished.emit()

    @staticmethod
    def read_as_grid_file(path):
        # Increase robustness by pre-determining delimiter
        # Currently limited to comma or whitespace
        with open(path, mode="r") as f:
            _ = f.readline()
            sep = (
                "," if "," in f.readline() else "\s+"
            )  # stackoverflow.com/a/59327911/13130795
        logger.debug(f"Detected delimiter as {sep}")
        try:
            grid = pd.read_csv(
                path,
                skiprows=1,
                names=["x1", "x2", "x3", "material"],
                sep=sep,
                skipinitialspace=True,
                usecols=[0, 1, 2, 3],
            )
        except Exception as err:
            raise err
        else:
            grid["iter"] = 0
            grid["m_global"] = grid.index
            grid.set_index(["iter", "m_global"], inplace=True)
            grid["u1"] = 0.0
            grid["u2"] = 0.0
            grid["u3"] = 0.0
            return grid
