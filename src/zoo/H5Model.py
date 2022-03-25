import typing
from abc import abstractmethod

import pandas as pd
from loguru import logger
from qtpy import QtCore as qtc
from scipy.spatial import cKDTree
from scipy.stats import mode

from .Loader import Loader

LARGE: float = 1e12


class H5Model(qtc.QAbstractItemModel):
    grid_spacing: typing.Tuple[float]

    loaded_file = qtc.Signal(bool)

    timesteps: typing.Tuple[int] = (None,)
    datasets: typing.Tuple[str] = (None,)

    def __init__(self, filename=None) -> None:
        super().__init__()
        if filename:
            self.load_file(filename)

    def load_file(self, filename) -> None:
        self.loader = Loader(filename)
        self.loader.setup(parent=self)

    def extract(self) -> None:
        self.df = self.loader.df
        if self.df is None:
            return

        self.datasets = tuple(self.df.columns)
        try:
            self.timesteps = tuple(self.df.index.levels[0])
        except:
            self.timesteps = tuple(self.df.index.unique())

        self.grid_spacing = self.guess_grid_spacing()
        self.loaded_file.emit(True)
        logger.info(f"Finished loading {self.loader.filename}")
        self.loader.df = None  # Allow memory to be released later

    def guess_grid_spacing(self) -> typing.Tuple[float, float, float]:
        coords = self.df.loc[self.timesteps[0], ["x1", "x2", "x3"]]
        tree = cKDTree(coords)
        distances = tree.query(coords, k=2, workers=-1)[0][:, 1]
        return (mode(distances)[0][0],) * 3
