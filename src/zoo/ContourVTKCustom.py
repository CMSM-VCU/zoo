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

from .ClippingBox import ClippingBox
from .LookupTable import LookupTable
from .H5Model import H5Model

LARGE: float = 1e12
EPSILON: float = 1e-6

srcGS = resources.read_text(__package__, "cubeGS.glsl")


class ContourVTKCustom(qtc.QAbstractItemModel):
    plotter: "InteractorLike"  # e.g. QtInteractor, vtkInteractor
    plot_dataset: str
    mask_dataset: str
    timestep_index: int
    glyph_size: float
    exaggeration: float

    plot_and_mask_same_dataset: bool = True

    changed_timestep = qtc.Signal(str)  # intended for a socket expecting a str, not int
    changed_grid_spacing = qtc.Signal(list)
    changed_exaggeration = qtc.Signal(list)
    changed_plot_dataset = qtc.Signal(str)
    changed_mask_dataset = qtc.Signal(str)
    changed_clipping_extents = qtc.Signal(tuple)
    changed_mask_limits = qtc.Signal(list)
    changed_colorbar_limits = qtc.Signal(list)
    program_changed_clipping_extents = qtc.Signal(tuple)
    program_changed_mask_limits = qtc.Signal(list)
    program_changed_colorbar_limits = qtc.Signal(list)
    moved_camera = qtc.Signal(list)
    destroyed = qtc.Signal()

    _timestep_index: int = 0
    _glyph_size: typing.List[float] = [None, None, None]
    _exaggeration: typing.List[float] = [0.0, 0.0, 0.0]
    _clipping_extents: typing.Tuple[float] = (None,) * 6
    _original_extents: typing.Tuple[float] = (None,) * 6
    _applied_extents: typing.Tuple[float] = (None,) * 6
    _mask_limits: typing.List[float] = [-LARGE, LARGE]
    _colorbar_limits: typing.List[float] = [-LARGE, LARGE]
    _plot_dataset_limits: typing.List[float] = [-LARGE, LARGE]
    _mask_dataset_limits: typing.List[float] = [-LARGE, LARGE]

    def __init__(self, model: H5Model) -> None:
        super().__init__()
        self.model = model
        self.shown_first_plot: bool = False

        self.plotter = pyvistaqt.QtInteractor()
        self.plotter.AddObserver(vtkCommand.InteractionEvent, self.emit_moved_camera)
        self.create_camera_control_widget()

        self.model.loaded_file.connect(self.initialize)
        self.changed_timestep.connect(self.construct_plot_at_timestep)
        self.changed_grid_spacing.connect(self.change_grid_spacing)
        self.changed_clipping_extents.connect(self.change_clipping_extents)
        self.changed_exaggeration.connect(self.change_exaggeration)
        self.changed_plot_dataset.connect(self.update_plot_dataset)
        self.changed_mask_dataset.connect(self.update_mask_dataset)
        self.changed_mask_limits.connect(self.change_mask_limits)
        self.changed_colorbar_limits.connect(self.change_colorbar_limits)

        self.clipping_box = ClippingBox(self, self.plotter)

        self.lut = LookupTable()

    @property
    def camera_location(self) -> typing.List[typing.Tuple[float, float, float]]:
        return self.plotter.camera_position

    @camera_location.setter
    def camera_location(
        self, location: typing.List[typing.Tuple[float, float, float]]
    ) -> None:
        self.plotter.camera_position = location

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

    def initialize(self) -> None:
        model = self.model
        self._timestep_index = 0
        self._plot_dataset = model.datasets[0]
        self._mask_dataset = self._plot_dataset
        self._glyph_size = model.grid_spacing

        self.construct_plot_at_timestep()

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

    def construct_plot_at_timestep(self, _=None) -> None:
        logger.info(f"Constructing: {self.timestep}")
        if not self.timestep:
            self._timestep_index = 0
        logger.info(f"Actually: {self.timestep}")
        self.polydata = self.construct_timestep_data(self.timestep)
        self.polydata.GetPointData().SetActiveScalars(self.plot_dataset)
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
        self.plotter.add_scalar_bar(render=False)
        self._set_clipping_extents(self._original_extents)
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
        shader_parameters.SetUniform4f("glyph_scale", [*self.glyph_size, 0.0])
        shader_parameters.SetUniform4f("disp_scale", [*self.exaggeration, 0.0])
        shader_parameters.SetUniform2f("mask_limits", self.mask_limits)
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

    def change_grid_spacing(self, _=None) -> None:
        logger.debug(f"Updating shaders with grid spacing {self.glyph_size}...")
        self.shader_parameters.SetUniform4f("glyph_scale", [*self.glyph_size, 0.0])

    def change_exaggeration(self, _=None) -> None:
        logger.debug(f"Updating shaders with exaggeration {self.exaggeration}...")
        self.shader_parameters.SetUniform4f("disp_scale", [*self.exaggeration, 0.0])

    def change_mask_limits(self, _=None) -> None:
        logger.debug(f"Updating shaders with mask limits {self.mask_limits}...")
        self.shader_parameters.SetUniform2f("mask_limits", self.mask_limits)

    def change_clipping_extents(self, extents: typing.Tuple[float]) -> None:
        logger.debug(f"Updating shaders with clipping extents {extents}...")
        if extents != self._applied_extents:
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
            self._applied_extents = extents
            self.clipping_box.update(self._applied_extents)
        else:
            logger.debug(
                f"Clipping extents {extents} same as current value. Update not applied."
            )

    def update_plot_dataset(self, _=None) -> None:
        logger.debug(f"Updating plot dataset to {self.plot_dataset}...")
        self._plot_dataset_limits = list(
            self.polydata.get_data_range(self.plot_dataset)
        )
        logger.debug(f"Detected value range of {self._plot_dataset_limits}")
        self._set_colorbar_limits(self._plot_dataset_limits)
        self.plotter.scalar_bar.SetTitle(self.plot_dataset)
        self.polydata.GetPointData().SetActiveScalars(self.plot_dataset)
        self.plotter.render()

        self.actor.GetMapper().MapDataArrayToVertexAttribute(
            "_scalar", self.plot_dataset, vtkDataObject.FIELD_ASSOCIATION_POINTS, -1
        )

    def update_mask_dataset(self, _=None) -> None:
        logger.debug(f"Updating mask dataset to {self.mask_dataset}...")
        self._mask_dataset_limits = list(
            self.polydata.get_data_range(self.mask_dataset)
        )
        logger.debug(f"Detected value range of {self._plot_dataset_limits}")
        self._set_mask_limits(self._mask_dataset_limits)
        self.actor.GetMapper().MapDataArrayToVertexAttribute(
            "_mask_scalar",
            self.mask_dataset,
            vtkDataObject.FIELD_ASSOCIATION_POINTS,
            -1,
        )

    def change_colorbar_limits(self, _=None) -> None:
        if self.colorbar_limits[0] <= self.colorbar_limits[1]:
            logger.debug(
                f"Colorbar limits {self.colorbar_limits} in correct order. Applying..."
            )
            self.plotter.update_scalar_bar_range(self.colorbar_limits)

    def emit_moved_camera(self, *args) -> None:
        """A method wrapping the signal emit is needed because the vtkInteractionEvent
        passes two arguments, and a signal can only handle one argument.
        """
        self.moved_camera.emit(list(self.plotter.camera_position))

    def create_camera_control_widget(self) -> None:
        camera_widget = vtkCameraOrientationWidget()
        camera_widget.SetParentRenderer(self.plotter.renderers[0])
        camera_widget.GetRepresentation().AnchorToLowerLeft()
        camera_widget.On()

        self.plotter.camera_widget = camera_widget

    def toggle_clipping_box(self, enable):
        self.clipping_box.SetEnabled(enable)

    @property
    def timestep_index(self) -> int:
        return self._timestep_index

    @timestep_index.setter
    def timestep_index(self, value: int) -> None:
        logger.debug(f"Setting timestep index to {value}...")
        self._timestep_index = max(0, min(len(self.model.timesteps) - 1, value))
        self.changed_timestep.emit(str(self.timestep))

    @property
    def timestep(self) -> int:
        return self.model.timesteps[self.timestep_index]

    @timestep.setter
    def timestep(self, value: int) -> None:
        logger.debug(f"Setting timestep to {value}...")
        if value in self.model.timesteps:
            self.timestep_index = self.model.timesteps.index(self.timestep)
        else:
            logger.warning(f"{value} not found in timesteps")
            return
        self.changed_timestep.emit(str(self.timestep))

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

    @glyph_size.setter
    def glyph_size(self, value: typing.Union[float, typing.Iterable[float]]) -> None:
        logger.debug(f"Setting grid spacing index to {value}...")
        if isinstance(value, typing.Iterable) and len(value) == 3:
            self._glyph_size = list(value)
        elif isinstance(value, float):
            self._glyph_size = list([value, value, value])
        else:
            logger.warning(f"Bad grid spacing value: {value}")
            return
        self.changed_grid_spacing.emit(self._glyph_size)

    @property
    def exaggeration(self) -> typing.List[float]:
        return list(self._exaggeration)

    @exaggeration.setter
    def exaggeration(self, value: typing.Union[float, typing.Iterable[float]]) -> None:
        logger.debug(f"Setting exaggeration to {value}...")
        if isinstance(value, typing.Iterable) and len(value) == 3:
            self._exaggeration = list(value)
        elif isinstance(value, float):
            self._exaggeration = list([value, value, value])
        else:
            logger.warning(f"Bad exaggeration value: {value}")
            return
        self.changed_exaggeration.emit(self._exaggeration)

    @property
    def plot_dataset(self) -> str:
        return self._plot_dataset

    @plot_dataset.setter
    def plot_dataset(self, name: str) -> None:
        logger.debug(f"Setting plot dataset to {name}...")
        if name in self.model.datasets:
            self._plot_dataset = name
        else:
            logger.warning(f"{name} not found in datasets")
            return
        self.changed_plot_dataset.emit(self._plot_dataset)
        if self.plot_and_mask_same_dataset:
            self.mask_dataset = name

    @property
    def mask_dataset(self) -> str:
        return self._mask_dataset

    @mask_dataset.setter
    def mask_dataset(self, name: str) -> None:
        logger.debug(f"Setting mask dataset to {name}...")
        if name in self.model.datasets:
            self._mask_dataset = name
        else:
            logger.warning(f"{name} not found in datasets")
            return
        self.changed_mask_dataset.emit(self._mask_dataset)

    @property
    def clipping_extents(self) -> typing.Tuple[float]:
        return self._clipping_extents

    @clipping_extents.setter
    def clipping_extents(self, extents: typing.Sequence[float]) -> None:
        logger.debug(f"Externally setting clipping extents to {extents}...")
        self._set_clipping_extents(extents=extents, external=True)

    def _set_clipping_extents(
        self, extents: typing.Sequence[float], external: bool = False
    ) -> None:
        logger.debug(
            f"Setting clipping extents to {extents}. Externally? {external}..."
        )
        self._clipping_extents = tuple(extents)
        self.changed_clipping_extents.emit(self._clipping_extents)
        if not external:
            self.program_changed_clipping_extents.emit(self._clipping_extents)

    def replace_clipping_extents(
        self, indeces: typing.Sequence[int], values: typing.Sequence[float]
    ) -> None:
        logger.debug(f"Replacing clipping extents {indeces} with {values}...")
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
        logger.debug(f"Externally setting mask limits to {value}...")
        self._set_mask_limits(value=value, external=True)

    def _set_mask_limits(
        self, value: typing.Iterable[float], external: bool = False
    ) -> None:
        logger.debug(f"Setting mask limits to {value}. Externally? {external}...")
        if isinstance(value, typing.Iterable) and len(value) == 2:
            self._mask_limits = list(value)
        elif value is None:
            self._mask_limits = [-LARGE, LARGE]
        else:
            logger.warning(f"Bad mask limits value: {value}")
            return
        self.changed_mask_limits.emit(self._mask_limits)
        if not external:
            self.program_changed_mask_limits.emit(self._mask_limits)

    @property
    def colorbar_limits(self) -> typing.List[float]:
        return self._colorbar_limits

    @colorbar_limits.setter
    def colorbar_limits(self, value: typing.Iterable[float]) -> None:
        logger.debug(f"Externally setting colorbar limits to {value}...")
        self._set_colorbar_limits(value=value, external=True)

    def _set_colorbar_limits(
        self, value: typing.Iterable[float], external: bool = False
    ) -> None:
        logger.debug(f"Setting colorbar limits to {value}. Externally? {external}...")
        if isinstance(value, typing.Iterable) and len(value) == 2:
            self._colorbar_limits = list(value)
        elif value is None:
            self._colorbar_limits = self._plot_dataset_limits
        else:
            logger.warning(f"Bad colorbar limits value: {value}")
            return
        self.changed_colorbar_limits.emit(self._colorbar_limits)
        if not external:
            self.program_changed_colorbar_limits.emit(self._colorbar_limits)

    def save_image(self, filename) -> None:
        self.plotter.screenshot(filename=filename)

    @property
    def background_color(self) -> typing.List[float]:
        return self.plotter.background_color

    @background_color.setter
    def background_color(self, color: typing.Sequence[float]) -> None:
        self.plotter.set_background(color)


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
