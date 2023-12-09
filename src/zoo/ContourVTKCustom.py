from functools import lru_cache

import numpy as np
import pyvista as pv
import pyvistaqt
from loguru import logger
from PySide6 import QtCore as qtc
from vtk.numpy_interface import dataset_adapter as dsa
from vtkmodules.vtkCommonCore import vtkCommand, vtkPoints
from vtkmodules.vtkCommonDataModel import vtkDataObject, vtkPolyData
from vtkmodules.vtkFiltersGeneral import vtkVertexGlyphFilter
from vtkmodules.vtkInteractionWidgets import vtkCameraOrientationWidget
from vtkmodules.vtkRenderingCore import vtkPolyDataMapper

from . import config
from .ClippingBox import ClippingBox
from .GlyphActor import GlyphActor
from .H5Model import H5Model
from .LookupTable import LookupTable
from .utils import instigator_type, truncate_int8_to_int4

LARGE: float = 1e12
EPSILON: float = 1e-6

pv.global_theme.background = pv.Color("#4c4c4c")
pv.global_theme.font.color = pv.Color("white")
pv.global_theme.multi_samples = 16  # MSAA samples


class ContourVTKCustom(qtc.QAbstractItemModel):
    plotter: "InteractorLike"  # e.g. QtInteractor, vtkInteractor

    _original_extents: tuple[float] = (None,) * 6
    _plot_dataset_limits: list[float] = [-LARGE, LARGE]
    _mask_dataset_limits: list[float] = [-LARGE, LARGE]

    destroyed = qtc.Signal()

    def __init__(self, model: H5Model, controller: "ContourController") -> None:
        super().__init__()
        self.model = model
        self.controller = controller
        self.shown_first_plot: bool = False

        self.plotter = pyvistaqt.QtInteractor()
        self.plotter.AddObserver(vtkCommand.InteractionEvent, self.emit_moved_camera)
        self.create_camera_control_widget()

        self._current_widget_properties = {}

        self.clipping_box = ClippingBox(self.controller, self.plotter)

        self.lut = LookupTable()

        self.construct_timestep_data = lru_cache(maxsize=config.cache_size)(
            self.construct_timestep_data
        )  # Setting cache size at runtime requires this alternate usage

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller
        self._controller.initialized.connect(self.construct_plot_at_timestep)
        self._controller.changed_timestep.connect(self.construct_plot_at_timestep)
        self._controller.changed_glyph_size.connect(self.change_glyph_size)
        self._controller.changed_clipping_extents.connect(self.change_clipping_extents)
        self._controller.changed_exaggeration.connect(self.change_exaggeration)
        self._controller.changed_plot_dataset.connect(self.update_plot_dataset)
        self._controller.changed_mask_dataset.connect(self.update_mask_dataset)
        self._controller.changed_mask_limits.connect(self.change_mask_limits)
        self._controller.changed_colorbar_limits.connect(self.change_colorbar_limits)
        self._controller.changed_widget_property.connect(self.update_widgets)
        self._controller.changed_opacity_enabled.connect(self.change_opacity_enabled)
        self._controller.changed_mask_opacity.connect(self.change_mask_opacity)
        self._controller.changed_clip_opacity.connect(self.change_clip_opacity)

    def construct_timestep_data(self, timestep: int) -> pv.PolyData:
        logger.debug("Constructing data object...")
        coords = self.model.get_data_at_timestep(("x1", "x2", "x3"), timestep).astype(
            float
        )  # Weird bug where multiple categorical columns sometimes stay as Object type
        points = vtkPoints()
        points.SetData(dsa.numpyTovtkDataArray(coords))
        polydata = vtkPolyData()
        polydata.SetPoints(points)

        polydata.GetPointData().SetNormals(
            dsa.numpyTovtkDataArray(np.empty_like(coords))
        )  # Assign dummy normals to trick VTK into enabling (specular?) lighting
        for dataset in self.model.datasets:
            polydata.GetPointData().AddArray(
                dsa.numpyTovtkDataArray(
                    self.model.get_data_at_timestep(dataset, timestep), name=dataset
                )
            )
        polydata.GetPointData().AddArray(
            dsa.numpyTovtkDataArray(
                self.model.get_data_at_timestep(("u1", "u2", "u3"), timestep).astype(
                    float
                ),
                name="_displacement",
            )
        )
        polydata.GetPointData().SetActiveScalars(self.model.datasets[0])
        return pv.utilities.wrap(polydata)

    def construct_data_mapper(self, polydata: pv.PolyData) -> "MapperHelper":
        logger.debug("Constructing VTK mapper...")
        vertexGlyphFilter = vtkVertexGlyphFilter()
        vertexGlyphFilter.AddInputDataObject(polydata)
        vertexGlyphFilter.Update()

        mapper = PolyDataMapper()
        mapper.interpolate_before_map = False
        mapper.SetInputConnection(vertexGlyphFilter.GetOutputPort())
        mapper.lookup_table = self.lut
        mapper.MapDataArrayToVertexAttribute(
            "_disp", "_displacement", vtkDataObject.FIELD_ASSOCIATION_POINTS, -1
        )

        return mapper

    def construct_plot_at_timestep(self, timestep: int, instigator=None) -> None:
        if timestep not in self.model.timesteps:
            logger.warning(f"Timestep {timestep} not found")
            return
        logger.info(f"Constructing: {timestep}")
        # if not self.timestep:
        #     self._timestep_index = 0
        # logger.info(f"Actually: {self.timestep}")
        self.polydata = self.construct_timestep_data(timestep)
        logger.debug(f"Timestep cache: {self.construct_timestep_data.cache_info()}")
        self.polydata.GetPointData().SetActiveScalars(self.controller.plot_dataset)
        self._original_extents = self.polydata.GetPoints().GetBounds()
        self.controller.set_clipping_extents(
            self._original_extents, instigator=id(self)
        )
        self._model_size = list(
            (
                np.array(self._original_extents[1::2])
                - np.array(self._original_extents[::2])
            )
        )
        for i, dim in enumerate(self._model_size):
            if dim == 0.0:
                self._model_size[i] = self.model.grid_spacing[0]

        logger.trace(f"Size: {self._model_size}")
        logger.trace(f"Extents: {self._original_extents}")
        if np.linalg.norm(self._model_size) ** 2 <= 1000.000000:
            logger.trace(f"System span^2={np.linalg.norm(self._model_size)**2} <= 1000")
            self.length_over_threshold = False
        else:
            logger.trace(f"System span^2={np.linalg.norm(self._model_size)**2} > 1000")
            self.length_over_threshold = True

        mapper = self.construct_data_mapper(self.polydata)
        self.actor = GlyphActor(mapper, self._original_extents, self.model.grid_spacing)
        self.update_shader()

        self.plotter.add_actor(self.actor, name="primary", render=False)
        self.plotter.mapper = mapper
        self.plotter.ren_win.SetAlphaBitPlanes(True)
        self.plotter.renderer.SetUseDepthPeeling(True)
        self.plotter.renderer.SetMaximumNumberOfPeels(200)
        self.plotter.renderer.SetOcclusionRatio(0.0)
        if not self.shown_first_plot:
            self.plotter.reset_camera(render=False)
            self.shown_first_plot = True
        self.plotter.add_scalar_bar(title="primary", render=False)
        self.plotter.scalar_bars["primary"].SetVisibility(
            self.controller.widget_properties.get("scalarbar", {}).get("visible", True)
        )
        self.controller.set_clipping_extents(
            self._original_extents, instigator=id(self)
        )
        self.controller.refresh()

    def update_shader(self):
        self.change_glyph_size(self.controller.glyph_size)
        self.change_exaggeration(self.controller.exaggeration)
        self.change_mask_limits(self.controller.mask_limits)
        self.change_clipping_extents(self.controller.clipping_extents)
        self.change_opacity_enabled(self.controller.opacity_enabled)
        self.change_mask_opacity(self.controller.mask_opacity)
        self.change_clip_opacity(self.controller.clip_opacity)

    def change_glyph_size(self, glyph_size: tuple, instigator: int = None) -> None:
        self.actor.glyph_size = glyph_size

    def change_exaggeration(self, exaggeration: tuple, instigator: int = None) -> None:
        self.actor.exaggeration = exaggeration

    def change_mask_limits(self, mask_limits: tuple, instigator: int = None) -> None:
        self.actor.mask_limits = mask_limits

    @qtc.Slot(tuple, instigator_type)
    def change_clipping_extents(self, extents: tuple, instigator: int = None) -> None:
        if instigator != truncate_int8_to_int4(id(self)):
            self.actor.clipping_extents = extents

    def change_opacity_enabled(self, enabled: bool, instigator: int = None) -> None:
        if instigator != truncate_int8_to_int4(id(self)):
            self.actor.opacity_enabled = enabled

    def change_mask_opacity(self, opacity: float, instigator: int = None) -> None:
        if instigator != truncate_int8_to_int4(id(self)):
            self.actor.mask_opacity = opacity

    def change_clip_opacity(self, opacity: float, instigator: int = None) -> None:
        if instigator != truncate_int8_to_int4(id(self)):
            self.actor.clip_opacity = opacity

    def update_plot_dataset(self, plot_dataset: str, instigator: int = None) -> None:
        logger.trace(f"Updating plot dataset to {plot_dataset}...")
        self._plot_dataset_limits = list(self.polydata.get_data_range(plot_dataset))
        logger.trace(f"Detected value range of {self._plot_dataset_limits}")
        self.controller.set_colorbar_limits(
            self._plot_dataset_limits, instigator=id(self)
        )
        self.plotter.scalar_bar.SetTitle(plot_dataset)
        self.polydata.GetPointData().SetActiveScalars(plot_dataset)
        self.plotter.render()

        self.actor.GetMapper().MapDataArrayToVertexAttribute(
            "_scalar", plot_dataset, vtkDataObject.FIELD_ASSOCIATION_POINTS, -1
        )

    def update_mask_dataset(self, mask_dataset: str, instigator: int = None) -> None:
        logger.trace(f"Updating mask dataset to {mask_dataset}...")
        self._mask_dataset_limits = list(self.polydata.get_data_range(mask_dataset))
        logger.trace(f"Detected value range of {self._plot_dataset_limits}")
        self.controller.set_mask_limits(self._mask_dataset_limits, instigator=id(self))
        self.actor.GetMapper().MapDataArrayToVertexAttribute(
            "_mask_scalar", mask_dataset, vtkDataObject.FIELD_ASSOCIATION_POINTS, -1
        )

    def change_colorbar_limits(self, colorbar_limits: tuple, instigator: int) -> None:
        if colorbar_limits[0] <= colorbar_limits[1]:
            logger.trace(
                f"Colorbar limits {colorbar_limits} in correct order. Applying..."
            )
            self.plotter.update_scalar_bar_range(colorbar_limits)

    def emit_moved_camera(self, *args) -> None:
        """A method wrapping the signal emit is needed because the vtkInteractionEvent
        passes two arguments, and a signal can only handle one argument.
        """
        self.controller.moved_camera.emit(
            list(self.controller.camera_location), id(self)
        )

    def create_camera_control_widget(self) -> None:
        self.plotter.camera_widget = self.plotter.add_camera_orientation_widget()
        self.plotter.camera_widget.GetRepresentation().AnchorToLowerLeft()
        self.plotter.camera_widget.SetEnabled(
            self.controller.widget_properties.get("orientation", {}).get(
                "visible", True
            )
        )

    def toggle_clipping_box(self, enable):
        self.clipping_box.SetEnabled(enable)

    def save_image(self, filename) -> None:
        self.plotter.screenshot(filename=filename)

    def update_widgets(self, widget_properties: dict, instigator: int) -> None:
        self.plotter.camera_widget.SetEnabled(
            widget_properties.get("orientation", {}).get("visible", True)
        )
        self.plotter.scalar_bars["primary"].SetVisibility(
            widget_properties.get("scalarbar", {}).get("visible", True)
        )
        self._current_widget_properties = widget_properties


def bbox_to_model_coordinates(bbox_bounds, base_bounds):
    base_bottom_left = np.array(base_bounds[::2])
    base_top_right = np.array(base_bounds[1::2])

    size = base_top_right - base_bottom_left
    if not np.all(size):
        logger.info(f"Padding zero-length bounds with {EPSILON}")
        size += EPSILON

    bbox_mc_bl = (np.array(bbox_bounds[::2]) - base_bottom_left) / (size) - 0.5

    bbox_mc_tr = ((np.array(bbox_bounds[1::2]) - base_top_right) / (size)) + 0.5
    return (bbox_mc_bl, bbox_mc_tr)


class PolyDataMapper(vtkPolyDataMapper, pv.mapper._BaseMapper):
    pass


if __name__ == "__main__":
    import sys

    from PySide6 import QtWidgets as qtw

    app = qtw.QApplication(sys.argv)

    model = ContourVTKCustom()
    model.load_file("./test_data/kylesheartest1.h5")
    model.construct_plot_at_timestep()
    print(model.mesh)
    print(model.actor)
    print(model.actor.GetShaderProperty())
    print(model.plotter)
