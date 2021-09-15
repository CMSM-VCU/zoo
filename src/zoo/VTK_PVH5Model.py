from PIL.Image import new
import numpy as np
import pandas as pd
import pyvista as pv
import pyvistaqt
import vtk
from vtk.numpy_interface import dataset_adapter as dsa

from qtpy import QtCore as qtc
from pyvista.plotting.mapper import make_mapper
from pyvista.utilities import wrap

from H5Model import H5Model


class VTK_PVH5Model(H5Model):
    raw_mesh_cache: dict = {}

    def __init__(self) -> None:
        super().__init__()
        self.timesteps = (None,)
        self.datasets = (None,)
        self.mesh = None

        self.plotter = pyvistaqt.QtInteractor()

        self.loaded_file.connect(self.load_mesh)
        self.changed_timestep.connect(self.load_mesh)
        self.changed_grid_spacing.connect(self.change_grid_spacing)
        self.changed_clipping_extents.connect(self.change_clipping_extents)
        self.changed_exaggeration.connect(self.change_exaggeration)
        self.changed_dataset.connect(self.update_dataset)
        self.changed_contour_threshold.connect(self.change_contour_threshold)
        self.changed_colorbar_limits.connect(self.change_colorbar_limits)

    def load_mesh(self, _=None) -> None:
        coords = self.df.loc[self.timestep, ("x1", "x2", "x3")].values
        points = vtk.vtkPoints()
        points.SetData(dsa.numpyTovtkDataArray(coords))
        self.polydata = vtk.vtkPolyData()
        self.polydata.SetPoints(points)
        self.polydata.GetPointData().SetNormals(
            dsa.numpyTovtkDataArray(np.empty_like(coords))
        )  # Assign dummy normals to trick VTK into enabling (specular?) lighting
        for dataset in self.datasets:
            self.polydata.GetPointData().AddArray(
                dsa.numpyTovtkDataArray(
                    self.df.loc[self.timestep, dataset].values, name=dataset
                )
            )
        self.polydata.GetPointData().AddArray(
            dsa.numpyTovtkDataArray(
                self.df.loc[self.timestep, ("u1", "u2", "u3")].values,
                name="_displacement",
            )
        )
        self.polydata.GetPointData().SetActiveScalars(self.datasets[0])
        self.polydata = wrap(self.polydata)
        vertexGlyphFilter = vtk.vtkVertexGlyphFilter()
        vertexGlyphFilter.AddInputDataObject(self.polydata)
        vertexGlyphFilter.Update()

        mapper = make_mapper(vtk.vtkPolyDataMapper)
        mapper.SetInputConnection(vertexGlyphFilter.GetOutputPort())
        lut = vtk.vtkLookupTable()
        lut.SetNumberOfColors(256)
        lut.SetHueRange([0.0, 0.667][::-1])  # Reverse indexing to reverse colorbar
        lut.Build()
        mapper.SetLookupTable(lut)

        mapper.MapDataArrayToVertexAttribute(
            "_disp", "_displacement", vtk.vtkDataObject.FIELD_ASSOCIATION_POINTS, -1
        )

        self.actor = vtk.vtkActor()
        self.actor.SetMapper(mapper)

        self.apply_shaders()
        self.plotter.add_actor(self.actor, name="primary", render=False)
        self.plotter.mapper = mapper
        self.plotter.add_scalar_bar(render=False)
        self._original_extents = self.polydata.GetPoints().GetBounds()
        self.clipping_extents = self._original_extents
        self.update_dataset()

    def apply_shaders(self):
        shader_property = self.actor.GetShaderProperty()

        shader_property.AddShaderReplacement(
            vtk.vtkShader.Vertex,
            "//VTK::PositionVC::Dec",
            True,
            "//VTK::PositionVC::Dec\n"
            "out vec4 vertexMCVSOutput;\n"
            "in vec3 _disp;\n"
            "out vec4 dispMCVSOutput;\n"
            "in float _scalar;\n"
            "out float scalarVSOutput;\n",
            False,
        )
        shader_property.AddShaderReplacement(
            vtk.vtkShader.Vertex,
            "//VTK::PositionVC::Impl",
            True,
            "//VTK::PositionVC::Impl\n"
            "vertexMCVSOutput = vertexMC;\n"
            "dispMCVSOutput = vec4(_disp, 0.0);\n"
            "scalarVSOutput = _scalar;\n",
            False,
        )
        with open("src/zoo/cubeGS.glsl", "r") as f:
            srcGS = f.read()
        shader_property.SetGeometryShaderCode(srcGS)

        self.shader_parameters = shader_property.GetGeometryCustomUniforms()
        self.shader_parameters.SetUniform3f("bottomLeft", [-1.0, -1.0, -1.0])
        self.shader_parameters.SetUniform3f("topRight", [1.0, 1.0, 1.0])
        self.shader_parameters.SetUniform4f("glyph_scale", [*self.grid_spacing, 0.0])
        self.shader_parameters.SetUniform4f("disp_scale", [*self.exaggeration, 0.0])
        self.shader_parameters.SetUniform2f("contour_threshold", self.contour_threshold)

    def change_grid_spacing(self, _=None) -> None:
        self.shader_parameters.SetUniform4f("glyph_scale", [*self.grid_spacing, 0.0])

    def change_exaggeration(self, _=None) -> None:
        self.shader_parameters.SetUniform4f("disp_scale", [*self.exaggeration, 0.0])

    def change_contour_threshold(self, _=None) -> None:
        self.shader_parameters.SetUniform2f("contour_threshold", self.contour_threshold)

    def change_clipping_extents(self, extents: tuple[float]) -> None:
        extents_MC = bbox_to_model_coordinates(extents, self._original_extents)

        self.shader_parameters.SetUniform3f("bottomLeft", extents_MC[0])
        self.shader_parameters.SetUniform3f("topRight", extents_MC[1])

    def update_dataset(self, _=None) -> None:
        self._dataset_limits = list(self.polydata.get_data_range(self.dataset))
        self.colorbar_limits = self._dataset_limits
        self.plotter.scalar_bar.SetTitle(self.dataset)
        self.plotter.update_scalars(
            scalars=self.dataset, mesh=self.polydata, render=True
        )

        self.actor.GetMapper().MapDataArrayToVertexAttribute(
            "_scalar", self.dataset, vtk.vtkDataObject.FIELD_ASSOCIATION_POINTS, -1
        )

    def change_colorbar_limits(self, _=None) -> None:
        self.plotter.update_scalar_bar_range(self.colorbar_limits)


def bbox_to_model_coordinates(bbox_bounds, base_bounds):
    base_bottom_left = np.array(base_bounds[0::2])
    base_top_right = np.array(base_bounds[1::2])
    bbox_mc_bl = (
        (np.array(bbox_bounds[0::2]) + base_bottom_left)
        / (base_top_right - base_bottom_left)
    ) + 0.5
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
    model.load_mesh()
    print(model.mesh)
    print(model.actor)
    print(model.actor.GetShaderProperty())
    print(model.plotter)
    pass
