import numpy as np
import pandas as pd
import pyvista as pv
import pyvistaqt
from qtpy import QtCore as qtc

from utils import measure

try:
    profile
except NameError:
    profile = lambda x: x


class H5Model(qtc.QAbstractItemModel):
    loaded_file = qtc.Signal(bool)
    changed_timestep = qtc.Signal(str)
    # changed_mesh_appearance = qtc.Signal()

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

        self.changed_timestep.connect(self.load_mesh)
        # self.changed_mesh_appearance.connect(self.refresh_mesh)

    @measure
    @profile
    def load_file(self, h5_filename) -> None:
        try:
            self.df = pd.read_hdf(h5_filename, key="data", mode="r")
        except Exception as err:
            raise err
        else:
            self.datasets = tuple(self.df.columns)
            self.timesteps = tuple(self.df.index.levels[0])

            self._dataset = self.datasets[0]
            # self.timestep = self.timesteps[0]
            self.loaded_file.emit(True)
            self.load_mesh()

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
    def grid_spacing(self) -> float:
        return self._grid_spacing

    @grid_spacing.setter
    def grid_spacing(self, value: float) -> None:
        if value > 0.0:
            self._grid_spacing = value
        # self.changed_mesh_appearance.emit()
        self.change_glyphs()

    @property
    def exaggeration(self) -> float:
        return self._exaggeration

    @exaggeration.setter
    def exaggeration(self, value: float) -> None:
        if value >= 0.0:
            self._exaggeration = value
        # self.changed_mesh_appearance.emit()
        self.change_exaggeration()

    @property
    def dataset(self) -> str:
        return self._dataset

    @dataset.setter
    def dataset(self, name: str) -> None:
        if name in self.datasets:
            self._dataset = name
        # self.changed_mesh_appearance.emit()
        self.refit_scalar_bar()

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
    def change_glyphs(self) -> None:
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
    def change_exaggeration(self) -> None:
        self.plotter.update_coordinates(
            self.glyphmesh_points + self.glyph_displacement * self.exaggeration
        )

    @measure
    @profile
    def refit_scalar_bar(self) -> None:
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

    model = H5Model()
    model.load_file("./test_data/kylesheartest1.h5")
    model.load_mesh()
