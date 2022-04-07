import typing

from loguru import logger
from qtpy import QtCore as qtc

from .ContourVTKCustom import ContourVTKCustom

# from .H5Model import H5Model

LARGE: float = 1e12


class ContourController(qtc.QAbstractItemModel):
    plot_dataset: str
    mask_dataset: str
    timestep_index: int
    glyph_size: typing.Tuple[float]
    exaggeration: typing.Tuple[float]
    clipping_extents: typing.Tuple[float]
    mask_limits: typing.Tuple[float]
    colorbar_limits: typing.Tuple[float]

    plot_and_mask_same_dataset: bool = True

    _timestep_index: int = 0

    camera_location: typing.List[typing.Tuple[float, float, float]]

    # fmt: off
    _glyph_size:          typing.List[float]  = [None, None, None]
    _exaggeration:        typing.List[float]  = [0.0, 0.0, 0.0]
    _clipping_extents:    typing.Tuple[float] = (None,) * 6
    _applied_extents:     typing.Tuple[float] = (None,) * 6
    _mask_limits:         typing.List[float]  = [-LARGE, LARGE]
    _colorbar_limits:     typing.List[float]  = [-LARGE, LARGE]

    initialized                      = qtc.Signal()
    changed_timestep                 = qtc.Signal(int)
    changed_glyph_size               = qtc.Signal(int)
    changed_exaggeration             = qtc.Signal(int)
    changed_plot_dataset             = qtc.Signal(int)
    changed_mask_dataset             = qtc.Signal(int)
    changed_clipping_extents         = qtc.Signal(tuple)
    changed_mask_limits              = qtc.Signal(list)
    changed_colorbar_limits          = qtc.Signal(list)

    program_changed_clipping_extents = qtc.Signal(tuple)
    program_changed_mask_limits      = qtc.Signal(list)
    program_changed_colorbar_limits  = qtc.Signal(list)

    moved_camera                     = qtc.Signal(list)
    # fmt: on

    def __init__(self, model: "H5Model") -> None:
        super().__init__()
        self.model = model
        self.model.loaded_file.connect(self.initialize)

        self.contour = ContourVTKCustom(model=self.model, controller=self)
        self.plotter = self.contour.plotter
        self.lut = self.contour.lut
        self.toggle_clipping_box = self.contour.toggle_clipping_box
        self.replace_clipping_extents = self.contour.replace_clipping_extents
        self.save_image = self.contour.save_image

    def initialize(self):
        self._timestep_index = 0
        self._plot_dataset = self.model.datasets[0]
        self._mask_dataset = self._plot_dataset
        self._glyph_size = self.model.grid_spacing

        self.initialized.emit()

    # @property
    # def plotter(self):
    #     return self.contour.plotter

    @property
    def timestep_index(self) -> int:
        return self._timestep_index

    def set_timestep_index(self, value: int, instigator: int) -> None:
        logger.debug(f"Setting timestep index to {value}...")
        self._timestep_index = max(0, min(len(self.model.timesteps) - 1, value))
        self.changed_timestep.emit(instigator)

    @property
    def timestep(self) -> int:
        return self.model.timesteps[self.timestep_index]

    def set_timestep(self, value: int, instigator: int) -> None:
        logger.debug(f"Setting timestep to {value}...")
        if value in self.model.timesteps:
            self.timestep_index = self.model.timesteps.index(self.timestep)
        else:
            logger.warning(f"{value} not found in timesteps")
            return
        self.changed_timestep.emit(instigator)

    @property
    def time(self) -> float:
        # TODO: Expand the list of possible time column names
        if "timex" in self.model.datasets:
            return self.model.get_data_at_timestep("timex", self.timestep)[0]
        else:
            return None

    @property
    def glyph_size(self) -> typing.List[float]:
        return list(self._glyph_size)

    def set_glyph_size(
        self, value: typing.Union[float, typing.Iterable[float]], instigator: int
    ) -> None:
        logger.debug(f"Setting grid spacing index to {value}...")
        if isinstance(value, typing.Iterable) and len(value) == 3:
            self._glyph_size = list(value)
        elif isinstance(value, float):
            self._glyph_size = [value, value, value]
        else:
            logger.warning(f"Bad grid spacing value: {value}")
            return
        self.changed_glyph_size.emit(instigator)

    @property
    def exaggeration(self) -> typing.List[float]:
        return list(self._exaggeration)

    def set_exaggeration(
        self, value: typing.Union[float, typing.Iterable[float]], instigator: int
    ) -> None:
        logger.debug(f"Setting exaggeration to {value}...")
        if isinstance(value, typing.Iterable) and len(value) == 3:
            self._exaggeration = list(value)
        elif isinstance(value, float):
            self._exaggeration = [value, value, value]
        else:
            logger.warning(f"Bad exaggeration value: {value}")
            return
        self.changed_exaggeration.emit(instigator)

    @property
    def plot_dataset(self) -> str:
        return self._plot_dataset

    def set_plot_dataset(self, name: str, instigator: int) -> None:
        logger.debug(f"Setting plot dataset to {name}...")
        if name in self.model.datasets:
            self._plot_dataset = name
        else:
            logger.warning(f"{name} not found in datasets")
            return
        self.changed_plot_dataset.emit(instigator)
        if self.plot_and_mask_same_dataset:
            self.set_mask_dataset(name, instigator)

    @property
    def mask_dataset(self) -> str:
        return self._mask_dataset

    def set_mask_dataset(self, name: str, instigator: int) -> None:
        logger.debug(f"Setting mask dataset to {name}...")
        if name in self.model.datasets:
            self._mask_dataset = name
        else:
            logger.warning(f"{name} not found in datasets")
            return
        self.changed_mask_dataset.emit(instigator)

    @property
    def clipping_extents(self) -> typing.Tuple[float]:
        return self._clipping_extents

    @clipping_extents.setter
    def clipping_extents(self, extents: typing.Sequence[float]) -> None:
        logger.debug(f"Externally setting clipping extents to {extents}...")
        self.contour._set_clipping_extents(extents=extents, external=True)

    @property
    def mask_limits(self) -> typing.List[float]:
        return self._mask_limits

    @mask_limits.setter
    def mask_limits(self, value: typing.Iterable[float]) -> None:
        logger.debug(f"Externally setting mask limits to {value}...")
        self.contour._set_mask_limits(value=value, external=True)

    @property
    def colorbar_limits(self) -> typing.List[float]:
        return self._colorbar_limits

    @colorbar_limits.setter
    def colorbar_limits(self, value: typing.Iterable[float]) -> None:
        logger.debug(f"Externally setting colorbar limits to {value}...")
        self.contour._set_colorbar_limits(value=value, external=True)

    @property
    def camera_location(self) -> typing.List[typing.Tuple[float, float, float]]:
        return self.contour.plotter.camera_position

    @camera_location.setter
    def camera_location(
        self, location: typing.List[typing.Tuple[float, float, float]]
    ) -> None:
        self.contour.plotter.camera_position = location

    @property
    def background_color(self) -> typing.List[float]:
        return self.contour.plotter.background_color

    @background_color.setter
    def background_color(self, color: typing.Sequence[float]) -> None:
        self.contour.plotter.set_background(color)
