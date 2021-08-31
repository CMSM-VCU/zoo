import sys

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
        self.hook_up_signals()

        self.model = None

        if show:
            self.show()

    def hook_up_signals(self):
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionExit.triggered.connect(self.close)

        self.ui.nextTimeStep.clicked.connect(self.increment_timestep)
        self.ui.prevTimeStep.clicked.connect(self.decrement_timestep)
        self.ui.timeStepSelector.currentTextChanged.connect(self.set_timestep)

        self.ui.gsSpinBox.valueChanged.connect(self.set_grid_spacing)
        self.ui.exagSpinBox.valueChanged.connect(self.set_exaggeration)

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

    def open_file(self):
        # stackoverflow.com/a/44076057/13130795
        filename, _ = qtw.QFileDialog.getOpenFileName(self)
        if filename:
            self.model = H5Model(filename)

    def increment_timestep(self):
        self.model.timestep_index += 1

    def decrement_timestep(self):
        self.model.timestep_index -= 1

    def set_timestep(self, new_time: str):
        self.model.timestep = int(new_time)

    def set_grid_spacing(self, value: float):
        self.model.grid_spacing = value

    def set_exaggeration(self, value: float):
        self.model.exaggeration = value

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
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
