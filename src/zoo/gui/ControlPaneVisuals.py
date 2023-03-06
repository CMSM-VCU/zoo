import os
from importlib import resources

from ..ContourController import ContourController
from ..utils import COLORMAPS
from . import ui

os.environ["QT_API"] = "pyqt5"

from qtpy import QtCore as qtc
from qtpy import QtGui as qtg
from qtpy import QtWidgets as qtw
from qtpy import uic


class ControlPaneVisuals(qtw.QWidget):
    _parent = None

    def __init__(self, parent: qtw.QWidget | None = None) -> None:
        super().__init__(parent=parent)
        with resources.open_text(ui, "controlpane_visuals.ui") as uifile:
            uic.loadUi(uifile, self)

        self._parent = parent
        self.organize_widgets()
        self.hook_up_signals()

    @property
    def controller(self) -> ContourController:
        if self._parent:
            return self._parent.controller
        else:
            return None

    def _connect_contour_controller(self, controller: ContourController) -> None:
        ...

    def organize_widgets(self):
        ...

    def hook_up_signals(self):
        self.colormapSelector.currentTextChanged.connect(self.set_colormap)
        self.colormapSelector.focusOutEvent = self.tabcomplete_colormap
        self.reverseCheckBox.stateChanged.connect(self.toggle_reverse)
        self.outofrangeCheckBox.stateChanged.connect(self.toggle_outofrange_color)
        self.scalarbarvisCheckBox.stateChanged.connect(self.toggle_scalarbar_vis)
        self.scalarbarmoveCheckBox.stateChanged.connect(self.toggle_scalarbar_move)
        self.orientationvisCheckBox.stateChanged.connect(self.toggle_orientation_vis)
        self.orientationmoveCheckBox.stateChanged.connect(self.toggle_orientation_move)

        self.bgcolorFrameButton.mousePressEvent = self.pick_color_bg
        self.abovecolorFrameButton.mousePressEvent = self.pick_color_above
        self.belowcolorFrameButton.mousePressEvent = self.pick_color_below

        self.window().width_changed.connect(self.widthLineEdit.setText)
        self.window().height_changed.connect(self.heightLineEdit.setText)
        self.widthLineEdit.editingFinished.connect(self.resize_window)
        self.heightLineEdit.editingFinished.connect(self.resize_window)

        self.widthLineEdit.setValidator(qtg.QIntValidator())
        self.heightLineEdit.setValidator(qtg.QIntValidator())

        self.opacityCheckBox.stateChanged.connect(self.toggle_opacity_control)
        self.maskopacitySlider.valueChanged.connect(self.update_mask_opacity_value)
        self.clipopacitySlider.valueChanged.connect(self.update_clip_opacity_value)

    def toggle_control_pane(self, enable: bool):
        self.setEnabled(enable)
        if enable:
            self.bgcolorFrameButton.setStyleSheet(
                f"background-color: rgb{tuple(int(c*255) for c in self.controller.background_color)}"
            )

            self.colormapSelector.clear()
            self.colormapSelector.addItems(COLORMAPS)
            self.colormap_completer = qtw.QCompleter(COLORMAPS)
            self.colormap_completer.setCaseSensitivity(False)
            self.colormapSelector.setCompleter(self.colormap_completer)
            self.colormapSelector.setCurrentIndex(
                self.colormapSelector.findText("rainbow4")
            )
            self.update_mask_opacity_value()
            self.update_clip_opacity_value()

    def resize_window(self, event=None) -> None:
        self.window().view_dimensions = [
            int(self.widthLineEdit.text()),
            int(self.heightLineEdit.text()),
        ]

    def pick_color_bg(self, event=None) -> None:
        if event.button() == 1:
            self.controller.background_color = self._pick_color(
                self.bgcolorFrameButton
            )[:3]

    def set_colormap(self, _: int) -> None:
        if self.colormapSelector.currentText() in COLORMAPS:
            self.controller.lut.cmap = self.colormapSelector.currentText()

    def tabcomplete_colormap(self, event=None) -> None:
        # https://doc.qt.io/qt-5/qt.html#FocusReason-enum
        if event.reason() == 1:
            self.colormap_completer.setCompletionPrefix(
                self.colormapSelector.currentText()
            )
            self.colormapSelector.setCurrentIndex(
                self.colormapSelector.findText(
                    self.colormap_completer.currentCompletion()
                )
            )
            self.colormapSelector.setFocus(
                qtc.Qt.OtherFocusReason
            )  # Undo the standard Tab behavior

    def toggle_reverse(self, enable: bool) -> None:
        self.controller.lut.reverse = enable

    def toggle_outofrange_color(self, enable: bool) -> None:
        self.abovecolorFrameButton.setEnabled(enable)
        self.abovecolorLabel.setEnabled(enable)
        self.belowcolorFrameButton.setEnabled(enable)
        self.belowcolorLabel.setEnabled(enable)
        if enable:
            self.controller.lut.above_color = (
                self.abovecolorFrameButton.palette()
                .color(qtg.QPalette.Background)
                .name()
            )
            self.controller.lut.below_color = (
                self.belowcolorFrameButton.palette()
                .color(qtg.QPalette.Background)
                .name()
            )
        else:
            self.controller.lut.above_color = None
            self.controller.lut.below_color = None

    def pick_color_above(self, event=None) -> None:
        if event.button() == 1:
            self.controller.lut.above_color = self._pick_color(
                self.abovecolorFrameButton
            )[:3]

    def pick_color_below(self, event=None) -> None:
        if event.button() == 1:
            self.controller.lut.below_color = self._pick_color(
                self.belowcolorFrameButton
            )[:3]

    def _widget_property_toggle(self, widget: str, property_: str, state: bool) -> None:
        self.controller.set_widget_property(
            widget, property_, state, instigator=id(self)
        )

    def toggle_scalarbar_vis(self, enable: int) -> None:
        self._widget_property_toggle("scalarbar", "visible", state=bool(enable))

    def toggle_scalarbar_move(self, enable: int) -> None:
        self._widget_property_toggle("scalarbar", "movable", state=bool(enable))

    def toggle_orientation_vis(self, enable: int) -> None:
        self._widget_property_toggle("orientation", "visible", state=bool(enable))

    def toggle_orientation_move(self, enable: int) -> None:
        self._widget_property_toggle("orientation", "movable", state=bool(enable))

    def toggle_opacity_control(self, enable: bool) -> None:
        self.opacitycontrolFrame.setEnabled(enable)
        self.controller.set_opacity_enabled(enable, instigator=id(self))
        if enable:
            self.update_mask_opacity_value()
            self.update_clip_opacity_value()
        else:
            self.controller.set_mask_opacity(0.0, instigator=id(self))
            self.controller.set_clip_opacity(0.0, instigator=id(self))

    def update_mask_opacity_value(self, _=None) -> None:
        self.maskopacityvalueLabel.setText(f"{self.maskopacitySlider.value()*5}%")
        self.controller.set_mask_opacity(
            self.maskopacitySlider.value() / self.maskopacitySlider.maximum(),
            instigator=id(self),
        )

    def update_clip_opacity_value(self, _=None) -> None:
        self.clipopacityvalueLabel.setText(f"{self.clipopacitySlider.value()*5}%")
        self.controller.set_clip_opacity(
            self.clipopacitySlider.value() / self.clipopacitySlider.maximum(),
            instigator=id(self),
        )

    @staticmethod
    def _pick_color(button) -> tuple:
        color = qtw.QColorDialog.getColor()
        button.setStyleSheet(f"background-color: rgb{color.getRgb()[:3]}")
        return color.getRgbF()
