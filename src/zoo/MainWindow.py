import os
import sys

os.environ["QT_API"] = "pyqt5"

from qtpy import QtCore as qtc
from qtpy import QtGui as qtg
from qtpy import QtWidgets as qtw

from H5Model import H5Model
from ui.zoo_ui import Ui_MainWindow


class MainWindow(qtw.QMainWindow):
    def __init__(self, parent=None, show=True) -> None:
        super().__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = H5Model()
        self.model.plotter.setParent(self.ui.viewport)
        self.ui.viewport.layout().addWidget(self.model.plotter.interactor)

        self.hook_up_signals()

        if show:
            self.show()

    def hook_up_signals(self):
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionExit.triggered.connect(self.close)

        self.ui.nextTimeStep.clicked.connect(self.increment_timestep)
        self.ui.prevTimeStep.clicked.connect(self.decrement_timestep)
        self.ui.timeStepSelector.activated.connect(self.set_timestep)

        self.ui.gsSpinBox.editingFinished.connect(self.set_grid_spacing)
        self.ui.exagSpinBox.editingFinished.connect(self.set_exaggeration)

        self.ui.datasetSelector.currentTextChanged.connect(self.select_dataset)
        self.ui.colorminSpinBox.valueChanged.connect(self.set_color_min)
        self.ui.colormaxSpinBox.valueChanged.connect(self.set_color_max)
        self.ui.maskminSpinBox.valueChanged.connect(self.set_mask_min)
        self.ui.maskmaxSpinBox.valueChanged.connect(self.set_mask_max)

        self.ui.xminSpinBox.valueChanged.connect(self.set_clip_xmin)
        self.ui.xmaxSpinBox.valueChanged.connect(self.set_clip_xmax)
        self.ui.yminSpinBox.valueChanged.connect(self.set_clip_ymin)
        self.ui.ymaxSpinBox.valueChanged.connect(self.set_clip_ymax)
        self.ui.zminSpinBox.valueChanged.connect(self.set_clip_zmin)
        self.ui.zmaxSpinBox.valueChanged.connect(self.set_clip_zmax)

        self.model.loaded_file.connect(self.toggle_controls)

        self.model.changed_timestep.connect(self.ui.timeStepSelector.setCurrentText)

    def open_file(self):
        # stackoverflow.com/a/44076057/13130795
        filename, _ = qtw.QFileDialog.getOpenFileName(self)
        if filename:
            self.model.load_file(filename)

    def toggle_controls(self, enable: bool):
        print("toggle_controls", enable)
        self.ui.timeStepSelector.addItems([str(i) for i in self.model.timesteps])
        self.ui.datasetSelector.addItems(self.model.datasets)

    def increment_timestep(self):
        self.model.timestep_index += 1

    def decrement_timestep(self):
        self.model.timestep_index -= 1

    def set_timestep(self, new_time: str):
        try:
            self.model.timestep = int(new_time)
        except:
            print("Bad timestep string: ", new_time)

    def set_grid_spacing(self):
        self.model.grid_spacing = self.ui.gsSpinBox.value()

    def set_exaggeration(self):
        self.model.exaggeration = self.ui.exagSpinBox.value()

    def select_dataset(self, new_dataset: str):
        self.model.dataset = new_dataset

    def set_color_min(self, value: float):
        print("set_color_min", value)

    def set_color_max(self, value: float):
        print("set_color_max", value)

    def set_mask_min(self, value: float):
        print("set_mask_min", value)

    def set_mask_max(self, value: float):
        print("set_mask_max", value)

    def set_clip_xmin(self, value: float):
        print("set_clip_xmin", value)

    def set_clip_xmax(self, value: float):
        print("set_clip_xmax", value)

    def set_clip_ymin(self, value: float):
        print("set_clip_ymin", value)

    def set_clip_ymax(self, value: float):
        print("set_clip_ymax", value)

    def set_clip_zmin(self, value: float):
        print("set_clip_zmin", value)

    def set_clip_zmax(self, value: float):
        print("set_clip_zmax", value)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
