from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
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
from .style import Fonts, default_spacer


class Ui_ControlPane_Visuals(object):
    def setupUi(self, ControlPane_Visuals):
        ControlPane_Visuals.resize(200, 630)

        self.create_viewport_group(ControlPane_Visuals)
        self.create_colormap_group(ControlPane_Visuals)
        self.create_widgets_group(ControlPane_Visuals)
        self.create_glyphs_group(ControlPane_Visuals)

        self.controls = QVBoxLayout()
        self.controls.addWidget(self.viewportGroup)
        self.controls.addItem(default_spacer())
        self.controls.addWidget(self.colormapGroup)
        self.controls.addItem(default_spacer())
        self.controls.addWidget(self.widgetsGroup)
        self.controls.addItem(default_spacer())
        self.controls.addWidget(self.glyphsGroup)
        self.controls.addItem(
            QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

        self.gridLayout = QGridLayout(ControlPane_Visuals)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.addLayout(self.controls, 0, 0, 1, 1)

        self.retranslateUi(ControlPane_Visuals)

        QMetaObject.connectSlotsByName(ControlPane_Visuals)

    def create_viewport_group(self, ControlPane_Visuals):
        self.viewportGroup = FoldingGroupBox(ControlPane_Visuals)
        self.viewportGroup.setAlignment(Qt.AlignCenter)
        verticalWidget = QWidget(self.viewportGroup)

        self.widthLineEdit = QLineEdit(verticalWidget)
        self.widthLineEdit.setFont(Fonts.numeric_small)

        self.heightLineEdit = QLineEdit(verticalWidget)
        self.heightLineEdit.setFont(Fonts.numeric_small)

        self.resolution_label = QLabel(verticalWidget)
        self.resolution_label.setFont(Fonts.label_small)

        self.x_label = QLabel(verticalWidget)

        gridLayout = QGridLayout()
        gridLayout.addWidget(self.widthLineEdit, 1, 0, 1, 1)
        gridLayout.addWidget(self.heightLineEdit, 1, 2, 1, 1)
        gridLayout.addWidget(self.resolution_label, 0, 0, 1, 1)
        gridLayout.addWidget(self.x_label, 1, 1, 1, 1)

        self.bgcolorFrameButton = QFrame(verticalWidget)
        self.bgcolorFrameButton.setMinimumSize(QSize(24, 24))
        self.bgcolorFrameButton.setMaximumSize(QSize(24, 16777215))
        self.bgcolorFrameButton.setStyleSheet("background-color: red")
        self.bgcolorFrameButton.setFrameShape(QFrame.Panel)
        self.bgcolorFrameButton.setFrameShadow(QFrame.Sunken)
        self.bgcolorFrameButton.setLineWidth(3)

        self.bgcolorLabel = QLabel(verticalWidget)
        self.bgcolorLabel.setFont(Fonts.label_small)

        horizontalLayout = QHBoxLayout()
        horizontalLayout.addWidget(self.bgcolorFrameButton)
        horizontalLayout.addWidget(self.bgcolorLabel)

        verticalLayout_1 = QVBoxLayout(verticalWidget)
        verticalLayout_1.setSpacing(4)
        verticalLayout_1.setContentsMargins(4, 4, 4, 4)
        verticalLayout_1.addLayout(gridLayout)
        verticalLayout_1.addLayout(horizontalLayout)

        verticalLayout_2 = QVBoxLayout(self.viewportGroup)
        verticalLayout_2.setSpacing(0)
        verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        verticalLayout_2.addWidget(verticalWidget)

    def create_colormap_group(self, ControlPane_Visuals):
        self.colormapGroup = FoldingGroupBox(ControlPane_Visuals)
        self.colormapGroup.setAlignment(Qt.AlignCenter)
        verticalWidget1 = QWidget(self.colormapGroup)

        self.colormapSelector = QComboBox(verticalWidget1)
        self.colormapSelector.setEditable(True)

        self.reverseCheckBox = QCheckBox(verticalWidget1)
        self.outofrangeCheckBox = QCheckBox(verticalWidget1)

        self.abovecolorFrameButton = QFrame(verticalWidget1)
        self.abovecolorFrameButton.setEnabled(False)
        self.abovecolorFrameButton.setMinimumSize(QSize(24, 24))
        self.abovecolorFrameButton.setMaximumSize(QSize(24, 16777215))
        self.abovecolorFrameButton.setStyleSheet("background-color: white")
        self.abovecolorFrameButton.setFrameShape(QFrame.Panel)
        self.abovecolorFrameButton.setFrameShadow(QFrame.Sunken)
        self.abovecolorFrameButton.setLineWidth(3)

        self.abovecolorLabel = QLabel(verticalWidget1)
        self.abovecolorLabel.setEnabled(False)
        self.abovecolorLabel.setFont(Fonts.label_small)

        horizontalLayout_1 = QHBoxLayout()
        horizontalLayout_1.addWidget(self.abovecolorFrameButton)
        horizontalLayout_1.addWidget(self.abovecolorLabel)

        self.belowcolorFrameButton = QFrame(verticalWidget1)
        self.belowcolorFrameButton.setEnabled(False)
        self.belowcolorFrameButton.setMinimumSize(QSize(24, 24))
        self.belowcolorFrameButton.setMaximumSize(QSize(24, 16777215))
        self.belowcolorFrameButton.setStyleSheet("background-color: black")
        self.belowcolorFrameButton.setFrameShape(QFrame.Panel)
        self.belowcolorFrameButton.setFrameShadow(QFrame.Sunken)
        self.belowcolorFrameButton.setLineWidth(3)

        self.belowcolorLabel = QLabel(verticalWidget1)
        self.belowcolorLabel.setEnabled(False)
        self.belowcolorLabel.setFont(Fonts.label_small)

        horizontalLayout_2 = QHBoxLayout()
        horizontalLayout_2.addWidget(self.belowcolorFrameButton)
        horizontalLayout_2.addWidget(self.belowcolorLabel)

        verticalLayout_1 = QVBoxLayout(verticalWidget1)
        verticalLayout_1.setSpacing(4)
        verticalLayout_1.setContentsMargins(4, 4, 4, 4)
        verticalLayout_1.addWidget(self.colormapSelector)
        verticalLayout_1.addWidget(self.reverseCheckBox)
        verticalLayout_1.addWidget(self.outofrangeCheckBox)
        verticalLayout_1.addLayout(horizontalLayout_1)
        verticalLayout_1.addLayout(horizontalLayout_2)

        verticalLayout_2 = QVBoxLayout(self.colormapGroup)
        verticalLayout_2.setSpacing(0)
        verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        verticalLayout_2.addWidget(verticalWidget1)

    def create_widgets_group(self, ControlPane_Visuals):
        self.widgetsGroup = FoldingGroupBox(ControlPane_Visuals)
        self.widgetsGroup.setAlignment(Qt.AlignCenter)
        verticalWidget_2 = QWidget(self.widgetsGroup)

        self.eyeLabel = QLabel(verticalWidget_2)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eyeLabel.sizePolicy().hasHeightForWidth())
        self.eyeLabel.setSizePolicy(sizePolicy)
        self.eyeLabel.setFont(Fonts.icon_normal)
        self.eyeLabel.setAlignment(Qt.AlignCenter)

        self.scalarbarvisCheckBox = QCheckBox(verticalWidget_2)
        self.scalarbarvisCheckBox.setChecked(True)

        self.scalarbarmoveCheckBox = QCheckBox(verticalWidget_2)
        self.scalarbarmoveCheckBox.setEnabled(False)

        self.orientationmoveCheckBox = QCheckBox(verticalWidget_2)
        self.orientationmoveCheckBox.setEnabled(False)

        self.orientationvisCheckBox = QCheckBox(verticalWidget_2)
        self.orientationvisCheckBox.setChecked(True)

        self.scalarbarLabel = QLabel(verticalWidget_2)
        self.orientationLabel = QLabel(verticalWidget_2)

        self.moveLabel = QLabel(verticalWidget_2)
        sizePolicy.setHeightForWidth(self.moveLabel.sizePolicy().hasHeightForWidth())
        self.moveLabel.setSizePolicy(sizePolicy)
        self.moveLabel.setFont(Fonts.icon_normal)
        self.moveLabel.setAlignment(Qt.AlignCenter)

        gridLayout = QGridLayout()
        gridLayout.setHorizontalSpacing(8)
        gridLayout.addWidget(self.eyeLabel, 0, 0, 1, 1)
        gridLayout.addWidget(self.orientationLabel, 2, 2, 1, 1)
        gridLayout.addWidget(self.scalarbarvisCheckBox, 1, 0, 1, 1, Qt.AlignHCenter)
        gridLayout.addWidget(self.scalarbarmoveCheckBox, 1, 1, 1, 1, Qt.AlignHCenter)
        gridLayout.addWidget(self.orientationmoveCheckBox, 2, 1, 1, 1, Qt.AlignHCenter)
        gridLayout.addWidget(self.orientationvisCheckBox, 2, 0, 1, 1, Qt.AlignHCenter)
        gridLayout.addWidget(self.scalarbarLabel, 1, 2, 1, 1)
        gridLayout.addWidget(self.moveLabel, 0, 1, 1, 1)

        verticalLayout_1 = QVBoxLayout(verticalWidget_2)
        verticalLayout_1.setSpacing(4)
        verticalLayout_1.setContentsMargins(4, 4, 4, 4)
        verticalLayout_1.addLayout(gridLayout)

        verticalLayout_2 = QVBoxLayout(self.widgetsGroup)
        verticalLayout_2.setSpacing(0)
        verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        verticalLayout_2.addWidget(verticalWidget_2)

    def create_glyphs_group(self, ControlPane_Visuals):
        self.glyphsGroup = FoldingGroupBox(ControlPane_Visuals)
        self.glyphsGroup.setAlignment(Qt.AlignCenter)
        verticalWidget = QWidget(self.glyphsGroup)

        self.opacityCheckBox = QCheckBox(verticalWidget)
        self.opacityCheckBox.setFont(Fonts.label_small)

        self.opacitycontrolFrame = QFrame(verticalWidget)
        self.opacitycontrolFrame.setEnabled(False)

        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(4)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(9)
        sizePolicy3.setVerticalStretch(0)
        # clipped
        self.clipped_label = QLabel(self.opacitycontrolFrame)
        sizePolicy1.setHeightForWidth(
            self.clipped_label.sizePolicy().hasHeightForWidth()
        )
        self.clipped_label.setSizePolicy(sizePolicy1)
        self.clipped_label.setFont(Fonts.label_small)

        self.clipopacitySlider = QSlider(self.opacitycontrolFrame)
        sizePolicy3.setHeightForWidth(
            self.clipopacitySlider.sizePolicy().hasHeightForWidth()
        )
        self.clipopacitySlider.setSizePolicy(sizePolicy3)
        self.clipopacitySlider.setMaximum(20)
        self.clipopacitySlider.setSingleStep(1)
        self.clipopacitySlider.setPageStep(4)
        self.clipopacitySlider.setOrientation(Qt.Horizontal)

        self.clipopacityvalueLabel = QLabel(self.opacitycontrolFrame)
        sizePolicy2.setHeightForWidth(
            self.clipopacityvalueLabel.sizePolicy().hasHeightForWidth()
        )
        self.clipopacityvalueLabel.setSizePolicy(sizePolicy2)
        self.clipopacityvalueLabel.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        # masked
        self.masked_label = QLabel(self.opacitycontrolFrame)
        sizePolicy1.setHeightForWidth(
            self.masked_label.sizePolicy().hasHeightForWidth()
        )
        self.masked_label.setSizePolicy(sizePolicy1)
        self.masked_label.setFont(Fonts.label_small)

        self.maskopacitySlider = QSlider(self.opacitycontrolFrame)
        sizePolicy3.setHeightForWidth(
            self.maskopacitySlider.sizePolicy().hasHeightForWidth()
        )
        self.maskopacitySlider.setSizePolicy(sizePolicy3)
        self.maskopacitySlider.setMouseTracking(False)
        self.maskopacitySlider.setMaximum(20)
        self.maskopacitySlider.setSingleStep(1)
        self.maskopacitySlider.setPageStep(4)
        self.maskopacitySlider.setOrientation(Qt.Horizontal)

        self.maskopacityvalueLabel = QLabel(self.opacitycontrolFrame)
        sizePolicy2.setHeightForWidth(
            self.maskopacityvalueLabel.sizePolicy().hasHeightForWidth()
        )
        self.maskopacityvalueLabel.setSizePolicy(sizePolicy2)
        self.maskopacityvalueLabel.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        gridLayout = QGridLayout(self.opacitycontrolFrame)
        gridLayout.setHorizontalSpacing(2)
        gridLayout.setContentsMargins(0, 0, 0, 0)
        gridLayout.addWidget(self.clipped_label, 1, 0, 1, 1)
        gridLayout.addWidget(self.maskopacityvalueLabel, 0, 2, 1, 1)
        gridLayout.addWidget(self.clipopacitySlider, 1, 1, 1, 1)
        gridLayout.addWidget(self.maskopacitySlider, 0, 1, 1, 1)
        gridLayout.addWidget(self.masked_label, 0, 0, 1, 1)
        gridLayout.addWidget(self.clipopacityvalueLabel, 1, 2, 1, 1)

        verticalLayout_1 = QVBoxLayout(verticalWidget)
        verticalLayout_1.setSpacing(4)
        verticalLayout_1.setContentsMargins(4, 4, 4, 4)
        verticalLayout_1.addWidget(self.opacityCheckBox)
        verticalLayout_1.addWidget(self.opacitycontrolFrame)

        verticalLayout_2 = QVBoxLayout(self.glyphsGroup)
        verticalLayout_2.setSpacing(0)
        verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        verticalLayout_2.addWidget(verticalWidget)

    def retranslateUi(self, ControlPane_Visuals):
        ControlPane_Visuals.setWindowTitle(
            QCoreApplication.translate("ControlPane_Visuals", "Form", None)
        )
        self.viewportGroup.setTitle(
            QCoreApplication.translate("ControlPane_Visuals", "Viewport", None)
        )
        self.resolution_label.setText(
            QCoreApplication.translate("ControlPane_Visuals", "Resolution", None)
        )
        self.x_label.setText(
            QCoreApplication.translate("ControlPane_Visuals", "X", None)
        )
        self.bgcolorLabel.setText(
            QCoreApplication.translate("ControlPane_Visuals", "Background Color", None)
        )
        self.colormapGroup.setTitle(
            QCoreApplication.translate("ControlPane_Visuals", "Colormap", None)
        )
        self.reverseCheckBox.setText(
            QCoreApplication.translate("ControlPane_Visuals", "Reverse colormap", None)
        )
        self.outofrangeCheckBox.setText(
            QCoreApplication.translate(
                "ControlPane_Visuals", "Out-of-range colors", None
            )
        )
        self.abovecolorLabel.setText(
            QCoreApplication.translate("ControlPane_Visuals", "Above-Range Color", None)
        )
        self.belowcolorLabel.setText(
            QCoreApplication.translate("ControlPane_Visuals", "Below-Range Color", None)
        )
        self.widgetsGroup.setTitle(
            QCoreApplication.translate("ControlPane_Visuals", "Widgets", None)
        )
        self.eyeLabel.setText(
            QCoreApplication.translate("ControlPane_Visuals", "\ue7b3", None)
        )
        self.orientationLabel.setText(
            QCoreApplication.translate("ControlPane_Visuals", "Orientation", None)
        )
        self.scalarbarvisCheckBox.setText("")
        self.scalarbarmoveCheckBox.setText("")
        self.orientationmoveCheckBox.setText("")
        self.orientationvisCheckBox.setText("")
        self.scalarbarLabel.setText(
            QCoreApplication.translate("ControlPane_Visuals", "Scalar bar", None)
        )
        self.moveLabel.setText(
            QCoreApplication.translate("ControlPane_Visuals", "\ue759", None)
        )
        self.glyphsGroup.setTitle(
            QCoreApplication.translate("ControlPane_Visuals", "Glyphs", None)
        )
        self.opacityCheckBox.setToolTip(
            QCoreApplication.translate(
                "ControlPane_Visuals", "WARNING: Seriously impacts performance!", None
            )
        )
        self.opacityCheckBox.setText(
            QCoreApplication.translate("ControlPane_Visuals", "Opacity \u26a0", None)
        )
        self.opacitycontrolFrame.setToolTip(
            QCoreApplication.translate(
                "ControlPane_Visuals", "Clipped opacity overrides masked opacity", None
            )
        )
        self.clipped_label.setText(
            QCoreApplication.translate(
                "ControlPane_Visuals",
                '<html><head/><body><p align="right">Clipped</p></body></html>',
                None,
            )
        )
        self.maskopacityvalueLabel.setText(
            QCoreApplication.translate("ControlPane_Visuals", "100%", None)
        )
        self.masked_label.setText(
            QCoreApplication.translate(
                "ControlPane_Visuals",
                '<html><head/><body><p align="right">Masked</p></body></html>',
                None,
            )
        )
        self.clipopacityvalueLabel.setText(
            QCoreApplication.translate("ControlPane_Visuals", "0%", None)
        )
