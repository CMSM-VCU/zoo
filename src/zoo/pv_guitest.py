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
    def __init__(self, parent=None, show=True):
        QtWidgets.QMainWindow.__init__(self, parent)

        # create the frame
        self.frame = QtWidgets.QFrame()
        vlayout = QtWidgets.QVBoxLayout()

        # add the pyvista interactor object
        self.plotter = QtInteractor(self.frame)
        vlayout.addWidget(self.plotter.interactor)

        self.frame.setLayout(vlayout)
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

        meshMenu = mainMenu.addMenu("View")
        self.show_grid_action = QtWidgets.QAction("Show Grid", self)
        self.show_grid_action.triggered.connect(self.show_grid)
        meshMenu.addAction(self.show_grid_action)

        if show:
            self.show()

    def open_file(self):
        # stackoverflow.com/a/44076057/13130795
        self.filename, _ = QFileDialog.getOpenFileName(self)
        if self.filename:
            self.h5_data = pd.read_hdf(self.filename, key="data", mode="r")

    def show_grid(self):
        grid = pv.PolyData(
            self.h5_data.loc[self.h5_data.index[-1][0], ("x1", "x2", "x3")].to_numpy()
        )
        grid["mypr"] = self.h5_data.loc[self.h5_data.index[-1][0], "mypr"].to_numpy()
        self.plotter.add_mesh(grid)
        self.plotter.reset_camera()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
