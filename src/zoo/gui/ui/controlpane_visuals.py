# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'controlpane_visuals.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

from zoo.gui.ui.foldinggroupbox import FoldingGroupBox

class Ui_ControlPane_Visuals(object):
    def setupUi(self, ControlPane_Visuals):
        if not ControlPane_Visuals.objectName():
            ControlPane_Visuals.setObjectName(u"ControlPane_Visuals")
        ControlPane_Visuals.resize(200, 630)
        self.gridLayout = QGridLayout(ControlPane_Visuals)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.controls = QVBoxLayout()
        self.controls.setObjectName(u"controls")
        self.viewportGroup = FoldingGroupBox(ControlPane_Visuals)
        self.viewportGroup.setObjectName(u"viewportGroup")
        self.viewportGroup.setEnabled(True)
        self.viewportGroup.setAlignment(Qt.AlignCenter)
        self.verticalLayout_4 = QVBoxLayout(self.viewportGroup)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget = QWidget(self.viewportGroup)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalLayout_2 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widthLineEdit = QLineEdit(self.verticalWidget)
        self.widthLineEdit.setObjectName(u"widthLineEdit")
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(8)
        self.widthLineEdit.setFont(font)

        self.gridLayout_3.addWidget(self.widthLineEdit, 1, 0, 1, 1)

        self.heightLineEdit = QLineEdit(self.verticalWidget)
        self.heightLineEdit.setObjectName(u"heightLineEdit")
        self.heightLineEdit.setFont(font)

        self.gridLayout_3.addWidget(self.heightLineEdit, 1, 2, 1, 1)

        self.label = QLabel(self.verticalWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(8)
        self.label.setFont(font1)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.verticalWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bgcolorFrameButton = QFrame(self.verticalWidget)
        self.bgcolorFrameButton.setObjectName(u"bgcolorFrameButton")
        self.bgcolorFrameButton.setMinimumSize(QSize(24, 24))
        self.bgcolorFrameButton.setMaximumSize(QSize(24, 16777215))
        self.bgcolorFrameButton.setStyleSheet(u"background-color: red")
        self.bgcolorFrameButton.setFrameShape(QFrame.Panel)
        self.bgcolorFrameButton.setFrameShadow(QFrame.Sunken)
        self.bgcolorFrameButton.setLineWidth(3)

        self.horizontalLayout_2.addWidget(self.bgcolorFrameButton)

        self.bgcolorLabel = QLabel(self.verticalWidget)
        self.bgcolorLabel.setObjectName(u"bgcolorLabel")
        self.bgcolorLabel.setFont(font1)

        self.horizontalLayout_2.addWidget(self.bgcolorLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addWidget(self.verticalWidget)


        self.controls.addWidget(self.viewportGroup)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.controls.addItem(self.verticalSpacer_7)

        self.colormapGroup = FoldingGroupBox(ControlPane_Visuals)
        self.colormapGroup.setObjectName(u"colormapGroup")
        self.colormapGroup.setEnabled(True)
        self.colormapGroup.setAlignment(Qt.AlignCenter)
        self.verticalLayout_5 = QVBoxLayout(self.colormapGroup)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget1 = QWidget(self.colormapGroup)
        self.verticalWidget1.setObjectName(u"verticalWidget1")
        self.verticalLayout = QVBoxLayout(self.verticalWidget1)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.colormapSelector = QComboBox(self.verticalWidget1)
        self.colormapSelector.setObjectName(u"colormapSelector")
        self.colormapSelector.setEditable(True)

        self.verticalLayout.addWidget(self.colormapSelector)

        self.reverseCheckBox = QCheckBox(self.verticalWidget1)
        self.reverseCheckBox.setObjectName(u"reverseCheckBox")

        self.verticalLayout.addWidget(self.reverseCheckBox)

        self.outofrangeCheckBox = QCheckBox(self.verticalWidget1)
        self.outofrangeCheckBox.setObjectName(u"outofrangeCheckBox")

        self.verticalLayout.addWidget(self.outofrangeCheckBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.abovecolorFrameButton = QFrame(self.verticalWidget1)
        self.abovecolorFrameButton.setObjectName(u"abovecolorFrameButton")
        self.abovecolorFrameButton.setEnabled(False)
        self.abovecolorFrameButton.setMinimumSize(QSize(24, 24))
        self.abovecolorFrameButton.setMaximumSize(QSize(24, 16777215))
        self.abovecolorFrameButton.setStyleSheet(u"background-color: white")
        self.abovecolorFrameButton.setFrameShape(QFrame.Panel)
        self.abovecolorFrameButton.setFrameShadow(QFrame.Sunken)
        self.abovecolorFrameButton.setLineWidth(3)

        self.horizontalLayout_3.addWidget(self.abovecolorFrameButton)

        self.abovecolorLabel = QLabel(self.verticalWidget1)
        self.abovecolorLabel.setObjectName(u"abovecolorLabel")
        self.abovecolorLabel.setEnabled(False)
        self.abovecolorLabel.setFont(font1)

        self.horizontalLayout_3.addWidget(self.abovecolorLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.belowcolorFrameButton = QFrame(self.verticalWidget1)
        self.belowcolorFrameButton.setObjectName(u"belowcolorFrameButton")
        self.belowcolorFrameButton.setEnabled(False)
        self.belowcolorFrameButton.setMinimumSize(QSize(24, 24))
        self.belowcolorFrameButton.setMaximumSize(QSize(24, 16777215))
        self.belowcolorFrameButton.setStyleSheet(u"background-color: black")
        self.belowcolorFrameButton.setFrameShape(QFrame.Panel)
        self.belowcolorFrameButton.setFrameShadow(QFrame.Sunken)
        self.belowcolorFrameButton.setLineWidth(3)

        self.horizontalLayout_4.addWidget(self.belowcolorFrameButton)

        self.belowcolorLabel = QLabel(self.verticalWidget1)
        self.belowcolorLabel.setObjectName(u"belowcolorLabel")
        self.belowcolorLabel.setEnabled(False)
        self.belowcolorLabel.setFont(font1)

        self.horizontalLayout_4.addWidget(self.belowcolorLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_5.addWidget(self.verticalWidget1)


        self.controls.addWidget(self.colormapGroup)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.controls.addItem(self.verticalSpacer_8)

        self.widgetsGroup = FoldingGroupBox(ControlPane_Visuals)
        self.widgetsGroup.setObjectName(u"widgetsGroup")
        self.widgetsGroup.setEnabled(True)
        self.widgetsGroup.setAlignment(Qt.AlignCenter)
        self.verticalLayout_6 = QVBoxLayout(self.widgetsGroup)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget_2 = QWidget(self.widgetsGroup)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(8)
        self.eyeLabel = QLabel(self.verticalWidget_2)
        self.eyeLabel.setObjectName(u"eyeLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eyeLabel.sizePolicy().hasHeightForWidth())
        self.eyeLabel.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Segoe Fluent Icons"])
        font2.setPointSize(14)
        self.eyeLabel.setFont(font2)
        self.eyeLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.eyeLabel, 0, 0, 1, 1)

        self.orientationLabel = QLabel(self.verticalWidget_2)
        self.orientationLabel.setObjectName(u"orientationLabel")

        self.gridLayout_2.addWidget(self.orientationLabel, 2, 2, 1, 1)

        self.scalarbarvisCheckBox = QCheckBox(self.verticalWidget_2)
        self.scalarbarvisCheckBox.setObjectName(u"scalarbarvisCheckBox")
        self.scalarbarvisCheckBox.setChecked(True)

        self.gridLayout_2.addWidget(self.scalarbarvisCheckBox, 1, 0, 1, 1, Qt.AlignHCenter)

        self.scalarbarmoveCheckBox = QCheckBox(self.verticalWidget_2)
        self.scalarbarmoveCheckBox.setObjectName(u"scalarbarmoveCheckBox")
        self.scalarbarmoveCheckBox.setEnabled(False)

        self.gridLayout_2.addWidget(self.scalarbarmoveCheckBox, 1, 1, 1, 1, Qt.AlignHCenter)

        self.orientationmoveCheckBox = QCheckBox(self.verticalWidget_2)
        self.orientationmoveCheckBox.setObjectName(u"orientationmoveCheckBox")
        self.orientationmoveCheckBox.setEnabled(False)

        self.gridLayout_2.addWidget(self.orientationmoveCheckBox, 2, 1, 1, 1, Qt.AlignHCenter)

        self.orientationvisCheckBox = QCheckBox(self.verticalWidget_2)
        self.orientationvisCheckBox.setObjectName(u"orientationvisCheckBox")
        self.orientationvisCheckBox.setChecked(True)

        self.gridLayout_2.addWidget(self.orientationvisCheckBox, 2, 0, 1, 1, Qt.AlignHCenter)

        self.scalarbarLabel = QLabel(self.verticalWidget_2)
        self.scalarbarLabel.setObjectName(u"scalarbarLabel")

        self.gridLayout_2.addWidget(self.scalarbarLabel, 1, 2, 1, 1)

        self.moveLabel = QLabel(self.verticalWidget_2)
        self.moveLabel.setObjectName(u"moveLabel")
        sizePolicy.setHeightForWidth(self.moveLabel.sizePolicy().hasHeightForWidth())
        self.moveLabel.setSizePolicy(sizePolicy)
        self.moveLabel.setFont(font2)
        self.moveLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.moveLabel, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)


        self.verticalLayout_6.addWidget(self.verticalWidget_2)


        self.controls.addWidget(self.widgetsGroup)

        self.verticalSpacer_9 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.controls.addItem(self.verticalSpacer_9)

        self.glyphsGroup = FoldingGroupBox(ControlPane_Visuals)
        self.glyphsGroup.setObjectName(u"glyphsGroup")
        self.glyphsGroup.setEnabled(True)
        self.glyphsGroup.setAlignment(Qt.AlignCenter)
        self.verticalLayout_7 = QVBoxLayout(self.glyphsGroup)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget_3 = QWidget(self.glyphsGroup)
        self.verticalWidget_3.setObjectName(u"verticalWidget_3")
        self.verticalLayout_8 = QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(4, 4, 4, 4)
        self.opacityCheckBox = QCheckBox(self.verticalWidget_3)
        self.opacityCheckBox.setObjectName(u"opacityCheckBox")
        self.opacityCheckBox.setFont(font1)

        self.verticalLayout_8.addWidget(self.opacityCheckBox)

        self.opacitycontrolFrame = QFrame(self.verticalWidget_3)
        self.opacitycontrolFrame.setObjectName(u"opacitycontrolFrame")
        self.opacitycontrolFrame.setEnabled(False)
        self.gridLayout_4 = QGridLayout(self.opacitycontrolFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.orientationLabel_2 = QLabel(self.opacitycontrolFrame)
        self.orientationLabel_2.setObjectName(u"orientationLabel_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(4)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.orientationLabel_2.sizePolicy().hasHeightForWidth())
        self.orientationLabel_2.setSizePolicy(sizePolicy1)
        self.orientationLabel_2.setFont(font1)

        self.gridLayout_4.addWidget(self.orientationLabel_2, 1, 0, 1, 1)

        self.maskopacityvalueLabel = QLabel(self.opacitycontrolFrame)
        self.maskopacityvalueLabel.setObjectName(u"maskopacityvalueLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.maskopacityvalueLabel.sizePolicy().hasHeightForWidth())
        self.maskopacityvalueLabel.setSizePolicy(sizePolicy2)
        self.maskopacityvalueLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.maskopacityvalueLabel, 0, 2, 1, 1)

        self.clipopacitySlider = QSlider(self.opacitycontrolFrame)
        self.clipopacitySlider.setObjectName(u"clipopacitySlider")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(9)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.clipopacitySlider.sizePolicy().hasHeightForWidth())
        self.clipopacitySlider.setSizePolicy(sizePolicy3)
        self.clipopacitySlider.setMaximum(20)
        self.clipopacitySlider.setSingleStep(1)
        self.clipopacitySlider.setPageStep(4)
        self.clipopacitySlider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.clipopacitySlider, 1, 1, 1, 1)

        self.maskopacitySlider = QSlider(self.opacitycontrolFrame)
        self.maskopacitySlider.setObjectName(u"maskopacitySlider")
        sizePolicy3.setHeightForWidth(self.maskopacitySlider.sizePolicy().hasHeightForWidth())
        self.maskopacitySlider.setSizePolicy(sizePolicy3)
        self.maskopacitySlider.setMouseTracking(False)
        self.maskopacitySlider.setMaximum(20)
        self.maskopacitySlider.setSingleStep(1)
        self.maskopacitySlider.setPageStep(4)
        self.maskopacitySlider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.maskopacitySlider, 0, 1, 1, 1)

        self.scalarbarLabel_2 = QLabel(self.opacitycontrolFrame)
        self.scalarbarLabel_2.setObjectName(u"scalarbarLabel_2")
        sizePolicy1.setHeightForWidth(self.scalarbarLabel_2.sizePolicy().hasHeightForWidth())
        self.scalarbarLabel_2.setSizePolicy(sizePolicy1)
        self.scalarbarLabel_2.setFont(font1)

        self.gridLayout_4.addWidget(self.scalarbarLabel_2, 0, 0, 1, 1)

        self.clipopacityvalueLabel = QLabel(self.opacitycontrolFrame)
        self.clipopacityvalueLabel.setObjectName(u"clipopacityvalueLabel")
        sizePolicy2.setHeightForWidth(self.clipopacityvalueLabel.sizePolicy().hasHeightForWidth())
        self.clipopacityvalueLabel.setSizePolicy(sizePolicy2)
        self.clipopacityvalueLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.clipopacityvalueLabel, 1, 2, 1, 1)


        self.verticalLayout_8.addWidget(self.opacitycontrolFrame)


        self.verticalLayout_7.addWidget(self.verticalWidget_3)


        self.controls.addWidget(self.glyphsGroup)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.controls.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.controls, 0, 0, 1, 1)


        self.retranslateUi(ControlPane_Visuals)

        QMetaObject.connectSlotsByName(ControlPane_Visuals)
    # setupUi

    def retranslateUi(self, ControlPane_Visuals):
        ControlPane_Visuals.setWindowTitle(QCoreApplication.translate("ControlPane_Visuals", u"Form", None))
        self.viewportGroup.setTitle(QCoreApplication.translate("ControlPane_Visuals", u"Viewport", None))
        self.label.setText(QCoreApplication.translate("ControlPane_Visuals", u"Resolution", None))
        self.label_2.setText(QCoreApplication.translate("ControlPane_Visuals", u"X", None))
        self.bgcolorLabel.setText(QCoreApplication.translate("ControlPane_Visuals", u"Background Color", None))
        self.colormapGroup.setTitle(QCoreApplication.translate("ControlPane_Visuals", u"Colormap", None))
        self.reverseCheckBox.setText(QCoreApplication.translate("ControlPane_Visuals", u"Reverse colormap", None))
        self.outofrangeCheckBox.setText(QCoreApplication.translate("ControlPane_Visuals", u"Out-of-range colors", None))
        self.abovecolorLabel.setText(QCoreApplication.translate("ControlPane_Visuals", u"Above-Range Color", None))
        self.belowcolorLabel.setText(QCoreApplication.translate("ControlPane_Visuals", u"Below-Range Color", None))
        self.widgetsGroup.setTitle(QCoreApplication.translate("ControlPane_Visuals", u"Widgets", None))
        self.eyeLabel.setText(QCoreApplication.translate("ControlPane_Visuals", u"\ue7b3", None))
        self.orientationLabel.setText(QCoreApplication.translate("ControlPane_Visuals", u"Orientation", None))
        self.scalarbarvisCheckBox.setText("")
        self.scalarbarmoveCheckBox.setText("")
        self.orientationmoveCheckBox.setText("")
        self.orientationvisCheckBox.setText("")
        self.scalarbarLabel.setText(QCoreApplication.translate("ControlPane_Visuals", u"Scalar bar", None))
        self.moveLabel.setText(QCoreApplication.translate("ControlPane_Visuals", u"\ue759", None))
        self.glyphsGroup.setTitle(QCoreApplication.translate("ControlPane_Visuals", u"Glyphs", None))
#if QT_CONFIG(tooltip)
        self.opacityCheckBox.setToolTip(QCoreApplication.translate("ControlPane_Visuals", u"WARNING: Seriously impacts performance!", None))
#endif // QT_CONFIG(tooltip)
        self.opacityCheckBox.setText(QCoreApplication.translate("ControlPane_Visuals", u"Opacity \u26a0", None))
#if QT_CONFIG(tooltip)
        self.opacitycontrolFrame.setToolTip(QCoreApplication.translate("ControlPane_Visuals", u"Clipped opacity overrides masked opacity", None))
#endif // QT_CONFIG(tooltip)
        self.orientationLabel_2.setText(QCoreApplication.translate("ControlPane_Visuals", u"<html><head/><body><p align=\"right\">Clipped</p></body></html>", None))
        self.maskopacityvalueLabel.setText(QCoreApplication.translate("ControlPane_Visuals", u"100%", None))
        self.scalarbarLabel_2.setText(QCoreApplication.translate("ControlPane_Visuals", u"<html><head/><body><p align=\"right\">Masked</p></body></html>", None))
        self.clipopacityvalueLabel.setText(QCoreApplication.translate("ControlPane_Visuals", u"0%", None))
    # retranslateUi

Error: controlpane_visuals.ui: Warning: The name 'verticalWidget' (QWidget) is already in use, defaulting to 'verticalWidget1'.

while executing 'C:\Users\hallrc\AppData\Local\Continuum\anaconda3\envs\zoodev2\Lib\site-packages\PySide6\uic -g python controlpane_visuals.ui'
