import pandas as pd
from qtpy import QtCore as qtc


class H5Model(qtc.QAbstractItemModel):
    loaded_file = qtc.Signal(bool)
    changed_timestep = qtc.Signal(str)

    _timestep_index: int = 0

    def __init__(self) -> None:
        super().__init__()
        self.timesteps = (None,)
        self.datasets = (None,)

    def load_file(self, h5_filename) -> None:
        try:
            self.df = pd.read_hdf(h5_filename, key="data", mode="r")
        except Exception as err:
            raise err
        else:
            self.loaded_file.emit(True)
            self.timesteps = tuple(self.df.index.levels[0])
            self.datasets = tuple(self.df.columns)

    @property
    def timestep_index(self) -> int:
        return self._timestep_index

    @timestep_index.setter
    def timestep_index(self, value: int) -> None:
        self._timestep_index = max(0, min(len(self.timesteps) - 1, value))
        self.changed_timestep.emit(str(self.timestep))

    @property
    def timestep(self) -> int:
        return self.timesteps[self.timestep_index]

    @timestep.setter
    def timestep(self, value: int) -> None:
        if value in self.timesteps:
            self.timestep_index = self.timesteps.index(self.timestep)
        self.changed_timestep.emit(str(self.timestep))

    @property
    def grid_spacing(self) -> float:
        return self._grid_spacing

    @grid_spacing.setter
    def grid_spacing(self, value: float) -> None:
        if value > 0.0:
            self._grid_spacing = value

    @property
    def exaggeration(self) -> float:
        return self._exaggeration

    @exaggeration.setter
    def exaggeration(self, value: float) -> None:
        if value >= 0.0:
            self._exaggeration = value

    @property
    def dataset(self) -> str:
        return self._dataset

    @dataset.setter
    def dataset(self, name: str) -> None:
        if name in self.datasets:
            self._dataset = name
