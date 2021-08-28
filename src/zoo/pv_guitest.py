# Setting the Qt bindings for QtPy
import os
import sys

os.environ["QT_API"] = "pyqt5"

import numpy as np
import pandas as pd
import pyvista as pv
from pyvistaqt import QtInteractor
from qtpy import QtWidgets
from qtpy.QtWidgets import QFileDialog, QMainWindow


class MainWindow(QMainWindow):
    h5_data: pd.DataFrame = None
    loaded_grid_timesteps: dict = {}
    plotted_timestep: int = None
    plotted_field: str = None

    def __init__(self, parent=None, show=True):
        QtWidgets.QMainWindow.__init__(self, parent)

        # create the frame
        self.frame = QtWidgets.QFrame()
        hlayout = QtWidgets.QHBoxLayout()

        # add the pyvista interactor object
        self.plotter = QtInteractor(self.frame)
        self.control_pane = QtWidgets.QFrame()
        hlayout.addWidget(self.plotter.interactor)
        hlayout.addWidget(self.control_pane)

        self.frame.setLayout(hlayout)
        self.setCentralWidget(self.frame)

        # simple menu to demo functions
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")

        openButton = QtWidgets.QAction("Open", self)
        openButton.setShortcut("Ctrl+O")
        openButton.triggered.connect(self.open_file)
        fileMenu.addAction(openButton)

        exitButton = QtWidgets.QAction("Exit", self)
        exitButton.setShortcut("Ctrl+Q")
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        viewMenu = mainMenu.addMenu("View")
        self.show_grid_action = QtWidgets.QAction("Show Grid", self)
        self.show_grid_action.triggered.connect(self.show_grid)
        viewMenu.addAction(self.show_grid_action)

        self.clear_cache_action = QtWidgets.QAction("Clear Grid Cache", self)
        self.clear_cache_action.triggered.connect(self.clear_grid_cache)
        viewMenu.addAction(self.clear_cache_action)

        if show:
            self.show()

    def open_file(self):
        # stackoverflow.com/a/44076057/13130795
        self.filename, _ = QFileDialog.getOpenFileName(self)
        if self.filename:
            self.h5_data = pd.read_hdf(self.filename, key="data", mode="r")
            self.populate_control_pane()
            self.clear_grid_cache()

    def show_grid(self):
        if self.h5_data is not None:
            self.plotted_timestep = list(self.h5_data.index.levels[0])[0]
            self.set_grid_at_timestep(self.plotted_timestep)
            self.plotter.reset_camera()

    def clear_grid_cache(self):
        self.loaded_grid_timesteps = {}

    def set_grid_at_timestep(self, timestep: int):
        try:
            grid = self.loaded_grid_timesteps[timestep]
        except KeyError:
            print(f"{timestep} is not cached.")
            grid = pv.PolyData(
                self.h5_data.loc[timestep, ("x1", "x2", "x3")].to_numpy()
            )
            for column in self.h5_data.columns:
                grid[column] = self.h5_data.loc[timestep, column].to_numpy()
            self.loaded_grid_timesteps[timestep] = grid
        else:
            print(f"{timestep} is cached!")
        print(self.loaded_grid_timesteps.keys())

        self.plotter.add_mesh(
            grid, scalars=self.plotted_field, name="primary", render=False
        )
        self.change_field(self.plotted_field)

    def populate_control_pane(self):
        vlayout = QtWidgets.QVBoxLayout()
        self.controls = {}

        field_picker = QtWidgets.QComboBox()
        field_picker.addItems(list(self.h5_data.columns))
        field_picker.currentTextChanged.connect(self.change_field)
        self.controls["field_picker"] = field_picker

        time_picker = QtWidgets.QComboBox()
        time_picker.addItems([str(i) for i in self.h5_data.index.levels[0]])
        time_picker.currentTextChanged.connect(self.change_time)
        self.controls["time_picker"] = time_picker

        for control in self.controls.values():
            vlayout.addWidget(control)
        self.control_pane.setLayout(vlayout)

    def change_field(self, new_field: str):
        print("Changed to: ", new_field)
        self.plotted_field = new_field
        self.plotter.update_scalars(new_field, render=False)
        self.plotter.scalar_bar.SetTitle(new_field)
        clim = self.plotter.mesh.get_data_range(new_field)
        self.plotter.update_scalar_bar_range(clim)

    def change_time(self, new_time: str):
        print("Time is now: ", int(new_time))
        self.plotted_timestep = int(new_time)
        self.set_grid_at_timestep(self.plotted_timestep)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
