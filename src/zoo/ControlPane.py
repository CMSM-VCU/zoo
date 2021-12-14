import typing
from importlib import resources

from qtpy import QtCore as qtc
from qtpy import QtWidgets as qtw
from qtpy import uic

from . import ui


class ControlPane(qtw.QWidget):
    def __init__(self, parent: typing.Optional["qtw.QWidget"] = None,) -> None:
        super().__init__(parent=parent)
        controlpane_uifile = resources.open_text(ui, "controlpane_primary.ui")
        uic.loadUi(controlpane_uifile, self)
