# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zoo.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(925, 743)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        MainWindow.setFont(font)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionDuplicate = QAction(MainWindow)
        self.actionDuplicate.setObjectName(u"actionDuplicate")
        self.actionSynchronizeTabs = QAction(MainWindow)
        self.actionSynchronizeTabs.setObjectName(u"actionSynchronizeTabs")
        self.actionSave_Image = QAction(MainWindow)
        self.actionSave_Image.setObjectName(u"actionSave_Image")
        self.actionCopy_Image = QAction(MainWindow)
        self.actionCopy_Image.setObjectName(u"actionCopy_Image")
        self.actionSave_All_Images = QAction(MainWindow)
        self.actionSave_All_Images.setObjectName(u"actionSave_All_Images")
        self.actionSave_All_Images_In_All_Tabs = QAction(MainWindow)
        self.actionSave_All_Images_In_All_Tabs.setObjectName(u"actionSave_All_Images_In_All_Tabs")
        self.actionNext_Timestep = QAction(MainWindow)
        self.actionNext_Timestep.setObjectName(u"actionNext_Timestep")
        self.actionPrevious_Timestep = QAction(MainWindow)
        self.actionPrevious_Timestep.setObjectName(u"actionPrevious_Timestep")
        self.actionFirst_Timestep = QAction(MainWindow)
        self.actionFirst_Timestep.setObjectName(u"actionFirst_Timestep")
        self.actionLast_Timestep = QAction(MainWindow)
        self.actionLast_Timestep.setObjectName(u"actionLast_Timestep")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 925, 21))
        font1 = QFont()
        font1.setPointSize(9)
        self.menubar.setFont(font1)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuNavigation = QMenu(self.menubar)
        self.menuNavigation.setObjectName(u"menuNavigation")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuNavigation.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionCopy_Image)
        self.menuFile.addAction(self.actionSave_Image)
        self.menuFile.addAction(self.actionSave_All_Images)
        self.menuFile.addAction(self.actionSave_All_Images_In_All_Tabs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionDuplicate)
        self.menuView.addAction(self.actionSynchronizeTabs)
        self.menuNavigation.addAction(self.actionFirst_Timestep)
        self.menuNavigation.addAction(self.actionPrevious_Timestep)
        self.menuNavigation.addAction(self.actionNext_Timestep)
        self.menuNavigation.addAction(self.actionLast_Timestep)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Zoo", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionDuplicate.setText(QCoreApplication.translate("MainWindow", u"Duplicate Tab", None))
        self.actionSynchronizeTabs.setText(QCoreApplication.translate("MainWindow", u"Synchronize Tabs", None))
        self.actionSave_Image.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
#if QT_CONFIG(shortcut)
        self.actionSave_Image.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionCopy_Image.setText(QCoreApplication.translate("MainWindow", u"Copy Image", None))
#if QT_CONFIG(shortcut)
        self.actionCopy_Image.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_All_Images.setText(QCoreApplication.translate("MainWindow", u"Save All Images", None))
#if QT_CONFIG(shortcut)
        self.actionSave_All_Images.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_All_Images_In_All_Tabs.setText(QCoreApplication.translate("MainWindow", u"Save All Images in All Tabs", None))
        self.actionNext_Timestep.setText(QCoreApplication.translate("MainWindow", u"Next Timestep", None))
#if QT_CONFIG(shortcut)
        self.actionNext_Timestep.setShortcut(QCoreApplication.translate("MainWindow", u"PgDown", None))
#endif // QT_CONFIG(shortcut)
        self.actionPrevious_Timestep.setText(QCoreApplication.translate("MainWindow", u"Previous Timestep", None))
#if QT_CONFIG(shortcut)
        self.actionPrevious_Timestep.setShortcut(QCoreApplication.translate("MainWindow", u"PgUp", None))
#endif // QT_CONFIG(shortcut)
        self.actionFirst_Timestep.setText(QCoreApplication.translate("MainWindow", u"First Timestep", None))
#if QT_CONFIG(shortcut)
        self.actionFirst_Timestep.setShortcut(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(shortcut)
        self.actionLast_Timestep.setText(QCoreApplication.translate("MainWindow", u"Last Timestep", None))
#if QT_CONFIG(shortcut)
        self.actionLast_Timestep.setShortcut(QCoreApplication.translate("MainWindow", u"End", None))
#endif // QT_CONFIG(shortcut)
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuNavigation.setTitle(QCoreApplication.translate("MainWindow", u"Navigation", None))
    # retranslateUi

