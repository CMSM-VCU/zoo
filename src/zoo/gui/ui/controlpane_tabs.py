# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'controlpane_tabs.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QTabWidget,
    QWidget)

class Ui_ControlPane_Tabs(object):
    def setupUi(self, ControlPane_Tabs):
        if not ControlPane_Tabs.objectName():
            ControlPane_Tabs.setObjectName(u"ControlPane_Tabs")
        ControlPane_Tabs.resize(220, 630)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ControlPane_Tabs.sizePolicy().hasHeightForWidth())
        ControlPane_Tabs.setSizePolicy(sizePolicy)
        ControlPane_Tabs.setMinimumSize(QSize(220, 0))
        ControlPane_Tabs.setMaximumSize(QSize(220, 16777215))
        self.gridLayout = QGridLayout(ControlPane_Tabs)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(ControlPane_Tabs)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.East)
        self.tabWidget.setDocumentMode(True)

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(ControlPane_Tabs)

        QMetaObject.connectSlotsByName(ControlPane_Tabs)
    # setupUi

    def retranslateUi(self, ControlPane_Tabs):
        ControlPane_Tabs.setWindowTitle(QCoreApplication.translate("ControlPane_Tabs", u"Form", None))
    # retranslateUi

