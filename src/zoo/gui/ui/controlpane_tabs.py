from PySide6.QtCore import QCoreApplication, QMetaObject, QSize
from PySide6.QtWidgets import QGridLayout, QSizePolicy, QTabWidget


class Ui_ControlPane_Tabs(object):
    def setupUi(self, ControlPane_Tabs):
        ControlPane_Tabs.resize(220, 630)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ControlPane_Tabs.sizePolicy().hasHeightForWidth())
        ControlPane_Tabs.setSizePolicy(sizePolicy)
        ControlPane_Tabs.setMinimumSize(QSize(220, 0))
        ControlPane_Tabs.setMaximumSize(QSize(220, 16777215))
        self.gridLayout = QGridLayout(ControlPane_Tabs)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(ControlPane_Tabs)
        self.tabWidget.setTabPosition(QTabWidget.East)
        self.tabWidget.setDocumentMode(True)

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.retranslateUi(ControlPane_Tabs)

        QMetaObject.connectSlotsByName(ControlPane_Tabs)

    def retranslateUi(self, ControlPane_Tabs):
        ControlPane_Tabs.setWindowTitle(
            QCoreApplication.translate("ControlPane_Tabs", "Form", None)
        )
