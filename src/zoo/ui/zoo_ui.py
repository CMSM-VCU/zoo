# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zoo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(925, 743)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.viewport = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewport.sizePolicy().hasHeightForWidth())
        self.viewport.setSizePolicy(sizePolicy)
        self.viewport.setMinimumSize(QtCore.QSize(300, 0))
        self.viewport.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.viewport.setFrameShadow(QtWidgets.QFrame.Raised)
        self.viewport.setObjectName("viewport")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.viewport)
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout.addWidget(self.viewport)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.controlPane = QtWidgets.QFrame(self.centralwidget)
        self.controlPane.setEnabled(True)
        self.controlPane.setMaximumSize(QtCore.QSize(200, 16777215))
        self.controlPane.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.controlPane.setFrameShadow(QtWidgets.QFrame.Raised)
        self.controlPane.setObjectName("controlPane")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.controlPane)
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.controls = QtWidgets.QVBoxLayout()
        self.controls.setSpacing(6)
        self.controls.setObjectName("controls")
        self.timeStepGroup = QtWidgets.QGroupBox(self.controlPane)
        self.timeStepGroup.setObjectName("timeStepGroup")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.timeStepGroup)
        self.verticalLayout_5.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.nextTimeStep = QtWidgets.QPushButton(self.timeStepGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextTimeStep.sizePolicy().hasHeightForWidth())
        self.nextTimeStep.setSizePolicy(sizePolicy)
        self.nextTimeStep.setMaximumSize(QtCore.QSize(24, 16777215))
        self.nextTimeStep.setBaseSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.nextTimeStep.setFont(font)
        self.nextTimeStep.setCheckable(False)
        self.nextTimeStep.setAutoRepeat(False)
        self.nextTimeStep.setFlat(False)
        self.nextTimeStep.setObjectName("nextTimeStep")
        self.gridLayout_6.addWidget(self.nextTimeStep, 0, 2, 1, 1)
        self.prevTimeStep = QtWidgets.QPushButton(self.timeStepGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prevTimeStep.sizePolicy().hasHeightForWidth())
        self.prevTimeStep.setSizePolicy(sizePolicy)
        self.prevTimeStep.setMaximumSize(QtCore.QSize(24, 16777215))
        self.prevTimeStep.setBaseSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.prevTimeStep.setFont(font)
        self.prevTimeStep.setObjectName("prevTimeStep")
        self.gridLayout_6.addWidget(self.prevTimeStep, 0, 0, 1, 1)
        self.timeStepSelector = QtWidgets.QComboBox(self.timeStepGroup)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.timeStepSelector.setFont(font)
        self.timeStepSelector.setEditable(False)
        self.timeStepSelector.setCurrentText("")
        self.timeStepSelector.setObjectName("timeStepSelector")
        self.gridLayout_6.addWidget(self.timeStepSelector, 0, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.timelabelLabel = QtWidgets.QLabel(self.timeStepGroup)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.timelabelLabel.setFont(font)
        self.timelabelLabel.setObjectName("timelabelLabel")
        self.horizontalLayout_4.addWidget(self.timelabelLabel)
        self.timeLabel = QtWidgets.QLabel(self.timeStepGroup)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.timeLabel.setFont(font)
        self.timeLabel.setText("")
        self.timeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout_4.addWidget(self.timeLabel)
        self.gridLayout_6.addLayout(self.horizontalLayout_4, 5, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_6)
        self.controls.addWidget(self.timeStepGroup)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.controls.addItem(spacerItem)
        self.contourDataGroup = QtWidgets.QGroupBox(self.controlPane)
        self.contourDataGroup.setEnabled(True)
        self.contourDataGroup.setObjectName("contourDataGroup")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.contourDataGroup)
        self.verticalLayout_4.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.colorLabel = QtWidgets.QLabel(self.contourDataGroup)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.colorLabel.setFont(font)
        self.colorLabel.setObjectName("colorLabel")
        self.verticalLayout_4.addWidget(self.colorLabel)
        self.plotdatasetSelector = QtWidgets.QComboBox(self.contourDataGroup)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plotdatasetSelector.setFont(font)
        self.plotdatasetSelector.setObjectName("plotdatasetSelector")
        self.verticalLayout_4.addWidget(self.plotdatasetSelector)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.colorCheckBox = QtWidgets.QCheckBox(self.contourDataGroup)
        self.colorCheckBox.setText("")
        self.colorCheckBox.setObjectName("colorCheckBox")
        self.horizontalLayout_6.addWidget(self.colorCheckBox)
        self.colorminLineEdit = QtWidgets.QLineEdit(self.contourDataGroup)
        self.colorminLineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.colorminLineEdit.setFont(font)
        self.colorminLineEdit.setObjectName("colorminLineEdit")
        self.horizontalLayout_6.addWidget(self.colorminLineEdit)
        self.colormaxLineEdit = QtWidgets.QLineEdit(self.contourDataGroup)
        self.colormaxLineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.colormaxLineEdit.setFont(font)
        self.colormaxLineEdit.setObjectName("colormaxLineEdit")
        self.horizontalLayout_6.addWidget(self.colormaxLineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_4.addItem(spacerItem1)
        self.maskingLabel = QtWidgets.QLabel(self.contourDataGroup)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.maskingLabel.setFont(font)
        self.maskingLabel.setObjectName("maskingLabel")
        self.verticalLayout_4.addWidget(self.maskingLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.maskdatasetSelector = QtWidgets.QComboBox(self.contourDataGroup)
        self.maskdatasetSelector.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.maskdatasetSelector.setFont(font)
        self.maskdatasetSelector.setObjectName("maskdatasetSelector")
        self.horizontalLayout_2.addWidget(self.maskdatasetSelector)
        self.maskdatasetLockButton = QtWidgets.QPushButton(self.contourDataGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maskdatasetLockButton.sizePolicy().hasHeightForWidth())
        self.maskdatasetLockButton.setSizePolicy(sizePolicy)
        self.maskdatasetLockButton.setMaximumSize(QtCore.QSize(24, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(11)
        self.maskdatasetLockButton.setFont(font)
        self.maskdatasetLockButton.setCheckable(True)
        self.maskdatasetLockButton.setChecked(True)
        self.maskdatasetLockButton.setObjectName("maskdatasetLockButton")
        self.horizontalLayout_2.addWidget(self.maskdatasetLockButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.maskCheckBox = QtWidgets.QCheckBox(self.contourDataGroup)
        self.maskCheckBox.setText("")
        self.maskCheckBox.setObjectName("maskCheckBox")
        self.horizontalLayout_7.addWidget(self.maskCheckBox)
        self.maskminLineEdit = QtWidgets.QLineEdit(self.contourDataGroup)
        self.maskminLineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.maskminLineEdit.setFont(font)
        self.maskminLineEdit.setObjectName("maskminLineEdit")
        self.horizontalLayout_7.addWidget(self.maskminLineEdit)
        self.maskmaxLineEdit = QtWidgets.QLineEdit(self.contourDataGroup)
        self.maskmaxLineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.maskmaxLineEdit.setFont(font)
        self.maskmaxLineEdit.setObjectName("maskmaxLineEdit")
        self.horizontalLayout_7.addWidget(self.maskmaxLineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.controls.addWidget(self.contourDataGroup)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.controls.addItem(spacerItem2)
        self.gsGroup = QtWidgets.QGroupBox(self.controlPane)
        self.gsGroup.setObjectName("gsGroup")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.gsGroup)
        self.horizontalLayout_10.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.xgsLineEdit = QtWidgets.QLineEdit(self.gsGroup)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.xgsLineEdit.setFont(font)
        self.xgsLineEdit.setObjectName("xgsLineEdit")
        self.gridLayout_5.addWidget(self.xgsLineEdit, 1, 1, 1, 1)
        self.ygsLineEdit = QtWidgets.QLineEdit(self.gsGroup)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.ygsLineEdit.setFont(font)
        self.ygsLineEdit.setObjectName("ygsLineEdit")
        self.gridLayout_5.addWidget(self.ygsLineEdit, 2, 1, 1, 1)
        self.zgsLineEdit = QtWidgets.QLineEdit(self.gsGroup)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.zgsLineEdit.setFont(font)
        self.zgsLineEdit.setObjectName("zgsLineEdit")
        self.gridLayout_5.addWidget(self.zgsLineEdit, 3, 1, 1, 1)
        self.gsLockButton = QtWidgets.QPushButton(self.gsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gsLockButton.sizePolicy().hasHeightForWidth())
        self.gsLockButton.setSizePolicy(sizePolicy)
        self.gsLockButton.setMaximumSize(QtCore.QSize(24, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(11)
        self.gsLockButton.setFont(font)
        self.gsLockButton.setCheckable(True)
        self.gsLockButton.setChecked(True)
        self.gsLockButton.setObjectName("gsLockButton")
        self.gridLayout_5.addWidget(self.gsLockButton, 1, 2, 1, 1)
        self.horizontalLayout_10.addLayout(self.gridLayout_5)
        self.controls.addWidget(self.gsGroup)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.controls.addItem(spacerItem3)
        self.exagGroup = QtWidgets.QGroupBox(self.controlPane)
        self.exagGroup.setEnabled(True)
        self.exagGroup.setCheckable(False)
        self.exagGroup.setObjectName("exagGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.exagGroup)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.xexagSpinBox = QtWidgets.QDoubleSpinBox(self.exagGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xexagSpinBox.sizePolicy().hasHeightForWidth())
        self.xexagSpinBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.xexagSpinBox.setFont(font)
        self.xexagSpinBox.setDecimals(1)
        self.xexagSpinBox.setMaximum(1000.0)
        self.xexagSpinBox.setObjectName("xexagSpinBox")
        self.gridLayout_4.addWidget(self.xexagSpinBox, 0, 0, 1, 1)
        self.yexagSpinBox = QtWidgets.QDoubleSpinBox(self.exagGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yexagSpinBox.sizePolicy().hasHeightForWidth())
        self.yexagSpinBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.yexagSpinBox.setFont(font)
        self.yexagSpinBox.setKeyboardTracking(False)
        self.yexagSpinBox.setSuffix("")
        self.yexagSpinBox.setDecimals(1)
        self.yexagSpinBox.setMaximum(1000.0)
        self.yexagSpinBox.setObjectName("yexagSpinBox")
        self.gridLayout_4.addWidget(self.yexagSpinBox, 0, 1, 1, 1)
        self.zexagSpinBox = QtWidgets.QDoubleSpinBox(self.exagGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zexagSpinBox.sizePolicy().hasHeightForWidth())
        self.zexagSpinBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.zexagSpinBox.setFont(font)
        self.zexagSpinBox.setDecimals(1)
        self.zexagSpinBox.setMaximum(1000.0)
        self.zexagSpinBox.setObjectName("zexagSpinBox")
        self.gridLayout_4.addWidget(self.zexagSpinBox, 0, 2, 1, 1)
        self.exagLockButton = QtWidgets.QPushButton(self.exagGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exagLockButton.sizePolicy().hasHeightForWidth())
        self.exagLockButton.setSizePolicy(sizePolicy)
        self.exagLockButton.setMaximumSize(QtCore.QSize(24, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(11)
        self.exagLockButton.setFont(font)
        self.exagLockButton.setCheckable(True)
        self.exagLockButton.setChecked(True)
        self.exagLockButton.setObjectName("exagLockButton")
        self.gridLayout_4.addWidget(self.exagLockButton, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.controls.addWidget(self.exagGroup)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.controls.addItem(spacerItem4)
        self.extentsGroup = QtWidgets.QGroupBox(self.controlPane)
        self.extentsGroup.setObjectName("extentsGroup")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.extentsGroup)
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.xminLineEdit = QtWidgets.QLineEdit(self.extentsGroup)
        self.xminLineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.xminLineEdit.setFont(font)
        self.xminLineEdit.setObjectName("xminLineEdit")
        self.gridLayout_2.addWidget(self.xminLineEdit, 0, 2, 1, 1)
        self.yminLineEdit = QtWidgets.QLineEdit(self.extentsGroup)
        self.yminLineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.yminLineEdit.setFont(font)
        self.yminLineEdit.setObjectName("yminLineEdit")
        self.gridLayout_2.addWidget(self.yminLineEdit, 2, 2, 1, 1)
        self.zminLineEdit = QtWidgets.QLineEdit(self.extentsGroup)
        self.zminLineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.zminLineEdit.setFont(font)
        self.zminLineEdit.setObjectName("zminLineEdit")
        self.gridLayout_2.addWidget(self.zminLineEdit, 3, 2, 1, 1)
        self.xmaxLineEdit = QtWidgets.QLineEdit(self.extentsGroup)
        self.xmaxLineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.xmaxLineEdit.setFont(font)
        self.xmaxLineEdit.setObjectName("xmaxLineEdit")
        self.gridLayout_2.addWidget(self.xmaxLineEdit, 0, 3, 1, 1)
        self.ymaxLineEdit = QtWidgets.QLineEdit(self.extentsGroup)
        self.ymaxLineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.ymaxLineEdit.setFont(font)
        self.ymaxLineEdit.setObjectName("ymaxLineEdit")
        self.gridLayout_2.addWidget(self.ymaxLineEdit, 2, 3, 1, 1)
        self.zmaxLineEdit = QtWidgets.QLineEdit(self.extentsGroup)
        self.zmaxLineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.zmaxLineEdit.setFont(font)
        self.zmaxLineEdit.setObjectName("zmaxLineEdit")
        self.gridLayout_2.addWidget(self.zmaxLineEdit, 3, 3, 1, 1)
        self.xLabel = QtWidgets.QLabel(self.extentsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xLabel.sizePolicy().hasHeightForWidth())
        self.xLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.xLabel.setFont(font)
        self.xLabel.setScaledContents(False)
        self.xLabel.setObjectName("xLabel")
        self.gridLayout_2.addWidget(self.xLabel, 0, 0, 1, 1)
        self.zLabel = QtWidgets.QLabel(self.extentsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zLabel.sizePolicy().hasHeightForWidth())
        self.zLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.zLabel.setFont(font)
        self.zLabel.setScaledContents(False)
        self.zLabel.setObjectName("zLabel")
        self.gridLayout_2.addWidget(self.zLabel, 3, 0, 1, 1)
        self.zclipCheckBox = QtWidgets.QCheckBox(self.extentsGroup)
        self.zclipCheckBox.setText("")
        self.zclipCheckBox.setObjectName("zclipCheckBox")
        self.gridLayout_2.addWidget(self.zclipCheckBox, 3, 1, 1, 1)
        self.yLabel = QtWidgets.QLabel(self.extentsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yLabel.sizePolicy().hasHeightForWidth())
        self.yLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.yLabel.setFont(font)
        self.yLabel.setScaledContents(False)
        self.yLabel.setObjectName("yLabel")
        self.gridLayout_2.addWidget(self.yLabel, 2, 0, 1, 1)
        self.yclipCheckBox = QtWidgets.QCheckBox(self.extentsGroup)
        self.yclipCheckBox.setText("")
        self.yclipCheckBox.setObjectName("yclipCheckBox")
        self.gridLayout_2.addWidget(self.yclipCheckBox, 2, 1, 1, 1)
        self.xclipCheckBox = QtWidgets.QCheckBox(self.extentsGroup)
        self.xclipCheckBox.setText("")
        self.xclipCheckBox.setObjectName("xclipCheckBox")
        self.gridLayout_2.addWidget(self.xclipCheckBox, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.controls.addWidget(self.extentsGroup)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.controls.addItem(spacerItem5)
        self.cameraLocationGroup = QtWidgets.QGroupBox(self.controlPane)
        self.cameraLocationGroup.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.cameraLocationGroup.setObjectName("cameraLocationGroup")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.cameraLocationGroup)
        self.gridLayout_3.setContentsMargins(4, 4, 0, 4)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.positionValue = QtWidgets.QLabel(self.cameraLocationGroup)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.positionValue.setFont(font)
        self.positionValue.setText("")
        self.positionValue.setObjectName("positionValue")
        self.gridLayout_3.addWidget(self.positionValue, 0, 1, 1, 1)
        self.focalLabel = QtWidgets.QLabel(self.cameraLocationGroup)
        self.focalLabel.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.focalLabel.setFont(font)
        self.focalLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.focalLabel.setObjectName("focalLabel")
        self.gridLayout_3.addWidget(self.focalLabel, 1, 0, 1, 1)
        self.positionLabel = QtWidgets.QLabel(self.cameraLocationGroup)
        self.positionLabel.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.positionLabel.setFont(font)
        self.positionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.positionLabel.setObjectName("positionLabel")
        self.gridLayout_3.addWidget(self.positionLabel, 0, 0, 1, 1)
        self.viewupLabel = QtWidgets.QLabel(self.cameraLocationGroup)
        self.viewupLabel.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.viewupLabel.setFont(font)
        self.viewupLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.viewupLabel.setObjectName("viewupLabel")
        self.gridLayout_3.addWidget(self.viewupLabel, 2, 0, 1, 1)
        self.focalValue = QtWidgets.QLabel(self.cameraLocationGroup)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.focalValue.setFont(font)
        self.focalValue.setText("")
        self.focalValue.setObjectName("focalValue")
        self.gridLayout_3.addWidget(self.focalValue, 1, 1, 1, 1)
        self.viewupValue = QtWidgets.QLabel(self.cameraLocationGroup)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.viewupValue.setFont(font)
        self.viewupValue.setText("")
        self.viewupValue.setObjectName("viewupValue")
        self.gridLayout_3.addWidget(self.viewupValue, 2, 1, 1, 1)
        self.controls.addWidget(self.cameraLocationGroup)
        self.verticalLayout_3.addLayout(self.controls)
        self.horizontalLayout.addWidget(self.controlPane)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 925, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionShow_Grid = QtWidgets.QAction(MainWindow)
        self.actionShow_Grid.setObjectName("actionShow_Grid")
        self.actionClear_Grid_Cache = QtWidgets.QAction(MainWindow)
        self.actionClear_Grid_Cache.setObjectName("actionClear_Grid_Cache")
        self.actionSave_Image = QtWidgets.QAction(MainWindow)
        self.actionSave_Image.setObjectName("actionSave_Image")
        self.actionCopy_Image = QtWidgets.QAction(MainWindow)
        self.actionCopy_Image.setObjectName("actionCopy_Image")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_Image)
        self.menuFile.addAction(self.actionCopy_Image)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionShow_Grid)
        self.menuView.addAction(self.actionClear_Grid_Cache)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.prevTimeStep, self.timeStepSelector)
        MainWindow.setTabOrder(self.timeStepSelector, self.nextTimeStep)
        MainWindow.setTabOrder(self.nextTimeStep, self.plotdatasetSelector)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Zoo"))
        self.timeStepGroup.setTitle(_translate("MainWindow", "Time Step"))
        self.nextTimeStep.setText(_translate("MainWindow", ""))
        self.nextTimeStep.setShortcut(_translate("MainWindow", "Ctrl+Right"))
        self.prevTimeStep.setText(_translate("MainWindow", ""))
        self.prevTimeStep.setShortcut(_translate("MainWindow", "Ctrl+Left"))
        self.timelabelLabel.setText(_translate("MainWindow", "Time:"))
        self.contourDataGroup.setTitle(_translate("MainWindow", "Contour Data"))
        self.colorLabel.setText(_translate("MainWindow", "Color"))
        self.maskingLabel.setText(_translate("MainWindow", "Masking"))
        self.maskdatasetLockButton.setToolTip(_translate("MainWindow", "Toggle separate mask and plot datasets"))
        self.maskdatasetLockButton.setText(_translate("MainWindow", ""))
        self.gsGroup.setTitle(_translate("MainWindow", "Grid Spacing"))
        self.gsLockButton.setToolTip(_translate("MainWindow", "Toggle uniform/non-uniform grid spacing"))
        self.gsLockButton.setText(_translate("MainWindow", ""))
        self.exagGroup.setTitle(_translate("MainWindow", "Exaggeration"))
        self.exagLockButton.setToolTip(_translate("MainWindow", "Toggle uniform/non-uniform exaggeration"))
        self.exagLockButton.setText(_translate("MainWindow", ""))
        self.extentsGroup.setTitle(_translate("MainWindow", "Clipping Extents"))
        self.xLabel.setText(_translate("MainWindow", "X"))
        self.zLabel.setText(_translate("MainWindow", "Z"))
        self.yLabel.setText(_translate("MainWindow", "Y"))
        self.cameraLocationGroup.setToolTip(_translate("MainWindow", "Left Click to copy camera location\n"
"Right Click to paste"))
        self.cameraLocationGroup.setTitle(_translate("MainWindow", "Camera Location"))
        self.focalLabel.setText(_translate("MainWindow", "Focal point:"))
        self.positionLabel.setText(_translate("MainWindow", "Position:"))
        self.viewupLabel.setText(_translate("MainWindow", "View-up:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionShow_Grid.setText(_translate("MainWindow", "Show Grid"))
        self.actionClear_Grid_Cache.setText(_translate("MainWindow", "Clear Grid Cache"))
        self.actionSave_Image.setText(_translate("MainWindow", "Save Image"))
        self.actionSave_Image.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCopy_Image.setText(_translate("MainWindow", "Copy Image"))
        self.actionCopy_Image.setShortcut(_translate("MainWindow", "Ctrl+C"))

