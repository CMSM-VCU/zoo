import typing
from importlib import resources

import numpy as np
import pyvista as pv
import pyvistaqt
import vtk
from qtpy import QtCore as qtc
from vtk.numpy_interface import dataset_adapter as dsa

from .H5Model import H5Model


class VTK_PVH5Model(H5Model):
    raw_mesh_cache: dict = {}

    def __init__(self) -> None:
        super().__init__()
        self.timesteps = (None,)
        self.datasets = (None,)
        self.mesh = None

        self.plotter = pyvistaqt.QtInteractor()

        self.loaded_file.connect(self.construct_plot_at_timestep)
        self.changed_timestep.connect(self.construct_plot_at_timestep)
        self.changed_grid_spacing.connect(self.change_grid_spacing)
        self.changed_clipping_extents.connect(self.change_clipping_extents)
        self.changed_exaggeration.connect(self.change_exaggeration)
        self.changed_plot_dataset.connect(self.update_plot_dataset)
        self.changed_mask_dataset.connect(self.update_mask_dataset)
        self.changed_mask_limits.connect(self.change_mask_limits)
        self.changed_colorbar_limits.connect(self.change_colorbar_limits)

    @property
    def camera_location(self) -> typing.List[typing.Tuple[float, float, float]]:
        return self.plotter.camera_position

    def construct_timestep_data(self) -> pv.PolyData:
        coords = self.df.loc[self.timestep, ("x1", "x2", "x3")].values
        points = vtk.vtkPoints()
        points.SetData(dsa.numpyTovtkDataArray(coords))
        polydata = vtk.vtkPolyData()
        polydata.SetPoints(points)

        polydata.GetPointData().SetNormals(
            dsa.numpyTovtkDataArray(np.empty_like(coords))
        )  # Assign dummy normals to trick VTK into enabling (specular?) lighting
        for dataset in self.datasets:
            polydata.GetPointData().AddArray(
                dsa.numpyTovtkDataArray(
                    self.df.loc[self.timestep, dataset].values, name=dataset
                )
            )
        polydata.GetPointData().AddArray(
            dsa.numpyTovtkDataArray(
                self.df.loc[self.timestep, ("u1", "u2", "u3")].values,
                name="_displacement",
            )
        )
        polydata.GetPointData().SetActiveScalars(self.datasets[0])
        return pv.utilities.wrap(polydata)

    def construct_data_mapper(self, polydata: pv.PolyData) -> "MapperHelper":
        vertexGlyphFilter = vtk.vtkVertexGlyphFilter()
        vertexGlyphFilter.AddInputDataObject(polydata)
        vertexGlyphFilter.Update()

        mapper = pv.mapper.make_mapper(vtk.vtkPolyDataMapper)
        mapper.SetInputConnection(vertexGlyphFilter.GetOutputPort())
        lut = vtk.vtkLookupTable()
        lut.SetNumberOfColors(256)
        lut.SetHueRange([0.0, 0.667][::-1])  # Reverse indexing to reverse colorbar
        lut.Build()
        mapper.SetLookupTable(lut)

        mapper.MapDataArrayToVertexAttribute(
            "_disp", "_displacement", vtk.vtkDataObject.FIELD_ASSOCIATION_POINTS, -1
        )

        return mapper

    def construct_plot_at_timestep(self, _=None) -> None:
        self.polydata = self.construct_timestep_data()
        mapper = self.construct_data_mapper(self.polydata)

        self.actor = vtk.vtkActor()
        self.actor.SetMapper(mapper)

        self.shader_parameters = self.apply_shaders(self.actor)

        self.plotter.AddObserver(
            vtk.vtkCommand.InteractionEvent, self.emit_moved_camera
        )
        self.plotter.add_actor(self.actor, name="primary", render=False)
        self.plotter.mapper = mapper
        self.plotter.add_axes()
        self.plotter.reset_camera()
        self.plotter.add_scalar_bar(render=False)
        self._original_extents = self.polydata.GetPoints().GetBounds()
        self.clipping_extents = self._original_extents
        self.update_plot_dataset()
        self.update_mask_dataset()

    def apply_shaders(self, actor: vtk.vtkActor):
        shader_property = actor.GetShaderProperty()

        shader_property.AddShaderReplacement(
            vtk.vtkShader.Vertex,
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
            vtk.vtkShader.Vertex,
            "//VTK::PositionVC::Impl",
            True,
            "//VTK::PositionVC::Impl\n"
            "vertexMCVSOutput = vertexMC;\n"
            "dispMCVSOutput = vec4(_disp, 0.0);\n"
            "scalarVSOutput = _scalar;\n"
            "maskscalarVSOutput = _mask_scalar;\n",
            False,
        )
        srcGS = resources.read_text(__package__, "cubeGS.glsl")
        shader_property.SetGeometryShaderCode(srcGS)

        shader_parameters = shader_property.GetGeometryCustomUniforms()
        shader_parameters.SetUniform3f("bottomLeft", [-1.0, -1.0, -1.0])
        shader_parameters.SetUniform3f("topRight", [1.0, 1.0, 1.0])
        shader_parameters.SetUniform4f("glyph_scale", [*self.grid_spacing, 0.0])
        shader_parameters.SetUniform4f("disp_scale", [*self.exaggeration, 0.0])
        shader_parameters.SetUniform2f("mask_limits", self.mask_limits)
        return shader_parameters

    def change_grid_spacing(self, _=None) -> None:
        self.shader_parameters.SetUniform4f("glyph_scale", [*self.grid_spacing, 0.0])

    def change_exaggeration(self, _=None) -> None:
        self.shader_parameters.SetUniform4f("disp_scale", [*self.exaggeration, 0.0])

    def change_mask_limits(self, _=None) -> None:
        self.shader_parameters.SetUniform2f("mask_limits", self.mask_limits)

    def change_clipping_extents(self, extents: typing.Tuple[float]) -> None:
        extents_MC = bbox_to_model_coordinates(extents, self._original_extents)

        self.shader_parameters.SetUniform3f("bottomLeft", extents_MC[0])
        self.shader_parameters.SetUniform3f("topRight", extents_MC[1])

    def update_plot_dataset(self, _=None) -> None:
        self._plot_dataset_limits = list(
            self.polydata.get_data_range(self.plot_dataset)
        )
        self.colorbar_limits = self._plot_dataset_limits
        self.plotter.scalar_bar.SetTitle(self.plot_dataset)
        self.plotter.update_scalars(
            scalars=self.plot_dataset, mesh=self.polydata, render=True
        )

        self.actor.GetMapper().MapDataArrayToVertexAttribute(
            "_scalar", self.plot_dataset, vtk.vtkDataObject.FIELD_ASSOCIATION_POINTS, -1
        )

    def update_mask_dataset(self, _=None) -> None:
        self._mask_dataset_limits = list(
            self.polydata.get_data_range(self.mask_dataset)
        )
        self.mask_limits = self._mask_dataset_limits
        self.actor.GetMapper().MapDataArrayToVertexAttribute(
            "_mask_scalar",
            self.mask_dataset,
            vtk.vtkDataObject.FIELD_ASSOCIATION_POINTS,
            -1,
        )

    def change_colorbar_limits(self, _=None) -> None:
        self.plotter.update_scalar_bar_range(self.colorbar_limits)

    def emit_moved_camera(self, *args) -> None:
        """A method wrapping the signal emit is needed because the vtkInteractionEvent
        passes two arguments, and a signal can only handle one argument.
        """
        self.moved_camera.emit(list(self.plotter.camera_position))


def bbox_to_model_coordinates(bbox_bounds, base_bounds):
    base_bottom_left = np.array(base_bounds[0::2])
    base_top_right = np.array(base_bounds[1::2])
    bbox_mc_bl = (
        (np.array(bbox_bounds[0::2]) - base_bottom_left)
        / (base_top_right - base_bottom_left)
    ) - 0.5
    bbox_mc_tr = (
        (np.array(bbox_bounds[1::2]) - base_top_right)
        / (base_top_right - base_bottom_left)
    ) + 0.5
    return (bbox_mc_bl, bbox_mc_tr)


if __name__ == "__main__":
    import sys

    from qtpy import QtWidgets as qtw

    app = qtw.QApplication(sys.argv)

    model = VTK_PVH5Model()
    model.load_file("./test_data/kylesheartest1.h5")
    model.construct_plot_at_timestep()
    print(model.mesh)
    print(model.actor)
    print(model.actor.GetShaderProperty())
    print(model.plotter)
    pass
