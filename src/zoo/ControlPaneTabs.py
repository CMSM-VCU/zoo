import typing
from importlib import resources

from qtpy import QtWidgets as qtw
from qtpy import uic

from zoo.ControlPaneVisuals import ControlPaneVisuals

from . import ui
from .ControlPanePrimary import ControlPanePrimary


class ControlPaneTabs(qtw.QWidget):
    _parent = None

    def __init__(self, parent: typing.Optional["qtw.QWidget"] = None,) -> None:
        super().__init__(parent=parent)
        with resources.open_text(ui, "controlpane_tabs.ui") as uifile:
            uic.loadUi(uifile, self)

        self._parent = parent
        self._primary_pane = ControlPanePrimary(parent=self._parent)
        self._visuals_pane = ControlPaneVisuals(parent=self._parent)
        self.tabWidget.addTab(self._primary_pane, "Primary")
        self.tabWidget.addTab(self._visuals_pane, "Visuals")

    def toggle_control_pane(self, enable: bool):
        self._primary_pane.toggle_control_pane(enable)

    def _connect_model(self, model) -> None:
        self._primary_pane._connect_model(model)
