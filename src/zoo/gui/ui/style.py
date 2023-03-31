from PySide6.QtGui import QFont
from PySide6.QtWidgets import QSizePolicy, QSpacerItem


class Fonts:
    numeric_base = QFont()
    numeric_base.setFamilies(["Consolas"])

    numeric_small = QFont(numeric_base)
    numeric_small.setPointSize(8)

    numeric_normal = QFont(numeric_base)
    numeric_normal.setPointSize(11)

    label_base = QFont()
    label_base.setFamilies(["Segoe UI"])

    label_small = QFont(label_base)
    label_small.setPointSize(8)

    label_normal = QFont(label_base)
    label_normal.setPointSize(10)

    icon_base = QFont()
    icon_base.setFamilies(["Segoe Fluent Icons"])

    icon_small = QFont(icon_base)
    icon_small.setPointSize(10)
    icon_small.setBold(True)

    icon_normal = QFont(icon_base)
    icon_normal.setPointSize(14)


def default_spacer():
    return QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)
