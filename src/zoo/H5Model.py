from collections.abc import Sequence

import numpy as np
from loguru import logger
from PySide6 import QtCore as qtc
from scipy.spatial import KDTree
from scipy.stats import mode

from .Loader import Loader

LARGE: float = 1e12


class H5Model(qtc.QAbstractItemModel):
    grid_spacing: tuple[float]

    loaded_file = qtc.Signal(bool)

    timesteps: tuple[int] = (None,)
    datasets: tuple[str] = (None,)

    def __init__(self, filename=None) -> None:
        super().__init__()
        if filename:
            self.load_file(filename)

    def load_file(self, filename) -> None:
        self.loader = Loader(filename)
        self.loader.setup(parent=self)

    def extract(self) -> None:
        self._df = self.loader.df
        if self._df is None:
            return

        self.datasets = tuple(self._df.columns)
        try:
            self.timesteps = tuple(self._df.index.levels[0])
        except:
            self.timesteps = tuple(self._df.index.unique())

        self.grid_spacing = self.guess_grid_spacing()
        self.loaded_file.emit(True)
        logger.info(f"Finished loading {self.loader.filename}")
        self.loader.df = None  # Allow memory to be released later

    def guess_grid_spacing(self) -> tuple[float, float, float]:
        coords = self.get_data_at_timestep(["x1", "x2", "x3"], self.timesteps[0])
        tree = KDTree(coords)
        distances = tree.query(coords, k=2, workers=-1)[0][:, 1]
        return (mode(distances, keepdims=False)[0],) * 3
        # keepdims for compatibility with scipy<1.11

    def get_data_at_timestep(
        self, dataset: str | Sequence[str], timestep: int
    ) -> np.ndarray:
        return self._df.loc[timestep, dataset].to_numpy()
