import typing
from importlib import resources

from qtpy import QtWidgets as qtw
from qtpy import uic

from zoo.ControlPaneVisuals import ControlPaneVisuals

from . import ui
from .ControlPanePrimary import ControlPanePrimary


class ControlPaneTabs(qtw.QWidget):
    _parent = None
    panes = dict()

    def __init__(self, parent: typing.Optional["qtw.QWidget"] = None,) -> None:
        super().__init__(parent=parent)
        with resources.open_text(ui, "controlpane_tabs.ui") as uifile:
            uic.loadUi(uifile, self)
        self.panes = {}

        self._parent = parent
        self.panes["primary"] = ControlPanePrimary(parent=self._parent)
        self.panes["visuals"] = ControlPaneVisuals(parent=self._parent)
        self.tabWidget.addTab(self.panes["primary"], "Primary")
        self.tabWidget.addTab(self.panes["visuals"], "Visuals")

    def toggle_control_pane(self, enable: bool):
        for pane in self.panes.values():
            pane.toggle_control_pane(enable)

    def _connect_model(self, model) -> None:
        for pane in self.panes.values():
            pane._connect_model(model)
