import os
import typing
from importlib import resources
from io import BytesIO
from pathlib import Path

import pyperclip
import win32clipboard

from . import ui
from .ControlPane import ControlPane
from .VTK_PVH5Model import VTK_PVH5Model

os.environ["QT_API"] = "pyqt5"

from PIL import Image
from qtpy import QtCore as qtc
from qtpy import QtGui as qtg
from qtpy import QtWidgets as qtw
from qtpy import uic


class MainWindow(qtw.QMainWindow):
    _model: VTK_PVH5Model = None

    def __init__(self, parent=None, show=True, file_to_load=None) -> None:
        super().__init__(parent=parent)
        mainwindow_uifile = resources.open_text(ui, "zoo.ui")
        uic.loadUi(mainwindow_uifile, self)
        self._base_window_title = self.windowTitle()
        self._control_pane = ControlPane(parent=self)
        self.horizontalLayout.addWidget(self._control_pane)

        self.organize_widgets()
        self.hook_up_signals()
        self.toggle_control_pane(enable=False)

        self.viewport.setAcceptDrops(True)
        self.viewport.dragEnterEvent = self._dragEnterEvent
        self.viewport.dropEvent = self._dropEvent

        if show:
            self.show()

        if file_to_load is not None:
            self.open_file(override=file_to_load)

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

    def organize_widgets(self):
        self.actions = {"open": self.actionOpen, "exit": self.actionExit}

    def hook_up_signals(self):
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave_Image.triggered.connect(self.save_image)
        self.actionCopy_Image.triggered.connect(self.copy_image)
        self.actionExit.triggered.connect(self.close)

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
        self.menuView.setEnabled(enable)
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

    def _dragEnterEvent(self, event):
        # Based on https://stackoverflow.com/a/4176083/13130795
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def _dropEvent(self, event):
        if event.mimeData().hasUrls():
            # Local file path is just one thing that counts as a URL
            if event.mimeData().urls()[0].toLocalFile():
                self.open_file(override=Path(event.mimeData().urls()[0].toLocalFile()))
        else:
            event.ignore()
