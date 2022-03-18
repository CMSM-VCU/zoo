import os
from importlib import resources
from io import BytesIO
from pathlib import Path
from loguru import logger

import win32clipboard
from PIL import Image

from . import ui
from .ControlPaneTabs import ControlPaneTabs
from .VTK_PVH5Model import VTK_PVH5Model

os.environ["QT_API"] = "pyqt5"

from qtpy import QtCore as qtc
from qtpy import QtWidgets as qtw
from qtpy import uic


class MainPage(qtw.QWidget):
    _parent = None
    _model: VTK_PVH5Model = None
    _filename = None

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        with resources.open_text(ui, "mainpage.ui") as uifile:
            uic.loadUi(uifile, self)
        self.setAttribute(qtc.Qt.WA_DeleteOnClose, True)
        self._parent = parent
        self._base_window_title = self.windowTitle()
        self._control_pane = ControlPaneTabs(parent=self)
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

    @property
    def tab_name(self) -> str:
        return self.windowTitle()

    @tab_name.setter
    def tab_name(self, name: str) -> None:
        self.setWindowTitle(name)

    def open_file(self, filename):
        self.model = VTK_PVH5Model()
        self.model.load_file(Path(filename))
        self.tab_name = f"{Path(filename).name}"
        self._filename = filename

        self.model.destroyed.connect(self.close_my_tab)

    def toggle_control_pane(self, enable: bool):
        self._control_pane.toggle_control_pane(enable)

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

    def save_image(self, _=None, override=None) -> None:
        if override:
            filename = override
        else:
            filename, _ = qtw.QFileDialog.getSaveFileName(self, filter="PNG (*.png)")
        if filename:
            logger.debug(f"Saving image at {Path(filename).absolute()}")
            self.model.save_image(filename)

    def save_all_images(self, _=None, name_prefix="image") -> None:
        folder = qtw.QFileDialog.getExistingDirectory(
            self, directory=str(Path(self._filename).parent)
        )
        if folder:
            logger.debug(f"Saving all images in {Path(folder).absolute()}")
            self.model.timestep_index = 0
            for _ in self.model.timesteps:
                self.model.timestep_index += 1
                self.save_image(
                    override=f"{folder}/{name_prefix}_{self.model.timestep:07d}.png"
                )

    def close_my_tab(self) -> None:
        self._parent.close_tab(page=self)

    def clean_up(self) -> None:
        self._model.df = None
        self._model.polydata = None
        self._model.construct_timestep_data.cache_clear()
        self.close()
