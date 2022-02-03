import os
import typing
from importlib import resources
from pathlib import Path

from loguru import logger

from . import ui
from . import utils
from .MainPage import MainPage

os.environ["QT_API"] = "pyqt5"

from qtpy import QtCore as qtc
from qtpy import QtGui as qtg
from qtpy import QtWidgets as qtw
from qtpy import uic


class MainWindow(qtw.QMainWindow):
    def __init__(self, parent=None, show=True, file_to_load=None) -> None:
        super().__init__(parent=parent)
        with resources.open_text(ui, "zoo.ui") as uifile:
            uic.loadUi(uifile, self)
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
        self.actionDuplicate.triggered.connect(self.duplicate_current_tab)

        self.tabWidget.tabCloseRequested.connect(self.close_tab)
        self.tabWidget.currentChanged.connect(self.tab_title_to_window)

    def open_file(self, *, override=None):
        # stackoverflow.com/a/44076057/13130795
        if not override:
            filename, _ = qtw.QFileDialog.getOpenFileName(self)
        else:
            filename = override
        if filename:
            self.setWindowTitle(f"Opening {Path(filename).name}...")
            new_page = MainPage(parent=self)
            new_page.open_file(filename)
            new_idx = self.tabWidget.addTab(new_page, new_page.windowTitle())
            self.tabWidget.setTabToolTip(new_idx, f"{filename}")
            self.tabWidget.setCurrentIndex(new_idx)

    def save_image(self, _=None) -> None:
        self.current_page.save_image()

    def copy_image(self, _=None) -> None:
        self.current_page.copy_image()

    def tab_title_to_window(self, idx: int) -> None:
        try:
            self.setWindowTitle(
                f"{self.tabWidget.widget(idx).tab_name} - {self._base_window_title}"
            )
        except:
            self.setWindowTitle(self._base_window_title)

    def close_tab(self, idx=None, *, page=None) -> None:
        if page:
            idx = self.tabWidget.indexOf(page)
        else:
            page = self.tabWidget.widget(idx)
        page.clean_up()
        self.tabWidget.removeTab(idx)

    def duplicate_current_tab(self, _=None) -> None:
        if self.current_page:
            self.open_file(override=self.current_page._filename)

    def _dragEnterEvent(self, event):
        # Based on https://stackoverflow.com/a/4176083/13130795
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def _dropEvent(self, event):
        if event.mimeData().hasUrls():
            # Local file path is just one thing that counts as a URL
            self.open_dropped_files(
                [
                    Path(url.toLocalFile())
                    for url in event.mimeData().urls()
                    if url.toLocalFile()
                ],
                depth=0,
            )
        else:
            event.ignore()

    def open_dropped_files(self, paths: typing.List, *, depth: int = 0) -> None:
        if depth > 1:
            logger.warn(f"Directory recursion depth at {depth}.")
        if len(paths) > 10:
            logger.warn(f"Attempting to open {len(paths)} in this iteration.")

        for path in paths:
            if path.is_file() and utils.has_known_extension(path):
                self.open_file(override=path)
            elif path.is_dir():
                self.open_dropped_files(list(path.iterdir()), depth=depth + 1)
