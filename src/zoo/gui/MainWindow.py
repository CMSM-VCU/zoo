from collections.abc import Sequence
from pathlib import Path

from loguru import logger
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw

from .. import utils
from .MainPage import MainPage
from .ui.mainwindow import Ui_MainWindow


class MainWindow(qtw.QMainWindow):
    width_changed = qtc.Signal(str)
    height_changed = qtc.Signal(str)

    def __init__(self, parent=None, show=True, file_to_load=None) -> None:
        super().__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._base_window_title = self.windowTitle()

        self.centralWidget().setAcceptDrops(True)
        self.centralWidget().dragEnterEvent = self._dragEnterEvent
        self.centralWidget().dropEvent = self._dropEvent
        self.resizeEvent = self._resizeEvent

        self.organize_widgets()
        self.hook_up_signals()

        self.master_controller = None

        if show:
            self.show()

        if file_to_load is not None:
            self.open_file(override=file_to_load)

    @property
    def current_page(self) -> MainPage:
        return self.ui.tabWidget.currentWidget()

    @property
    def other_pages(self) -> list[MainPage]:
        return [page for page in self.pages if page is not self.current_page]

    @property
    def pages(self) -> list[MainPage]:
        return [
            self.ui.tabWidget.widget(idx) for idx in range(self.ui.tabWidget.count())
        ]

    tabs = pages  # Alias

    @property
    def window_dimensions(self) -> list[int]:
        return [self.width(), self.height()]

    @property
    def view_dimensions(self) -> list[int]:
        try:
            return [
                self.current_page.controller.plotter.width(),
                self.current_page.controller.plotter.height(),
            ]
        except:
            return [-1, -1]

    @view_dimensions.setter
    def view_dimensions(self, dims: Sequence[int]) -> None:
        gui_padding = [
            b - a for a, b in zip(self.view_dimensions, self.window_dimensions)
        ]
        self.resize(dims[0] + gui_padding[0], dims[1] + gui_padding[1])

    def organize_widgets(self):
        self.actions = {"open": self.ui.actionOpen, "exit": self.ui.actionExit}

    def hook_up_signals(self):
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionCopy_Image.triggered.connect(self.copy_image)
        self.ui.actionSave_Image.triggered.connect(self.save_image)
        self.ui.actionSave_All_Images.triggered.connect(self.save_all_images)
        self.ui.actionSave_All_Images_In_All_Tabs.triggered.connect(
            self.save_all_images_in_all_tabs
        )
        self.ui.actionClear_Cache.triggered.connect(self.clear_cache)
        self.ui.actionDisable_Cache.triggered.connect(self.disable_cache)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionDuplicate.triggered.connect(self.duplicate_current_tab)
        self.ui.actionSynchronizeTabs.triggered.connect(self.unify_tabs)

        self.ui.actionFirst_Timestep.triggered.connect(self.first_timestep)
        self.ui.actionPrevious_Timestep.triggered.connect(self.previous_timestep)
        self.ui.actionNext_Timestep.triggered.connect(self.next_timestep)
        self.ui.actionLast_Timestep.triggered.connect(self.last_timestep)

        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)
        self.ui.tabWidget.currentChanged.connect(self.tab_title_to_window)

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
            new_idx = self.ui.tabWidget.addTab(new_page, new_page.windowTitle())
            self.ui.tabWidget.setTabToolTip(new_idx, f"{filename}")
            self.ui.tabWidget.setCurrentIndex(new_idx)

    def copy_image(self, _=None) -> None:
        self.current_page.copy_image()

    def save_image(self, _=None) -> None:
        self.current_page.save_image()

    def save_all_images(self, _=None) -> None:
        self.current_page.save_all_images()

    def save_all_images_in_all_tabs(self, _=None) -> None:
        folder_name, _ = qtw.QInputDialog.getText(
            self, "Folder name?", "Name of folders to save images in?"
        )
        if not folder_name:
            return
        checkpoints = qtw.QMessageBox.question(
            self, "Checkpoints?", "Occasionally ask to continue?"
        )
        checkpoints = checkpoints == qtw.QMessageBox.Yes

        folders = self.make_folder_for_every_tab(folder_name)

        for i, ts in enumerate(self.master_controller.model.timesteps):
            self.master_controller.set_timestep_index(i, instigator=id(self))
            for tab, folder in zip(self.pages, folders):
                tab._original_controller.contour_primary.plotter.render()
                tab.save_image(override=f"{folder}/image_{ts:07d}.png")
            if checkpoints and not (i % 20):
                if (
                    qtw.QMessageBox.question(self, "Keep going?", "Keep going?")
                    != qtw.QMessageBox.Yes
                ):
                    break

    def make_folder_for_every_tab(
        self, folder_name: str, exist_ok: bool = True
    ) -> list[Path]:
        folders = [Path(tab._filename).parent / Path(folder_name) for tab in self.pages]
        for folder in folders:
            Path.mkdir(folder, exist_ok=exist_ok)
        return folders

    def tab_title_to_window(self, idx: int) -> None:
        try:
            self.setWindowTitle(
                f"{self.ui.tabWidget.widget(idx).tab_name} - {self._base_window_title}"
            )
        except:
            self.setWindowTitle(self._base_window_title)

    def close_tab(self, idx=None, *, page=None) -> None:
        if page:
            idx = self.ui.tabWidget.indexOf(page)
        else:
            page = self.ui.tabWidget.widget(idx)
        page.clean_up()
        self.ui.tabWidget.removeTab(idx)

    def duplicate_current_tab(self, _=None) -> None:
        if self.current_page:
            self.open_file(override=self.current_page._filename)

    def first_timestep(self, _=None) -> None:
        self.current_page.first_timestep()

    def previous_timestep(self, _=None) -> None:
        self.current_page.previous_timestep()

    def next_timestep(self, _=None) -> None:
        self.current_page.next_timestep()

    def last_timestep(self, _=None) -> None:
        self.current_page.last_timestep()

    def clear_cache(self, _=None) -> None:
        for page in self.pages:
            page.clear_cache()

    def disable_cache(self, _=None) -> None:
        for page in self.pages:
            page.disable_cache()

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

    def _resizeEvent(self, event):
        qtw.QMainWindow.resizeEvent(self, event)
        self.width_changed.emit(str(self.view_dimensions[0]))
        self.height_changed.emit(str(self.view_dimensions[1]))

    def open_dropped_files(self, paths: list, *, depth: int = 0) -> None:
        if depth > 1:
            logger.warning(f"Directory recursion depth at {depth}.")
        if len(paths) > 10:
            logger.warning(f"Attempting to open {len(paths)} items in this iteration.")

        for path in paths:
            if path.is_file() and utils.has_known_extension(path):
                self.open_file(override=path)
            elif path.is_dir():
                self.open_dropped_files(list(path.iterdir()), depth=depth + 1)

    def unify_tabs(self) -> None:
        for tab in self.other_pages:
            self.current_page.controller.add_contour(tab.controller.contour_primary)
            tab._master_controller = self.current_page.controller
        self.master_controller = self.current_page.controller
