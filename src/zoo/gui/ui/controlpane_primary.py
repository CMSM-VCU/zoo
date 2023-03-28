from PySide6.QtCore import QMetaObject, QSize, Qt
from PySide6.QtGui import QCursor, QFont
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)

from zoo.gui.ui.foldinggroupbox import FoldingGroupBox


class Ui_ControlPane_Primary(object):
    def setupUi(self, ControlPane_Primary):
        if not ControlPane_Primary.objectName():
            ControlPane_Primary.setObjectName("ControlPane_Primary")
        ControlPane_Primary.resize(200, 630)
        self.gridLayout = QGridLayout(ControlPane_Primary)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.controls = QVBoxLayout()
        self.controls.setObjectName("controls")
        self.timeStepGroup = FoldingGroupBox(ControlPane_Primary)
        self.timeStepGroup.setObjectName("timeStepGroup")
        self.timeStepGroup.setAlignment(Qt.AlignCenter)
        self.verticalLayout_5 = QVBoxLayout(self.timeStepGroup)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.timestepdummyWidget = QWidget(self.timeStepGroup)
        self.timestepdummyWidget.setObjectName("timestepdummyWidget")
        self.gridLayout_6 = QGridLayout(self.timestepdummyWidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(2)
        self.gridLayout_6.setContentsMargins(3, 1, 3, 4)
        self.nextTimeStep = QPushButton(self.timestepdummyWidget)
        self.nextTimeStep.setObjectName("nextTimeStep")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextTimeStep.sizePolicy().hasHeightForWidth())
        self.nextTimeStep.setSizePolicy(sizePolicy)
        self.nextTimeStep.setMaximumSize(QSize(24, 16777215))
        self.nextTimeStep.setBaseSize(QSize(16, 16))
        font = QFont()
        font.setFamilies(["Segoe Fluent Icons"])
        font.setPointSize(10)
        font.setBold(True)
        font.setStrikeOut(False)
        self.nextTimeStep.setFont(font)
        self.nextTimeStep.setCheckable(False)
        self.nextTimeStep.setAutoRepeat(False)
        self.nextTimeStep.setFlat(False)

        self.gridLayout_6.addWidget(self.nextTimeStep, 0, 2, 1, 1)

        self.prevTimeStep = QPushButton(self.timestepdummyWidget)
        self.prevTimeStep.setObjectName("prevTimeStep")
        sizePolicy.setHeightForWidth(self.prevTimeStep.sizePolicy().hasHeightForWidth())
        self.prevTimeStep.setSizePolicy(sizePolicy)
        self.prevTimeStep.setMaximumSize(QSize(24, 16777215))
        self.prevTimeStep.setBaseSize(QSize(16, 16))
        self.prevTimeStep.setFont(font)

        self.gridLayout_6.addWidget(self.prevTimeStep, 0, 0, 1, 1)

        self.timeStepSelector = QComboBox(self.timestepdummyWidget)
        self.timeStepSelector.setObjectName("timeStepSelector")
        font1 = QFont()
        font1.setFamilies(["Consolas"])
        font1.setPointSize(11)
        self.timeStepSelector.setFont(font1)
        self.timeStepSelector.setEditable(False)

        self.gridLayout_6.addWidget(self.timeStepSelector, 0, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.timelabelLabel = QLabel(self.timestepdummyWidget)
        self.timelabelLabel.setObjectName("timelabelLabel")
        font2 = QFont()
        font2.setPointSize(8)
        self.timelabelLabel.setFont(font2)

        self.horizontalLayout_4.addWidget(self.timelabelLabel)

        self.timeLabel = QLabel(self.timestepdummyWidget)
        self.timeLabel.setObjectName("timeLabel")
        self.timeLabel.setFont(font2)
        self.timeLabel.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.timeLabel)

        self.gridLayout_6.addLayout(self.horizontalLayout_4, 5, 1, 1, 1)

        self.verticalLayout_5.addWidget(self.timestepdummyWidget)

        self.controls.addWidget(self.timeStepGroup)

        self.verticalSpacer_3 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum
        )

        self.controls.addItem(self.verticalSpacer_3)

        self.contourDataGroup = FoldingGroupBox(ControlPane_Primary)
        self.contourDataGroup.setObjectName("contourDataGroup")
        self.contourDataGroup.setEnabled(True)
        self.contourDataGroup.setAlignment(Qt.AlignCenter)
        self.verticalLayout_4 = QVBoxLayout(self.contourDataGroup)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget = QWidget(self.contourDataGroup)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_6 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.colorLabel = QLabel(self.verticalWidget)
        self.colorLabel.setObjectName("colorLabel")
        self.colorLabel.setFont(font2)

        self.verticalLayout_6.addWidget(self.colorLabel)

        self.contourdummyWidget2_2 = QWidget(self.verticalWidget)
        self.contourdummyWidget2_2.setObjectName("contourdummyWidget2_2")
        self.horizontalLayout_3 = QHBoxLayout(self.contourdummyWidget2_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.plotdatasetSelector = QComboBox(self.contourdummyWidget2_2)
        self.plotdatasetSelector.setObjectName("plotdatasetSelector")
        font3 = QFont()
        font3.setPointSize(10)
        self.plotdatasetSelector.setFont(font3)

        self.horizontalLayout_3.addWidget(self.plotdatasetSelector)

        self.verticalLayout_6.addWidget(self.contourdummyWidget2_2)

        self.contourdummyWidget1 = QWidget(self.verticalWidget)
        self.contourdummyWidget1.setObjectName("contourdummyWidget1")
        self.horizontalLayout_6 = QHBoxLayout(self.contourdummyWidget1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.colorCheckBox = QCheckBox(self.contourdummyWidget1)
        self.colorCheckBox.setObjectName("colorCheckBox")

        self.horizontalLayout_6.addWidget(self.colorCheckBox)

        self.colorminLineEdit = QLineEdit(self.contourdummyWidget1)
        self.colorminLineEdit.setObjectName("colorminLineEdit")
        self.colorminLineEdit.setEnabled(False)
        font4 = QFont()
        font4.setFamilies(["Consolas"])
        font4.setPointSize(8)
        self.colorminLineEdit.setFont(font4)

        self.horizontalLayout_6.addWidget(self.colorminLineEdit)

        self.colormaxLineEdit = QLineEdit(self.contourdummyWidget1)
        self.colormaxLineEdit.setObjectName("colormaxLineEdit")
        self.colormaxLineEdit.setEnabled(False)
        self.colormaxLineEdit.setFont(font4)

        self.horizontalLayout_6.addWidget(self.colormaxLineEdit)

        self.verticalLayout_6.addWidget(self.contourdummyWidget1)

        self.maskingLabel = QLabel(self.verticalWidget)
        self.maskingLabel.setObjectName("maskingLabel")
        self.maskingLabel.setFont(font2)

        self.verticalLayout_6.addWidget(self.maskingLabel)

        self.contourdummyWidget2 = QWidget(self.verticalWidget)
        self.contourdummyWidget2.setObjectName("contourdummyWidget2")
        self.horizontalLayout_2 = QHBoxLayout(self.contourdummyWidget2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.maskdatasetSelector = QComboBox(self.contourdummyWidget2)
        self.maskdatasetSelector.setObjectName("maskdatasetSelector")
        self.maskdatasetSelector.setEnabled(False)
        self.maskdatasetSelector.setFont(font3)

        self.horizontalLayout_2.addWidget(self.maskdatasetSelector)

        self.maskdatasetLockButton = QPushButton(self.contourdummyWidget2)
        self.maskdatasetLockButton.setObjectName("maskdatasetLockButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.maskdatasetLockButton.sizePolicy().hasHeightForWidth()
        )
        self.maskdatasetLockButton.setSizePolicy(sizePolicy1)
        self.maskdatasetLockButton.setMaximumSize(QSize(24, 16777215))
        font5 = QFont()
        font5.setFamilies(["Segoe Fluent Icons"])
        font5.setPointSize(11)
        self.maskdatasetLockButton.setFont(font5)
        self.maskdatasetLockButton.setCheckable(True)
        self.maskdatasetLockButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.maskdatasetLockButton)

        self.verticalLayout_6.addWidget(self.contourdummyWidget2)

        self.contourdummyWidget3 = QWidget(self.verticalWidget)
        self.contourdummyWidget3.setObjectName("contourdummyWidget3")
        self.horizontalLayout_7 = QHBoxLayout(self.contourdummyWidget3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.maskCheckBox = QCheckBox(self.contourdummyWidget3)
        self.maskCheckBox.setObjectName("maskCheckBox")

        self.horizontalLayout_7.addWidget(self.maskCheckBox)

        self.maskminLineEdit = QLineEdit(self.contourdummyWidget3)
        self.maskminLineEdit.setObjectName("maskminLineEdit")
        self.maskminLineEdit.setEnabled(False)
        self.maskminLineEdit.setFont(font4)

        self.horizontalLayout_7.addWidget(self.maskminLineEdit)

        self.maskmaxLineEdit = QLineEdit(self.contourdummyWidget3)
        self.maskmaxLineEdit.setObjectName("maskmaxLineEdit")
        self.maskmaxLineEdit.setEnabled(False)
        self.maskmaxLineEdit.setFont(font4)

        self.horizontalLayout_7.addWidget(self.maskmaxLineEdit)

        self.verticalLayout_6.addWidget(self.contourdummyWidget3)

        self.verticalLayout_4.addWidget(self.verticalWidget)

        self.controls.addWidget(self.contourDataGroup)

        self.verticalSpacer_4 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum
        )

        self.controls.addItem(self.verticalSpacer_4)

        self.gsGroup = FoldingGroupBox(ControlPane_Primary)
        self.gsGroup.setObjectName("gsGroup")
        self.gsGroup.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_10 = QHBoxLayout(self.gsGroup)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gsdummyWidget = QWidget(self.gsGroup)
        self.gsdummyWidget.setObjectName("gsdummyWidget")
        self.gridLayout_5 = QGridLayout(self.gsdummyWidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_5.setContentsMargins(4, 4, 4, 4)
        self.xgsLineEdit = QLineEdit(self.gsdummyWidget)
        self.xgsLineEdit.setObjectName("xgsLineEdit")
        font6 = QFont()
        font6.setFamilies(["Consolas"])
        font6.setPointSize(9)
        self.xgsLineEdit.setFont(font6)

        self.gridLayout_5.addWidget(self.xgsLineEdit, 1, 1, 1, 1)

        self.ygsLineEdit = QLineEdit(self.gsdummyWidget)
        self.ygsLineEdit.setObjectName("ygsLineEdit")
        self.ygsLineEdit.setFont(font6)

        self.gridLayout_5.addWidget(self.ygsLineEdit, 2, 1, 1, 1)

        self.zgsLineEdit = QLineEdit(self.gsdummyWidget)
        self.zgsLineEdit.setObjectName("zgsLineEdit")
        self.zgsLineEdit.setFont(font6)

        self.gridLayout_5.addWidget(self.zgsLineEdit, 3, 1, 1, 1)

        self.gsLockButton = QPushButton(self.gsdummyWidget)
        self.gsLockButton.setObjectName("gsLockButton")
        sizePolicy1.setHeightForWidth(
            self.gsLockButton.sizePolicy().hasHeightForWidth()
        )
        self.gsLockButton.setSizePolicy(sizePolicy1)
        self.gsLockButton.setMaximumSize(QSize(24, 16777215))
        self.gsLockButton.setFont(font5)
        self.gsLockButton.setCheckable(True)
        self.gsLockButton.setChecked(True)

        self.gridLayout_5.addWidget(self.gsLockButton, 1, 2, 1, 1)

        self.horizontalLayout_10.addWidget(self.gsdummyWidget)

        self.controls.addWidget(self.gsGroup)

        self.verticalSpacer_5 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum
        )

        self.controls.addItem(self.verticalSpacer_5)

        self.exagGroup = FoldingGroupBox(ControlPane_Primary)
        self.exagGroup.setObjectName("exagGroup")
        self.exagGroup.setEnabled(True)
        self.exagGroup.setAlignment(Qt.AlignCenter)
        self.exagGroup.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.exagGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.exagdummyWidget = QWidget(self.exagGroup)
        self.exagdummyWidget.setObjectName("exagdummyWidget")
        self.gridLayout_4 = QGridLayout(self.exagdummyWidget)
        self.gridLayout_4.setSpacing(4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(4, 4, 4, 4)
        self.xexagSpinBox = QDoubleSpinBox(self.exagdummyWidget)
        self.xexagSpinBox.setObjectName("xexagSpinBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.xexagSpinBox.sizePolicy().hasHeightForWidth()
        )
        self.xexagSpinBox.setSizePolicy(sizePolicy2)
        self.xexagSpinBox.setMinimumSize(QSize(45, 0))
        self.xexagSpinBox.setFont(font4)
        self.xexagSpinBox.setDecimals(1)
        self.xexagSpinBox.setMaximum(1000.000000000000000)

        self.gridLayout_4.addWidget(self.xexagSpinBox, 0, 0, 1, 1)

        self.yexagSpinBox = QDoubleSpinBox(self.exagdummyWidget)
        self.yexagSpinBox.setObjectName("yexagSpinBox")
        sizePolicy2.setHeightForWidth(
            self.yexagSpinBox.sizePolicy().hasHeightForWidth()
        )
        self.yexagSpinBox.setSizePolicy(sizePolicy2)
        self.yexagSpinBox.setMinimumSize(QSize(45, 0))
        self.yexagSpinBox.setFont(font4)
        self.yexagSpinBox.setKeyboardTracking(False)
        self.yexagSpinBox.setDecimals(1)
        self.yexagSpinBox.setMaximum(1000.000000000000000)

        self.gridLayout_4.addWidget(self.yexagSpinBox, 0, 1, 1, 1)

        self.zexagSpinBox = QDoubleSpinBox(self.exagdummyWidget)
        self.zexagSpinBox.setObjectName("zexagSpinBox")
        sizePolicy2.setHeightForWidth(
            self.zexagSpinBox.sizePolicy().hasHeightForWidth()
        )
        self.zexagSpinBox.setSizePolicy(sizePolicy2)
        self.zexagSpinBox.setMinimumSize(QSize(45, 0))
        self.zexagSpinBox.setFont(font4)
        self.zexagSpinBox.setDecimals(1)
        self.zexagSpinBox.setMaximum(1000.000000000000000)

        self.gridLayout_4.addWidget(self.zexagSpinBox, 0, 2, 1, 1)

        self.exagLockButton = QPushButton(self.exagdummyWidget)
        self.exagLockButton.setObjectName("exagLockButton")
        sizePolicy1.setHeightForWidth(
            self.exagLockButton.sizePolicy().hasHeightForWidth()
        )
        self.exagLockButton.setSizePolicy(sizePolicy1)
        self.exagLockButton.setMaximumSize(QSize(24, 16777215))
        self.exagLockButton.setFont(font5)
        self.exagLockButton.setCheckable(True)
        self.exagLockButton.setChecked(True)

        self.gridLayout_4.addWidget(self.exagLockButton, 0, 3, 1, 1)

        self.verticalLayout.addWidget(self.exagdummyWidget)

        self.controls.addWidget(self.exagGroup)

        self.verticalSpacer_2 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum
        )

        self.controls.addItem(self.verticalSpacer_2)

        self.extentsGroup = FoldingGroupBox(ControlPane_Primary)
        self.extentsGroup.setObjectName("extentsGroup")
        self.extentsGroup.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2 = QVBoxLayout(self.extentsGroup)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.clippingboxButton = QPushButton(self.extentsGroup)
        self.clippingboxButton.setObjectName("clippingboxButton")
        self.clippingboxButton.setCheckable(True)

        self.verticalLayout_2.addWidget(self.clippingboxButton)

        self.extentsdummyWidget = QWidget(self.extentsGroup)
        self.extentsdummyWidget.setObjectName("extentsdummyWidget")
        self.gridLayout_2 = QGridLayout(self.extentsdummyWidget)
        self.gridLayout_2.setSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(4, 1, 4, 4)
        self.xminLineEdit = QLineEdit(self.extentsdummyWidget)
        self.xminLineEdit.setObjectName("xminLineEdit")
        self.xminLineEdit.setEnabled(False)
        self.xminLineEdit.setFont(font4)

        self.gridLayout_2.addWidget(self.xminLineEdit, 0, 2, 1, 1)

        self.yminLineEdit = QLineEdit(self.extentsdummyWidget)
        self.yminLineEdit.setObjectName("yminLineEdit")
        self.yminLineEdit.setEnabled(False)
        self.yminLineEdit.setFont(font4)

        self.gridLayout_2.addWidget(self.yminLineEdit, 2, 2, 1, 1)

        self.zminLineEdit = QLineEdit(self.extentsdummyWidget)
        self.zminLineEdit.setObjectName("zminLineEdit")
        self.zminLineEdit.setEnabled(False)
        self.zminLineEdit.setFont(font4)

        self.gridLayout_2.addWidget(self.zminLineEdit, 3, 2, 1, 1)

        self.xmaxLineEdit = QLineEdit(self.extentsdummyWidget)
        self.xmaxLineEdit.setObjectName("xmaxLineEdit")
        self.xmaxLineEdit.setEnabled(False)
        self.xmaxLineEdit.setFont(font4)

        self.gridLayout_2.addWidget(self.xmaxLineEdit, 0, 3, 1, 1)

        self.ymaxLineEdit = QLineEdit(self.extentsdummyWidget)
        self.ymaxLineEdit.setObjectName("ymaxLineEdit")
        self.ymaxLineEdit.setEnabled(False)
        self.ymaxLineEdit.setFont(font4)

        self.gridLayout_2.addWidget(self.ymaxLineEdit, 2, 3, 1, 1)

        self.zmaxLineEdit = QLineEdit(self.extentsdummyWidget)
        self.zmaxLineEdit.setObjectName("zmaxLineEdit")
        self.zmaxLineEdit.setEnabled(False)
        self.zmaxLineEdit.setFont(font4)

        self.gridLayout_2.addWidget(self.zmaxLineEdit, 3, 3, 1, 1)

        self.xLabel = QLabel(self.extentsdummyWidget)
        self.xLabel.setObjectName("xLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.xLabel.sizePolicy().hasHeightForWidth())
        self.xLabel.setSizePolicy(sizePolicy3)
        self.xLabel.setFont(font2)
        self.xLabel.setScaledContents(False)

        self.gridLayout_2.addWidget(self.xLabel, 0, 0, 1, 1)

        self.zLabel = QLabel(self.extentsdummyWidget)
        self.zLabel.setObjectName("zLabel")
        sizePolicy3.setHeightForWidth(self.zLabel.sizePolicy().hasHeightForWidth())
        self.zLabel.setSizePolicy(sizePolicy3)
        self.zLabel.setFont(font2)
        self.zLabel.setScaledContents(False)

        self.gridLayout_2.addWidget(self.zLabel, 3, 0, 1, 1)

        self.zclipCheckBox = QCheckBox(self.extentsdummyWidget)
        self.zclipCheckBox.setObjectName("zclipCheckBox")

        self.gridLayout_2.addWidget(self.zclipCheckBox, 3, 1, 1, 1)

        self.yLabel = QLabel(self.extentsdummyWidget)
        self.yLabel.setObjectName("yLabel")
        sizePolicy3.setHeightForWidth(self.yLabel.sizePolicy().hasHeightForWidth())
        self.yLabel.setSizePolicy(sizePolicy3)
        self.yLabel.setFont(font2)
        self.yLabel.setScaledContents(False)

        self.gridLayout_2.addWidget(self.yLabel, 2, 0, 1, 1)

        self.yclipCheckBox = QCheckBox(self.extentsdummyWidget)
        self.yclipCheckBox.setObjectName("yclipCheckBox")

        self.gridLayout_2.addWidget(self.yclipCheckBox, 2, 1, 1, 1)

        self.xclipCheckBox = QCheckBox(self.extentsdummyWidget)
        self.xclipCheckBox.setObjectName("xclipCheckBox")

        self.gridLayout_2.addWidget(self.xclipCheckBox, 0, 1, 1, 1)

        self.verticalLayout_2.addWidget(self.extentsdummyWidget)

        self.controls.addWidget(self.extentsGroup)

        self.verticalSpacer = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.controls.addItem(self.verticalSpacer)

        self.cameraLocationGroup = FoldingGroupBox(ControlPane_Primary)
        self.cameraLocationGroup.setObjectName("cameraLocationGroup")
        self.cameraLocationGroup.setAlignment(Qt.AlignCenter)
        self.verticalLayout_3 = QVBoxLayout(self.cameraLocationGroup)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cameralocationdummyWidget = QWidget(self.cameraLocationGroup)
        self.cameralocationdummyWidget.setObjectName("cameralocationdummyWidget")
        self.cameralocationdummyWidget.setCursor(QCursor(Qt.WhatsThisCursor))
        self.verticalLayout_7 = QVBoxLayout(self.cameralocationdummyWidget)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(4, 1, 4, 4)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setSpacing(2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, -1, -1, 0)
        self.viewupLabel = QLabel(self.cameralocationdummyWidget)
        self.viewupLabel.setObjectName("viewupLabel")
        self.viewupLabel.setMaximumSize(QSize(65, 16777215))
        font7 = QFont()
        font7.setPointSize(9)
        self.viewupLabel.setFont(font7)
        self.viewupLabel.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.gridLayout_7.addWidget(self.viewupLabel, 0, 0, 1, 1)

        self.positionLabel = QLabel(self.cameralocationdummyWidget)
        self.positionLabel.setObjectName("positionLabel")
        self.positionLabel.setMaximumSize(QSize(65, 16777215))
        self.positionLabel.setFont(font7)
        self.positionLabel.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.gridLayout_7.addWidget(self.positionLabel, 1, 0, 1, 1)

        self.focalLabel = QLabel(self.cameralocationdummyWidget)
        self.focalLabel.setObjectName("focalLabel")
        self.focalLabel.setMaximumSize(QSize(65, 16777215))
        self.focalLabel.setFont(font7)
        self.focalLabel.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.focalLabel, 2, 0, 1, 1)

        self.focalValue = QLabel(self.cameralocationdummyWidget)
        self.focalValue.setObjectName("focalValue")
        self.focalValue.setFont(font4)

        self.gridLayout_7.addWidget(self.focalValue, 2, 1, 1, 1)

        self.positionValue = QLabel(self.cameralocationdummyWidget)
        self.positionValue.setObjectName("positionValue")
        self.positionValue.setFont(font4)

        self.gridLayout_7.addWidget(self.positionValue, 1, 1, 1, 1)

        self.viewupValue = QLabel(self.cameralocationdummyWidget)
        self.viewupValue.setObjectName("viewupValue")
        self.viewupValue.setFont(font4)

        self.gridLayout_7.addWidget(self.viewupValue, 0, 1, 1, 1)

        self.verticalLayout_7.addLayout(self.gridLayout_7)

        self.verticalLayout_3.addWidget(self.cameralocationdummyWidget)

        self.controls.addWidget(self.cameraLocationGroup)

        self.gridLayout.addLayout(self.controls, 0, 0, 1, 1)

        self.retranslateUi(ControlPane_Primary)

        QMetaObject.connectSlotsByName(ControlPane_Primary)
