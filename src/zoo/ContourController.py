from collections.abc import Iterable, Sequence
from typing import Any

from loguru import logger
from PySide6 import QtCore as qtc

from zoo.utils import instigator_type, truncate_int8_to_int4

from .ContourVTKCustom import ContourVTKCustom

# from .H5Model import H5Model

LARGE: float = 1e12


class ContourController(qtc.QAbstractItemModel):
    plot_dataset: str
    mask_dataset: str
    timestep_index: int
    glyph_size: tuple[float]
    exaggeration: tuple[float]
    clipping_extents: tuple[float]
    mask_limits: tuple[float]
    colorbar_limits: tuple[float]
    opacity_enabled: bool
    mask_opacity: float
    clip_opacity: float

    plot_and_mask_same_dataset: bool = True

    _timestep_index: int = 0

    camera_location: list[tuple[float, float, float]]

    # fmt: off
    _glyph_size:          list[float]  = [None, None, None]
    _exaggeration:        list[float]  = [0.0, 0.0, 0.0]
    _clipping_extents:    tuple[float] = (None,) * 6
    _applied_extents:     tuple[float] = (None,) * 6
    _mask_limits:         list[float]  = [-LARGE, LARGE]
    _colorbar_limits:     list[float]  = [-LARGE, LARGE]
    _opacity_enabled: bool = False
    _mask_opacity: float = 0.0
    _clip_opacity: float = 0.0

    initialized                      = qtc.Signal(int)
    changed_timestep                 = qtc.Signal(int, instigator_type)
    changed_time                     = qtc.Signal(float, instigator_type)
    changed_glyph_size               = qtc.Signal(tuple, instigator_type)
    changed_exaggeration             = qtc.Signal(tuple, instigator_type)
    changed_plot_dataset             = qtc.Signal(str, instigator_type)
    changed_mask_dataset             = qtc.Signal(str, instigator_type)
    changed_clipping_extents         = qtc.Signal(tuple, instigator_type)
    changed_mask_limits              = qtc.Signal(tuple, instigator_type)
    changed_colorbar_limits          = qtc.Signal(tuple, instigator_type)
    changed_widget_property          = qtc.Signal(dict, instigator_type)
    changed_opacity_enabled          = qtc.Signal(bool, instigator_type)
    changed_mask_opacity             = qtc.Signal(float, instigator_type)
    changed_clip_opacity             = qtc.Signal(float, instigator_type)

    moved_camera                     = qtc.Signal(list, instigator_type)
    # fmt: on

    def __init__(self, model: "H5Model") -> None:
        super().__init__()
        self.model = model
        self.model.loaded_file.connect(self.initialize)

        self.widget_properties = {}
        self.contour_primary = ContourVTKCustom(model=self.model, controller=self)
        self.contours = [
            self.contour_primary,
        ]
        self.plotter = self.contour_primary.plotter
        self.lut = self.contour_primary.lut
        self.toggle_clipping_box = self.contour_primary.toggle_clipping_box
        self.save_image = self.contour_primary.save_image
        self.moved_camera.connect(self.distribute_camera_location)

    def initialize(self):
        self._timestep_index = 0
        self._plot_dataset = self.model.datasets[0]
        self._mask_dataset = self._plot_dataset
        self._glyph_size = self.model.grid_spacing

        self.initialized.emit(self.timestep)

    def refresh(self):
        # self.changed_timestep.emit(self.timestep, None)   # Nope! Infinite loop
        self.changed_time.emit(self.time, None)
        self.changed_glyph_size.emit(self.glyph_size, None)
        self.changed_exaggeration.emit(self.exaggeration, None)
        self.changed_plot_dataset.emit(self.plot_dataset, None)
        self.changed_mask_dataset.emit(self.mask_dataset, None)
        self.changed_clipping_extents.emit(self.clipping_extents, None)
        self.changed_mask_limits.emit(self.mask_limits, None)
        self.changed_colorbar_limits.emit(self.colorbar_limits, None)
        self.changed_widget_property.emit(self.widget_properties, None)
        self.changed_opacity_enabled.emit(self.opacity_enabled, None)
        self.changed_mask_opacity.emit(self.mask_opacity, None)
        self.changed_clip_opacity.emit(self.clip_opacity, None)

    # @property
    # def plotter(self):
    #     return self.contour.plotter

    @property
    def timestep_index(self) -> int:
        return self._timestep_index

    def set_timestep_index(self, value: int, instigator: int) -> None:
        logger.debug(f"Setting timestep index to {value}...")
        value %= len(self.model.timesteps)
        self._timestep_index = max(0, min(len(self.model.timesteps) - 1, value))
        self.changed_timestep.emit(self.timestep, instigator)
        self.changed_time.emit(self.time, instigator)

    @property
    def timestep(self) -> int:
        return self.model.timesteps[self.timestep_index]

    def set_timestep(self, value: int, instigator: int) -> None:
        logger.debug(f"Setting timestep to {value}...")
        if value in self.model.timesteps:
            self.set_timestep_index(
                self.model.timesteps.index(value), instigator=instigator
            )
        else:
            logger.warning(f"{value} not found in timesteps")
            return
        self.changed_timestep.emit(self.timestep, instigator)
        self.changed_time.emit(self.time, instigator)

    def increment_timestep(self, instigator: int) -> None:
        self.set_timestep_index(self.timestep_index + 1, instigator=instigator)

    def decrement_timestep(self, instigator: int) -> None:
        self.set_timestep_index(self.timestep_index - 1, instigator=instigator)

    def first_timestep(self, instigator: int) -> None:
        self.set_timestep_index(0, instigator=instigator)

    def last_timestep(self, instigator: int) -> None:
        self.set_timestep_index(-1, instigator=instigator)

    @property
    def time(self) -> float:
        # TODO: Expand the list of possible time column names
        if "timex" in self.model.datasets:
            return self.model.get_data_at_timestep("timex", self.timestep)[0]
        else:
            return -1.0

    @property
    def glyph_size(self) -> tuple[float]:
        return tuple(self._glyph_size)

    def set_glyph_size(self, value: float | Iterable[float], instigator: int) -> None:
        logger.debug(f"Setting grid spacing index to {value}...")
        if isinstance(value, Iterable) and len(value) == 3:
            self._glyph_size = list(value)
        elif isinstance(value, float):
            self._glyph_size = [value, value, value]
        else:
            logger.warning(f"Bad grid spacing value: {value}")
            return
        self.changed_glyph_size.emit(self.glyph_size, instigator)

    @property
    def exaggeration(self) -> tuple[float]:
        return tuple(self._exaggeration)

    def set_exaggeration(self, value: float | Iterable[float], instigator: int) -> None:
        logger.debug(f"Setting exaggeration to {value}...")
        if isinstance(value, Iterable) and len(value) == 3:
            self._exaggeration = list(value)
        elif isinstance(value, float):
            self._exaggeration = [value, value, value]
        else:
            logger.warning(f"Bad exaggeration value: {value}")
            return
        self.changed_exaggeration.emit(self.exaggeration, instigator)

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
        self.changed_plot_dataset.emit(self.plot_dataset, instigator)
        if self.plot_and_mask_same_dataset:
            self.set_mask_dataset(name, instigator=id(self))

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
        self.changed_mask_dataset.emit(self.mask_dataset, instigator)

    @property
    def clipping_extents(self) -> tuple[float]:
        return self._clipping_extents

    def set_clipping_extents(self, extents: Sequence[float], instigator: int) -> None:
        logger.debug(f"Setting clipping extents to {extents}...")
        self._clipping_extents = tuple(extents)
        self.changed_clipping_extents.emit(self.clipping_extents, instigator)

    def replace_clipping_extents(
        self,
        indeces: Sequence[int],
        values: Sequence[float],
        instigator: int,
    ) -> None:
        logger.debug(f"Replacing clipping extents {indeces} with {values}...")
        extents = list(self._clipping_extents)
        for index, value in zip(indeces, values):
            extents[index] = (
                value
                if value is not None
                else self.contour_primary._original_extents[index]
            )
        self.set_clipping_extents(tuple(extents), instigator)

    @property
    def mask_limits(self) -> tuple[float]:
        return tuple(self._mask_limits)

    def set_mask_limits(self, value: Iterable[float], instigator: int) -> None:
        logger.debug(f"Externally setting mask limits to {value}...")
        if isinstance(value, Iterable) and len(value) == 2:
            self._mask_limits = list(value)
        elif value is None:
            self._mask_limits = [-LARGE, LARGE]
        else:
            logger.warning(f"Bad mask limits value: {value}")
            return
        self.changed_mask_limits.emit(self.mask_limits, instigator)

    @property
    def colorbar_limits(self) -> tuple[float]:
        return tuple(self._colorbar_limits)

    def set_colorbar_limits(self, value: Iterable[float], instigator: int) -> None:
        logger.debug(f"Externally setting colorbar limits to {value}...")
        if isinstance(value, Iterable) and len(value) == 2:
            self._colorbar_limits = list(value)
        elif value is None:
            self._colorbar_limits = self.contour_primary._plot_dataset_limits
        else:
            logger.warning(f"Bad colorbar limits value: {value}")
            return
        self.changed_colorbar_limits.emit(self.colorbar_limits, instigator)

    @property
    def opacity_enabled(self) -> bool:
        return self._opacity_enabled

    def set_opacity_enabled(self, enabled: bool, instigator: int) -> None:
        self._opacity_enabled = enabled
        self.changed_opacity_enabled.emit(self.opacity_enabled, instigator)

    @property
    def mask_opacity(self) -> float:
        return self._mask_opacity

    def set_mask_opacity(self, value: float, instigator: int) -> None:
        _value = max(min(value, 1.0), 0.0)  # clamped
        self._mask_opacity = _value
        self.changed_mask_opacity.emit(self.mask_opacity, instigator)

    @property
    def clip_opacity(self) -> float:
        return self._clip_opacity

    def set_clip_opacity(self, value: float, instigator: int) -> None:
        _value = max(min(value, 1.0), 0.0)  # clamped
        self._clip_opacity = _value
        self.changed_clip_opacity.emit(self.clip_opacity, instigator)

    @property
    def camera_location(self) -> list[tuple[float, float, float]]:
        return list(self.contour_primary.plotter.camera_position)

    @camera_location.setter
    def camera_location(self, location: list[tuple[float, float, float]]) -> None:
        for contour in self.contours:
            contour.plotter.camera_position = location

    def distribute_camera_location(
        self, camera_location: list, instigator: int
    ) -> None:
        for contour in self.contours:
            if instigator != truncate_int8_to_int4(id(contour)):
                contour.plotter.camera_position = camera_location

    @property
    def background_color(self) -> list[float]:
        return self.contour_primary.plotter.background_color.float_rgb

    @background_color.setter
    def background_color(self, color: Sequence[float]) -> None:
        for contour in self.contours:
            contour.plotter.set_background(color)

    @property
    def widgets(self) -> dict:
        return {
            "scalarbar": self.plotter.scalar_bars["primary"],
            "orientation": self.plotter.camera_widget,
        }

    def set_widget_property(
        self, widget: str, property_: str, value: Any, instigator: int
    ) -> None:
        widget = widget.lower()
        property_ = property_.lower()
        if widget not in self.widget_properties:
            self.widget_properties[widget] = {}
        self.widget_properties[widget][property_] = value
        self.changed_widget_property.emit(self.widget_properties, instigator)

    def add_contour(self, contour) -> None:
        if contour not in self.contours:
            self.contours.append(contour)
            contour.controller = self
