# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'controlpane_primary.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from zoo.gui.ui.foldinggroupbox import FoldingGroupBox

class Ui_ControlPane_Primary(object):
    def setupUi(self, ControlPane_Primary):
        if not ControlPane_Primary.objectName():
            ControlPane_Primary.setObjectName(u"ControlPane_Primary")
        ControlPane_Primary.resize(200, 630)
        self.gridLayout = QGridLayout(ControlPane_Primary)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.controls = QVBoxLayout()
        self.controls.setObjectName(u"controls")
        self.timeStepGroup = FoldingGroupBox(ControlPane_Primary)
        self.timeStepGroup.setObjectName(u"timeStepGroup")
        self.timeStepGroup.setAlignment(Qt.AlignCenter)
        self.verticalLayout_5 = QVBoxLayout(self.timeStepGroup)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.timestepdummyWidget = QWidget(self.timeStepGroup)
        self.timestepdummyWidget.setObjectName(u"timestepdummyWidget")
        self.gridLayout_6 = QGridLayout(self.timestepdummyWidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(2)
        self.gridLayout_6.setContentsMargins(3, 1, 3, 4)
        self.nextTimeStep = QPushButton(self.timestepdummyWidget)
        self.nextTimeStep.setObjectName(u"nextTimeStep")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextTimeStep.sizePolicy().hasHeightForWidth())
        self.nextTimeStep.setSizePolicy(sizePolicy)
        self.nextTimeStep.setMaximumSize(QSize(24, 16777215))
        self.nextTimeStep.setBaseSize(QSize(16, 16))
        font = QFont()
        font.setFamilies([u"Segoe Fluent Icons"])
        font.setPointSize(10)
        font.setBold(True)
        font.setStrikeOut(False)
        self.nextTimeStep.setFont(font)
        self.nextTimeStep.setCheckable(False)
        self.nextTimeStep.setAutoRepeat(False)
        self.nextTimeStep.setFlat(False)

        self.gridLayout_6.addWidget(self.nextTimeStep, 0, 2, 1, 1)

        self.prevTimeStep = QPushButton(self.timestepdummyWidget)
        self.prevTimeStep.setObjectName(u"prevTimeStep")
        sizePolicy.setHeightForWidth(self.prevTimeStep.sizePolicy().hasHeightForWidth())
        self.prevTimeStep.setSizePolicy(sizePolicy)
        self.prevTimeStep.setMaximumSize(QSize(24, 16777215))
        self.prevTimeStep.setBaseSize(QSize(16, 16))
        self.prevTimeStep.setFont(font)

        self.gridLayout_6.addWidget(self.prevTimeStep, 0, 0, 1, 1)

        self.timeStepSelector = QComboBox(self.timestepdummyWidget)
        self.timeStepSelector.setObjectName(u"timeStepSelector")
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(11)
        self.timeStepSelector.setFont(font1)
        self.timeStepSelector.setEditable(False)

        self.gridLayout_6.addWidget(self.timeStepSelector, 0, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.timelabelLabel = QLabel(self.timestepdummyWidget)
        self.timelabelLabel.setObjectName(u"timelabelLabel")
        font2 = QFont()
        font2.setPointSize(8)
        self.timelabelLabel.setFont(font2)

        self.horizontalLayout_4.addWidget(self.timelabelLabel)

        self.timeLabel = QLabel(self.timestepdummyWidget)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setFont(font2)
        self.timeLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.timeLabel)


        self.gridLayout_6.addLayout(self.horizontalLayout_4, 5, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.timestepdummyWidget)


        self.controls.addWidget(self.timeStepGroup)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.controls.addItem(self.verticalSpacer_3)

        self.contourDataGroup = FoldingGroupBox(ControlPane_Primary)
        self.contourDataGroup.setObjectName(u"contourDataGroup")
        self.contourDataGroup.setEnabled(True)
        self.contourDataGroup.setAlignment(Qt.AlignCenter)
        self.verticalLayout_4 = QVBoxLayout(self.contourDataGroup)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget = QWidget(self.contourDataGroup)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalLayout_6 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.colorLabel = QLabel(self.verticalWidget)
        self.colorLabel.setObjectName(u"colorLabel")
        self.colorLabel.setFont(font2)

        self.verticalLayout_6.addWidget(self.colorLabel)

        self.contourdummyWidget2_2 = QWidget(self.verticalWidget)
        self.contourdummyWidget2_2.setObjectName(u"contourdummyWidget2_2")
        self.horizontalLayout_3 = QHBoxLayout(self.contourdummyWidget2_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.plotdatasetSelector = QComboBox(self.contourdummyWidget2_2)
        self.plotdatasetSelector.setObjectName(u"plotdatasetSelector")
        font3 = QFont()
        font3.setPointSize(10)
        self.plotdatasetSelector.setFont(font3)

        self.horizontalLayout_3.addWidget(self.plotdatasetSelector)


        self.verticalLayout_6.addWidget(self.contourdummyWidget2_2)

        self.contourdummyWidget1 = QWidget(self.verticalWidget)
        self.contourdummyWidget1.setObjectName(u"contourdummyWidget1")
        self.horizontalLayout_6 = QHBoxLayout(self.contourdummyWidget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.colorCheckBox = QCheckBox(self.contourdummyWidget1)
        self.colorCheckBox.setObjectName(u"colorCheckBox")

        self.horizontalLayout_6.addWidget(self.colorCheckBox)

        self.colorminLineEdit = QLineEdit(self.contourdummyWidget1)
        self.colorminLineEdit.setObjectName(u"colorminLineEdit")
        self.colorminLineEdit.setEnabled(False)
        font4 = QFont()
        font4.setFamilies([u"Consolas"])
        font4.setPointSize(8)
        self.colorminLineEdit.setFont(font4)

        self.horizontalLayout_6.addWidget(self.colorminLineEdit)

        self.colormaxLineEdit = QLineEdit(self.contourdummyWidget1)
        self.colormaxLineEdit.setObjectName(u"colormaxLineEdit")
        self.colormaxLineEdit.setEnabled(False)
        self.colormaxLineEdit.setFont(font4)

        self.horizontalLayout_6.addWidget(self.colormaxLineEdit)


        self.verticalLayout_6.addWidget(self.contourdummyWidget1)

        self.maskingLabel = QLabel(self.verticalWidget)
        self.maskingLabel.setObjectName(u"maskingLabel")
        self.maskingLabel.setFont(font2)

        self.verticalLayout_6.addWidget(self.maskingLabel)

        self.contourdummyWidget2 = QWidget(self.verticalWidget)
        self.contourdummyWidget2.setObjectName(u"contourdummyWidget2")
        self.horizontalLayout_2 = QHBoxLayout(self.contourdummyWidget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.maskdatasetSelector = QComboBox(self.contourdummyWidget2)
        self.maskdatasetSelector.setObjectName(u"maskdatasetSelector")
        self.maskdatasetSelector.setEnabled(False)
        self.maskdatasetSelector.setFont(font3)

        self.horizontalLayout_2.addWidget(self.maskdatasetSelector)

        self.maskdatasetLockButton = QPushButton(self.contourdummyWidget2)
        self.maskdatasetLockButton.setObjectName(u"maskdatasetLockButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.maskdatasetLockButton.sizePolicy().hasHeightForWidth())
        self.maskdatasetLockButton.setSizePolicy(sizePolicy1)
        self.maskdatasetLockButton.setMaximumSize(QSize(24, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Segoe Fluent Icons"])
        font5.setPointSize(11)
        self.maskdatasetLockButton.setFont(font5)
        self.maskdatasetLockButton.setCheckable(True)
        self.maskdatasetLockButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.maskdatasetLockButton)


        self.verticalLayout_6.addWidget(self.contourdummyWidget2)

        self.contourdummyWidget3 = QWidget(self.verticalWidget)
        self.contourdummyWidget3.setObjectName(u"contourdummyWidget3")
        self.horizontalLayout_7 = QHBoxLayout(self.contourdummyWidget3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.maskCheckBox = QCheckBox(self.contourdummyWidget3)
        self.maskCheckBox.setObjectName(u"maskCheckBox")

        self.horizontalLayout_7.addWidget(self.maskCheckBox)

        self.maskminLineEdit = QLineEdit(self.contourdummyWidget3)
        self.maskminLineEdit.setObjectName(u"maskminLineEdit")
        self.maskminLineEdit.setEnabled(False)
        self.maskminLineEdit.setFont(font4)

        self.horizontalLayout_7.addWidget(self.maskminLineEdit)

        self.maskmaxLineEdit = QLineEdit(self.contourdummyWidget3)
        self.maskmaxLineEdit.setObjectName(u"maskmaxLineEdit")
        self.maskmaxLineEdit.setEnabled(False)
        self.maskmaxLineEdit.setFont(font4)

        self.horizontalLayout_7.addWidget(self.maskmaxLineEdit)


        self.verticalLayout_6.addWidget(self.contourdummyWidget3)


        self.verticalLayout_4.addWidget(self.verticalWidget)


        self.controls.addWidget(self.contourDataGroup)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.controls.addItem(self.verticalSpacer_4)

        self.gsGroup = FoldingGroupBox(ControlPane_Primary)
        self.gsGroup.setObjectName(u"gsGroup")
        self.gsGroup.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_10 = QHBoxLayout(self.gsGroup)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gsdummyWidget = QWidget(self.gsGroup)
        self.gsdummyWidget.setObjectName(u"gsdummyWidget")
        self.gridLayout_5 = QGridLayout(self.gsdummyWidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(4, 4, 4, 4)
        self.xgsLineEdit = QLineEdit(self.gsdummyWidget)
        self.xgsLineEdit.setObjectName(u"xgsLineEdit")
        font6 = QFont()
        font6.setFamilies([u"Consolas"])
        font6.setPointSize(9)
        self.xgsLineEdit.setFont(font6)

        self.gridLayout_5.addWidget(self.xgsLineEdit, 1, 1, 1, 1)

        self.ygsLineEdit = QLineEdit(self.gsdummyWidget)
        self.ygsLineEdit.setObjectName(u"ygsLineEdit")
        self.ygsLineEdit.setFont(font6)

        self.gridLayout_5.addWidget(self.ygsLineEdit, 2, 1, 1, 1)

        self.zgsLineEdit = QLineEdit(self.gsdummyWidget)
        self.zgsLineEdit.setObjectName(u"zgsLineEdit")
        self.zgsLineEdit.setFont(font6)

        self.gridLayout_5.addWidget(self.zgsLineEdit, 3, 1, 1, 1)

        self.gsLockButton = QPushButton(self.gsdummyWidget)
        self.gsLockButton.setObjectName(u"gsLockButton")
        sizePolicy1.setHeightForWidth(self.gsLockButton.sizePolicy().hasHeightForWidth())
        self.gsLockButton.setSizePolicy(sizePolicy1)
        self.gsLockButton.setMaximumSize(QSize(24, 16777215))
        self.gsLockButton.setFont(font5)
        self.gsLockButton.setCheckable(True)
        self.gsLockButton.setChecked(True)

        self.gridLayout_5.addWidget(self.gsLockButton, 1, 2, 1, 1)


        self.horizontalLayout_10.addWidget(self.gsdummyWidget)


        self.controls.addWidget(self.gsGroup)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.controls.addItem(self.verticalSpacer_5)

        self.exagGroup = FoldingGroupBox(ControlPane_Primary)
        self.exagGroup.setObjectName(u"exagGroup")
        self.exagGroup.setEnabled(True)
        self.exagGroup.setAlignment(Qt.AlignCenter)
        self.exagGroup.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.exagGroup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.exagdummyWidget = QWidget(self.exagGroup)
        self.exagdummyWidget.setObjectName(u"exagdummyWidget")
        self.gridLayout_4 = QGridLayout(self.exagdummyWidget)
        self.gridLayout_4.setSpacing(4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(4, 4, 4, 4)
        self.xexagSpinBox = QDoubleSpinBox(self.exagdummyWidget)
        self.xexagSpinBox.setObjectName(u"xexagSpinBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.xexagSpinBox.sizePolicy().hasHeightForWidth())
        self.xexagSpinBox.setSizePolicy(sizePolicy2)
        self.xexagSpinBox.setMinimumSize(QSize(45, 0))
        self.xexagSpinBox.setFont(font4)
        self.xexagSpinBox.setDecimals(1)
        self.xexagSpinBox.setMaximum(1000.000000000000000)

        self.gridLayout_4.addWidget(self.xexagSpinBox, 0, 0, 1, 1)

        self.yexagSpinBox = QDoubleSpinBox(self.exagdummyWidget)
        self.yexagSpinBox.setObjectName(u"yexagSpinBox")
        sizePolicy2.setHeightForWidth(self.yexagSpinBox.sizePolicy().hasHeightForWidth())
        self.yexagSpinBox.setSizePolicy(sizePolicy2)
        self.yexagSpinBox.setMinimumSize(QSize(45, 0))
        self.yexagSpinBox.setFont(font4)
        self.yexagSpinBox.setKeyboardTracking(False)
        self.yexagSpinBox.setDecimals(1)
        self.yexagSpinBox.setMaximum(1000.000000000000000)

        self.gridLayout_4.addWidget(self.yexagSpinBox, 0, 1, 1, 1)

        self.zexagSpinBox = QDoubleSpinBox(self.exagdummyWidget)
        self.zexagSpinBox.setObjectName(u"zexagSpinBox")
        sizePolicy2.setHeightForWidth(self.zexagSpinBox.sizePolicy().hasHeightForWidth())
        self.zexagSpinBox.setSizePolicy(sizePolicy2)
        self.zexagSpinBox.setMinimumSize(QSize(45, 0))
        self.zexagSpinBox.setFont(font4)
        self.zexagSpinBox.setDecimals(1)
        self.zexagSpinBox.setMaximum(1000.000000000000000)

        self.gridLayout_4.addWidget(self.zexagSpinBox, 0, 2, 1, 1)

        self.exagLockButton = QPushButton(self.exagdummyWidget)
        self.exagLockButton.setObjectName(u"exagLockButton")
        sizePolicy1.setHeightForWidth(self.exagLockButton.sizePolicy().hasHeightForWidth())
        self.exagLockButton.setSizePolicy(sizePolicy1)
        self.exagLockButton.setMaximumSize(QSize(24, 16777215))
        self.exagLockButton.setFont(font5)
        self.exagLockButton.setCheckable(True)
        self.exagLockButton.setChecked(True)

        self.gridLayout_4.addWidget(self.exagLockButton, 0, 3, 1, 1)


        self.verticalLayout.addWidget(self.exagdummyWidget)


        self.controls.addWidget(self.exagGroup)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.controls.addItem(self.verticalSpacer_2)

        self.extentsGroup = FoldingGroupBox(ControlPane_Primary)
        self.extentsGroup.setObjectName(u"extentsGroup")
        self.extentsGroup.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2 = QVBoxLayout(self.extentsGroup)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.clippingboxButton = QPushButton(self.extentsGroup)
        self.clippingboxButton.setObjectName(u"clippingboxButton")
        self.clippingboxButton.setCheckable(True)

        self.verticalLayout_2.addWidget(self.clippingboxButton)

        self.extentsdummyWidget = QWidget(self.extentsGroup)
        self.extentsdummyWidget.setObjectName(u"extentsdummyWidget")
        self.gridLayout_2 = QGridLayout(self.extentsdummyWidget)
        self.gridLayout_2.setSpacing(4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(4, 1, 4, 4)
        self.xminLineEdit = QLineEdit(self.extentsdummyWidget)
        self.xminLineEdit.setObjectName(u"xminLineEdit")
        self.xminLineEdit.setEnabled(False)
        self.xminLineEdit.setFont(font4)

        self.gridLayout_2.addWidget(self.xminLineEdit, 0, 2, 1, 1)

        self.yminLineEdit = QLineEdit(self.extentsdummyWidget)
        self.yminLineEdit.setObjectName(u"yminLineEdit")
        self.yminLineEdit.setEnabled(False)
        self.yminLineEdit.setFont(font4)

        self.gridLayout_2.addWidget(self.yminLineEdit, 2, 2, 1, 1)

        self.zminLineEdit = QLineEdit(self.extentsdummyWidget)
        self.zminLineEdit.setObjectName(u"zminLineEdit")
        self.zminLineEdit.setEnabled(False)
        self.zminLineEdit.setFont(font4)

        self.gridLayout_2.addWidget(self.zminLineEdit, 3, 2, 1, 1)

        self.xmaxLineEdit = QLineEdit(self.extentsdummyWidget)
        self.xmaxLineEdit.setObjectName(u"xmaxLineEdit")
        self.xmaxLineEdit.setEnabled(False)
        self.xmaxLineEdit.setFont(font4)

        self.gridLayout_2.addWidget(self.xmaxLineEdit, 0, 3, 1, 1)

        self.ymaxLineEdit = QLineEdit(self.extentsdummyWidget)
        self.ymaxLineEdit.setObjectName(u"ymaxLineEdit")
        self.ymaxLineEdit.setEnabled(False)
        self.ymaxLineEdit.setFont(font4)

        self.gridLayout_2.addWidget(self.ymaxLineEdit, 2, 3, 1, 1)

        self.zmaxLineEdit = QLineEdit(self.extentsdummyWidget)
        self.zmaxLineEdit.setObjectName(u"zmaxLineEdit")
        self.zmaxLineEdit.setEnabled(False)
        self.zmaxLineEdit.setFont(font4)

        self.gridLayout_2.addWidget(self.zmaxLineEdit, 3, 3, 1, 1)

        self.xLabel = QLabel(self.extentsdummyWidget)
        self.xLabel.setObjectName(u"xLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.xLabel.sizePolicy().hasHeightForWidth())
        self.xLabel.setSizePolicy(sizePolicy3)
        self.xLabel.setFont(font2)
        self.xLabel.setScaledContents(False)

        self.gridLayout_2.addWidget(self.xLabel, 0, 0, 1, 1)

        self.zLabel = QLabel(self.extentsdummyWidget)
        self.zLabel.setObjectName(u"zLabel")
        sizePolicy3.setHeightForWidth(self.zLabel.sizePolicy().hasHeightForWidth())
        self.zLabel.setSizePolicy(sizePolicy3)
        self.zLabel.setFont(font2)
        self.zLabel.setScaledContents(False)

        self.gridLayout_2.addWidget(self.zLabel, 3, 0, 1, 1)

        self.zclipCheckBox = QCheckBox(self.extentsdummyWidget)
        self.zclipCheckBox.setObjectName(u"zclipCheckBox")

        self.gridLayout_2.addWidget(self.zclipCheckBox, 3, 1, 1, 1)

        self.yLabel = QLabel(self.extentsdummyWidget)
        self.yLabel.setObjectName(u"yLabel")
        sizePolicy3.setHeightForWidth(self.yLabel.sizePolicy().hasHeightForWidth())
        self.yLabel.setSizePolicy(sizePolicy3)
        self.yLabel.setFont(font2)
        self.yLabel.setScaledContents(False)

        self.gridLayout_2.addWidget(self.yLabel, 2, 0, 1, 1)

        self.yclipCheckBox = QCheckBox(self.extentsdummyWidget)
        self.yclipCheckBox.setObjectName(u"yclipCheckBox")

        self.gridLayout_2.addWidget(self.yclipCheckBox, 2, 1, 1, 1)

        self.xclipCheckBox = QCheckBox(self.extentsdummyWidget)
        self.xclipCheckBox.setObjectName(u"xclipCheckBox")

        self.gridLayout_2.addWidget(self.xclipCheckBox, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.extentsdummyWidget)


        self.controls.addWidget(self.extentsGroup)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.controls.addItem(self.verticalSpacer)

        self.cameraLocationGroup = FoldingGroupBox(ControlPane_Primary)
        self.cameraLocationGroup.setObjectName(u"cameraLocationGroup")
        self.cameraLocationGroup.setAlignment(Qt.AlignCenter)
        self.verticalLayout_3 = QVBoxLayout(self.cameraLocationGroup)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cameralocationdummyWidget = QWidget(self.cameraLocationGroup)
        self.cameralocationdummyWidget.setObjectName(u"cameralocationdummyWidget")
        self.cameralocationdummyWidget.setCursor(QCursor(Qt.WhatsThisCursor))
        self.verticalLayout_7 = QVBoxLayout(self.cameralocationdummyWidget)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(4, 1, 4, 4)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setSpacing(2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, -1, -1, 0)
        self.viewupLabel = QLabel(self.cameralocationdummyWidget)
        self.viewupLabel.setObjectName(u"viewupLabel")
        self.viewupLabel.setMaximumSize(QSize(65, 16777215))
        font7 = QFont()
        font7.setPointSize(9)
        self.viewupLabel.setFont(font7)
        self.viewupLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.viewupLabel, 0, 0, 1, 1)

        self.positionLabel = QLabel(self.cameralocationdummyWidget)
        self.positionLabel.setObjectName(u"positionLabel")
        self.positionLabel.setMaximumSize(QSize(65, 16777215))
        self.positionLabel.setFont(font7)
        self.positionLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.positionLabel, 1, 0, 1, 1)

        self.focalLabel = QLabel(self.cameralocationdummyWidget)
        self.focalLabel.setObjectName(u"focalLabel")
        self.focalLabel.setMaximumSize(QSize(65, 16777215))
        self.focalLabel.setFont(font7)
        self.focalLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.focalLabel, 2, 0, 1, 1)

        self.focalValue = QLabel(self.cameralocationdummyWidget)
        self.focalValue.setObjectName(u"focalValue")
        self.focalValue.setFont(font4)

        self.gridLayout_7.addWidget(self.focalValue, 2, 1, 1, 1)

        self.positionValue = QLabel(self.cameralocationdummyWidget)
        self.positionValue.setObjectName(u"positionValue")
        self.positionValue.setFont(font4)

        self.gridLayout_7.addWidget(self.positionValue, 1, 1, 1, 1)

        self.viewupValue = QLabel(self.cameralocationdummyWidget)
        self.viewupValue.setObjectName(u"viewupValue")
        self.viewupValue.setFont(font4)

        self.gridLayout_7.addWidget(self.viewupValue, 0, 1, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_7)


        self.verticalLayout_3.addWidget(self.cameralocationdummyWidget)


        self.controls.addWidget(self.cameraLocationGroup)


        self.gridLayout.addLayout(self.controls, 0, 0, 1, 1)


        self.retranslateUi(ControlPane_Primary)

        QMetaObject.connectSlotsByName(ControlPane_Primary)
    # setupUi

    def retranslateUi(self, ControlPane_Primary):
        ControlPane_Primary.setWindowTitle(QCoreApplication.translate("ControlPane_Primary", u"Form", None))
        self.timeStepGroup.setTitle(QCoreApplication.translate("ControlPane_Primary", u"Time Step", None))
        self.nextTimeStep.setText(QCoreApplication.translate("ControlPane_Primary", u"\ue72a", None))
#if QT_CONFIG(shortcut)
        self.nextTimeStep.setShortcut(QCoreApplication.translate("ControlPane_Primary", u"Ctrl+Right", None))
#endif // QT_CONFIG(shortcut)
        self.prevTimeStep.setText(QCoreApplication.translate("ControlPane_Primary", u"\ue72b", None))
#if QT_CONFIG(shortcut)
        self.prevTimeStep.setShortcut(QCoreApplication.translate("ControlPane_Primary", u"Ctrl+Left", None))
#endif // QT_CONFIG(shortcut)
        self.timeStepSelector.setCurrentText("")
        self.timelabelLabel.setText(QCoreApplication.translate("ControlPane_Primary", u"Time:", None))
        self.timeLabel.setText("")
        self.contourDataGroup.setTitle(QCoreApplication.translate("ControlPane_Primary", u"Contour Data", None))
        self.colorLabel.setText(QCoreApplication.translate("ControlPane_Primary", u"Color", None))
        self.colorCheckBox.setText("")
        self.maskingLabel.setText(QCoreApplication.translate("ControlPane_Primary", u"Masking", None))
#if QT_CONFIG(tooltip)
        self.maskdatasetLockButton.setToolTip(QCoreApplication.translate("ControlPane_Primary", u"Toggle separate mask and plot datasets", None))
#endif // QT_CONFIG(tooltip)
        self.maskdatasetLockButton.setText(QCoreApplication.translate("ControlPane_Primary", u"\ue72e", None))
        self.maskCheckBox.setText("")
        self.gsGroup.setTitle(QCoreApplication.translate("ControlPane_Primary", u"Grid Spacing", None))
#if QT_CONFIG(tooltip)
        self.gsLockButton.setToolTip(QCoreApplication.translate("ControlPane_Primary", u"Toggle uniform/non-uniform grid spacing", None))
#endif // QT_CONFIG(tooltip)
        self.gsLockButton.setText(QCoreApplication.translate("ControlPane_Primary", u"\ue72e", None))
        self.exagGroup.setTitle(QCoreApplication.translate("ControlPane_Primary", u"Exaggeration", None))
        self.yexagSpinBox.setSuffix("")
#if QT_CONFIG(tooltip)
        self.exagLockButton.setToolTip(QCoreApplication.translate("ControlPane_Primary", u"Toggle uniform/non-uniform exaggeration", None))
#endif // QT_CONFIG(tooltip)
        self.exagLockButton.setText(QCoreApplication.translate("ControlPane_Primary", u"\ue72e", None))
        self.extentsGroup.setTitle(QCoreApplication.translate("ControlPane_Primary", u"Clipping Extents", None))
        self.clippingboxButton.setText(QCoreApplication.translate("ControlPane_Primary", u"\u26f6", None))
        self.xLabel.setText(QCoreApplication.translate("ControlPane_Primary", u"X", None))
        self.zLabel.setText(QCoreApplication.translate("ControlPane_Primary", u"Z", None))
        self.zclipCheckBox.setText("")
        self.yLabel.setText(QCoreApplication.translate("ControlPane_Primary", u"Y", None))
        self.yclipCheckBox.setText("")
        self.xclipCheckBox.setText("")
        self.cameraLocationGroup.setTitle(QCoreApplication.translate("ControlPane_Primary", u"Camera Location", None))
#if QT_CONFIG(tooltip)
        self.cameralocationdummyWidget.setToolTip(QCoreApplication.translate("ControlPane_Primary", u"Left Click to copy camera location\n"
"Right Click to paste", None))
#endif // QT_CONFIG(tooltip)
        self.viewupLabel.setText(QCoreApplication.translate("ControlPane_Primary", u"View-up:", None))
        self.positionLabel.setText(QCoreApplication.translate("ControlPane_Primary", u"Position:", None))
        self.focalLabel.setText(QCoreApplication.translate("ControlPane_Primary", u"Focal point:", None))
        self.focalValue.setText("")
        self.positionValue.setText("")
        self.viewupValue.setText("")
    # retranslateUi

