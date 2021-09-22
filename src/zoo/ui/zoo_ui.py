# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zoo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


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
        self.timeStepSelection = QtWidgets.QHBoxLayout()
        self.timeStepSelection.setSpacing(0)
        self.timeStepSelection.setObjectName("timeStepSelection")
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
        self.timeStepSelection.addWidget(self.prevTimeStep)
        self.timeStepSelector = QtWidgets.QComboBox(self.timeStepGroup)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.timeStepSelector.setFont(font)
        self.timeStepSelector.setEditable(False)
        self.timeStepSelector.setCurrentText("")
        self.timeStepSelector.setObjectName("timeStepSelector")
        self.timeStepSelection.addWidget(self.timeStepSelector)
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
        self.timeStepSelection.addWidget(self.nextTimeStep)
        self.verticalLayout_5.addLayout(self.timeStepSelection)
        self.controls.addWidget(self.timeStepGroup)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.controls.addItem(spacerItem)
        self.contourDataGroup = QtWidgets.QGroupBox(self.controlPane)
        self.contourDataGroup.setEnabled(True)
        self.contourDataGroup.setObjectName("contourDataGroup")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.contourDataGroup)
        self.verticalLayout_4.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.datasetSelector = QtWidgets.QComboBox(self.contourDataGroup)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.datasetSelector.setFont(font)
        self.datasetSelector.setObjectName("datasetSelector")
        self.verticalLayout_4.addWidget(self.datasetSelector)
        self.colorlimitLabel = QtWidgets.QLabel(self.contourDataGroup)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.colorlimitLabel.setFont(font)
        self.colorlimitLabel.setObjectName("colorlimitLabel")
        self.verticalLayout_4.addWidget(self.colorlimitLabel)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.colorCheckBox = QtWidgets.QCheckBox(self.contourDataGroup)
        self.colorCheckBox.setText("")
        self.colorCheckBox.setObjectName("colorCheckBox")
        self.horizontalLayout_6.addWidget(self.colorCheckBox)
        self.colorminSpinBox = QtWidgets.QDoubleSpinBox(self.contourDataGroup)
        self.colorminSpinBox.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.colorminSpinBox.setFont(font)
        self.colorminSpinBox.setDecimals(3)
        self.colorminSpinBox.setMinimum(-99999999999.0)
        self.colorminSpinBox.setMaximum(99999999999.0)
        self.colorminSpinBox.setObjectName("colorminSpinBox")
        self.horizontalLayout_6.addWidget(self.colorminSpinBox)
        self.colormaxSpinBox = QtWidgets.QDoubleSpinBox(self.contourDataGroup)
        self.colormaxSpinBox.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.colormaxSpinBox.setFont(font)
        self.colormaxSpinBox.setDecimals(3)
        self.colormaxSpinBox.setMinimum(-99999999999.0)
        self.colormaxSpinBox.setMaximum(99999999999.0)
        self.colormaxSpinBox.setObjectName("colormaxSpinBox")
        self.horizontalLayout_6.addWidget(self.colormaxSpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.maskingLabel = QtWidgets.QLabel(self.contourDataGroup)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.maskingLabel.setFont(font)
        self.maskingLabel.setObjectName("maskingLabel")
        self.verticalLayout_4.addWidget(self.maskingLabel)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.maskCheckBox = QtWidgets.QCheckBox(self.contourDataGroup)
        self.maskCheckBox.setText("")
        self.maskCheckBox.setObjectName("maskCheckBox")
        self.horizontalLayout_7.addWidget(self.maskCheckBox)
        self.maskminSpinBox = QtWidgets.QDoubleSpinBox(self.contourDataGroup)
        self.maskminSpinBox.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.maskminSpinBox.setFont(font)
        self.maskminSpinBox.setDecimals(3)
        self.maskminSpinBox.setMinimum(-99999999999.0)
        self.maskminSpinBox.setMaximum(99999999999.0)
        self.maskminSpinBox.setObjectName("maskminSpinBox")
        self.horizontalLayout_7.addWidget(self.maskminSpinBox)
        self.maskmaxSpinBox = QtWidgets.QDoubleSpinBox(self.contourDataGroup)
        self.maskmaxSpinBox.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.maskmaxSpinBox.setFont(font)
        self.maskmaxSpinBox.setDecimals(3)
        self.maskmaxSpinBox.setMinimum(-99999999999.0)
        self.maskmaxSpinBox.setMaximum(99999999999.0)
        self.maskmaxSpinBox.setObjectName("maskmaxSpinBox")
        self.horizontalLayout_7.addWidget(self.maskmaxSpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.controls.addWidget(self.contourDataGroup)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.controls.addItem(spacerItem1)
        self.gsGroup = QtWidgets.QGroupBox(self.controlPane)
        self.gsGroup.setObjectName("gsGroup")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.gsGroup)
        self.horizontalLayout_10.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.xgsSpinBox = QtWidgets.QDoubleSpinBox(self.gsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xgsSpinBox.sizePolicy().hasHeightForWidth())
        self.xgsSpinBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.xgsSpinBox.setFont(font)
        self.xgsSpinBox.setSuffix("")
        self.xgsSpinBox.setDecimals(5)
        self.xgsSpinBox.setMaximum(99999999.0)
        self.xgsSpinBox.setSingleStep(0.001)
        self.xgsSpinBox.setProperty("value", 0.005)
        self.xgsSpinBox.setObjectName("xgsSpinBox")
        self.gridLayout_5.addWidget(self.xgsSpinBox, 0, 0, 1, 1)
        self.ygsSpinBox = QtWidgets.QDoubleSpinBox(self.gsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ygsSpinBox.sizePolicy().hasHeightForWidth())
        self.ygsSpinBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.ygsSpinBox.setFont(font)
        self.ygsSpinBox.setVisible(False)
        self.ygsSpinBox.setDecimals(5)
        self.ygsSpinBox.setMaximum(99999999.0)
        self.ygsSpinBox.setSingleStep(0.001)
        self.ygsSpinBox.setProperty("value", 0.005)
        self.ygsSpinBox.setObjectName("ygsSpinBox")
        self.gridLayout_5.addWidget(self.ygsSpinBox, 1, 0, 1, 1)
        self.zgsSpinBox = QtWidgets.QDoubleSpinBox(self.gsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zgsSpinBox.sizePolicy().hasHeightForWidth())
        self.zgsSpinBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.zgsSpinBox.setFont(font)
        self.zgsSpinBox.setVisible(False)
        self.zgsSpinBox.setDecimals(5)
        self.zgsSpinBox.setMaximum(99999999.0)
        self.zgsSpinBox.setSingleStep(0.001)
        self.zgsSpinBox.setProperty("value", 0.005)
        self.zgsSpinBox.setObjectName("zgsSpinBox")
        self.gridLayout_5.addWidget(self.zgsSpinBox, 2, 0, 1, 1)
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
        self.gridLayout_5.addWidget(self.gsLockButton, 0, 1, 1, 1)
        self.horizontalLayout_10.addLayout(self.gridLayout_5)
        self.controls.addWidget(self.gsGroup)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.controls.addItem(spacerItem2)
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
        font.setPointSize(9)
        self.xexagSpinBox.setFont(font)
        self.xexagSpinBox.setSuffix("")
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
        font.setPointSize(9)
        self.yexagSpinBox.setFont(font)
        self.yexagSpinBox.setVisible(False)
        self.yexagSpinBox.setDecimals(1)
        self.yexagSpinBox.setMaximum(1000.0)
        self.yexagSpinBox.setObjectName("yexagSpinBox")
        self.gridLayout_4.addWidget(self.yexagSpinBox, 1, 0, 1, 1)
        self.zexagSpinBox = QtWidgets.QDoubleSpinBox(self.exagGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zexagSpinBox.sizePolicy().hasHeightForWidth())
        self.zexagSpinBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.zexagSpinBox.setFont(font)
        self.zexagSpinBox.setVisible(False)
        self.zexagSpinBox.setDecimals(1)
        self.zexagSpinBox.setMaximum(1000.0)
        self.zexagSpinBox.setObjectName("zexagSpinBox")
        self.gridLayout_4.addWidget(self.zexagSpinBox, 2, 0, 1, 1)
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
        self.gridLayout_4.addWidget(self.exagLockButton, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.controls.addWidget(self.exagGroup)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.controls.addItem(spacerItem3)
        self.extentsGroup = QtWidgets.QGroupBox(self.controlPane)
        self.extentsGroup.setObjectName("extentsGroup")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.extentsGroup)
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.zminSpinBox = QtWidgets.QDoubleSpinBox(self.extentsGroup)
        self.zminSpinBox.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.zminSpinBox.setFont(font)
        self.zminSpinBox.setDecimals(3)
        self.zminSpinBox.setMinimum(-99999999999.0)
        self.zminSpinBox.setMaximum(99999999999.0)
        self.zminSpinBox.setObjectName("zminSpinBox")
        self.gridLayout_2.addWidget(self.zminSpinBox, 3, 2, 1, 1)
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
        self.ymaxSpinBox = QtWidgets.QDoubleSpinBox(self.extentsGroup)
        self.ymaxSpinBox.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.ymaxSpinBox.setFont(font)
        self.ymaxSpinBox.setDecimals(3)
        self.ymaxSpinBox.setMinimum(-99999999999.0)
        self.ymaxSpinBox.setMaximum(99999999999.0)
        self.ymaxSpinBox.setObjectName("ymaxSpinBox")
        self.gridLayout_2.addWidget(self.ymaxSpinBox, 2, 3, 1, 1)
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
        self.zmaxSpinBox = QtWidgets.QDoubleSpinBox(self.extentsGroup)
        self.zmaxSpinBox.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.zmaxSpinBox.setFont(font)
        self.zmaxSpinBox.setDecimals(3)
        self.zmaxSpinBox.setMinimum(-99999999999.0)
        self.zmaxSpinBox.setMaximum(99999999999.0)
        self.zmaxSpinBox.setObjectName("zmaxSpinBox")
        self.gridLayout_2.addWidget(self.zmaxSpinBox, 3, 3, 1, 1)
        self.xmaxSpinBox = QtWidgets.QDoubleSpinBox(self.extentsGroup)
        self.xmaxSpinBox.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.xmaxSpinBox.setFont(font)
        self.xmaxSpinBox.setDecimals(3)
        self.xmaxSpinBox.setMinimum(-99999999999.0)
        self.xmaxSpinBox.setMaximum(99999999999.0)
        self.xmaxSpinBox.setObjectName("xmaxSpinBox")
        self.gridLayout_2.addWidget(self.xmaxSpinBox, 0, 3, 1, 1)
        self.yminSpinBox = QtWidgets.QDoubleSpinBox(self.extentsGroup)
        self.yminSpinBox.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.yminSpinBox.setFont(font)
        self.yminSpinBox.setDecimals(3)
        self.yminSpinBox.setMinimum(-99999999999.0)
        self.yminSpinBox.setMaximum(99999999999.0)
        self.yminSpinBox.setObjectName("yminSpinBox")
        self.gridLayout_2.addWidget(self.yminSpinBox, 2, 2, 1, 1)
        self.xminSpinBox = QtWidgets.QDoubleSpinBox(self.extentsGroup)
        self.xminSpinBox.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.xminSpinBox.setFont(font)
        self.xminSpinBox.setDecimals(3)
        self.xminSpinBox.setMinimum(-99999999999.0)
        self.xminSpinBox.setMaximum(99999999999.0)
        self.xminSpinBox.setObjectName("xminSpinBox")
        self.gridLayout_2.addWidget(self.xminSpinBox, 0, 2, 1, 1)
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
        self.zclipCheckBox = QtWidgets.QCheckBox(self.extentsGroup)
        self.zclipCheckBox.setText("")
        self.zclipCheckBox.setObjectName("zclipCheckBox")
        self.gridLayout_2.addWidget(self.zclipCheckBox, 3, 1, 1, 1)
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
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.controls.addItem(spacerItem4)
        self.cameraGroup = QtWidgets.QGroupBox(self.controlPane)
        self.cameraGroup.setObjectName("cameraGroup")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.cameraGroup)
        self.gridLayout_3.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pitchSlider = QtWidgets.QSlider(self.cameraGroup)
        self.pitchSlider.setMinimum(-899)
        self.pitchSlider.setMaximum(899)
        self.pitchSlider.setSingleStep(10)
        self.pitchSlider.setPageStep(100)
        self.pitchSlider.setOrientation(QtCore.Qt.Horizontal)
        self.pitchSlider.setInvertedAppearance(False)
        self.pitchSlider.setInvertedControls(False)
        self.pitchSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.pitchSlider.setTickInterval(30)
        self.pitchSlider.setObjectName("pitchSlider")
        self.gridLayout_3.addWidget(self.pitchSlider, 0, 1, 1, 1)
        self.yawSlider = QtWidgets.QSlider(self.cameraGroup)
        self.yawSlider.setMinimum(-180)
        self.yawSlider.setMaximum(180)
        self.yawSlider.setSingleStep(1)
        self.yawSlider.setPageStep(10)
        self.yawSlider.setOrientation(QtCore.Qt.Horizontal)
        self.yawSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.yawSlider.setTickInterval(90)
        self.yawSlider.setObjectName("yawSlider")
        self.gridLayout_3.addWidget(self.yawSlider, 1, 1, 1, 1)
        self.rollSlider = QtWidgets.QSlider(self.cameraGroup)
        self.rollSlider.setMinimum(-180)
        self.rollSlider.setMaximum(180)
        self.rollSlider.setSingleStep(1)
        self.rollSlider.setPageStep(10)
        self.rollSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rollSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.rollSlider.setTickInterval(90)
        self.rollSlider.setObjectName("rollSlider")
        self.gridLayout_3.addWidget(self.rollSlider, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.cameraGroup)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.cameraGroup)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.cameraGroup)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.pitchSpinBox = QtWidgets.QSpinBox(self.cameraGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pitchSpinBox.sizePolicy().hasHeightForWidth())
        self.pitchSpinBox.setSizePolicy(sizePolicy)
        self.pitchSpinBox.setMaximumSize(QtCore.QSize(38, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.pitchSpinBox.setFont(font)
        self.pitchSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pitchSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.pitchSpinBox.setMinimum(-90)
        self.pitchSpinBox.setMaximum(90)
        self.pitchSpinBox.setObjectName("pitchSpinBox")
        self.gridLayout_3.addWidget(self.pitchSpinBox, 0, 2, 1, 1)
        self.yawSpinBox = QtWidgets.QSpinBox(self.cameraGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yawSpinBox.sizePolicy().hasHeightForWidth())
        self.yawSpinBox.setSizePolicy(sizePolicy)
        self.yawSpinBox.setMaximumSize(QtCore.QSize(38, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.yawSpinBox.setFont(font)
        self.yawSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yawSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.yawSpinBox.setMinimum(-180)
        self.yawSpinBox.setMaximum(180)
        self.yawSpinBox.setObjectName("yawSpinBox")
        self.gridLayout_3.addWidget(self.yawSpinBox, 1, 2, 1, 1)
        self.rollSpinBox = QtWidgets.QSpinBox(self.cameraGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rollSpinBox.sizePolicy().hasHeightForWidth())
        self.rollSpinBox.setSizePolicy(sizePolicy)
        self.rollSpinBox.setMaximumSize(QtCore.QSize(38, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.rollSpinBox.setFont(font)
        self.rollSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rollSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.rollSpinBox.setMinimum(-180)
        self.rollSpinBox.setMaximum(180)
        self.rollSpinBox.setObjectName("rollSpinBox")
        self.gridLayout_3.addWidget(self.rollSpinBox, 2, 2, 1, 1)
        self.controls.addWidget(self.cameraGroup)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.controls.addItem(spacerItem5)
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
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionShow_Grid)
        self.menuView.addAction(self.actionClear_Grid_Cache)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.colorlimitLabel.setBuddy(self.colorminSpinBox)
        self.maskingLabel.setBuddy(self.maskminSpinBox)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.prevTimeStep, self.timeStepSelector)
        MainWindow.setTabOrder(self.timeStepSelector, self.nextTimeStep)
        MainWindow.setTabOrder(self.nextTimeStep, self.datasetSelector)
        MainWindow.setTabOrder(self.datasetSelector, self.colorminSpinBox)
        MainWindow.setTabOrder(self.colorminSpinBox, self.colormaxSpinBox)
        MainWindow.setTabOrder(self.colormaxSpinBox, self.maskminSpinBox)
        MainWindow.setTabOrder(self.maskminSpinBox, self.maskmaxSpinBox)
        MainWindow.setTabOrder(self.maskmaxSpinBox, self.xminSpinBox)
        MainWindow.setTabOrder(self.xminSpinBox, self.xmaxSpinBox)
        MainWindow.setTabOrder(self.xmaxSpinBox, self.yminSpinBox)
        MainWindow.setTabOrder(self.yminSpinBox, self.ymaxSpinBox)
        MainWindow.setTabOrder(self.ymaxSpinBox, self.zminSpinBox)
        MainWindow.setTabOrder(self.zminSpinBox, self.zmaxSpinBox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.timeStepGroup.setTitle(_translate("MainWindow", "Time Step"))
        self.prevTimeStep.setText(_translate("MainWindow", ""))
        self.prevTimeStep.setShortcut(_translate("MainWindow", "Ctrl+Left"))
        self.nextTimeStep.setText(_translate("MainWindow", ""))
        self.nextTimeStep.setShortcut(_translate("MainWindow", "Ctrl+Right"))
        self.contourDataGroup.setTitle(_translate("MainWindow", "Contour Data"))
        self.colorlimitLabel.setText(_translate("MainWindow", "Color Limits"))
        self.maskingLabel.setText(_translate("MainWindow", "Masking Thresholds"))
        self.gsGroup.setTitle(_translate("MainWindow", "Grid Spacing"))
        self.gsLockButton.setText(_translate("MainWindow", ""))
        self.exagGroup.setTitle(_translate("MainWindow", "Exaggeration"))
        self.exagLockButton.setText(_translate("MainWindow", ""))
        self.extentsGroup.setTitle(_translate("MainWindow", "Clipping Extents"))
        self.zLabel.setText(_translate("MainWindow", "Z"))
        self.xLabel.setText(_translate("MainWindow", "X"))
        self.yLabel.setText(_translate("MainWindow", "Y"))
        self.cameraGroup.setTitle(_translate("MainWindow", "Camera"))
        self.label_2.setText(_translate("MainWindow", "↔"))
        self.label.setText(_translate("MainWindow", "↕"))
        self.label_3.setText(_translate("MainWindow", "🔄"))
        self.pitchSpinBox.setSuffix(_translate("MainWindow", "°"))
        self.yawSpinBox.setSuffix(_translate("MainWindow", "°"))
        self.rollSpinBox.setSuffix(_translate("MainWindow", "°"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionShow_Grid.setText(_translate("MainWindow", "Show Grid"))
        self.actionClear_Grid_Cache.setText(_translate("MainWindow", "Clear Grid Cache"))
