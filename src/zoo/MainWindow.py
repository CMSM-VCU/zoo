import os
from pathlib import Path
import sys

from PyVistaH5Model import PyVistaH5Model
from VTK_PVH5Model import VTK_PVH5Model
from ui.zoo_ui import Ui_MainWindow

os.environ["QT_API"] = "pyqt5"

from qtpy import QtCore as qtc
from qtpy import QtGui as qtg
from qtpy import QtWidgets as qtw


class MainWindow(qtw.QMainWindow):
    def __init__(self, parent=None, show=True, file_to_load=None) -> None:
        super().__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.model = PyVistaH5Model()
        self.model = VTK_PVH5Model()
        self.model.plotter.setParent(self.ui.viewport)
        self.ui.viewport.layout().addWidget(self.model.plotter.interactor)

        self.hook_up_signals()
        self.toggle_control_pane(enable=False)

        if show:
            self.show()

        if file_to_load is not None:
            self.model.load_file(file_to_load)

    def hook_up_signals(self):
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionExit.triggered.connect(self.close)
        # self.ui.actionShow_Grid.triggered.connect(self.model.add_filters)

        self.ui.nextTimeStep.clicked.connect(self.increment_timestep)
        self.ui.prevTimeStep.clicked.connect(self.decrement_timestep)
        self.ui.timeStepSelector.activated.connect(self.set_timestep)

        self.ui.gsSpinBox.valueChanged.connect(self.set_grid_spacing)
        self.ui.exagSpinBox.valueChanged.connect(self.set_exaggeration)

        self.ui.datasetSelector.currentTextChanged.connect(self.select_dataset)
        self.ui.colorCheckBox.stateChanged.connect(self.toggle_color_controls)
        self.ui.maskCheckBox.stateChanged.connect(self.toggle_mask_controls)
        self.ui.colorminSpinBox.editingFinished.connect(self.set_color_min)
        self.ui.colormaxSpinBox.editingFinished.connect(self.set_color_max)
        self.ui.maskminSpinBox.editingFinished.connect(self.set_mask_min)
        self.ui.maskmaxSpinBox.editingFinished.connect(self.set_mask_max)

        self.ui.xclipCheckBox.stateChanged.connect(self.toggle_xclip_controls)
        self.ui.yclipCheckBox.stateChanged.connect(self.toggle_yclip_controls)
        self.ui.zclipCheckBox.stateChanged.connect(self.toggle_zclip_controls)
        self.ui.xminSpinBox.editingFinished.connect(self.set_clip_xmin)
        self.ui.xmaxSpinBox.editingFinished.connect(self.set_clip_xmax)
        self.ui.yminSpinBox.editingFinished.connect(self.set_clip_ymin)
        self.ui.ymaxSpinBox.editingFinished.connect(self.set_clip_ymax)
        self.ui.zminSpinBox.editingFinished.connect(self.set_clip_zmin)
        self.ui.zmaxSpinBox.editingFinished.connect(self.set_clip_zmax)

        self.model.loaded_file.connect(self.toggle_control_pane)
        self.model.changed_timestep.connect(self.ui.timeStepSelector.setCurrentText)
        self.model.changed_clipping_extents.connect(self.update_extents_boxes)

    def open_file(self):
        # stackoverflow.com/a/44076057/13130795
        filename, _ = qtw.QFileDialog.getOpenFileName(self)
        if filename:
            self.model.load_file(filename)

    def toggle_control_pane(self, enable: bool):
        self.ui.controlPane.setEnabled(enable)
        self.ui.menuView.setEnabled(enable)
        if enable:
            self.ui.timeStepSelector.addItems([str(i) for i in self.model.timesteps])
            self.ui.datasetSelector.addItems(self.model.datasets)
            self.ui.gsSpinBox.setValue(self.model.grid_spacing[0])
            self.ui.exagSpinBox.setValue(self.model.exaggeration[0])
        else:
            self.ui.colorCheckBox.setChecked(enable)
            self.ui.maskCheckBox.setChecked(enable)
            self.ui.xclipCheckBox.setChecked(enable)
            self.ui.yclipCheckBox.setChecked(enable)
            self.ui.zclipCheckBox.setChecked(enable)

    def update_extents_boxes(self, extents: tuple[float]) -> None:
        self.ui.xminSpinBox.setValue(extents[0])
        self.ui.xmaxSpinBox.setValue(extents[1])
        self.ui.yminSpinBox.setValue(extents[2])
        self.ui.ymaxSpinBox.setValue(extents[3])
        self.ui.zminSpinBox.setValue(extents[4])
        self.ui.zmaxSpinBox.setValue(extents[5])

    def toggle_color_controls(self, enable: bool):
        self.ui.colorminSpinBox.setEnabled(enable)
        self.ui.colormaxSpinBox.setEnabled(enable)

    def toggle_mask_controls(self, enable: bool):
        self.ui.maskminSpinBox.setEnabled(enable)
        self.ui.maskmaxSpinBox.setEnabled(enable)

    def toggle_xclip_controls(self, enable: bool):
        self.ui.xminSpinBox.setEnabled(enable)
        self.ui.xmaxSpinBox.setEnabled(enable)
        self.model.replace_clipping_extents(indeces=[0, 1], values=[None, None])

    def toggle_yclip_controls(self, enable: bool):
        self.ui.yminSpinBox.setEnabled(enable)
        self.ui.ymaxSpinBox.setEnabled(enable)
        self.model.replace_clipping_extents(indeces=[2, 3], values=[None, None])

    def toggle_zclip_controls(self, enable: bool):
        self.ui.zminSpinBox.setEnabled(enable)
        self.ui.zmaxSpinBox.setEnabled(enable)
        self.model.replace_clipping_extents(indeces=[4, 5], values=[None, None])

    def increment_timestep(self):
        self.model.timestep_index += 1

    def decrement_timestep(self):
        self.model.timestep_index -= 1

    def set_timestep(self, new_timestep: str):
        self.model.timestep_index = int(new_timestep)

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

    def set_clip_xmin(self):
        self.model.replace_clipping_extents(
            indeces=[0], values=[self.ui.xminSpinBox.value()]
        )

    def set_clip_xmax(self):
        self.model.replace_clipping_extents(
            indeces=[1], values=[self.ui.xmaxSpinBox.value()]
        )

    def set_clip_ymin(self):
        self.model.replace_clipping_extents(
            indeces=[2], values=[self.ui.yminSpinBox.value()]
        )

    def set_clip_ymax(self):
        self.model.replace_clipping_extents(
            indeces=[3], values=[self.ui.ymaxSpinBox.value()]
        )

    def set_clip_zmin(self):
        self.model.replace_clipping_extents(
            indeces=[4], values=[self.ui.zminSpinBox.value()]
        )

    def set_clip_zmax(self):
        self.model.replace_clipping_extents(
            indeces=[5], values=[self.ui.zmaxSpinBox.value()]
        )


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    try:
        file_to_load = Path(sys.argv[1])
        assert file_to_load.is_file()
    except IndexError:
        file_to_load = None
    except:
        print(f"Could not find a file at {sys.argv[1]}")
        file_to_load = None
    finally:
        window = MainWindow(file_to_load=file_to_load)
    sys.exit(app.exec_())
