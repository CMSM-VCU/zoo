from abc import abstractmethod
import typing
import pandas as pd

from qtpy import QtCore as qtc

LARGE: float = 1e12


class H5Model(qtc.QAbstractItemModel):
    plotter: "InteractorLike"  # e.g. QtInteractor, vtkInteractor
    plot_dataset: str
    mask_dataset: str
    timestep_index: int
    grid_spacing: float
    exaggeration: float

    plot_and_mask_same_dataset: bool = True

    loaded_file = qtc.Signal(bool)
    changed_timestep = qtc.Signal(str)  # intended for a socket expecting a str, not int
    changed_grid_spacing = qtc.Signal(list)
    changed_exaggeration = qtc.Signal(list)
    changed_plot_dataset = qtc.Signal(str)
    changed_mask_dataset = qtc.Signal(str)
    changed_clipping_extents = qtc.Signal(tuple)
    changed_mask_limits = qtc.Signal(list)
    changed_colorbar_limits = qtc.Signal(list)
    moved_camera = qtc.Signal(list)

    timesteps: typing.Tuple[int] = (None,)
    datasets: typing.Tuple[str] = (None,)

    _timestep_index: int = 0
    _grid_spacing: typing.List[float] = [0.005, 0.005, 0.005]
    _exaggeration: typing.List[float] = [0.0, 0.0, 0.0]
    _clipping_extents: typing.Tuple[float] = (None,) * 6
    _original_extents: typing.Tuple[float] = (None,) * 6
    _mask_limits: typing.List[float] = [-LARGE, LARGE]
    _colorbar_limits: typing.List[float] = [-LARGE, LARGE]
    _plot_dataset_limits: typing.List[float] = [-LARGE, LARGE]
    _mask_dataset_limits: typing.List[float] = [-LARGE, LARGE]

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

            self._plot_dataset = self.datasets[0]
            self._mask_dataset = self._plot_dataset
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
    def grid_spacing(self) -> typing.List[float]:
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
    def exaggeration(self) -> typing.List[float]:
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
    def plot_dataset(self) -> str:
        return self._plot_dataset

    @plot_dataset.setter
    def plot_dataset(self, name: str) -> None:
        if name in self.datasets:
            self._plot_dataset = name
        self.changed_plot_dataset.emit(self._plot_dataset)
        if self.plot_and_mask_same_dataset:
            self.mask_dataset = name

    @property
    def mask_dataset(self) -> str:
        return self._mask_dataset

    @mask_dataset.setter
    def mask_dataset(self, name: str) -> None:
        if name in self.datasets:
            self._mask_dataset = name
        self.changed_mask_dataset.emit(self._mask_dataset)

    @property
    def clipping_extents(self) -> typing.Tuple[float]:
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
    def mask_limits(self) -> typing.List[float]:
        return self._mask_limits

    @mask_limits.setter
    def mask_limits(self, value: typing.Iterable[float]) -> None:
        if isinstance(value, typing.Iterable) and len(value) == 2:
            self._mask_limits = list(value)
        elif value is None:
            self._mask_limits = [-LARGE, LARGE]
        else:
            return None
        self.changed_mask_limits.emit(self._mask_limits)

    @property
    def colorbar_limits(self) -> typing.List[float]:
        return self._colorbar_limits

    @colorbar_limits.setter
    def colorbar_limits(self, value: typing.Iterable[float]) -> None:
        if isinstance(value, typing.Iterable) and len(value) == 2:
            self._colorbar_limits = list(value)
        elif value is None:
            self._colorbar_limits = self._plot_dataset_limits
        else:
            return None
        self.changed_colorbar_limits.emit(self._colorbar_limits)

    @property
    @abstractmethod
    def camera_location(self) -> typing.List[typing.Tuple[float, float, float]]:
        ...

    def save_image(self, filename) -> None:
        self.plotter.screenshot(filename=filename)
