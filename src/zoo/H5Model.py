from abc import abstractmethod
import typing
import pandas as pd

from qtpy import QtCore as qtc

LARGE: float = 1e12


class H5Model(qtc.QAbstractItemModel):
    plotter: "InteractorLike"  # e.g. QtInteractor, vtkInteractor
    dataset: str
    timestep_index: int
    grid_spacing: float
    exaggeration: float

    loaded_file = qtc.Signal(bool)
    changed_timestep = qtc.Signal(str)  # intended for a socket expecting a str, not int
    changed_grid_spacing = qtc.Signal(list)
    changed_exaggeration = qtc.Signal(list)
    changed_dataset = qtc.Signal(str)
    changed_clipping_extents = qtc.Signal(tuple)
    changed_contour_threshold = qtc.Signal(list)
    changed_colorbar_limits = qtc.Signal(list)

    timesteps: tuple[int] = (None,)
    datasets: tuple[str] = (None,)

    _timestep_index: int = 0
    _grid_spacing: list[float] = [0.005, 0.005, 0.005]
    _exaggeration: list[float] = [0.0, 0.0, 0.0]
    _clipping_extents: tuple[float] = (None,) * 6
    _original_extents: tuple[float] = (None,) * 6
    _contour_threshold: list[float] = [-LARGE, LARGE]
    _colorbar_limits: list[float] = [-LARGE, LARGE]
    _dataset_limits: list[float] = [-LARGE, LARGE]

    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    def load_file(self, filename) -> None:
        try:
            self.df = pd.read_hdf(filename, key="data", mode="r")
        except Exception as err:
            raise err
        else:
            self.datasets = tuple(self.df.columns)
            self.timesteps = tuple(self.df.index.levels[0])

            self._dataset = self.datasets[0]
            self.loaded_file.emit(True)

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
    def grid_spacing(self) -> list[float]:
        return list(self._grid_spacing)

    @grid_spacing.setter
    def grid_spacing(self, value: typing.Union[float, typing.Iterable[float]]) -> None:
        if isinstance(value, typing.Iterable) and len(value) == 3:
            self._grid_spacing = list(value)
        elif isinstance(value, float):
            self._grid_spacing = list([value, value, value])
        else:
            return None
        self.changed_grid_spacing.emit(self._grid_spacing)

    @property
    def exaggeration(self) -> list[float]:
        return list(self._exaggeration)

    @exaggeration.setter
    def exaggeration(self, value: typing.Union[float, typing.Iterable[float]]) -> None:
        if isinstance(value, typing.Iterable) and len(value) == 3:
            self._exaggeration = list(value)
        elif isinstance(value, float):
            self._exaggeration = list([value, value, value])
        else:
            return None
        self.changed_exaggeration.emit(self._exaggeration)

    @property
    def dataset(self) -> str:
        return self._dataset

    @dataset.setter
    def dataset(self, name: str) -> None:
        if name in self.datasets:
            self._dataset = name
        self.changed_dataset.emit(self._dataset)

    @property
    def clipping_extents(self) -> tuple[float]:
        return self._clipping_extents

    @clipping_extents.setter
    def clipping_extents(self, extents: typing.Sequence[float]) -> None:
        self._clipping_extents = tuple(extents)
        self.changed_clipping_extents.emit(self._clipping_extents)

    def replace_clipping_extents(
        self, indeces: typing.Sequence[int], values: typing.Sequence[float]
    ) -> None:
        extents = list(self._clipping_extents)
        for index, value in zip(indeces, values):
            extents[index] = (
                value if value is not None else self._original_extents[index]
            )
        self.clipping_extents = tuple(extents)

    @property
    def contour_threshold(self) -> list[float]:
        return self._contour_threshold

    @contour_threshold.setter
    def contour_threshold(self, value: typing.Iterable[float]) -> None:
        if isinstance(value, typing.Iterable) and len(value) == 2:
            self._contour_threshold = list(value)
        elif value is None:
            self._contour_threshold = [-LARGE, LARGE]
        else:
            return None
        self.changed_contour_threshold.emit(self._contour_threshold)

    @property
    def colorbar_limits(self) -> list[float]:
        return self._colorbar_limits

    @colorbar_limits.setter
    def colorbar_limits(self, value: typing.Iterable[float]) -> None:
        if isinstance(value, typing.Iterable) and len(value) == 2:
            self._colorbar_limits = list(value)
        elif value is None:
            self._colorbar_limits = self._dataset_limits
        else:
            return None
        self.changed_colorbar_limits.emit(self._colorbar_limits)
