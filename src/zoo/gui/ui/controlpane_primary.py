from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QCursor
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

from .foldinggroupbox import FoldingGroupBox
from .style import Fonts, default_spacer


class Ui_ControlPane_Primary(object):
    def setupUi(self, ControlPane_Primary):
        ControlPane_Primary.resize(200, 630)

        self.create_timestep_group(ControlPane_Primary)
        self.create_contour_data_group(ControlPane_Primary)
        self.create_grid_spacing_group(ControlPane_Primary)
        self.create_exaggeration_group(ControlPane_Primary)
        self.create_clipping_extents_group(ControlPane_Primary)
        self.create_camera_location_group(ControlPane_Primary)

        self.controls = QVBoxLayout()
        self.controls.addWidget(self.timeStepGroup)
        self.controls.addItem(default_spacer())
        self.controls.addWidget(self.contourDataGroup)
        self.controls.addItem(default_spacer())
        self.controls.addWidget(self.gsGroup)
        self.controls.addItem(default_spacer())
        self.controls.addWidget(self.exagGroup)
        self.controls.addItem(default_spacer())
        self.controls.addWidget(self.extentsGroup)
        self.controls.addItem(
            QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )
        self.controls.addWidget(self.cameraLocationGroup)

        self.gridLayout = QGridLayout(ControlPane_Primary)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.addLayout(self.controls, 0, 0, 1, 1)

        self.retranslateUi(ControlPane_Primary)

        QMetaObject.connectSlotsByName(ControlPane_Primary)

    def create_timestep_group(self, ControlPane_Primary):
        self.timeStepGroup = FoldingGroupBox(ControlPane_Primary)
        self.timeStepGroup.setAlignment(Qt.AlignCenter)
        self.timestepdummyWidget = QWidget(self.timeStepGroup)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.nextTimeStep = QPushButton(self.timestepdummyWidget)
        sizePolicy.setHeightForWidth(self.nextTimeStep.sizePolicy().hasHeightForWidth())
        self.nextTimeStep.setSizePolicy(sizePolicy)
        self.nextTimeStep.setMaximumSize(QSize(24, 16777215))
        self.nextTimeStep.setBaseSize(QSize(16, 16))
        self.nextTimeStep.setFont(Fonts.icon_small)

        self.prevTimeStep = QPushButton(self.timestepdummyWidget)
        sizePolicy.setHeightForWidth(self.prevTimeStep.sizePolicy().hasHeightForWidth())
        self.prevTimeStep.setSizePolicy(sizePolicy)
        self.prevTimeStep.setMaximumSize(QSize(24, 16777215))
        self.prevTimeStep.setBaseSize(QSize(16, 16))
        self.prevTimeStep.setFont(Fonts.icon_small)

        self.timeStepSelector = QComboBox(self.timestepdummyWidget)
        self.timeStepSelector.setFont(Fonts.numeric_normal)

        self.timelabelLabel = QLabel(self.timestepdummyWidget)
        self.timelabelLabel.setFont(Fonts.label_small)

        self.timeLabel = QLabel(self.timestepdummyWidget)
        self.timeLabel.setFont(Fonts.label_small)
        self.timeLabel.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.addWidget(self.timelabelLabel)
        self.horizontalLayout_4.addWidget(self.timeLabel)

        self.gridLayout_6 = QGridLayout(self.timestepdummyWidget)
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(2)
        self.gridLayout_6.setContentsMargins(3, 1, 3, 4)
        self.gridLayout_6.addWidget(self.nextTimeStep, 0, 2, 1, 1)
        self.gridLayout_6.addWidget(self.prevTimeStep, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.timeStepSelector, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.horizontalLayout_4, 5, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout(self.timeStepGroup)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.addWidget(self.timestepdummyWidget)

    def create_contour_data_group(self, ControlPane_Primary):
        self.contourDataGroup = FoldingGroupBox(ControlPane_Primary)
        self.contourDataGroup.setAlignment(Qt.AlignCenter)
        self.verticalWidget = QWidget(self.contourDataGroup)
        # color label
        self.colorLabel = QLabel(self.verticalWidget)
        self.colorLabel.setFont(Fonts.label_small)
        # color selector
        self.selectordummy = QWidget(self.verticalWidget)
        self.plotdatasetSelector = QComboBox(self.selectordummy)
        self.plotdatasetSelector.setFont(Fonts.label_normal)

        self.horizontalLayout_3 = QHBoxLayout(self.selectordummy)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.addWidget(self.plotdatasetSelector)
        # color value edit
        self.colorvaluedummy = QWidget(self.verticalWidget)
        self.colorCheckBox = QCheckBox(self.colorvaluedummy)

        self.colorminLineEdit = QLineEdit(self.colorvaluedummy)
        self.colorminLineEdit.setEnabled(False)
        self.colorminLineEdit.setFont(Fonts.numeric_small)

        self.colormaxLineEdit = QLineEdit(self.colorvaluedummy)
        self.colormaxLineEdit.setEnabled(False)
        self.colormaxLineEdit.setFont(Fonts.numeric_small)

        self.horizontalLayout_6 = QHBoxLayout(self.colorvaluedummy)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.addWidget(self.colorCheckBox)
        self.horizontalLayout_6.addWidget(self.colorminLineEdit)
        self.horizontalLayout_6.addWidget(self.colormaxLineEdit)
        # mask label
        self.maskingLabel = QLabel(self.verticalWidget)
        self.maskingLabel.setFont(Fonts.label_small)
        # mask selector
        self.maskselectordummy = QWidget(self.verticalWidget)
        self.maskdatasetSelector = QComboBox(self.maskselectordummy)
        self.maskdatasetSelector.setEnabled(False)
        self.maskdatasetSelector.setFont(Fonts.label_normal)

        self.maskdatasetLockButton = QPushButton(self.maskselectordummy)
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.maskdatasetLockButton.sizePolicy().hasHeightForWidth()
        )
        self.maskdatasetLockButton.setSizePolicy(sizePolicy1)
        self.maskdatasetLockButton.setMaximumSize(QSize(24, 16777215))
        self.maskdatasetLockButton.setFont(Fonts.icon_small)
        self.maskdatasetLockButton.setCheckable(True)
        self.maskdatasetLockButton.setChecked(True)

        self.horizontalLayout_2 = QHBoxLayout(self.maskselectordummy)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.addWidget(self.maskdatasetSelector)
        self.horizontalLayout_2.addWidget(self.maskdatasetLockButton)
        # mask value edit
        self.maskvaluedummy = QWidget(self.verticalWidget)
        self.maskCheckBox = QCheckBox(self.maskvaluedummy)

        self.maskminLineEdit = QLineEdit(self.maskvaluedummy)
        self.maskminLineEdit.setEnabled(False)
        self.maskminLineEdit.setFont(Fonts.numeric_small)

        self.maskmaxLineEdit = QLineEdit(self.maskvaluedummy)
        self.maskmaxLineEdit.setEnabled(False)
        self.maskmaxLineEdit.setFont(Fonts.numeric_small)

        self.horizontalLayout_7 = QHBoxLayout(self.maskvaluedummy)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.addWidget(self.maskCheckBox)
        self.horizontalLayout_7.addWidget(self.maskminLineEdit)
        self.horizontalLayout_7.addWidget(self.maskmaxLineEdit)
        # assemble it all
        self.verticalLayout_6 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_6.addWidget(self.colorLabel)
        self.verticalLayout_6.addWidget(self.selectordummy)
        self.verticalLayout_6.addWidget(self.colorvaluedummy)
        self.verticalLayout_6.addWidget(self.maskingLabel)
        self.verticalLayout_6.addWidget(self.maskselectordummy)
        self.verticalLayout_6.addWidget(self.maskvaluedummy)

        self.verticalLayout_4 = QVBoxLayout(self.contourDataGroup)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.addWidget(self.verticalWidget)

    def create_grid_spacing_group(self, ControlPane_Primary):
        self.gsGroup = FoldingGroupBox(ControlPane_Primary)
        self.gsGroup.setAlignment(Qt.AlignCenter)
        self.gsdummyWidget = QWidget(self.gsGroup)

        self.xgsLineEdit = QLineEdit(self.gsdummyWidget)
        self.xgsLineEdit.setFont(Fonts.numeric_small)
        self.ygsLineEdit = QLineEdit(self.gsdummyWidget)
        self.ygsLineEdit.setFont(Fonts.numeric_small)
        self.zgsLineEdit = QLineEdit(self.gsdummyWidget)
        self.zgsLineEdit.setFont(Fonts.numeric_small)

        self.gsLockButton = QPushButton(self.gsdummyWidget)
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.gsLockButton.sizePolicy().hasHeightForWidth()
        )
        self.gsLockButton.setSizePolicy(sizePolicy1)
        self.gsLockButton.setMaximumSize(QSize(24, 16777215))
        self.gsLockButton.setFont(Fonts.icon_small)
        self.gsLockButton.setCheckable(True)
        self.gsLockButton.setChecked(True)

        self.gridLayout_5 = QGridLayout(self.gsdummyWidget)
        self.gridLayout_5.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_5.addWidget(self.xgsLineEdit, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.ygsLineEdit, 2, 1, 1, 1)
        self.gridLayout_5.addWidget(self.zgsLineEdit, 3, 1, 1, 1)
        self.gridLayout_5.addWidget(self.gsLockButton, 1, 2, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout(self.gsGroup)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.addWidget(self.gsdummyWidget)

    def create_exaggeration_group(self, ControlPane_Primary):
        self.exagGroup = FoldingGroupBox(ControlPane_Primary)
        self.exagGroup.setAlignment(Qt.AlignCenter)
        self.exagdummyWidget = QWidget(self.exagGroup)

        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)

        self.xexagSpinBox = QDoubleSpinBox(self.exagdummyWidget)
        sizePolicy2.setHeightForWidth(
            self.xexagSpinBox.sizePolicy().hasHeightForWidth()
        )
        self.xexagSpinBox.setSizePolicy(sizePolicy2)
        self.xexagSpinBox.setMinimumSize(QSize(45, 0))
        self.xexagSpinBox.setFont(Fonts.numeric_small)
        self.xexagSpinBox.setDecimals(1)
        self.xexagSpinBox.setMaximum(1000.000000000000000)

        self.yexagSpinBox = QDoubleSpinBox(self.exagdummyWidget)
        sizePolicy2.setHeightForWidth(
            self.yexagSpinBox.sizePolicy().hasHeightForWidth()
        )
        self.yexagSpinBox.setSizePolicy(sizePolicy2)
        self.yexagSpinBox.setMinimumSize(QSize(45, 0))
        self.yexagSpinBox.setFont(Fonts.numeric_small)
        self.yexagSpinBox.setKeyboardTracking(False)
        self.yexagSpinBox.setDecimals(1)
        self.yexagSpinBox.setMaximum(1000.000000000000000)

        self.zexagSpinBox = QDoubleSpinBox(self.exagdummyWidget)
        sizePolicy2.setHeightForWidth(
            self.zexagSpinBox.sizePolicy().hasHeightForWidth()
        )
        self.zexagSpinBox.setSizePolicy(sizePolicy2)
        self.zexagSpinBox.setMinimumSize(QSize(45, 0))
        self.zexagSpinBox.setFont(Fonts.numeric_small)
        self.zexagSpinBox.setDecimals(1)
        self.zexagSpinBox.setMaximum(1000.000000000000000)

        self.exagLockButton = QPushButton(self.exagdummyWidget)
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.exagLockButton.sizePolicy().hasHeightForWidth()
        )
        self.exagLockButton.setSizePolicy(sizePolicy1)
        self.exagLockButton.setMaximumSize(QSize(24, 16777215))
        self.exagLockButton.setFont(Fonts.icon_small)
        self.exagLockButton.setCheckable(True)
        self.exagLockButton.setChecked(True)

        self.gridLayout_4 = QGridLayout(self.exagdummyWidget)
        self.gridLayout_4.setSpacing(4)
        self.gridLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_4.addWidget(self.xexagSpinBox, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.yexagSpinBox, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.zexagSpinBox, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.exagLockButton, 0, 3, 1, 1)

        self.verticalLayout = QVBoxLayout(self.exagGroup)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.addWidget(self.exagdummyWidget)

    def create_clipping_extents_group(self, ControlPane_Primary):
        self.extentsGroup = FoldingGroupBox(ControlPane_Primary)
        self.extentsGroup.setAlignment(Qt.AlignCenter)
        self.extentsdummyWidget = QWidget(self.extentsGroup)

        self.clippingboxButton = QPushButton(self.extentsGroup)
        self.clippingboxButton.setCheckable(True)

        self.xminLineEdit = QLineEdit(self.extentsdummyWidget)
        self.xminLineEdit.setEnabled(False)
        self.xminLineEdit.setFont(Fonts.numeric_small)

        self.yminLineEdit = QLineEdit(self.extentsdummyWidget)
        self.yminLineEdit.setEnabled(False)
        self.yminLineEdit.setFont(Fonts.numeric_small)

        self.zminLineEdit = QLineEdit(self.extentsdummyWidget)
        self.zminLineEdit.setEnabled(False)
        self.zminLineEdit.setFont(Fonts.numeric_small)

        self.xmaxLineEdit = QLineEdit(self.extentsdummyWidget)
        self.xmaxLineEdit.setEnabled(False)
        self.xmaxLineEdit.setFont(Fonts.numeric_small)

        self.ymaxLineEdit = QLineEdit(self.extentsdummyWidget)
        self.ymaxLineEdit.setEnabled(False)
        self.ymaxLineEdit.setFont(Fonts.numeric_small)

        self.zmaxLineEdit = QLineEdit(self.extentsdummyWidget)
        self.zmaxLineEdit.setEnabled(False)
        self.zmaxLineEdit.setFont(Fonts.numeric_small)

        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)

        self.xLabel = QLabel(self.extentsdummyWidget)
        sizePolicy3.setHeightForWidth(self.xLabel.sizePolicy().hasHeightForWidth())
        self.xLabel.setSizePolicy(sizePolicy3)
        self.xLabel.setFont(Fonts.label_small)
        self.xLabel.setScaledContents(False)

        self.yLabel = QLabel(self.extentsdummyWidget)
        sizePolicy3.setHeightForWidth(self.yLabel.sizePolicy().hasHeightForWidth())
        self.yLabel.setSizePolicy(sizePolicy3)
        self.yLabel.setFont(Fonts.label_small)
        self.yLabel.setScaledContents(False)

        self.zLabel = QLabel(self.extentsdummyWidget)
        sizePolicy3.setHeightForWidth(self.zLabel.sizePolicy().hasHeightForWidth())
        self.zLabel.setSizePolicy(sizePolicy3)
        self.zLabel.setFont(Fonts.label_small)
        self.zLabel.setScaledContents(False)

        self.xclipCheckBox = QCheckBox(self.extentsdummyWidget)
        self.yclipCheckBox = QCheckBox(self.extentsdummyWidget)
        self.zclipCheckBox = QCheckBox(self.extentsdummyWidget)

        self.gridLayout_2 = QGridLayout(self.extentsdummyWidget)
        self.gridLayout_2.setSpacing(4)
        self.gridLayout_2.setContentsMargins(4, 1, 4, 4)
        self.gridLayout_2.addWidget(self.xminLineEdit, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.yminLineEdit, 2, 2, 1, 1)
        self.gridLayout_2.addWidget(self.zminLineEdit, 3, 2, 1, 1)
        self.gridLayout_2.addWidget(self.xmaxLineEdit, 0, 3, 1, 1)
        self.gridLayout_2.addWidget(self.ymaxLineEdit, 2, 3, 1, 1)
        self.gridLayout_2.addWidget(self.zmaxLineEdit, 3, 3, 1, 1)
        self.gridLayout_2.addWidget(self.xLabel, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.zLabel, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.zclipCheckBox, 3, 1, 1, 1)
        self.gridLayout_2.addWidget(self.yLabel, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.yclipCheckBox, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.xclipCheckBox, 0, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout(self.extentsGroup)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.addWidget(self.clippingboxButton)
        self.verticalLayout_2.addWidget(self.extentsdummyWidget)

    def create_camera_location_group(self, ControlPane_Primary):
        self.cameraLocationGroup = FoldingGroupBox(ControlPane_Primary)
        self.cameraLocationGroup.setAlignment(Qt.AlignCenter)
        self.cameralocationdummyWidget = QWidget(self.cameraLocationGroup)
        self.cameralocationdummyWidget.setCursor(QCursor(Qt.WhatsThisCursor))

        self.viewupLabel = QLabel(self.cameralocationdummyWidget)
        self.viewupLabel.setMaximumSize(QSize(65, 16777215))
        self.viewupLabel.setFont(Fonts.label_small)
        self.viewupLabel.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.positionLabel = QLabel(self.cameralocationdummyWidget)
        self.positionLabel.setMaximumSize(QSize(65, 16777215))
        self.positionLabel.setFont(Fonts.label_small)
        self.positionLabel.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.focalLabel = QLabel(self.cameralocationdummyWidget)
        self.focalLabel.setMaximumSize(QSize(65, 16777215))
        self.focalLabel.setFont(Fonts.label_small)
        self.focalLabel.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.focalValue = QLabel(self.cameralocationdummyWidget)
        self.focalValue.setFont(Fonts.numeric_small)

        self.positionValue = QLabel(self.cameralocationdummyWidget)
        self.positionValue.setFont(Fonts.numeric_small)

        self.viewupValue = QLabel(self.cameralocationdummyWidget)
        self.viewupValue.setFont(Fonts.numeric_small)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setSpacing(2)
        self.gridLayout_7.setContentsMargins(0, -1, -1, 0)
        self.gridLayout_7.addWidget(self.viewupLabel, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.positionLabel, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.focalLabel, 2, 0, 1, 1)
        self.gridLayout_7.addWidget(self.focalValue, 2, 1, 1, 1)
        self.gridLayout_7.addWidget(self.positionValue, 1, 1, 1, 1)
        self.gridLayout_7.addWidget(self.viewupValue, 0, 1, 1, 1)

        self.verticalLayout_7 = QVBoxLayout(self.cameralocationdummyWidget)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setContentsMargins(4, 1, 4, 4)
        self.verticalLayout_7.addLayout(self.gridLayout_7)

        self.verticalLayout_3 = QVBoxLayout(self.cameraLocationGroup)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.addWidget(self.cameralocationdummyWidget)

    def retranslateUi(self, ControlPane_Primary):
        ControlPane_Primary.setWindowTitle(
            QCoreApplication.translate("ControlPane_Primary", "Form", None)
        )
        self.timeStepGroup.setTitle(
            QCoreApplication.translate("ControlPane_Primary", "Time Step", None)
        )
        self.nextTimeStep.setText(
            QCoreApplication.translate("ControlPane_Primary", "\ue72a", None)
        )
        self.nextTimeStep.setShortcut(
            QCoreApplication.translate("ControlPane_Primary", "Ctrl+Right", None)
        )
        self.prevTimeStep.setText(
            QCoreApplication.translate("ControlPane_Primary", "\ue72b", None)
        )
        self.prevTimeStep.setShortcut(
            QCoreApplication.translate("ControlPane_Primary", "Ctrl+Left", None)
        )
        self.timeStepSelector.setCurrentText("")
        self.timelabelLabel.setText(
            QCoreApplication.translate("ControlPane_Primary", "Time:", None)
        )
        self.timeLabel.setText("")
        self.contourDataGroup.setTitle(
            QCoreApplication.translate("ControlPane_Primary", "Contour Data", None)
        )
        self.colorLabel.setText(
            QCoreApplication.translate("ControlPane_Primary", "Color", None)
        )
        self.colorCheckBox.setText("")
        self.maskingLabel.setText(
            QCoreApplication.translate("ControlPane_Primary", "Masking", None)
        )
        self.maskdatasetLockButton.setToolTip(
            QCoreApplication.translate(
                "ControlPane_Primary", "Toggle separate mask and plot datasets", None
            )
        )
        self.maskdatasetLockButton.setText(
            QCoreApplication.translate("ControlPane_Primary", "\ue72e", None)
        )
        self.maskCheckBox.setText("")
        self.gsGroup.setTitle(
            QCoreApplication.translate("ControlPane_Primary", "Grid Spacing", None)
        )
        self.gsLockButton.setToolTip(
            QCoreApplication.translate(
                "ControlPane_Primary", "Toggle uniform/non-uniform grid spacing", None
            )
        )
        self.gsLockButton.setText(
            QCoreApplication.translate("ControlPane_Primary", "\ue72e", None)
        )
        self.exagGroup.setTitle(
            QCoreApplication.translate("ControlPane_Primary", "Exaggeration", None)
        )
        self.yexagSpinBox.setSuffix("")
        self.exagLockButton.setToolTip(
            QCoreApplication.translate(
                "ControlPane_Primary", "Toggle uniform/non-uniform exaggeration", None
            )
        )
        self.exagLockButton.setText(
            QCoreApplication.translate("ControlPane_Primary", "\ue72e", None)
        )
        self.extentsGroup.setTitle(
            QCoreApplication.translate("ControlPane_Primary", "Clipping Extents", None)
        )
        self.clippingboxButton.setText(
            QCoreApplication.translate("ControlPane_Primary", "\u26f6", None)
        )
        self.xLabel.setText(
            QCoreApplication.translate("ControlPane_Primary", "X", None)
        )
        self.zLabel.setText(
            QCoreApplication.translate("ControlPane_Primary", "Z", None)
        )
        self.zclipCheckBox.setText("")
        self.yLabel.setText(
            QCoreApplication.translate("ControlPane_Primary", "Y", None)
        )
        self.yclipCheckBox.setText("")
        self.xclipCheckBox.setText("")
        self.cameraLocationGroup.setTitle(
            QCoreApplication.translate("ControlPane_Primary", "Camera Location", None)
        )
        self.cameralocationdummyWidget.setToolTip(
            QCoreApplication.translate(
                "ControlPane_Primary",
                "Left Click to copy camera location\n" "Right Click to paste",
                None,
            )
        )
        self.viewupLabel.setText(
            QCoreApplication.translate("ControlPane_Primary", "View-up:", None)
        )
        self.positionLabel.setText(
            QCoreApplication.translate("ControlPane_Primary", "Position:", None)
        )
        self.focalLabel.setText(
            QCoreApplication.translate("ControlPane_Primary", "Focal point:", None)
        )
        self.focalValue.setText("")
        self.positionValue.setText("")
        self.viewupValue.setText("")
