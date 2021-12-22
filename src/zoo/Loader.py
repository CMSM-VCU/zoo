import pandas as pd
from loguru import logger
from qtpy import QtCore as qtc

H5_FILE_EXTENSIONS = (".h5", ".hdf5")
GRID_FILE_EXTENSIONS = (".csv", ".grid")


class Loader(qtc.QObject):
    finished = qtc.Signal()
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
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

    def load(self) -> None:
        logger.info(f"Starting to load {self.filename}...")
        if self.filename.suffix in H5_FILE_EXTENSIONS:
            logger.info("Reading as hdf5...")
            try:
                df = pd.read_hdf(self.filename, key="data", mode="r")
            except Exception as err:
                raise err
        elif self.filename.suffix in GRID_FILE_EXTENSIONS:
            logger.info("Reading as csv...")
            # Increase robustness by pre-determining delimiter
            # Currently limited to comma or whitespace
            with open(self.filename, mode="r") as f:
                _ = f.readline()
                sep = (
                    "," if "," in f.readline() else "\s+"
                )  # stackoverflow.com/a/59327911/13130795
            logger.debug(f"Detected delimiter as {sep}")
            try:
                grid = pd.read_csv(
                    self.filename,
                    skiprows=1,
                    names=["x1", "x2", "x3", "material"],
                    sep=sep,
                    skipinitialspace=True,
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
                df = grid
        else:
            logger.warning(f"Unrecognized file extension: {self.filename.suffix}")
            df = None
        self.df = df
        self.finished.emit()
