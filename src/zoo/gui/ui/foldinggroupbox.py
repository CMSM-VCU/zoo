import typing

from PySide6 import QtWidgets as qtw


class FoldingGroupBox(qtw.QGroupBox):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._unfolded = True

        self.button = qtw.QPushButton("", parent=self)
        self.button.move(0, 1)
        self.button.setFixedSize(15, 15)
        self.button.clicked.connect(self.toggle_fold)

    @property
    def children_to_hide(self) -> typing.List:
        return [child for child in self.children() if child is not self.button]

    def toggle_fold(self, _=None) -> None:
        self._unfolded = not self._unfolded
        for child in self.children_to_hide:
            if child.isWidgetType():
                child.setVisible(self._unfolded)
        self.setFlat(not self._unfolded)
