from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QGridLayout, QMenu, QMenuBar, QTabWidget, QWidget

from .style import Fonts


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(925, 743)
        MainWindow.setFont(Fonts.label_normal)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDuplicate = QAction(MainWindow)
        self.actionDuplicate.setObjectName("actionDuplicate")
        self.actionSynchronizeTabs = QAction(MainWindow)
        self.actionSynchronizeTabs.setObjectName("actionSynchronizeTabs")
        self.actionSave_Image = QAction(MainWindow)
        self.actionSave_Image.setObjectName("actionSave_Image")
        self.actionCopy_Image = QAction(MainWindow)
        self.actionCopy_Image.setObjectName("actionCopy_Image")
        self.actionSave_All_Images = QAction(MainWindow)
        self.actionSave_All_Images.setObjectName("actionSave_All_Images")
        self.actionSave_All_Images_In_All_Tabs = QAction(MainWindow)
        self.actionSave_All_Images_In_All_Tabs.setObjectName(
            "actionSave_All_Images_In_All_Tabs"
        )
        self.actionNext_Timestep = QAction(MainWindow)
        self.actionNext_Timestep.setObjectName("actionNext_Timestep")
        self.actionPrevious_Timestep = QAction(MainWindow)
        self.actionPrevious_Timestep.setObjectName("actionPrevious_Timestep")
        self.actionFirst_Timestep = QAction(MainWindow)
        self.actionFirst_Timestep.setObjectName("actionFirst_Timestep")
        self.actionLast_Timestep = QAction(MainWindow)
        self.actionLast_Timestep.setObjectName("actionLast_Timestep")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setEnabled(True)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 925, 21))
        self.menubar.setFont(Fonts.label_small)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuNavigation = QMenu(self.menubar)
        self.menuNavigation.setObjectName("menuNavigation")
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

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Zoo", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", "Open", None))
        self.actionOpen.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+O", None)
        )
        self.actionExit.setText(QCoreApplication.translate("MainWindow", "Exit", None))
        self.actionExit.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+Q", None)
        )
        self.actionDuplicate.setText(
            QCoreApplication.translate("MainWindow", "Duplicate Tab", None)
        )
        self.actionSynchronizeTabs.setText(
            QCoreApplication.translate("MainWindow", "Synchronize Tabs", None)
        )
        self.actionSave_Image.setText(
            QCoreApplication.translate("MainWindow", "Save Image", None)
        )
        self.actionSave_Image.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+S", None)
        )
        self.actionCopy_Image.setText(
            QCoreApplication.translate("MainWindow", "Copy Image", None)
        )
        self.actionCopy_Image.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+C", None)
        )
        self.actionSave_All_Images.setText(
            QCoreApplication.translate("MainWindow", "Save All Images", None)
        )
        self.actionSave_All_Images.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+Shift+S", None)
        )
        self.actionSave_All_Images_In_All_Tabs.setText(
            QCoreApplication.translate(
                "MainWindow", "Save All Images in All Tabs", None
            )
        )
        self.actionNext_Timestep.setText(
            QCoreApplication.translate("MainWindow", "Next Timestep", None)
        )
        self.actionNext_Timestep.setShortcut(
            QCoreApplication.translate("MainWindow", "PgDown", None)
        )
        self.actionPrevious_Timestep.setText(
            QCoreApplication.translate("MainWindow", "Previous Timestep", None)
        )
        self.actionPrevious_Timestep.setShortcut(
            QCoreApplication.translate("MainWindow", "PgUp", None)
        )
        self.actionFirst_Timestep.setText(
            QCoreApplication.translate("MainWindow", "First Timestep", None)
        )
        self.actionFirst_Timestep.setShortcut(
            QCoreApplication.translate("MainWindow", "Home", None)
        )
        self.actionLast_Timestep.setText(
            QCoreApplication.translate("MainWindow", "Last Timestep", None)
        )
        self.actionLast_Timestep.setShortcut(
            QCoreApplication.translate("MainWindow", "End", None)
        )
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", "View", None))
        self.menuNavigation.setTitle(
            QCoreApplication.translate("MainWindow", "Navigation", None)
        )
