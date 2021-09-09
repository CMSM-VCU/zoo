import numpy as np
import pandas as pd
import pyvista as pv
import pyvistaqt
from qtpy import QtCore as qtc

from H5Model import H5Model
from utils import measure

try:
    profile
except NameError:
    profile = lambda x: x


class PyVistaH5Model(H5Model):
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
        self.changed_grid_spacing.connect(self.change_glyphs)
        self.changed_exaggeration.connect(self.change_exaggeration)
        self.changed_dataset.connect(self.refit_scalar_bar)

    @measure
    @profile
    def load_mesh(self, _=None) -> None:
        try:
            self.raw_mesh = self.raw_mesh_cache[self.timestep]
        except KeyError:
            mesh = pv.PolyData(self.df.loc[self.timestep, ("x1", "x2", "x3")].values)
            for dataset in self.datasets:
                mesh[dataset] = self.df.loc[self.timestep, dataset].values
            mesh["_displacement"] = self.df.loc[
                self.timestep, ("u1", "u2", "u3")
            ].values
            self.raw_mesh_cache[self.timestep] = mesh.copy()
            self.raw_mesh = self.raw_mesh_cache[self.timestep]
        self.glyph_displacement = np.repeat(self.raw_mesh["_displacement"], 24, axis=0)

        self.mesh = self.raw_mesh

        self.change_glyphs()
        self.change_exaggeration()
        self.refit_scalar_bar()

    @measure
    @profile
    def change_glyphs(self, _=None) -> None:
        if self.mesh:
            self.glyphmesh = self.mesh.glyph(
                scale=False,
                orient=False,
                factor=self.grid_spacing,
                geom=pv.Cube(),
                progress_bar=True,
            )
            self.glyphmesh_points = self.glyphmesh.points
            self.plotter.add_mesh(
                self.glyphmesh, scalars=self.dataset, name="primary", render=False,
            )

    @measure
    @profile
    def change_exaggeration(self, _=None) -> None:
        self.plotter.update_coordinates(
            self.glyphmesh_points + self.glyph_displacement * self.exaggeration
        )

    @measure
    @profile
    def refit_scalar_bar(self, _=None) -> None:
        if self.mesh:
            self.plotter.update_scalars(self.dataset, render=False)
            self.plotter.scalar_bar.SetTitle(self.dataset)
            clim = self.plotter.mesh.get_data_range(self.dataset)
            self.plotter.update_scalar_bar_range(clim)

    @measure
    @profile
    def add_filters(self, _=None) -> None:
        # # self.plotter.mesh.threshold((0, 3), scalars=self.dataset, inplace=True)
        # self.plotter.mesh = self.plotter.mesh.threshold(
        #     (0, 3), scalars=self.dataset
        # ).clip_box((0, 9, 0, 9, 0, 9))
        self.plotter.add_mesh_clip_box(
            self.plotter.mesh, rotation_enabled=False, name="primary"
        )
        pass


if __name__ == "__main__":
    import sys
    from qtpy import QtWidgets as qtw

    app = qtw.QApplication(sys.argv)

    model = PyVistaH5Model()
    model.load_file("./test_data/kylesheartest1.h5")
    model.load_mesh()
