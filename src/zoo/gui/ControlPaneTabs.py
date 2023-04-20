from qtpy import QtWidgets as qtw

from .ControlPanePrimary import ControlPanePrimary
from .ControlPaneVisuals import ControlPaneVisuals
from .ui.controlpane_tabs import Ui_ControlPane_Tabs


class ControlPaneTabs(qtw.QWidget):
    _parent = None
    panes = dict()

    def __init__(
        self,
        parent: qtw.QWidget | None = None,
    ) -> None:
        super().__init__(parent=parent)
        self.ui = Ui_ControlPane_Tabs()
        self.ui.setupUi(self)

        self.panes = {}

        self._parent = parent
        self.panes["primary"] = ControlPanePrimary(parent=self._parent)
        self.panes["visuals"] = ControlPaneVisuals(parent=self._parent)
        self.ui.tabWidget.addTab(self.panes["primary"], "Primary")
        self.ui.tabWidget.addTab(self.panes["visuals"], "Visuals")

    def toggle_control_pane(self, enable: bool):
        for pane in self.panes.values():
            pane.toggle_control_pane(enable)

    def _connect_contour_controller(self, model) -> None:
        for pane in self.panes.values():
            pane._connect_contour_controller(model)
