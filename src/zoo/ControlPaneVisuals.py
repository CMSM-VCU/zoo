import os
import typing
from importlib import resources

from . import ui
from .utils import COLORMAPS
from .VTK_PVH5Model import VTK_PVH5Model

os.environ["QT_API"] = "pyqt5"

from qtpy import QtCore as qtc
from qtpy import QtGui as qtg
from qtpy import QtWidgets as qtw
from qtpy import uic


class ControlPaneVisuals(qtw.QWidget):
    _parent = None

    def __init__(self, parent: typing.Optional["qtw.QWidget"] = None,) -> None:
        super().__init__(parent=parent)
        with resources.open_text(ui, "controlpane_visuals.ui") as uifile:
            uic.loadUi(uifile, self)

        self._parent = parent
        self.organize_widgets()
        self.hook_up_signals()

    @property
    def model(self) -> VTK_PVH5Model:
        if self._parent:
            return self._parent.model
        else:
            return None

    def _connect_model(self, model: VTK_PVH5Model) -> None:
        ...

    def organize_widgets(self):
        ...

    def hook_up_signals(self):
        self.colormapSelector.currentTextChanged.connect(self.set_colormap)
        self.colormapSelector.focusOutEvent = self.tabcomplete_colormap
        self.reverseCheckBox.stateChanged.connect(self.toggle_reverse)
        self.outofrangeCheckBox.stateChanged.connect(self.toggle_outofrange_color)

        self.bgcolorFrameButton.mousePressEvent = self.pick_color_bg
        self.abovecolorFrameButton.mousePressEvent = self.pick_color_above
        self.belowcolorFrameButton.mousePressEvent = self.pick_color_below

    def toggle_control_pane(self, enable: bool):
        self.setEnabled(enable)
        if enable:
            self.bgcolorFrameButton.setStyleSheet(
                f"background-color: rgb{tuple(int(c*255) for c in self.model.background_color)}"
            )

            self.colormapSelector.clear()
            self.colormapSelector.addItems(COLORMAPS)
            self.colormap_completer = qtw.QCompleter(COLORMAPS)
            self.colormap_completer.setCaseSensitivity(False)
            self.colormapSelector.setCompleter(self.colormap_completer)
            self.colormapSelector.setCurrentIndex(self.colormapSelector.findText("jet"))

    def pick_color_bg(self, event=None) -> None:
        if event.button() == 1:
            self.model.background_color = self._pick_color(self.bgcolorFrameButton)[:3]

    def set_colormap(self, _: int) -> None:
        if self.colormapSelector.currentText() in COLORMAPS:
            self.model.lut.cmap = self.colormapSelector.currentText()

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
            self.colormapSelector.setFocus(7)  # Undo the standard Tab behavior

    def toggle_reverse(self, enable: bool) -> None:
        self.model.lut.reverse = enable

    def toggle_outofrange_color(self, enable: bool) -> None:
        self.abovecolorFrameButton.setEnabled(enable)
        self.abovecolorLabel.setEnabled(enable)
        self.belowcolorFrameButton.setEnabled(enable)
        self.belowcolorLabel.setEnabled(enable)
        if enable:
            self.model.lut.above_color = (
                self.abovecolorFrameButton.palette()
                .color(qtg.QPalette.Background)
                .name()
            )
            self.model.lut.below_color = (
                self.belowcolorFrameButton.palette()
                .color(qtg.QPalette.Background)
                .name()
            )
        else:
            self.model.lut.above_color = None
            self.model.lut.below_color = None

    def pick_color_above(self, event=None) -> None:
        if event.button() == 1:
            self.model.lut.above_color = self._pick_color(self.abovecolorFrameButton)[
                :3
            ]

    def pick_color_below(self, event=None) -> None:
        if event.button() == 1:
            self.model.lut.below_color = self._pick_color(self.belowcolorFrameButton)[
                :3
            ]

    @staticmethod
    def _pick_color(button) -> typing.Tuple:
        color = qtw.QColorDialog.getColor()
        button.setStyleSheet(f"background-color: rgb{color.getRgb()[:3]}")
        return color.getRgbF()
