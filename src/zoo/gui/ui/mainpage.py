# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainpage.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QWidget)

class Ui_MainPage(object):
    def setupUi(self, MainPage):
        if not MainPage.objectName():
            MainPage.setObjectName(u"MainPage")
        MainPage.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(MainPage)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.viewport = QFrame(MainPage)
        self.viewport.setObjectName(u"viewport")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewport.sizePolicy().hasHeightForWidth())
        self.viewport.setSizePolicy(sizePolicy)
        self.viewport.setMinimumSize(QSize(300, 0))
        self.viewport.setFrameShape(QFrame.StyledPanel)
        self.viewport.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.viewport)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.viewport)

        self.line = QFrame(MainPage)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QFrame.VLine)

        self.horizontalLayout.addWidget(self.line)


        self.retranslateUi(MainPage)

        QMetaObject.connectSlotsByName(MainPage)
    # setupUi

    def retranslateUi(self, MainPage):
        MainPage.setWindowTitle(QCoreApplication.translate("MainPage", u"Form", None))
    # retranslateUi

