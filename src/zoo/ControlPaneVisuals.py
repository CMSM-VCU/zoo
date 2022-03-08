import os
import typing
from importlib import resources

from . import ui
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

    def organize_widgets(self):
        ...

    def hook_up_signals(self):
        ...
