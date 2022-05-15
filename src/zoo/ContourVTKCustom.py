import typing
from functools import lru_cache
from importlib import resources

import numpy as np
import pyvista as pv
import pyvistaqt
from loguru import logger
from qtpy import QtCore as qtc
from vtk.numpy_interface import dataset_adapter as dsa
from vtkmodules.vtkCommonCore import vtkCommand, vtkPoints
from vtkmodules.vtkCommonDataModel import vtkDataObject, vtkPolyData
from vtkmodules.vtkFiltersGeneral import vtkVertexGlyphFilter
from vtkmodules.vtkInteractionWidgets import vtkCameraOrientationWidget
from vtkmodules.vtkRenderingCore import vtkActor, vtkPolyDataMapper
from vtkmodules.vtkRenderingOpenGL2 import vtkShader

# from .ContourController import ContourController

from .ClippingBox import ClippingBox
from .LookupTable import LookupTable
from .H5Model import H5Model
from .utils import truncate_int8_to_int4

LARGE: float = 1e12
EPSILON: float = 1e-6

srcGS = resources.read_text(__package__, "cubeGS.glsl")


class ContourVTKCustom(qtc.QAbstractItemModel):
    plotter: "InteractorLike"  # e.g. QtInteractor, vtkInteractor

    _original_extents: typing.Tuple[float] = (None,) * 6
    _plot_dataset_limits: typing.List[float] = [-LARGE, LARGE]
    _mask_dataset_limits: typing.List[float] = [-LARGE, LARGE]

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

    @lru_cache(maxsize=8)
    def construct_timestep_data(self, timestep: int) -> pv.PolyData:
        logger.debug("Constructing data object...")
        coords = self.model.get_data_at_timestep(("x1", "x2", "x3"), timestep)
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
                self.model.get_data_at_timestep(("u1", "u2", "u3"), timestep),
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

        mapper = pv.mapper.make_mapper(vtkPolyDataMapper)
        mapper.SetInputConnection(vertexGlyphFilter.GetOutputPort())
        mapper.SetLookupTable(self.lut)

        mapper.MapDataArrayToVertexAttribute(
            "_disp", "_displacement", vtkDataObject.FIELD_ASSOCIATION_POINTS, -1
        )

        return mapper

    def construct_plot_at_timestep(self, instigator=None) -> None:
        logger.info(f"Constructing: {self.controller.timestep}")
        # if not self.timestep:
        #     self._timestep_index = 0
        # logger.info(f"Actually: {self.timestep}")
        self.polydata = self.construct_timestep_data(self.controller.timestep)
        self.polydata.GetPointData().SetActiveScalars(self.controller.plot_dataset)
        self._original_extents = self.polydata.GetPoints().GetBounds()
        self._model_size = list(
            (
                np.array(self._original_extents[1::2])
                - np.array(self._original_extents[::2])
            )
        )
        for i, dim in enumerate(self._model_size):
            if dim == 0.0:
                self._model_size[i] = self.model.grid_spacing[0]

        logger.debug(f"Size: {self._model_size}")
        logger.debug(f"Extents: {self._original_extents}")
        if np.linalg.norm(self._model_size) ** 2 <= 1000.000000:
            logger.debug(f"System span^2={np.linalg.norm(self._model_size)**2} <= 1000")
            self.length_over_threshold = False
        else:
            logger.debug(f"System span^2={np.linalg.norm(self._model_size)**2} > 1000")
            self.length_over_threshold = True

        self.actor = vtkActor()
        mapper = self.construct_data_mapper(self.polydata)
        self.actor.SetMapper(mapper)

        self.shader_parameters = self.apply_shaders(self.actor)

        self.plotter.add_actor(self.actor, name="primary", render=False)
        self.plotter.mapper = mapper
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
        self.clipping_box.update(self._original_extents)
        self.update_plot_dataset()
        self.update_mask_dataset()

    def apply_shaders(self, actor: vtkActor):
        logger.debug("Applying shaders...")
        shader_property = actor.GetShaderProperty()

        shader_property.AddShaderReplacement(
            vtkShader.Vertex,
            "//VTK::PositionVC::Dec",
            True,
            "//VTK::PositionVC::Dec\n"
            "out vec4 vertexMCVSOutput;\n"
            "in vec3 _disp;\n"
            "out vec4 dispMCVSOutput;\n"
            "in float _scalar;\n"
            "in float _mask_scalar;\n"
            "out float scalarVSOutput;\n"
            "out float maskscalarVSOutput;\n",
            False,
        )
        shader_property.AddShaderReplacement(
            vtkShader.Vertex,
            "//VTK::PositionVC::Impl",
            True,
            "//VTK::PositionVC::Impl\n"
            "vertexMCVSOutput = vertexMC;\n"
            "dispMCVSOutput = vec4(_disp, 0.0);\n"
            "scalarVSOutput = _scalar;\n"
            "maskscalarVSOutput = _mask_scalar;\n",
            False,
        )
        shader_property.SetGeometryShaderCode(srcGS)

        shader_parameters = shader_property.GetGeometryCustomUniforms()
        shader_parameters.SetUniform4f(
            "glyph_scale", [*self.controller.glyph_size, 0.0]
        )
        shader_parameters.SetUniform4f(
            "disp_scale", [*self.controller.exaggeration, 0.0]
        )
        shader_parameters.SetUniform2f("mask_limits", self.controller.mask_limits)
        if self.length_over_threshold:
            shader_parameters.SetUniform4f("modelSize", [*self._model_size, 1.0])
            shader_parameters.SetUniform3f("bottomLeft", [-1.0, -1.0, -1.0])
            shader_parameters.SetUniform3f("topRight", [1.0, 1.0, 1.0])
            shader_parameters.SetUniform3f("epsilon_vector", [1e-3] * 3)
        else:
            shader_parameters.SetUniform4f("modelSize", [1.0, 1.0, 1.0, 1.0])
            shader_parameters.SetUniform3f("bottomLeft", self._original_extents[::2])
            shader_parameters.SetUniform3f("topRight", self._original_extents[1::2])
            shader_parameters.SetUniform3f(
                "epsilon_vector", [np.linalg.norm(self._model_size) / 1000.0] * 3
            )

        return shader_parameters

    def change_glyph_size(self, instigator: int = None) -> None:
        logger.debug(
            f"Updating shaders with grid spacing {self.controller.glyph_size}..."
        )
        self.shader_parameters.SetUniform4f(
            "glyph_scale", [*self.controller.glyph_size, 0.0]
        )

    def change_exaggeration(self, instigator: int = None) -> None:
        logger.debug(
            f"Updating shaders with exaggeration {self.controller.exaggeration}..."
        )
        self.shader_parameters.SetUniform4f(
            "disp_scale", [*self.controller.exaggeration, 0.0]
        )

    def change_mask_limits(self, instigator: int) -> None:
        logger.debug(
            f"Updating shaders with mask limits {self.controller.mask_limits}..."
        )
        self.shader_parameters.SetUniform2f("mask_limits", self.controller.mask_limits)

    def change_clipping_extents(self, instigator: int) -> None:
        extents = self.controller.clipping_extents
        logger.debug(f"Updating shaders with clipping extents {extents}...")
        if (
            extents != self.controller._applied_extents
            or self is not self.controller.contour_primary
        ):
            extents_MC = bbox_to_model_coordinates(extents, self._original_extents)

            logger.debug(
                f"Actual values sent to shaders: bottom left - {extents_MC[0]}, top right - {extents_MC[1]}"
            )
            if self.length_over_threshold:
                self.shader_parameters.SetUniform3f("bottomLeft", extents_MC[0])
                self.shader_parameters.SetUniform3f("topRight", extents_MC[1])
            else:
                self.shader_parameters.SetUniform3f("bottomLeft", extents[::2])
                self.shader_parameters.SetUniform3f("topRight", extents[1::2])
            self.controller._applied_extents = extents
            self.clipping_box.update(self.controller._applied_extents)
        else:
            logger.debug(
                f"Clipping extents {extents} same as current value. Update not applied."
            )

    def update_plot_dataset(self, instigator: int = None) -> None:
        logger.debug(f"Updating plot dataset to {self.controller.plot_dataset}...")
        self._plot_dataset_limits = list(
            self.polydata.get_data_range(self.controller.plot_dataset)
        )
        logger.debug(f"Detected value range of {self._plot_dataset_limits}")
        self.controller.set_colorbar_limits(
            self._plot_dataset_limits, instigator=id(self)
        )
        self.plotter.scalar_bar.SetTitle(self.controller.plot_dataset)
        self.polydata.GetPointData().SetActiveScalars(self.controller.plot_dataset)
        self.plotter.render()

        self.actor.GetMapper().MapDataArrayToVertexAttribute(
            "_scalar",
            self.controller.plot_dataset,
            vtkDataObject.FIELD_ASSOCIATION_POINTS,
            -1,
        )

    def update_mask_dataset(self, instigator: int = None) -> None:
        logger.debug(f"Updating mask dataset to {self.controller.mask_dataset}...")
        self._mask_dataset_limits = list(
            self.polydata.get_data_range(self.controller.mask_dataset)
        )
        logger.debug(f"Detected value range of {self._plot_dataset_limits}")
        self.controller.set_mask_limits(self._mask_dataset_limits, instigator=id(self))
        self.actor.GetMapper().MapDataArrayToVertexAttribute(
            "_mask_scalar",
            self.controller.mask_dataset,
            vtkDataObject.FIELD_ASSOCIATION_POINTS,
            -1,
        )

    def change_colorbar_limits(self, instigator: int) -> None:
        if self.controller.colorbar_limits[0] <= self.controller.colorbar_limits[1]:
            logger.debug(
                f"Colorbar limits {self.controller.colorbar_limits} in correct order. Applying..."
            )
            self.plotter.update_scalar_bar_range(self.controller.colorbar_limits)

    def emit_moved_camera(self, *args) -> None:
        """A method wrapping the signal emit is needed because the vtkInteractionEvent
        passes two arguments, and a signal can only handle one argument.
        """
        self.controller.moved_camera.emit(id(self))

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

    def update_widgets(self, instigator: int) -> None:
        self.plotter.camera_widget.SetEnabled(
            self.controller.widget_properties.get("orientation", {}).get(
                "visible", True
            )
        )
        self.plotter.scalar_bars["primary"].SetVisibility(
            self.controller.widget_properties.get("scalarbar", {}).get("visible", True)
        )
        self._current_widget_properties = self.controller.widget_properties


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


if __name__ == "__main__":
    import sys

    from qtpy import QtWidgets as qtw

    app = qtw.QApplication(sys.argv)

    model = ContourVTKCustom()
    model.load_file("./test_data/kylesheartest1.h5")
    model.construct_plot_at_timestep()
    print(model.mesh)
    print(model.actor)
    print(model.actor.GetShaderProperty())
    print(model.plotter)
