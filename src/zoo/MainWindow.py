import os
import typing
from importlib import resources
from pathlib import Path

from . import ui
from .MainPage import MainPage

os.environ["QT_API"] = "pyqt5"

from qtpy import QtCore as qtc
from qtpy import QtGui as qtg
from qtpy import QtWidgets as qtw
from qtpy import uic


class MainWindow(qtw.QMainWindow):
    def __init__(self, parent=None, show=True, file_to_load=None) -> None:
        super().__init__(parent=parent)
        mainwindow_uifile = resources.open_text(ui, "zoo.ui")
        uic.loadUi(mainwindow_uifile, self)
        self._base_window_title = self.windowTitle()

        self.centralWidget().setAcceptDrops(True)
        self.centralWidget().dragEnterEvent = self._dragEnterEvent
        self.centralWidget().dropEvent = self._dropEvent

        self.organize_widgets()
        self.hook_up_signals()

        if show:
            self.show()

        if file_to_load is not None:
            self.open_file(override=file_to_load)

    @property
    def current_page(self) -> MainPage:
        return self.tabWidget.currentWidget()

    def organize_widgets(self):
        self.actions = {"open": self.actionOpen, "exit": self.actionExit}

    def hook_up_signals(self):
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave_Image.triggered.connect(self.save_image)
        self.actionCopy_Image.triggered.connect(self.copy_image)
        self.actionExit.triggered.connect(self.close)

        self.tabWidget.tabCloseRequested.connect(self.close_tab)

    def open_file(self, *, override=None):
        # stackoverflow.com/a/44076057/13130795
        if not override:
            filename, _ = qtw.QFileDialog.getOpenFileName(self)
        else:
            filename = override
        if filename:
            self.setWindowTitle(f"Opening {Path(filename).name}...")
            new_page = MainPage(parent=self.tabWidget)
            new_page.open_file(filename)
            self.tabWidget.addTab(new_page, new_page.windowTitle())
            self.setWindowTitle(new_page.windowTitle())

    def save_image(self, _=None) -> None:
        self.current_page.save_image()

    def copy_image(self, _=None) -> None:
        self.current_page.copy_image()

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
