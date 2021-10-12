import os
import typing
from functools import partial
from pathlib import Path

import pyperclip

from .ui.zoo_ui import Ui_MainWindow
from .VTK_PVH5Model import VTK_PVH5Model

os.environ["QT_API"] = "pyqt5"

from qtpy import QtCore as qtc
from qtpy import QtGui as qtg
from qtpy import QtWidgets as qtw


class MainWindow(qtw.QMainWindow):
    _model: VTK_PVH5Model = None

    def __init__(self, parent=None, show=True, file_to_load=None) -> None:
        super().__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._base_window_title = self.windowTitle()

        self._generate_method_lists()
        self.organize_widgets()
        self.hook_up_signals()
        self.toggle_control_pane(enable=False)

        if show:
            self.show()

        if file_to_load is not None:
            self.open_file(override=file_to_load)

    @property
    def model(self) -> VTK_PVH5Model:
        return self._model

    @model.setter
    def model(self, model: VTK_PVH5Model) -> None:
        if self._model:
            del self._model
        self._model = model

        model.plotter.setParent(self.ui.viewport)
        if self.ui.viewport.layout().count() != 0:
            old = self.ui.viewport.layout().takeAt(0)
            del old
        self.ui.viewport.layout().addWidget(model.plotter.interactor)

        model.loaded_file.connect(self.toggle_control_pane)
        model.changed_timestep.connect(self.ui.timeStepSelector.setCurrentText)
        model.changed_timestep.connect(self.update_time_value)
        model.changed_mask_dataset.connect(self.ui.maskdatasetSelector.setCurrentText)
        model.program_changed_clipping_extents.connect(self.update_extents_boxes)
        model.program_changed_colorbar_limits.connect(self.update_colorlimit_boxes)
        model.program_changed_mask_limits.connect(self.update_masklimit_boxes)
        model.moved_camera.connect(self.update_camera_readout)

    def organize_widgets(self):
        self.actions = {"open": self.ui.actionOpen, "exit": self.ui.actionExit}

        self.gs_lineedits = (
            self.ui.xgsLineEdit,
            self.ui.ygsLineEdit,
            self.ui.zgsLineEdit,
        )
        self.exag_spinboxes = (
            self.ui.xexagSpinBox,
            self.ui.yexagSpinBox,
            self.ui.zexagSpinBox,
        )
        self.color_lineedits = (self.ui.colorminLineEdit, self.ui.colormaxLineEdit)
        self.mask_lineedits = (self.ui.maskminLineEdit, self.ui.maskmaxLineEdit)
        self.clip_lineedits = (
            self.ui.xminLineEdit,
            self.ui.xmaxLineEdit,
            self.ui.yminLineEdit,
            self.ui.ymaxLineEdit,
            self.ui.zminLineEdit,
            self.ui.zmaxLineEdit,
        )
        self.clip_checkboxes = (
            self.ui.xclipCheckBox,
            self.ui.yclipCheckBox,
            self.ui.zclipCheckBox,
        )

    def hook_up_signals(self):
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave_Image.triggered.connect(self.save_image)
        self.ui.actionExit.triggered.connect(self.close)

        self.ui.nextTimeStep.clicked.connect(self.increment_timestep)
        self.ui.prevTimeStep.clicked.connect(self.decrement_timestep)
        self.ui.timeStepSelector.activated.connect(self.set_timestep)

        self.ui.gsLockButton.toggled.connect(self.toggle_uniform_gs)
        self.ui.xgsLineEdit.textEdited.connect(self.set_grid_spacing_uniform)

        self.ui.exagLockButton.toggled.connect(self.toggle_uniform_exag)
        self.ui.xexagSpinBox.valueChanged.connect(self.set_exaggeration_uniform)

        self.ui.plotdatasetSelector.activated.connect(self.select_plot_dataset)
        self.ui.colorCheckBox.stateChanged.connect(self.toggle_color_controls)
        self.ui.colorminLineEdit.textEdited.connect(self.set_color_min)
        self.ui.colormaxLineEdit.textEdited.connect(self.set_color_max)

        self.ui.maskdatasetLockButton.toggled.connect(self.toggle_maskplot_lock)
        self.ui.maskdatasetSelector.activated.connect(self.select_mask_dataset)
        self.ui.maskCheckBox.stateChanged.connect(self.toggle_mask_controls)
        self.ui.maskminLineEdit.textEdited.connect(self.set_mask_min)
        self.ui.maskmaxLineEdit.textEdited.connect(self.set_mask_max)

        self.ui.xclipCheckBox.stateChanged.connect(self.toggle_xclip_controls)
        self.ui.yclipCheckBox.stateChanged.connect(self.toggle_yclip_controls)
        self.ui.zclipCheckBox.stateChanged.connect(self.toggle_zclip_controls)
        for i, box in enumerate(self.clip_lineedits):
            box.textEdited.connect(self.set_clipping_extent[i])

        # QGroupBox only emits clicked signal if it is checkable. Bypass this by
        # binding directly to the mousePressEvent.
        self.ui.cameraLocationGroup.mousePressEvent = self.copy_camera_location

        self.ui.xgsLineEdit.setValidator(qtg.QDoubleValidator())
        self.ui.ygsLineEdit.setValidator(qtg.QDoubleValidator())
        self.ui.zgsLineEdit.setValidator(qtg.QDoubleValidator())

        self.ui.ygsLineEdit.setVisible(False)
        self.ui.zgsLineEdit.setVisible(False)

        self.ui.yexagSpinBox.setVisible(False)
        self.ui.zexagSpinBox.setVisible(False)

    def open_file(self, *, override=None):
        # stackoverflow.com/a/44076057/13130795
        if not override:
            filename, _ = qtw.QFileDialog.getOpenFileName(self)
        else:
            filename = override
        if filename:
            self.model = VTK_PVH5Model()
            self.model.load_file(Path(filename))
            self.setWindowTitle(f"{Path(filename).name} - {self._base_window_title}")

    def toggle_control_pane(self, enable: bool):
        self.ui.controlPane.setEnabled(enable)
        self.ui.menuView.setEnabled(enable)
        if enable:
            self.ui.timeStepSelector.clear()
            self.ui.timeStepSelector.addItems([str(i) for i in self.model.timesteps])
            self.update_time_value()

            self.ui.plotdatasetSelector.clear()
            self.ui.plotdatasetSelector.addItems(self.model.datasets)
            self.ui.maskdatasetSelector.clear()
            self.ui.maskdatasetSelector.addItems(self.model.datasets)

            self.ui.xgsLineEdit.setText(str(self.model.grid_spacing[0]))
            self.ui.xexagSpinBox.setValue(self.model.exaggeration[0])
        else:
            self.ui.colorCheckBox.setChecked(enable)
            self.ui.maskCheckBox.setChecked(enable)
            self.ui.xclipCheckBox.setChecked(enable)
            self.ui.yclipCheckBox.setChecked(enable)
            self.ui.zclipCheckBox.setChecked(enable)

    @staticmethod
    def _template_toggle_uniform_vector_spinbox(
        spinboxes: typing.List,
        component_funcs: typing.List[typing.Callable],
        uniform_func: typing.Callable,
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

    @staticmethod
    def _template_toggle_uniform_vector_lineedit(
        lineedits: typing.List,
        component_funcs: typing.List[typing.Callable],
        uniform_func: typing.Callable,
        enable: bool,
    ) -> None:
        if enable:
            for lineedit in lineedits:
                lineedit.textEdited.disconnect()

            lineedits[0].textEdited.connect(uniform_func)
            lineedits[0].textEdited.emit(lineedits[0].text())
        else:
            for lineedit in lineedits[1:]:
                lineedit.setText(lineedits[0].text())

            lineedits[0].textEdited.disconnect()
            for i, box in enumerate(lineedits):
                box.textEdited.connect(component_funcs[i])

        for lineedit in lineedits[1:]:
            lineedit.setVisible(not enable)

    def toggle_uniform_gs(self, enable: bool) -> None:
        self._template_toggle_uniform_vector_lineedit(
            lineedits=self.gs_lineedits,
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

    def update_extents_boxes(self, extents: typing.Tuple[float]) -> None:
        for i, extent in enumerate(extents):
            if not self.clip_checkboxes[i // 2].isChecked():
                self.clip_lineedits[i].setText(str(extent))

    def update_colorlimit_boxes(self, limits: typing.Tuple[float]) -> None:
        if not self.ui.colorCheckBox.isChecked():
            self.ui.colorminLineEdit.setText(str(limits[0]))
            self.ui.colormaxLineEdit.setText(str(limits[1]))

    def update_masklimit_boxes(self, limits: typing.Tuple[float]) -> None:
        if not self.ui.maskCheckBox.isChecked():
            self.ui.maskminLineEdit.setText(str(limits[0]))
            self.ui.maskmaxLineEdit.setText(str(limits[1]))

    def toggle_color_controls(self, enable: bool):
        self.ui.colorminLineEdit.setEnabled(enable)
        self.ui.colormaxLineEdit.setEnabled(enable)
        if not enable:
            self.model.colorbar_limits = None

    def toggle_mask_controls(self, enable: bool):
        self.ui.maskminLineEdit.setEnabled(enable)
        self.ui.maskmaxLineEdit.setEnabled(enable)
        if not enable:
            self.model.mask_limits = None

    def toggle_xclip_controls(self, enable: bool):
        self.ui.xminLineEdit.setEnabled(enable)
        self.ui.xmaxLineEdit.setEnabled(enable)
        self.model.replace_clipping_extents(indeces=[0, 1], values=[None, None])

    def toggle_yclip_controls(self, enable: bool):
        self.ui.yminLineEdit.setEnabled(enable)
        self.ui.ymaxLineEdit.setEnabled(enable)
        self.model.replace_clipping_extents(indeces=[2, 3], values=[None, None])

    def toggle_zclip_controls(self, enable: bool):
        self.ui.zminLineEdit.setEnabled(enable)
        self.ui.zmaxLineEdit.setEnabled(enable)
        self.model.replace_clipping_extents(indeces=[4, 5], values=[None, None])

    def increment_timestep(self):
        self.model.timestep_index += 1

    def decrement_timestep(self):
        self.model.timestep_index -= 1

    def set_timestep(self, new_timestep: str):
        self.model.timestep_index = int(new_timestep)

    def select_plot_dataset(self, _=None, *, override: str = None):
        self.model.plot_dataset = (
            override
            if override is not None
            else self.ui.plotdatasetSelector.currentText()
        )

    def select_mask_dataset(self, _=None, *, override: str = None):
        self.model.mask_dataset = (
            override
            if override is not None
            else self.ui.maskdatasetSelector.currentText()
        )

    def toggle_maskplot_lock(self, enable: bool):
        self.ui.maskdatasetSelector.setEnabled(not enable)
        self.model.plot_and_mask_same_dataset = enable
        if enable:
            self.select_mask_dataset(override=self.ui.plotdatasetSelector.currentText())
        else:
            self.select_mask_dataset()

    def set_color_min(self, _=None):
        if self.ui.colorCheckBox.isChecked():
            self.model.colorbar_limits = [
                float_or_zero(self.color_lineedits[0].text()),
                self.model.colorbar_limits[1],
            ]

    def set_color_max(self, _=None):
        if self.ui.colorCheckBox.isChecked():
            self.model.colorbar_limits = [
                self.model.colorbar_limits[0],
                float_or_zero(self.color_lineedits[1].text()),
            ]

    def set_mask_min(self, _=None):
        if self.ui.maskCheckBox.isChecked():
            self.model.mask_limits = [
                float_or_zero(self.mask_lineedits[0].text()),
                self.model.mask_limits[1],
            ]

    def set_mask_max(self, _=None):
        if self.ui.maskCheckBox.isChecked():
            self.model.mask_limits = [
                self.model.mask_limits[0],
                float_or_zero(self.mask_lineedits[1].text()),
            ]

    @staticmethod
    def set_clipping_extent_n(obj, index: int):
        if obj.clip_checkboxes[index // 2].isChecked():
            obj.model.replace_clipping_extents(
                indeces=[index],
                values=[float_or_zero(obj.clip_lineedits[index].text())],
            )

    @staticmethod
    def set_grid_spacing_n(obj, index):
        gs_vector = obj.model.grid_spacing
        gs_vector[index] = float_or_zero(obj.gs_lineedits[index].text())
        obj.model.grid_spacing = gs_vector

    def set_grid_spacing_uniform(self, new_gs: str) -> None:
        self.model.grid_spacing = [float_or_zero(new_gs)] * 3

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

    def update_camera_readout(self, data: typing.List) -> None:
        pos = data[0]
        foc = data[1]
        up = data[2]
        self.ui.positionValue.setText(f"{pos[0]:.2f}, {pos[1]:.2f}, {pos[2]:.2f}")
        self.ui.focalValue.setText(f"{foc[0]:.2f}, {foc[1]:.2f}, {foc[2]:.2f}")
        self.ui.viewupValue.setText(f"{up[0]:.2f}, {up[1]:.2f}, {up[2]:.2f}")

    def update_time_value(self, _=None) -> None:
        try:
            time = self.model.time
            self.ui.timeLabel.setText(f"{time:.3e}")
            self.ui.timeLabel.setToolTip(f"{time:.8e}")
        except TypeError:
            self.ui.timeLabel.setText("not found")

    def copy_camera_location(self, _=None) -> None:
        print("Copied!")
        pyperclip.copy(str(self.model.camera_location))

    def save_image(self, _=None) -> None:
        filename, _ = qtw.QFileDialog.getSaveFileName(self, filter="PNG (*.png)")
        if filename:
            self.model.save_image(filename)


def float_or_zero(string: str) -> float:
    try:
        return float(string)
    except ValueError:
        return 0.0
    except Exception as err:
        raise err
