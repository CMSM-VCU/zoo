from PySide6.QtCore import QMetaObject, QSize, Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QSlider,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)

from .foldinggroupbox import FoldingGroupBox
from .style import Fonts


class Ui_ControlPane_Visuals(object):
    def setupUi(self, ControlPane_Visuals):
        if not ControlPane_Visuals.objectName():
            ControlPane_Visuals.setObjectName("ControlPane_Visuals")
        ControlPane_Visuals.resize(200, 630)
        self.gridLayout = QGridLayout(ControlPane_Visuals)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.controls = QVBoxLayout()
        self.controls.setObjectName("controls")
        self.viewportGroup = FoldingGroupBox(ControlPane_Visuals)
        self.viewportGroup.setObjectName("viewportGroup")
        self.viewportGroup.setEnabled(True)
        self.viewportGroup.setAlignment(Qt.AlignCenter)
        self.verticalLayout_4 = QVBoxLayout(self.viewportGroup)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget = QWidget(self.viewportGroup)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_2 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widthLineEdit = QLineEdit(self.verticalWidget)
        self.widthLineEdit.setObjectName("widthLineEdit")
        self.widthLineEdit.setFont(Fonts.numeric_small)

        self.gridLayout_3.addWidget(self.widthLineEdit, 1, 0, 1, 1)

        self.heightLineEdit = QLineEdit(self.verticalWidget)
        self.heightLineEdit.setObjectName("heightLineEdit")
        self.heightLineEdit.setFont(Fonts.numeric_small)

        self.gridLayout_3.addWidget(self.heightLineEdit, 1, 2, 1, 1)

        self.label = QLabel(self.verticalWidget)
        self.label.setObjectName("label")
        self.label.setFont(Fonts.label_small)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.verticalWidget)
        self.label_2.setObjectName("label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 1, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bgcolorFrameButton = QFrame(self.verticalWidget)
        self.bgcolorFrameButton.setObjectName("bgcolorFrameButton")
        self.bgcolorFrameButton.setMinimumSize(QSize(24, 24))
        self.bgcolorFrameButton.setMaximumSize(QSize(24, 16777215))
        self.bgcolorFrameButton.setStyleSheet("background-color: red")
        self.bgcolorFrameButton.setFrameShape(QFrame.Panel)
        self.bgcolorFrameButton.setFrameShadow(QFrame.Sunken)
        self.bgcolorFrameButton.setLineWidth(3)

        self.horizontalLayout_2.addWidget(self.bgcolorFrameButton)

        self.bgcolorLabel = QLabel(self.verticalWidget)
        self.bgcolorLabel.setObjectName("bgcolorLabel")
        self.bgcolorLabel.setFont(Fonts.label_small)

        self.horizontalLayout_2.addWidget(self.bgcolorLabel)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4.addWidget(self.verticalWidget)

        self.controls.addWidget(self.viewportGroup)

        self.verticalSpacer_7 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum
        )

        self.controls.addItem(self.verticalSpacer_7)

        self.colormapGroup = FoldingGroupBox(ControlPane_Visuals)
        self.colormapGroup.setObjectName("colormapGroup")
        self.colormapGroup.setEnabled(True)
        self.colormapGroup.setAlignment(Qt.AlignCenter)
        self.verticalLayout_5 = QVBoxLayout(self.colormapGroup)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget1 = QWidget(self.colormapGroup)
        self.verticalWidget1.setObjectName("verticalWidget1")
        self.verticalLayout = QVBoxLayout(self.verticalWidget1)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.colormapSelector = QComboBox(self.verticalWidget1)
        self.colormapSelector.setObjectName("colormapSelector")
        self.colormapSelector.setEditable(True)

        self.verticalLayout.addWidget(self.colormapSelector)

        self.reverseCheckBox = QCheckBox(self.verticalWidget1)
        self.reverseCheckBox.setObjectName("reverseCheckBox")

        self.verticalLayout.addWidget(self.reverseCheckBox)

        self.outofrangeCheckBox = QCheckBox(self.verticalWidget1)
        self.outofrangeCheckBox.setObjectName("outofrangeCheckBox")

        self.verticalLayout.addWidget(self.outofrangeCheckBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.abovecolorFrameButton = QFrame(self.verticalWidget1)
        self.abovecolorFrameButton.setObjectName("abovecolorFrameButton")
        self.abovecolorFrameButton.setEnabled(False)
        self.abovecolorFrameButton.setMinimumSize(QSize(24, 24))
        self.abovecolorFrameButton.setMaximumSize(QSize(24, 16777215))
        self.abovecolorFrameButton.setStyleSheet("background-color: white")
        self.abovecolorFrameButton.setFrameShape(QFrame.Panel)
        self.abovecolorFrameButton.setFrameShadow(QFrame.Sunken)
        self.abovecolorFrameButton.setLineWidth(3)

        self.horizontalLayout_3.addWidget(self.abovecolorFrameButton)

        self.abovecolorLabel = QLabel(self.verticalWidget1)
        self.abovecolorLabel.setObjectName("abovecolorLabel")
        self.abovecolorLabel.setEnabled(False)
        self.abovecolorLabel.setFont(Fonts.label_small)

        self.horizontalLayout_3.addWidget(self.abovecolorLabel)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.belowcolorFrameButton = QFrame(self.verticalWidget1)
        self.belowcolorFrameButton.setObjectName("belowcolorFrameButton")
        self.belowcolorFrameButton.setEnabled(False)
        self.belowcolorFrameButton.setMinimumSize(QSize(24, 24))
        self.belowcolorFrameButton.setMaximumSize(QSize(24, 16777215))
        self.belowcolorFrameButton.setStyleSheet("background-color: black")
        self.belowcolorFrameButton.setFrameShape(QFrame.Panel)
        self.belowcolorFrameButton.setFrameShadow(QFrame.Sunken)
        self.belowcolorFrameButton.setLineWidth(3)

        self.horizontalLayout_4.addWidget(self.belowcolorFrameButton)

        self.belowcolorLabel = QLabel(self.verticalWidget1)
        self.belowcolorLabel.setObjectName("belowcolorLabel")
        self.belowcolorLabel.setEnabled(False)
        self.belowcolorLabel.setFont(Fonts.label_small)

        self.horizontalLayout_4.addWidget(self.belowcolorLabel)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalLayout_5.addWidget(self.verticalWidget1)

        self.controls.addWidget(self.colormapGroup)

        self.verticalSpacer_8 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum
        )

        self.controls.addItem(self.verticalSpacer_8)

        self.widgetsGroup = FoldingGroupBox(ControlPane_Visuals)
        self.widgetsGroup.setObjectName("widgetsGroup")
        self.widgetsGroup.setEnabled(True)
        self.widgetsGroup.setAlignment(Qt.AlignCenter)
        self.verticalLayout_6 = QVBoxLayout(self.widgetsGroup)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget_2 = QWidget(self.widgetsGroup)
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(8)
        self.eyeLabel = QLabel(self.verticalWidget_2)
        self.eyeLabel.setObjectName("eyeLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eyeLabel.sizePolicy().hasHeightForWidth())
        self.eyeLabel.setSizePolicy(sizePolicy)
        self.eyeLabel.setFont(Fonts.icon_normal)
        self.eyeLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.eyeLabel, 0, 0, 1, 1)

        self.orientationLabel = QLabel(self.verticalWidget_2)
        self.orientationLabel.setObjectName("orientationLabel")

        self.gridLayout_2.addWidget(self.orientationLabel, 2, 2, 1, 1)

        self.scalarbarvisCheckBox = QCheckBox(self.verticalWidget_2)
        self.scalarbarvisCheckBox.setObjectName("scalarbarvisCheckBox")
        self.scalarbarvisCheckBox.setChecked(True)

        self.gridLayout_2.addWidget(
            self.scalarbarvisCheckBox, 1, 0, 1, 1, Qt.AlignHCenter
        )

        self.scalarbarmoveCheckBox = QCheckBox(self.verticalWidget_2)
        self.scalarbarmoveCheckBox.setObjectName("scalarbarmoveCheckBox")
        self.scalarbarmoveCheckBox.setEnabled(False)

        self.gridLayout_2.addWidget(
            self.scalarbarmoveCheckBox, 1, 1, 1, 1, Qt.AlignHCenter
        )

        self.orientationmoveCheckBox = QCheckBox(self.verticalWidget_2)
        self.orientationmoveCheckBox.setObjectName("orientationmoveCheckBox")
        self.orientationmoveCheckBox.setEnabled(False)

        self.gridLayout_2.addWidget(
            self.orientationmoveCheckBox, 2, 1, 1, 1, Qt.AlignHCenter
        )

        self.orientationvisCheckBox = QCheckBox(self.verticalWidget_2)
        self.orientationvisCheckBox.setObjectName("orientationvisCheckBox")
        self.orientationvisCheckBox.setChecked(True)

        self.gridLayout_2.addWidget(
            self.orientationvisCheckBox, 2, 0, 1, 1, Qt.AlignHCenter
        )

        self.scalarbarLabel = QLabel(self.verticalWidget_2)
        self.scalarbarLabel.setObjectName("scalarbarLabel")

        self.gridLayout_2.addWidget(self.scalarbarLabel, 1, 2, 1, 1)

        self.moveLabel = QLabel(self.verticalWidget_2)
        self.moveLabel.setObjectName("moveLabel")
        sizePolicy.setHeightForWidth(self.moveLabel.sizePolicy().hasHeightForWidth())
        self.moveLabel.setSizePolicy(sizePolicy)
        self.moveLabel.setFont(Fonts.icon_normal)
        self.moveLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.moveLabel, 0, 1, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.verticalLayout_6.addWidget(self.verticalWidget_2)

        self.controls.addWidget(self.widgetsGroup)

        self.verticalSpacer_9 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum
        )

        self.controls.addItem(self.verticalSpacer_9)

        self.glyphsGroup = FoldingGroupBox(ControlPane_Visuals)
        self.glyphsGroup.setObjectName("glyphsGroup")
        self.glyphsGroup.setEnabled(True)
        self.glyphsGroup.setAlignment(Qt.AlignCenter)
        self.verticalLayout_7 = QVBoxLayout(self.glyphsGroup)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget_3 = QWidget(self.glyphsGroup)
        self.verticalWidget_3.setObjectName("verticalWidget_3")
        self.verticalLayout_8 = QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(4, 4, 4, 4)
        self.opacityCheckBox = QCheckBox(self.verticalWidget_3)
        self.opacityCheckBox.setObjectName("opacityCheckBox")
        self.opacityCheckBox.setFont(Fonts.label_small)

        self.verticalLayout_8.addWidget(self.opacityCheckBox)

        self.opacitycontrolFrame = QFrame(self.verticalWidget_3)
        self.opacitycontrolFrame.setObjectName("opacitycontrolFrame")
        self.opacitycontrolFrame.setEnabled(False)
        self.gridLayout_4 = QGridLayout(self.opacitycontrolFrame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.orientationLabel_2 = QLabel(self.opacitycontrolFrame)
        self.orientationLabel_2.setObjectName("orientationLabel_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(4)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.orientationLabel_2.sizePolicy().hasHeightForWidth()
        )
        self.orientationLabel_2.setSizePolicy(sizePolicy1)
        self.orientationLabel_2.setFont(Fonts.label_small)

        self.gridLayout_4.addWidget(self.orientationLabel_2, 1, 0, 1, 1)

        self.maskopacityvalueLabel = QLabel(self.opacitycontrolFrame)
        self.maskopacityvalueLabel.setObjectName("maskopacityvalueLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.maskopacityvalueLabel.sizePolicy().hasHeightForWidth()
        )
        self.maskopacityvalueLabel.setSizePolicy(sizePolicy2)
        self.maskopacityvalueLabel.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.gridLayout_4.addWidget(self.maskopacityvalueLabel, 0, 2, 1, 1)

        self.clipopacitySlider = QSlider(self.opacitycontrolFrame)
        self.clipopacitySlider.setObjectName("clipopacitySlider")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(9)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.clipopacitySlider.sizePolicy().hasHeightForWidth()
        )
        self.clipopacitySlider.setSizePolicy(sizePolicy3)
        self.clipopacitySlider.setMaximum(20)
        self.clipopacitySlider.setSingleStep(1)
        self.clipopacitySlider.setPageStep(4)
        self.clipopacitySlider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.clipopacitySlider, 1, 1, 1, 1)

        self.maskopacitySlider = QSlider(self.opacitycontrolFrame)
        self.maskopacitySlider.setObjectName("maskopacitySlider")
        sizePolicy3.setHeightForWidth(
            self.maskopacitySlider.sizePolicy().hasHeightForWidth()
        )
        self.maskopacitySlider.setSizePolicy(sizePolicy3)
        self.maskopacitySlider.setMouseTracking(False)
        self.maskopacitySlider.setMaximum(20)
        self.maskopacitySlider.setSingleStep(1)
        self.maskopacitySlider.setPageStep(4)
        self.maskopacitySlider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.maskopacitySlider, 0, 1, 1, 1)

        self.scalarbarLabel_2 = QLabel(self.opacitycontrolFrame)
        self.scalarbarLabel_2.setObjectName("scalarbarLabel_2")
        sizePolicy1.setHeightForWidth(
            self.scalarbarLabel_2.sizePolicy().hasHeightForWidth()
        )
        self.scalarbarLabel_2.setSizePolicy(sizePolicy1)
        self.scalarbarLabel_2.setFont(Fonts.label_small)

        self.gridLayout_4.addWidget(self.scalarbarLabel_2, 0, 0, 1, 1)

        self.clipopacityvalueLabel = QLabel(self.opacitycontrolFrame)
        self.clipopacityvalueLabel.setObjectName("clipopacityvalueLabel")
        sizePolicy2.setHeightForWidth(
            self.clipopacityvalueLabel.sizePolicy().hasHeightForWidth()
        )
        self.clipopacityvalueLabel.setSizePolicy(sizePolicy2)
        self.clipopacityvalueLabel.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.gridLayout_4.addWidget(self.clipopacityvalueLabel, 1, 2, 1, 1)

        self.verticalLayout_8.addWidget(self.opacitycontrolFrame)

        self.verticalLayout_7.addWidget(self.verticalWidget_3)

        self.controls.addWidget(self.glyphsGroup)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.controls.addItem(self.verticalSpacer)

        self.gridLayout.addLayout(self.controls, 0, 0, 1, 1)

        QMetaObject.connectSlotsByName(ControlPane_Visuals)
