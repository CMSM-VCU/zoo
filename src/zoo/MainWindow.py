import os
import sys
from functools import partial
from pathlib import Path
from typing import Callable

from PyVistaH5Model import PyVistaH5Model
from ui.zoo_ui import Ui_MainWindow
from VTK_PVH5Model import VTK_PVH5Model

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

        self._generate_method_lists()
        self.organize_widgets()
        self.hook_up_signals()
        self.toggle_control_pane(enable=False)

        if show:
            self.show()

        if file_to_load is not None:
            self.model.load_file(file_to_load)

    def organize_widgets(self):
        self.actions = {"open": self.ui.actionOpen, "exit": self.ui.actionExit}

        self.gs_spinboxes = (self.ui.xgsSpinBox, self.ui.ygsSpinBox, self.ui.zgsSpinBox)
        self.exag_spinboxes = (
            self.ui.xexagSpinBox,
            self.ui.yexagSpinBox,
            self.ui.zexagSpinBox,
        )
        self.color_spinboxes = (self.ui.colorminSpinBox, self.ui.colormaxSpinBox)
        self.mask_spinboxes = (self.ui.maskminSpinBox, self.ui.maskmaxSpinBox)
        self.clip_spinboxes = (
            self.ui.xminSpinBox,
            self.ui.xmaxSpinBox,
            self.ui.yminSpinBox,
            self.ui.ymaxSpinBox,
            self.ui.zminSpinBox,
            self.ui.zmaxSpinBox,
        )

    def hook_up_signals(self):
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionExit.triggered.connect(self.close)
        # self.ui.actionShow_Grid.triggered.connect(self.model.add_filters)

        self.ui.nextTimeStep.clicked.connect(self.increment_timestep)
        self.ui.prevTimeStep.clicked.connect(self.decrement_timestep)
        self.ui.timeStepSelector.activated.connect(self.set_timestep)

        self.ui.gsLockButton.toggled.connect(self.toggle_uniform_gs)
        self.ui.xgsSpinBox.valueChanged.connect(self.set_grid_spacing_uniform)

        self.ui.exagLockButton.toggled.connect(self.toggle_uniform_exag)
        self.ui.xexagSpinBox.valueChanged.connect(self.set_exaggeration_uniform)

        self.ui.datasetSelector.currentTextChanged.connect(self.select_dataset)
        self.ui.colorCheckBox.stateChanged.connect(self.toggle_color_controls)
        self.ui.maskCheckBox.stateChanged.connect(self.toggle_mask_controls)
        self.ui.colorminSpinBox.editingFinished.connect(self.set_color_min)
        self.ui.colormaxSpinBox.editingFinished.connect(self.set_color_max)
        self.ui.maskminSpinBox.valueChanged.connect(self.set_mask_min)
        self.ui.maskmaxSpinBox.valueChanged.connect(self.set_mask_max)

        self.ui.xclipCheckBox.stateChanged.connect(self.toggle_xclip_controls)
        self.ui.yclipCheckBox.stateChanged.connect(self.toggle_yclip_controls)
        self.ui.zclipCheckBox.stateChanged.connect(self.toggle_zclip_controls)
        for i, box in enumerate(self.clip_spinboxes):
            box.editingFinished.connect(self.set_clipping_extent[i])

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
            self.ui.xgsSpinBox.setValue(self.model.grid_spacing[0])
            self.ui.xexagSpinBox.setValue(self.model.exaggeration[0])
        else:
            self.ui.colorCheckBox.setChecked(enable)
            self.ui.maskCheckBox.setChecked(enable)
            self.ui.xclipCheckBox.setChecked(enable)
            self.ui.yclipCheckBox.setChecked(enable)
            self.ui.zclipCheckBox.setChecked(enable)

    @staticmethod
    def _template_toggle_uniform_vector_spinbox(
        spinboxes: list,
        component_funcs: list[Callable],
        uniform_func: Callable,
        enable: bool,
    ) -> None:
        if enable:
            for spinbox in spinboxes:
                spinbox.valueChanged.disconnect()

            spinboxes[0].valueChanged.connect(uniform_func)
            spinboxes[0].valueChanged.emit(spinboxes[0].value())
        else:
            for spinbox in spinboxes[1:]:
                spinbox.setValue(spinboxes[0].value())

            spinboxes[0].valueChanged.disconnect()
            for i, box in enumerate(spinboxes):
                box.valueChanged.connect(component_funcs[i])

        for spinbox in spinboxes[1:]:
            spinbox.setVisible(not enable)

    def toggle_uniform_gs(self, enable: bool) -> None:
        self._template_toggle_uniform_vector_spinbox(
            spinboxes=self.gs_spinboxes,
            component_funcs=self.set_grid_spacing,
            uniform_func=self.set_grid_spacing_uniform,
            enable=enable,
        )

    def toggle_uniform_exag(self, enable: bool) -> None:
        self._template_toggle_uniform_vector_spinbox(
            spinboxes=self.exag_spinboxes,
            component_funcs=self.set_exaggeration,
            uniform_func=self.set_exaggeration_uniform,
            enable=enable,
        )

    def update_extents_boxes(self, extents: tuple[float]) -> None:
        for i, extent in enumerate(extents):
            self.clip_spinboxes[i].setValue(extent)

    def toggle_color_controls(self, enable: bool):
        self.ui.colorminSpinBox.setEnabled(enable)
        self.ui.colormaxSpinBox.setEnabled(enable)

    def toggle_mask_controls(self, enable: bool):
        self.ui.maskminSpinBox.setEnabled(enable)
        self.ui.maskmaxSpinBox.setEnabled(enable)
        if not enable:
            self.model.contour_threshold = None

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

    def select_dataset(self, new_dataset: str):
        self.model.dataset = new_dataset

    def set_color_min(self, value: float):
        print("set_color_min", value)

    def set_color_max(self, value: float):
        print("set_color_max", value)

    def set_mask_min(self, _=None):
        self.model.contour_threshold = [
            self.mask_spinboxes[0].value(),
            self.model.contour_threshold[1],
        ]

    def set_mask_max(self, _=None):
        self.model.contour_threshold = [
            self.model.contour_threshold[0],
            self.mask_spinboxes[1].value(),
        ]

    def set_clipping_extent_n(self, index: int):
        self.model.replace_clipping_extents(
            indeces=[index], values=[self.clip_spinboxes[index]]
        )

    @staticmethod
    def set_grid_spacing_n(obj, index):
        new_gs = obj.model.grid_spacing
        new_gs[index] = obj.gs_spinboxes[index].value()
        obj.model.grid_spacing = new_gs

    def set_grid_spacing_uniform(self, new_gs: float) -> None:
        self.model.grid_spacing = [new_gs] * 3

    @staticmethod
    def set_exaggeration_n(obj, index):
        new_exag = obj.model.exaggeration
        new_exag[index] = obj.exag_spinboxes[index].value()
        obj.model.exaggeration = new_exag

    def set_exaggeration_uniform(self, new_exag: float) -> None:
        self.model.exaggeration = [new_exag] * 3

    def _generate_method_lists(self) -> None:
        self.set_grid_spacing = tuple(
            partial(self.set_grid_spacing_n, self, i) for i in range(3)
        )
        self.set_exaggeration = tuple(
            partial(self.set_exaggeration_n, self, i) for i in range(3)
        )
        self.set_clipping_extent = tuple(
            partial(self.set_clipping_extent_n, self, i) for i in range(6)
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
