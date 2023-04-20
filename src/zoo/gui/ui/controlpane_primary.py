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
        timestepdummyWidget = QWidget(self.timeStepGroup)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.nextTimeStep = QPushButton(timestepdummyWidget)
        sizePolicy.setHeightForWidth(self.nextTimeStep.sizePolicy().hasHeightForWidth())
        self.nextTimeStep.setSizePolicy(sizePolicy)
        self.nextTimeStep.setMaximumSize(QSize(24, 16777215))
        self.nextTimeStep.setBaseSize(QSize(16, 16))
        self.nextTimeStep.setFont(Fonts.icon_small)

        self.prevTimeStep = QPushButton(timestepdummyWidget)
        sizePolicy.setHeightForWidth(self.prevTimeStep.sizePolicy().hasHeightForWidth())
        self.prevTimeStep.setSizePolicy(sizePolicy)
        self.prevTimeStep.setMaximumSize(QSize(24, 16777215))
        self.prevTimeStep.setBaseSize(QSize(16, 16))
        self.prevTimeStep.setFont(Fonts.icon_small)

        self.timeStepSelector = QComboBox(timestepdummyWidget)
        self.timeStepSelector.setFont(Fonts.numeric_normal)

        self.timelabelLabel = QLabel(timestepdummyWidget)
        self.timelabelLabel.setFont(Fonts.label_small)

        self.timeLabel = QLabel(timestepdummyWidget)
        self.timeLabel.setFont(Fonts.label_small)
        self.timeLabel.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        layout_timevalue = QHBoxLayout()
        layout_timevalue.addWidget(self.timelabelLabel)
        layout_timevalue.addWidget(self.timeLabel)

        layout_grid = QGridLayout(timestepdummyWidget)
        layout_grid.setHorizontalSpacing(0)
        layout_grid.setVerticalSpacing(2)
        layout_grid.setContentsMargins(3, 1, 3, 4)
        layout_grid.addWidget(self.nextTimeStep, 0, 2, 1, 1)
        layout_grid.addWidget(self.prevTimeStep, 0, 0, 1, 1)
        layout_grid.addWidget(self.timeStepSelector, 0, 1, 1, 1)
        layout_grid.addLayout(layout_timevalue, 5, 1, 1, 1)

        layout_groupbox = QVBoxLayout(self.timeStepGroup)
        layout_groupbox.setContentsMargins(0, 0, 0, 0)
        layout_groupbox.addWidget(timestepdummyWidget)

    def create_contour_data_group(self, ControlPane_Primary):
        self.contourDataGroup = FoldingGroupBox(ControlPane_Primary)
        self.contourDataGroup.setAlignment(Qt.AlignCenter)
        verticalWidget = QWidget(self.contourDataGroup)
        # color label
        self.colorLabel = QLabel(verticalWidget)
        self.colorLabel.setFont(Fonts.label_small)
        # color selector
        selectordummy = QWidget(verticalWidget)
        self.plotdatasetSelector = QComboBox(selectordummy)
        self.plotdatasetSelector.setFont(Fonts.label_normal)

        horizontalLayout_1 = QHBoxLayout(selectordummy)
        horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_1.addWidget(self.plotdatasetSelector)
        # color value edit
        colorvaluedummy = QWidget(verticalWidget)
        self.colorCheckBox = QCheckBox(colorvaluedummy)

        self.colorminLineEdit = QLineEdit(colorvaluedummy)
        self.colorminLineEdit.setEnabled(False)
        self.colorminLineEdit.setFont(Fonts.numeric_small)

        self.colormaxLineEdit = QLineEdit(colorvaluedummy)
        self.colormaxLineEdit.setEnabled(False)
        self.colormaxLineEdit.setFont(Fonts.numeric_small)

        horizontalLayout_2 = QHBoxLayout(colorvaluedummy)
        horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_2.addWidget(self.colorCheckBox)
        horizontalLayout_2.addWidget(self.colorminLineEdit)
        horizontalLayout_2.addWidget(self.colormaxLineEdit)
        # mask label
        self.maskingLabel = QLabel(verticalWidget)
        self.maskingLabel.setFont(Fonts.label_small)
        # mask selector
        maskselectordummy = QWidget(verticalWidget)
        self.maskdatasetSelector = QComboBox(maskselectordummy)
        self.maskdatasetSelector.setEnabled(False)
        self.maskdatasetSelector.setFont(Fonts.label_normal)

        self.maskdatasetLockButton = QPushButton(maskselectordummy)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.maskdatasetLockButton.sizePolicy().hasHeightForWidth()
        )
        self.maskdatasetLockButton.setSizePolicy(sizePolicy)
        self.maskdatasetLockButton.setMaximumSize(QSize(24, 16777215))
        self.maskdatasetLockButton.setFont(Fonts.icon_small)
        self.maskdatasetLockButton.setCheckable(True)
        self.maskdatasetLockButton.setChecked(True)

        horizontalLayout_3 = QHBoxLayout(maskselectordummy)
        horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_3.addWidget(self.maskdatasetSelector)
        horizontalLayout_3.addWidget(self.maskdatasetLockButton)
        # mask value edit
        maskvaluedummy = QWidget(verticalWidget)
        self.maskCheckBox = QCheckBox(maskvaluedummy)

        self.maskminLineEdit = QLineEdit(maskvaluedummy)
        self.maskminLineEdit.setEnabled(False)
        self.maskminLineEdit.setFont(Fonts.numeric_small)

        self.maskmaxLineEdit = QLineEdit(maskvaluedummy)
        self.maskmaxLineEdit.setEnabled(False)
        self.maskmaxLineEdit.setFont(Fonts.numeric_small)

        horizontalLayout_4 = QHBoxLayout(maskvaluedummy)
        horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_4.addWidget(self.maskCheckBox)
        horizontalLayout_4.addWidget(self.maskminLineEdit)
        horizontalLayout_4.addWidget(self.maskmaxLineEdit)
        # assemble it all
        verticalLayout_1 = QVBoxLayout(verticalWidget)
        verticalLayout_1.setSpacing(4)
        verticalLayout_1.setContentsMargins(4, 4, 4, 4)
        verticalLayout_1.addWidget(self.colorLabel)
        verticalLayout_1.addWidget(selectordummy)
        verticalLayout_1.addWidget(colorvaluedummy)
        verticalLayout_1.addWidget(self.maskingLabel)
        verticalLayout_1.addWidget(maskselectordummy)
        verticalLayout_1.addWidget(maskvaluedummy)

        verticalLayout_2 = QVBoxLayout(self.contourDataGroup)
        verticalLayout_2.setSpacing(0)
        verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        verticalLayout_2.addWidget(verticalWidget)

    def create_grid_spacing_group(self, ControlPane_Primary):
        self.gsGroup = FoldingGroupBox(ControlPane_Primary)
        self.gsGroup.setAlignment(Qt.AlignCenter)
        gsdummyWidget = QWidget(self.gsGroup)

        self.xgsLineEdit = QLineEdit(gsdummyWidget)
        self.xgsLineEdit.setFont(Fonts.numeric_small)
        self.ygsLineEdit = QLineEdit(gsdummyWidget)
        self.ygsLineEdit.setFont(Fonts.numeric_small)
        self.zgsLineEdit = QLineEdit(gsdummyWidget)
        self.zgsLineEdit.setFont(Fonts.numeric_small)

        self.gsLockButton = QPushButton(gsdummyWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gsLockButton.sizePolicy().hasHeightForWidth())
        self.gsLockButton.setSizePolicy(sizePolicy)
        self.gsLockButton.setMaximumSize(QSize(24, 16777215))
        self.gsLockButton.setFont(Fonts.icon_small)
        self.gsLockButton.setCheckable(True)
        self.gsLockButton.setChecked(True)

        gridLayout = QGridLayout(gsdummyWidget)
        gridLayout.setContentsMargins(4, 4, 4, 4)
        gridLayout.addWidget(self.xgsLineEdit, 1, 1, 1, 1)
        gridLayout.addWidget(self.ygsLineEdit, 2, 1, 1, 1)
        gridLayout.addWidget(self.zgsLineEdit, 3, 1, 1, 1)
        gridLayout.addWidget(self.gsLockButton, 1, 2, 1, 1)

        horizontalLayout = QHBoxLayout(self.gsGroup)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.addWidget(gsdummyWidget)

    def create_exaggeration_group(self, ControlPane_Primary):
        self.exagGroup = FoldingGroupBox(ControlPane_Primary)
        self.exagGroup.setAlignment(Qt.AlignCenter)
        exagdummyWidget = QWidget(self.exagGroup)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.xexagSpinBox = QDoubleSpinBox(exagdummyWidget)
        sizePolicy.setHeightForWidth(self.xexagSpinBox.sizePolicy().hasHeightForWidth())
        self.xexagSpinBox.setSizePolicy(sizePolicy)
        self.xexagSpinBox.setMinimumSize(QSize(45, 0))
        self.xexagSpinBox.setFont(Fonts.numeric_small)
        self.xexagSpinBox.setDecimals(1)
        self.xexagSpinBox.setMaximum(1000.000000000000000)

        self.yexagSpinBox = QDoubleSpinBox(exagdummyWidget)
        sizePolicy.setHeightForWidth(self.yexagSpinBox.sizePolicy().hasHeightForWidth())
        self.yexagSpinBox.setSizePolicy(sizePolicy)
        self.yexagSpinBox.setMinimumSize(QSize(45, 0))
        self.yexagSpinBox.setFont(Fonts.numeric_small)
        self.yexagSpinBox.setKeyboardTracking(False)
        self.yexagSpinBox.setDecimals(1)
        self.yexagSpinBox.setMaximum(1000.000000000000000)

        self.zexagSpinBox = QDoubleSpinBox(exagdummyWidget)
        sizePolicy.setHeightForWidth(self.zexagSpinBox.sizePolicy().hasHeightForWidth())
        self.zexagSpinBox.setSizePolicy(sizePolicy)
        self.zexagSpinBox.setMinimumSize(QSize(45, 0))
        self.zexagSpinBox.setFont(Fonts.numeric_small)
        self.zexagSpinBox.setDecimals(1)
        self.zexagSpinBox.setMaximum(1000.000000000000000)

        self.exagLockButton = QPushButton(exagdummyWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.exagLockButton.sizePolicy().hasHeightForWidth()
        )
        self.exagLockButton.setSizePolicy(sizePolicy)
        self.exagLockButton.setMaximumSize(QSize(24, 16777215))
        self.exagLockButton.setFont(Fonts.icon_small)
        self.exagLockButton.setCheckable(True)
        self.exagLockButton.setChecked(True)

        gridLayout = QGridLayout(exagdummyWidget)
        gridLayout.setSpacing(4)
        gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        gridLayout.setContentsMargins(4, 4, 4, 4)
        gridLayout.addWidget(self.xexagSpinBox, 0, 0, 1, 1)
        gridLayout.addWidget(self.yexagSpinBox, 0, 1, 1, 1)
        gridLayout.addWidget(self.zexagSpinBox, 0, 2, 1, 1)
        gridLayout.addWidget(self.exagLockButton, 0, 3, 1, 1)

        verticalLayout = QVBoxLayout(self.exagGroup)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.addWidget(exagdummyWidget)

    def create_clipping_extents_group(self, ControlPane_Primary):
        self.extentsGroup = FoldingGroupBox(ControlPane_Primary)
        self.extentsGroup.setAlignment(Qt.AlignCenter)
        extentsdummyWidget = QWidget(self.extentsGroup)

        self.clippingboxButton = QPushButton(self.extentsGroup)
        self.clippingboxButton.setCheckable(True)

        self.xminLineEdit = QLineEdit(extentsdummyWidget)
        self.xminLineEdit.setEnabled(False)
        self.xminLineEdit.setFont(Fonts.numeric_small)

        self.yminLineEdit = QLineEdit(extentsdummyWidget)
        self.yminLineEdit.setEnabled(False)
        self.yminLineEdit.setFont(Fonts.numeric_small)

        self.zminLineEdit = QLineEdit(extentsdummyWidget)
        self.zminLineEdit.setEnabled(False)
        self.zminLineEdit.setFont(Fonts.numeric_small)

        self.xmaxLineEdit = QLineEdit(extentsdummyWidget)
        self.xmaxLineEdit.setEnabled(False)
        self.xmaxLineEdit.setFont(Fonts.numeric_small)

        self.ymaxLineEdit = QLineEdit(extentsdummyWidget)
        self.ymaxLineEdit.setEnabled(False)
        self.ymaxLineEdit.setFont(Fonts.numeric_small)

        self.zmaxLineEdit = QLineEdit(extentsdummyWidget)
        self.zmaxLineEdit.setEnabled(False)
        self.zmaxLineEdit.setFont(Fonts.numeric_small)

        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.xLabel = QLabel(extentsdummyWidget)
        sizePolicy.setHeightForWidth(self.xLabel.sizePolicy().hasHeightForWidth())
        self.xLabel.setSizePolicy(sizePolicy)
        self.xLabel.setFont(Fonts.label_small)
        self.xLabel.setScaledContents(False)

        self.yLabel = QLabel(extentsdummyWidget)
        sizePolicy.setHeightForWidth(self.yLabel.sizePolicy().hasHeightForWidth())
        self.yLabel.setSizePolicy(sizePolicy)
        self.yLabel.setFont(Fonts.label_small)
        self.yLabel.setScaledContents(False)

        self.zLabel = QLabel(extentsdummyWidget)
        sizePolicy.setHeightForWidth(self.zLabel.sizePolicy().hasHeightForWidth())
        self.zLabel.setSizePolicy(sizePolicy)
        self.zLabel.setFont(Fonts.label_small)
        self.zLabel.setScaledContents(False)

        self.xclipCheckBox = QCheckBox(extentsdummyWidget)
        self.yclipCheckBox = QCheckBox(extentsdummyWidget)
        self.zclipCheckBox = QCheckBox(extentsdummyWidget)

        gridLayout = QGridLayout(extentsdummyWidget)
        gridLayout.setSpacing(4)
        gridLayout.setContentsMargins(4, 1, 4, 4)
        gridLayout.addWidget(self.xminLineEdit, 0, 2, 1, 1)
        gridLayout.addWidget(self.yminLineEdit, 2, 2, 1, 1)
        gridLayout.addWidget(self.zminLineEdit, 3, 2, 1, 1)
        gridLayout.addWidget(self.xmaxLineEdit, 0, 3, 1, 1)
        gridLayout.addWidget(self.ymaxLineEdit, 2, 3, 1, 1)
        gridLayout.addWidget(self.zmaxLineEdit, 3, 3, 1, 1)
        gridLayout.addWidget(self.xLabel, 0, 0, 1, 1)
        gridLayout.addWidget(self.zLabel, 3, 0, 1, 1)
        gridLayout.addWidget(self.zclipCheckBox, 3, 1, 1, 1)
        gridLayout.addWidget(self.yLabel, 2, 0, 1, 1)
        gridLayout.addWidget(self.yclipCheckBox, 2, 1, 1, 1)
        gridLayout.addWidget(self.xclipCheckBox, 0, 1, 1, 1)

        verticalLayout = QVBoxLayout(self.extentsGroup)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.addWidget(self.clippingboxButton)
        verticalLayout.addWidget(extentsdummyWidget)

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

        gridLayout = QGridLayout()
        gridLayout.setSpacing(2)
        gridLayout.setContentsMargins(0, -1, -1, 0)
        gridLayout.addWidget(self.viewupLabel, 0, 0, 1, 1)
        gridLayout.addWidget(self.positionLabel, 1, 0, 1, 1)
        gridLayout.addWidget(self.focalLabel, 2, 0, 1, 1)
        gridLayout.addWidget(self.focalValue, 2, 1, 1, 1)
        gridLayout.addWidget(self.positionValue, 1, 1, 1, 1)
        gridLayout.addWidget(self.viewupValue, 0, 1, 1, 1)

        verticalLayout_1 = QVBoxLayout(self.cameralocationdummyWidget)
        verticalLayout_1.setSpacing(4)
        verticalLayout_1.setContentsMargins(4, 1, 4, 4)
        verticalLayout_1.addLayout(gridLayout)

        verticalLayout_2 = QVBoxLayout(self.cameraLocationGroup)
        verticalLayout_2.setSpacing(0)
        verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        verticalLayout_2.addWidget(self.cameralocationdummyWidget)

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
