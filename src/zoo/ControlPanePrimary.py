import ast
import os
import typing
from functools import partial
from importlib import resources
from loguru import logger

import pyperclip

from . import ui
from .ContourController import ContourController
from .utils import truncate_int8_to_int4

os.environ["QT_API"] = "pyqt5"

from qtpy import QtCore as qtc
from qtpy import QtGui as qtg
from qtpy import QtWidgets as qtw
from qtpy import uic


class ControlPanePrimary(qtw.QWidget):
    _parent = None

    def __init__(self, parent: typing.Optional["qtw.QWidget"] = None,) -> None:
        super().__init__(parent=parent)
        with resources.open_text(ui, "controlpane_primary.ui") as uifile:
            uic.loadUi(uifile, self)

        self._parent = parent
        self._generate_method_lists()
        self.organize_widgets()
        self.hook_up_signals()

    @property
    def controller(self) -> ContourController:
        if self._parent:
            return self._parent.controller
        else:
            return None

    def _connect_contour_controller(self, controller: ContourController) -> None:
        controller.changed_timestep.connect(self.update_timestep_value)
        controller.changed_time.connect(self.update_time_value)
        controller.changed_mask_dataset.connect(self.update_maskdataset_box)
        controller.changed_clipping_extents.connect(self.update_extents_boxes)
        controller.changed_colorbar_limits.connect(self.update_colorlimit_boxes)
        controller.changed_mask_limits.connect(self.update_masklimit_boxes)
        controller.moved_camera.connect(self.update_camera_readout)

    def organize_widgets(self):
        self.gs_lineedits = (
            self.xgsLineEdit,
            self.ygsLineEdit,
            self.zgsLineEdit,
        )
        self.exag_spinboxes = (
            self.xexagSpinBox,
            self.yexagSpinBox,
            self.zexagSpinBox,
        )
        self.color_lineedits = (self.colorminLineEdit, self.colormaxLineEdit)
        self.mask_lineedits = (self.maskminLineEdit, self.maskmaxLineEdit)
        self.clip_lineedits = (
            self.xminLineEdit,
            self.xmaxLineEdit,
            self.yminLineEdit,
            self.ymaxLineEdit,
            self.zminLineEdit,
            self.zmaxLineEdit,
        )
        self.clip_checkboxes = (
            self.xclipCheckBox,
            self.yclipCheckBox,
            self.zclipCheckBox,
        )

    def hook_up_signals(self):
        self.nextTimeStep.clicked.connect(self.increment_timestep)
        self.prevTimeStep.clicked.connect(self.decrement_timestep)
        self.timeStepSelector.activated.connect(self.set_timestep)

        self.gsLockButton.toggled.connect(self.toggle_uniform_gs)
        self.xgsLineEdit.textEdited.connect(self.set_grid_spacing_uniform)

        self.exagLockButton.toggled.connect(self.toggle_uniform_exag)
        self.xexagSpinBox.valueChanged.connect(self.set_exaggeration_uniform)

        self.plotdatasetSelector.activated.connect(self.select_plot_dataset)
        self.colorCheckBox.stateChanged.connect(self.toggle_color_controls)
        self.colorminLineEdit.textEdited.connect(self.set_color_min)
        self.colormaxLineEdit.textEdited.connect(self.set_color_max)

        self.maskdatasetLockButton.toggled.connect(self.toggle_maskplot_lock)
        self.maskdatasetSelector.activated.connect(self.select_mask_dataset)
        self.maskCheckBox.stateChanged.connect(self.toggle_mask_controls)
        self.maskminLineEdit.textEdited.connect(self.set_mask_min)
        self.maskmaxLineEdit.textEdited.connect(self.set_mask_max)

        self.xclipCheckBox.stateChanged.connect(self.toggle_xclip_controls)
        self.yclipCheckBox.stateChanged.connect(self.toggle_yclip_controls)
        self.zclipCheckBox.stateChanged.connect(self.toggle_zclip_controls)
        self.clippingboxButton.toggled.connect(self.toggle_clipping_box)
        for i, box in enumerate(self.clip_lineedits):
            box.textEdited.connect(self.set_clipping_extent[i])
            box.defaultMousePressEvent = box.mousePressEvent
            box.mousePressEvent = lambda x, b=box: select_all_wrapper(b, event=x)

        # QGroupBox only emits clicked signal if it is checkable. Bypass this by
        # binding directly to the mousePressEvent.
        self.cameraLocationGroup.mousePressEvent = self.copypaste_camera_location

        self.xgsLineEdit.setValidator(qtg.QDoubleValidator())
        self.ygsLineEdit.setValidator(qtg.QDoubleValidator())
        self.zgsLineEdit.setValidator(qtg.QDoubleValidator())

        self.ygsLineEdit.setVisible(False)
        self.zgsLineEdit.setVisible(False)

        self.yexagSpinBox.setVisible(False)
        self.zexagSpinBox.setVisible(False)

    def toggle_control_pane(self, enable: bool):
        self.setEnabled(enable)
        if enable:
            self.timeStepSelector.clear()
            self.timeStepSelector.addItems(
                [str(i) for i in self.controller.model.timesteps]
            )
            # self.update_time_value()

            self.plotdatasetSelector.clear()
            self.plotdatasetSelector.addItems(self.controller.model.datasets)
            self.maskdatasetSelector.clear()
            self.maskdatasetSelector.addItems(self.controller.model.datasets)

            self.xgsLineEdit.setText(str(self.controller.glyph_size[0]))
            self.xexagSpinBox.setValue(self.controller.exaggeration[0])
        else:
            self.colorCheckBox.setChecked(enable)
            self.maskCheckBox.setChecked(enable)
            self.xclipCheckBox.setChecked(enable)
            self.yclipCheckBox.setChecked(enable)
            self.zclipCheckBox.setChecked(enable)

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

    def update_maskdataset_box(self, mask_dataset: str, instigator: int) -> None:
        if instigator == truncate_int8_to_int4(id(self)):
            return

        self.maskdatasetSelector.setCurrentText(mask_dataset)

    def update_extents_boxes(
        self, clipping_extents: typing.Tuple, instigator: int
    ) -> None:
        if instigator == truncate_int8_to_int4(id(self)):
            return

        for i, extent in enumerate(clipping_extents):
            if not self.clip_checkboxes[i // 2].isChecked():
                self.clip_lineedits[i].setText(f"{extent:.4g}")
            else:
                self.set_clipping_extent[i]()

    def update_colorlimit_boxes(
        self, colorbar_limits: typing.Tuple, instigator: int
    ) -> None:
        if instigator == truncate_int8_to_int4(id(self)):
            return

        if not self.colorCheckBox.isChecked():
            self.colorminLineEdit.setText(str(colorbar_limits[0]))
            self.colormaxLineEdit.setText(str(colorbar_limits[1]))
        else:
            self.set_color_min()
            self.set_color_max()

    def update_masklimit_boxes(
        self, mask_limits: typing.Tuple, instigator: int
    ) -> None:
        if instigator == truncate_int8_to_int4(id(self)):
            return

        if not self.maskCheckBox.isChecked():
            self.maskminLineEdit.setText(str(mask_limits[0]))
            self.maskmaxLineEdit.setText(str(mask_limits[1]))
        else:
            self.set_mask_min()
            self.set_mask_max()

    def toggle_color_controls(self, enable: bool):
        self.colorminLineEdit.setEnabled(enable)
        self.colormaxLineEdit.setEnabled(enable)
        if not enable:
            self.controller.set_colorbar_limits(None, instigator=id(self))
        else:
            self.set_color_min()
            self.set_color_max()

    def toggle_mask_controls(self, enable: bool):
        self.maskminLineEdit.setEnabled(enable)
        self.maskmaxLineEdit.setEnabled(enable)
        if not enable:
            self.controller.set_mask_limits(None, instigator=id(self))
        else:
            self.set_mask_min()
            self.set_mask_max()

    def toggle_xclip_controls(self, enable: bool):
        self.xminLineEdit.setEnabled(enable)
        self.xmaxLineEdit.setEnabled(enable)
        if not enable:
            self.controller.replace_clipping_extents(
                indeces=[0, 1], values=[None, None], instigator=id(self)
            )
        else:
            self.set_clipping_extent[0]()
            self.set_clipping_extent[1]()

    def toggle_yclip_controls(self, enable: bool):
        self.yminLineEdit.setEnabled(enable)
        self.ymaxLineEdit.setEnabled(enable)
        if not enable:
            self.controller.replace_clipping_extents(
                indeces=[2, 3], values=[None, None], instigator=id(self)
            )
        else:
            self.set_clipping_extent[2]()
            self.set_clipping_extent[3]()

    def toggle_zclip_controls(self, enable: bool):
        self.zminLineEdit.setEnabled(enable)
        self.zmaxLineEdit.setEnabled(enable)
        if not enable:
            self.controller.replace_clipping_extents(
                indeces=[4, 5], values=[None, None], instigator=id(self)
            )
        else:
            self.set_clipping_extent[4]()
            self.set_clipping_extent[5]()

    def increment_timestep(self):
        self.controller.increment_timestep(instigator=id(self))

    def decrement_timestep(self):
        self.controller.decrement_timestep(instigator=id(self))

    def set_timestep(self, new_timestep: str):
        self.controller.set_timestep_index(int(new_timestep), instigator=id(self))

    def select_plot_dataset(self, _=None, *, override: str = None):
        logger.debug(
            f"Selected plot dataset {self.plotdatasetSelector.currentText()} overridden by {override}"
        )
        new_set = (
            override if override is not None else self.plotdatasetSelector.currentText()
        )
        self.controller.set_plot_dataset(new_set, instigator=id(self))

    def select_mask_dataset(self, _=None, *, override: str = None):
        logger.debug(
            f"Selected mask dataset {self.maskdatasetSelector.currentText()} overridden by {override}"
        )
        new_set = (
            override if override is not None else self.maskdatasetSelector.currentText()
        )
        self.controller.set_mask_dataset(new_set, instigator=id(self))

    def toggle_maskplot_lock(self, enable: bool):
        self.maskdatasetSelector.setEnabled(not enable)
        self.controller.plot_and_mask_same_dataset = enable
        if enable:
            self.select_mask_dataset(override=self.plotdatasetSelector.currentText())
        else:
            self.select_mask_dataset()

    def set_color_min(self, _=None):
        if self.colorCheckBox.isChecked():
            self.controller.set_colorbar_limits(
                [
                    float_or_zero(self.color_lineedits[0].text()),
                    self.controller.colorbar_limits[1],
                ],
                instigator=id(self),
            )

    def set_color_max(self, _=None):
        if self.colorCheckBox.isChecked():
            self.controller.set_colorbar_limits(
                [
                    self.controller.colorbar_limits[0],
                    float_or_zero(self.color_lineedits[1].text()),
                ],
                instigator=id(self),
            )

    def set_mask_min(self, _=None):
        if self.maskCheckBox.isChecked():
            self.controller.set_mask_limits(
                [
                    float_or_zero(self.mask_lineedits[0].text()),
                    self.controller.mask_limits[1],
                ],
                instigator=id(self),
            )

    def set_mask_max(self, _=None):
        if self.maskCheckBox.isChecked():
            self.controller.set_mask_limits(
                [
                    self.controller.mask_limits[0],
                    float_or_zero(self.mask_lineedits[1].text()),
                ],
                instigator=id(self),
            )

    @staticmethod
    def set_clipping_extent_n(obj, index: int):
        if obj.clip_checkboxes[index // 2].isChecked():
            obj.controller.replace_clipping_extents(
                indeces=[index],
                values=[float_or_zero(obj.clip_lineedits[index].text())],
                instigator=id(obj),
            )

    @staticmethod
    def set_grid_spacing_n(obj, index):
        gs_vector = list(obj.controller.glyph_size)
        gs_vector[index] = float_or_zero(obj.gs_lineedits[index].text())
        obj.controller.set_glyph_size(gs_vector, instigator=id(obj))

    def set_grid_spacing_uniform(self, new_gs: str) -> None:
        self.controller.set_glyph_size([float_or_zero(new_gs)] * 3, instigator=id(self))

    @staticmethod
    def set_exaggeration_n(obj, index):
        new_exag = list(obj.controller.exaggeration)
        new_exag[index] = obj.exag_spinboxes[index].value()
        obj.controller.set_exaggeration(new_exag, instigator=id(obj))

    def set_exaggeration_uniform(self, new_exag: float) -> None:
        self.controller.set_exaggeration([new_exag] * 3, instigator=id(self))

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

    def update_camera_readout(
        self, camera_location: typing.List, instigator: int
    ) -> None:
        pos = camera_location[0]
        foc = camera_location[1]
        up = camera_location[2]
        self.positionValue.setText(f"{pos[0]:.2f}, {pos[1]:.2f}, {pos[2]:.2f}")
        self.focalValue.setText(f"{foc[0]:.2f}, {foc[1]:.2f}, {foc[2]:.2f}")
        self.viewupValue.setText(f"{up[0]:.2f}, {up[1]:.2f}, {up[2]:.2f}")

    def update_timestep_value(self, timestep: int, instigator=None) -> None:
        self.timeStepSelector.setCurrentText(str(timestep))

    def update_time_value(self, time: float, instigator=None) -> None:
        try:
            self.timeLabel.setText(f"{time:.3e}")
            self.timeLabel.setToolTip(f"{time:.8e}")
        except TypeError:
            self.timeLabel.setText("not found")

    def copypaste_camera_location(self, event=None) -> None:
        if event.button() == 1:
            print("Copied!")
            pyperclip.copy(str(self.controller.camera_location))
        elif event.button() == 2:
            try:
                paste_data = ast.literal_eval(pyperclip.paste().strip())
                assert (
                    isinstance(paste_data, typing.Iterable) and len(paste_data) == 3
                ), "Paste data must contain 3 items."
                assert all(
                    isinstance(item, typing.Iterable) and len(item) == 3
                    for item in paste_data
                ), "Each item in paste data must be a vector of length 3."
            except (SyntaxError, ValueError):
                print("Bad paste data - syntax")
            except AssertionError as err:
                print(err)
            else:
                self.controller.camera_location = paste_data
                self.controller.moved_camera.emit(
                    self.controller.camera_location, id(self)
                )
                self.update_camera_readout(self.controller.camera_location, instigator=id(self))
                print("Pasted!")

    def toggle_clipping_box(self, enable: bool):
        self.controller.toggle_clipping_box(enable)


def select_all_wrapper(box, event):
    if not box.isModified() and not box.hasSelectedText():
        box.selectAll()
    else:
        box.defaultMousePressEvent(event)


def float_or_zero(string: str) -> float:
    try:
        return float(string)
    except ValueError:
        return 0.0
    except Exception as err:
        raise err
