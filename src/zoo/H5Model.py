import numpy as np
import pandas as pd
import pyvista as pv
import pyvistaqt
from qtpy import QtCore as qtc


class H5Model(qtc.QAbstractItemModel):
    loaded_file = qtc.Signal(bool)
    changed_timestep = qtc.Signal(str)
    # changed_mesh_appearance = qtc.Signal()

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

    def load_file(self, h5_filename) -> None:
        try:
            self.df = pd.read_hdf(h5_filename, key="data", mode="r")
        except Exception as err:
            raise err
        else:
            self.datasets = tuple(self.df.columns)
            self.timesteps = tuple(self.df.index.levels[0])

            self.dataset = self.datasets[0]
            self.timestep = self.timesteps[0]
            self.loaded_file.emit(True)

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
        self.change_glyphs()

    @property
    def dataset(self) -> str:
        return self._dataset

    @dataset.setter
    def dataset(self, name: str) -> None:
        if name in self.datasets:
            self._dataset = name
        # self.changed_mesh_appearance.emit()
        self.refit_scalar_bar()

    def load_mesh(self) -> None:
        self.mesh = pv.PolyData(
            self.df.loc[self.timestep, ("x1", "x2", "x3")].to_numpy()
        )
        for dataset in self.datasets:
            self.mesh[dataset] = self.df.loc[self.timestep, dataset].to_numpy()
        self.mesh["_displacement"] = self.df.loc[
            self.timestep, ("u1", "u2", "u3")
        ].to_numpy()

        self.change_glyphs()
        self.refit_scalar_bar()

    def change_glyphs(self) -> None:
        if self.mesh:
            self.glyphmesh = self.mesh.warp_by_vector(
                "_displacement", factor=self.exaggeration,
            ).glyph(scale=False, orient=False, factor=self.grid_spacing, geom=pv.Cube())
            self.plotter.add_mesh(
                self.glyphmesh, scalars=self.dataset, name="primary", render=False
            )

    def refit_scalar_bar(self) -> None:
        if self.mesh:
            self.plotter.update_scalars(self.dataset, render=False)
            self.plotter.scalar_bar.SetTitle(self.dataset)
            clim = self.plotter.mesh.get_data_range(self.dataset)
            self.plotter.update_scalar_bar_range(clim)
