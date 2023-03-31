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
        self.verticalWidget = QWidget(self.viewportGroup)

        self.widthLineEdit = QLineEdit(self.verticalWidget)
        self.widthLineEdit.setFont(Fonts.numeric_small)

        self.heightLineEdit = QLineEdit(self.verticalWidget)
        self.heightLineEdit.setFont(Fonts.numeric_small)

        self.resolution_label = QLabel(self.verticalWidget)
        self.resolution_label.setFont(Fonts.label_small)

        self.x_label = QLabel(self.verticalWidget)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.addWidget(self.widthLineEdit, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.heightLineEdit, 1, 2, 1, 1)
        self.gridLayout_3.addWidget(self.resolution_label, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.x_label, 1, 1, 1, 1)

        self.bgcolorFrameButton = QFrame(self.verticalWidget)
        self.bgcolorFrameButton.setMinimumSize(QSize(24, 24))
        self.bgcolorFrameButton.setMaximumSize(QSize(24, 16777215))
        self.bgcolorFrameButton.setStyleSheet("background-color: red")
        self.bgcolorFrameButton.setFrameShape(QFrame.Panel)
        self.bgcolorFrameButton.setFrameShadow(QFrame.Sunken)
        self.bgcolorFrameButton.setLineWidth(3)

        self.bgcolorLabel = QLabel(self.verticalWidget)
        self.bgcolorLabel.setFont(Fonts.label_small)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.addWidget(self.bgcolorFrameButton)
        self.horizontalLayout_2.addWidget(self.bgcolorLabel)

        self.verticalLayout_2 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4 = QVBoxLayout(self.viewportGroup)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.addWidget(self.verticalWidget)

    def create_colormap_group(self, ControlPane_Visuals):
        self.colormapGroup = FoldingGroupBox(ControlPane_Visuals)
        self.colormapGroup.setAlignment(Qt.AlignCenter)
        self.verticalWidget1 = QWidget(self.colormapGroup)

        self.colormapSelector = QComboBox(self.verticalWidget1)
        self.colormapSelector.setEditable(True)

        self.reverseCheckBox = QCheckBox(self.verticalWidget1)
        self.outofrangeCheckBox = QCheckBox(self.verticalWidget1)

        self.abovecolorFrameButton = QFrame(self.verticalWidget1)
        self.abovecolorFrameButton.setEnabled(False)
        self.abovecolorFrameButton.setMinimumSize(QSize(24, 24))
        self.abovecolorFrameButton.setMaximumSize(QSize(24, 16777215))
        self.abovecolorFrameButton.setStyleSheet("background-color: white")
        self.abovecolorFrameButton.setFrameShape(QFrame.Panel)
        self.abovecolorFrameButton.setFrameShadow(QFrame.Sunken)
        self.abovecolorFrameButton.setLineWidth(3)

        self.abovecolorLabel = QLabel(self.verticalWidget1)
        self.abovecolorLabel.setEnabled(False)
        self.abovecolorLabel.setFont(Fonts.label_small)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.addWidget(self.abovecolorFrameButton)
        self.horizontalLayout_3.addWidget(self.abovecolorLabel)

        self.belowcolorFrameButton = QFrame(self.verticalWidget1)
        self.belowcolorFrameButton.setEnabled(False)
        self.belowcolorFrameButton.setMinimumSize(QSize(24, 24))
        self.belowcolorFrameButton.setMaximumSize(QSize(24, 16777215))
        self.belowcolorFrameButton.setStyleSheet("background-color: black")
        self.belowcolorFrameButton.setFrameShape(QFrame.Panel)
        self.belowcolorFrameButton.setFrameShadow(QFrame.Sunken)
        self.belowcolorFrameButton.setLineWidth(3)

        self.belowcolorLabel = QLabel(self.verticalWidget1)
        self.belowcolorLabel.setEnabled(False)
        self.belowcolorLabel.setFont(Fonts.label_small)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.addWidget(self.belowcolorFrameButton)
        self.horizontalLayout_4.addWidget(self.belowcolorLabel)

        self.verticalLayout = QVBoxLayout(self.verticalWidget1)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.addWidget(self.colormapSelector)
        self.verticalLayout.addWidget(self.reverseCheckBox)
        self.verticalLayout.addWidget(self.outofrangeCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalLayout_5 = QVBoxLayout(self.colormapGroup)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.addWidget(self.verticalWidget1)

    def create_widgets_group(self, ControlPane_Visuals):
        self.widgetsGroup = FoldingGroupBox(ControlPane_Visuals)
        self.widgetsGroup.setAlignment(Qt.AlignCenter)
        self.verticalWidget_2 = QWidget(self.widgetsGroup)

        self.eyeLabel = QLabel(self.verticalWidget_2)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eyeLabel.sizePolicy().hasHeightForWidth())
        self.eyeLabel.setSizePolicy(sizePolicy)
        self.eyeLabel.setFont(Fonts.icon_normal)
        self.eyeLabel.setAlignment(Qt.AlignCenter)

        self.scalarbarvisCheckBox = QCheckBox(self.verticalWidget_2)
        self.scalarbarvisCheckBox.setChecked(True)

        self.scalarbarmoveCheckBox = QCheckBox(self.verticalWidget_2)
        self.scalarbarmoveCheckBox.setEnabled(False)

        self.orientationmoveCheckBox = QCheckBox(self.verticalWidget_2)
        self.orientationmoveCheckBox.setEnabled(False)

        self.orientationvisCheckBox = QCheckBox(self.verticalWidget_2)
        self.orientationvisCheckBox.setChecked(True)

        self.scalarbarLabel = QLabel(self.verticalWidget_2)
        self.orientationLabel = QLabel(self.verticalWidget_2)

        self.moveLabel = QLabel(self.verticalWidget_2)
        sizePolicy.setHeightForWidth(self.moveLabel.sizePolicy().hasHeightForWidth())
        self.moveLabel.setSizePolicy(sizePolicy)
        self.moveLabel.setFont(Fonts.icon_normal)
        self.moveLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(8)
        self.gridLayout_2.addWidget(self.eyeLabel, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.orientationLabel, 2, 2, 1, 1)
        self.gridLayout_2.addWidget(
            self.scalarbarvisCheckBox, 1, 0, 1, 1, Qt.AlignHCenter
        )
        self.gridLayout_2.addWidget(
            self.scalarbarmoveCheckBox, 1, 1, 1, 1, Qt.AlignHCenter
        )
        self.gridLayout_2.addWidget(
            self.orientationmoveCheckBox, 2, 1, 1, 1, Qt.AlignHCenter
        )
        self.gridLayout_2.addWidget(
            self.orientationvisCheckBox, 2, 0, 1, 1, Qt.AlignHCenter
        )
        self.gridLayout_2.addWidget(self.scalarbarLabel, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.moveLabel, 0, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.verticalLayout_6 = QVBoxLayout(self.widgetsGroup)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.addWidget(self.verticalWidget_2)

    def create_glyphs_group(self, ControlPane_Visuals):
        self.glyphsGroup = FoldingGroupBox(ControlPane_Visuals)
        self.glyphsGroup.setAlignment(Qt.AlignCenter)
        self.verticalWidget_3 = QWidget(self.glyphsGroup)

        self.opacityCheckBox = QCheckBox(self.verticalWidget_3)
        self.opacityCheckBox.setFont(Fonts.label_small)

        self.opacitycontrolFrame = QFrame(self.verticalWidget_3)
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

        self.gridLayout_4 = QGridLayout(self.opacitycontrolFrame)
        self.gridLayout_4.setHorizontalSpacing(2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.addWidget(self.clipped_label, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.maskopacityvalueLabel, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.clipopacitySlider, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.maskopacitySlider, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.masked_label, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.clipopacityvalueLabel, 1, 2, 1, 1)

        self.verticalLayout_8 = QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_8.addWidget(self.opacityCheckBox)
        self.verticalLayout_8.addWidget(self.opacitycontrolFrame)

        self.verticalLayout_7 = QVBoxLayout(self.glyphsGroup)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.addWidget(self.verticalWidget_3)

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
