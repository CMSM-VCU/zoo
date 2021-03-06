import os
from importlib import resources
from io import BytesIO
from pathlib import Path
from loguru import logger

import win32clipboard
from PIL import Image

from . import ui
from .ControlPaneTabs import ControlPaneTabs
from .ContourController import ContourController
from .H5Model import H5Model

os.environ["QT_API"] = "pyqt5"

from qtpy import QtCore as qtc
from qtpy import QtWidgets as qtw
from qtpy import uic


class MainPage(qtw.QWidget):
    _parent = None
    _original_controller: ContourController = None
    _master_controller: ContourController = None
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
    def controller(self) -> ContourController:
        return (
            self._master_controller
            if self._master_controller is not None
            else self._original_controller
        )

    @controller.setter
    def controller(self, controller: ContourController) -> None:
        if self._original_controller is not None:
            raise AttributeError("Controller attribute has already been set")
        self._original_controller = controller

        controller.plotter.setParent(self.viewport)
        if self.viewport.layout().count() != 0:
            old = self.viewport.layout().takeAt(0)
            del old
        self.viewport.layout().addWidget(controller.plotter.interactor)

        controller.model.loaded_file.connect(self.toggle_control_pane)
        self._control_pane._connect_contour_controller(controller)

    @property
    def tab_name(self) -> str:
        return self.windowTitle()

    @tab_name.setter
    def tab_name(self, name: str) -> None:
        self.setWindowTitle(name)

    def open_file(self, filename):
        _model = H5Model()
        self.controller = ContourController(_model)
        _model.load_file(Path(filename))
        self.tab_name = f"{Path(filename).name}"
        self._filename = filename

        self.controller.destroyed.connect(self.close_my_tab)

    def toggle_control_pane(self, enable: bool):
        self._control_pane.toggle_control_pane(enable)

    def copy_image(self, _=None) -> None:
        image = Image.fromarray(self._original_controller.plotter.image)
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
            self._original_controller.save_image(filename)

    def save_all_images(self, _=None, name_prefix="image") -> None:
        if self._master_controller is not None:
            logger.warning(
                "Save All Images may have unexpected behavior for synchronized tabs."
            )
        folder = qtw.QFileDialog.getExistingDirectory(
            self, directory=str(Path(self._filename).parent)
        )
        if folder:
            logger.debug(f"Saving all images in {Path(folder).absolute()}")
            for ts in self._original_controller.model.timesteps:
                self.controller.set_timestep(ts, instigator=id(self))
                self._original_controller.contour_primary.plotter.render()
                self.save_image(override=f"{folder}/{name_prefix}_{ts:07d}.png")

    def close_my_tab(self) -> None:
        self._parent.close_tab(page=self)

    def clean_up(self) -> None:
        # self.controller.polydata = None
        # self._controller.construct_timestep_data.cache_clear()
        self.close()

    def first_timestep(self, _=None) -> None:
        self.controller.first_timestep(instigator=id(self))

    def previous_timestep(self, _=None) -> None:
        self.controller.decrement_timestep(instigator=id(self))

    def next_timestep(self, _=None) -> None:
        self.controller.increment_timestep(instigator=id(self))

    def last_timestep(self, _=None) -> None:
        self.controller.last_timestep(instigator=id(self))
