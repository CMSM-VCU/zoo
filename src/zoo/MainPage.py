import os
from importlib import resources
from io import BytesIO
from pathlib import Path

import win32clipboard
from PIL import Image

from . import ui
from .ControlPane import ControlPane
from .VTK_PVH5Model import VTK_PVH5Model

os.environ["QT_API"] = "pyqt5"

from qtpy import QtWidgets as qtw
from qtpy import uic


class MainPage(qtw.QWidget):
    _model: VTK_PVH5Model = None

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        mainpage_uifile = resources.open_text(ui, "mainpage.ui")
        uic.loadUi(mainpage_uifile, self)
        self._base_window_title = self.windowTitle()
        self._control_pane = ControlPane(parent=self)
        self.horizontalLayout.addWidget(self._control_pane)

        self.toggle_control_pane(enable=False)

    @property
    def model(self) -> VTK_PVH5Model:
        return self._model

    @model.setter
    def model(self, model: VTK_PVH5Model) -> None:
        if self._model:
            del self._model
        self._model = model

        model.plotter.setParent(self.viewport)
        if self.viewport.layout().count() != 0:
            old = self.viewport.layout().takeAt(0)
            del old
        self.viewport.layout().addWidget(model.plotter.interactor)

        model.loaded_file.connect(self.toggle_control_pane)
        self._control_pane._connect_model(model)

    def open_file(self, *, override=None):
        # stackoverflow.com/a/44076057/13130795
        if not override:
            filename, _ = qtw.QFileDialog.getOpenFileName(self)
        else:
            filename = override
        if filename:
            self.setWindowTitle(f"Opening {Path(filename).name}...")
            self.model = VTK_PVH5Model()
            self.model.load_file(Path(filename))
            self.setWindowTitle(f"{Path(filename).name} - {self._base_window_title}")

    def toggle_control_pane(self, enable: bool):
        self._control_pane.toggle_control_pane(enable)

    def save_image(self, _=None) -> None:
        filename, _ = qtw.QFileDialog.getSaveFileName(self, filter="PNG (*.png)")
        if filename:
            self.model.save_image(filename)

    def copy_image(self, _=None) -> None:
        image = Image.fromarray(self.model.plotter.image)
        # https://stackoverflow.com/a/61546024/13130795
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
