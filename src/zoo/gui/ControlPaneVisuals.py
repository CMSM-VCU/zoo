
from qtpy import QtCore as qtc
from qtpy import QtGui as qtg
from qtpy import QtWidgets as qtw

from ..ContourController import ContourController
from ..utils import COLORMAPS
from .ui.controlpane_visuals import Ui_ControlPane_Visuals


class ControlPaneVisuals(qtw.QWidget):
    _parent = None

    def __init__(self, parent: qtw.QWidget | None = None) -> None:
        super().__init__(parent=parent)
        self.ui = Ui_ControlPane_Visuals()
        self.ui.setupUi(self)

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
        self.ui.colormapSelector.currentTextChanged.connect(self.set_colormap)
        self.ui.colormapSelector.focusOutEvent = self.tabcomplete_colormap
        self.ui.reverseCheckBox.stateChanged.connect(self.toggle_reverse)
        self.ui.outofrangeCheckBox.stateChanged.connect(self.toggle_outofrange_color)
        self.ui.scalarbarvisCheckBox.stateChanged.connect(self.toggle_scalarbar_vis)
        self.ui.scalarbarmoveCheckBox.stateChanged.connect(self.toggle_scalarbar_move)
        self.ui.orientationvisCheckBox.stateChanged.connect(self.toggle_orientation_vis)
        self.ui.orientationmoveCheckBox.stateChanged.connect(
            self.toggle_orientation_move
        )

        self.ui.bgcolorFrameButton.mousePressEvent = self.pick_color_bg
        self.ui.abovecolorFrameButton.mousePressEvent = self.pick_color_above
        self.ui.belowcolorFrameButton.mousePressEvent = self.pick_color_below

        self.window().width_changed.connect(self.ui.widthLineEdit.setText)
        self.window().height_changed.connect(self.ui.heightLineEdit.setText)
        self.ui.widthLineEdit.editingFinished.connect(self.resize_window)
        self.ui.heightLineEdit.editingFinished.connect(self.resize_window)

        self.ui.widthLineEdit.setValidator(qtg.QIntValidator())
        self.ui.heightLineEdit.setValidator(qtg.QIntValidator())

        self.ui.opacityCheckBox.stateChanged.connect(self.toggle_opacity_control)
        self.ui.maskopacitySlider.valueChanged.connect(self.update_mask_opacity_value)
        self.ui.clipopacitySlider.valueChanged.connect(self.update_clip_opacity_value)

    def toggle_control_pane(self, enable: bool):
        self.setEnabled(enable)
        if enable:
            self.ui.bgcolorFrameButton.setStyleSheet(
                f"background-color: rgb{tuple(int(c*255) for c in self.controller.background_color)}"
            )

            self.ui.colormapSelector.clear()
            self.ui.colormapSelector.addItems(COLORMAPS)
            self.ui.colormap_completer = qtw.QCompleter(COLORMAPS)
            self.ui.colormap_completer.setCaseSensitivity(qtc.Qt.CaseInsensitive)
            self.ui.colormapSelector.setCompleter(self.ui.colormap_completer)
            self.ui.colormapSelector.setCurrentIndex(
                self.ui.colormapSelector.findText("rainbow4")
            )
            self.update_mask_opacity_value()
            self.update_clip_opacity_value()

    def resize_window(self, event=None) -> None:
        self.window().view_dimensions = [
            int(self.ui.widthLineEdit.text()),
            int(self.ui.heightLineEdit.text()),
        ]

    def pick_color_bg(self, event=None) -> None:
        if event.button() == 1:
            self.controller.background_color = self._pick_color(
                self.ui.bgcolorFrameButton
            )[:3]

    def set_colormap(self, _: int) -> None:
        if self.ui.colormapSelector.currentText() in COLORMAPS:
            self.controller.lut.cmap = self.ui.colormapSelector.currentText()

    def tabcomplete_colormap(self, event=None) -> None:
        # https://doc.qt.io/qt-5/qt.html#FocusReason-enum
        if event.reason() == 1:
            self.ui.colormap_completer.setCompletionPrefix(
                self.ui.colormapSelector.currentText()
            )
            self.ui.colormapSelector.setCurrentIndex(
                self.ui.colormapSelector.findText(
                    self.ui.colormap_completer.currentCompletion()
                )
            )
            self.ui.olormapSelector.setFocus(
                qtc.Qt.OtherFocusReason
            )  # Undo the standard Tab behavior

    def toggle_reverse(self, enable: bool) -> None:
        self.controller.lut.reverse = enable

    def toggle_outofrange_color(self, enable: bool) -> None:
        self.ui.abovecolorFrameButton.setEnabled(enable)
        self.ui.abovecolorLabel.setEnabled(enable)
        self.ui.belowcolorFrameButton.setEnabled(enable)
        self.ui.belowcolorLabel.setEnabled(enable)
        if enable:
            self.controller.lut.above_color = (
                self.ui.abovecolorFrameButton.palette()
                .color(qtg.QPalette.Background)
                .name()
            )
            self.controller.lut.below_color = (
                self.ui.belowcolorFrameButton.palette()
                .color(qtg.QPalette.Background)
                .name()
            )
        else:
            self.controller.lut.above_color = None
            self.controller.lut.below_color = None

    def pick_color_above(self, event=None) -> None:
        if event.button() == 1:
            self.controller.lut.above_color = self._pick_color(
                self.ui.abovecolorFrameButton
            )[:3]

    def pick_color_below(self, event=None) -> None:
        if event.button() == 1:
            self.controller.lut.below_color = self._pick_color(
                self.ui.belowcolorFrameButton
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
        self.ui.opacitycontrolFrame.setEnabled(enable)
        self.controller.set_opacity_enabled(enable, instigator=id(self))
        if enable:
            self.update_mask_opacity_value()
            self.update_clip_opacity_value()
        else:
            self.controller.set_mask_opacity(0.0, instigator=id(self))
            self.controller.set_clip_opacity(0.0, instigator=id(self))

    def update_mask_opacity_value(self, _=None) -> None:
        self.ui.maskopacityvalueLabel.setText(f"{self.ui.maskopacitySlider.value()*5}%")
        self.controller.set_mask_opacity(
            self.ui.maskopacitySlider.value() / self.ui.maskopacitySlider.maximum(),
            instigator=id(self),
        )

    def update_clip_opacity_value(self, _=None) -> None:
        self.ui.clipopacityvalueLabel.setText(f"{self.ui.clipopacitySlider.value()*5}%")
        self.controller.set_clip_opacity(
            self.ui.clipopacitySlider.value() / self.ui.clipopacitySlider.maximum(),
            instigator=id(self),
        )

    @staticmethod
    def _pick_color(button) -> tuple:
        color = qtw.QColorDialog.getColor()
        button.setStyleSheet(f"background-color: rgb{color.getRgb()[:3]}")
        return color.getRgbF()
