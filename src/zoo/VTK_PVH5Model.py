import numpy as np
import pandas as pd
import pyvista as pv
import pyvistaqt
import vtk
from vtk.numpy_interface import dataset_adapter as dsa

from qtpy import QtCore as qtc

from H5Model import H5Model


class VTK_PVH5Model(H5Model):
    raw_mesh_cache: dict = {}

    _timestep_index: int = 0
    _grid_spacing: float = 0.005
    _exaggeration: float = 0.0

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
        # self.changed_exaggeration.connect()
        # self.changed_dataset.connect()

    def load_mesh(self, _=None) -> None:
        coords = self.df.loc[self.timestep, ("x1", "x2", "x3")].values
        points = vtk.vtkPoints()
        points.SetData(dsa.numpyTovtkDataArray(coords))
        polydata = vtk.vtkPolyData()
        polydata.SetPoints(points)
        polydata.GetPointData().SetNormals(
            dsa.numpyTovtkDataArray(np.empty_like(coords))
        )  # Assign dummy normals to trick VTK into enabling (specular?) lighting
        for dataset in self.datasets:
            polydata.GetPointData().SetScalars(
                dsa.numpyTovtkDataArray(
                    self.df.loc[self.timestep, dataset].values, name=dataset
                )
            )
        vertexGlyphFilter = vtk.vtkVertexGlyphFilter()
        vertexGlyphFilter.AddInputDataObject(polydata)
        vertexGlyphFilter.Update()

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(vertexGlyphFilter.GetOutputPort())
        self.actor = vtk.vtkActor()
        self.actor.SetMapper(mapper)

        self.apply_shaders()
        self.plotter.add_actor(self.actor)
        self._original_extents = polydata.GetPoints().GetBounds()
        self.clipping_extents = self._original_extents

    def apply_shaders(self):
        shader_property = self.actor.GetShaderProperty()

        shader_property.AddShaderReplacement(
            vtk.vtkShader.Vertex,
            "//VTK::PositionVC::Dec",
            True,
            "//VTK::PositionVC::Dec\n" "out vec4 vertexMCVSOutput;\n",
            False,
        )
        shader_property.AddShaderReplacement(
            vtk.vtkShader.Vertex,
            "//VTK::PositionVC::Impl",
            True,
            "//VTK::PositionVC::Impl\n" "vertexMCVSOutput = vertexMC;\n",
            False,
        )
        with open("src/zoo/cubeGS.glsl", "r") as f:
            srcGS = f.read()
        shader_property.SetGeometryShaderCode(srcGS)

        self.uniforms = shader_property.GetGeometryCustomUniforms()
        self.uniforms.SetUniform3f("bottomLeft", [-1.0, -1.0, -1.0])
        self.uniforms.SetUniform3f("topRight", [1.0, 1.0, 1.0])
        self.uniforms.SetUniformf("glyph_scale", self.grid_spacing)

    def change_grid_spacing(self, new_value: float) -> None:
        self.uniforms.SetUniformf("glyph_scale", new_value)

    def change_clipping_extents(self, extents: tuple[float]) -> None:
        extents_MC = bbox_to_model_coordinates(extents, self._original_extents)

        self.uniforms.SetUniform3f("bottomLeft", extents_MC[0])
        self.uniforms.SetUniform3f("topRight", extents_MC[1])


def bbox_to_model_coordinates(bbox_bounds, base_bounds):
    base_bottom_left = np.array(base_bounds[0::2])
    base_top_right = np.array(base_bounds[1::2])
    bbox_mc_bl = (
        (base_bottom_left - np.array(bbox_bounds[0::2]))
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
    model.load_mesh()
    print(model.mesh)
    print(model.actor)
    print(model.actor.GetShaderProperty())
    print(model.plotter)
    pass
