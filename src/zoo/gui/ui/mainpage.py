from PySide6.QtCore import QMetaObject, QSize
from PySide6.QtWidgets import QFrame, QHBoxLayout, QSizePolicy


class Ui_MainPage(object):
    def setupUi(self, MainPage):
        if not MainPage.objectName():
            MainPage.setObjectName("MainPage")
        MainPage.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(MainPage)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.viewport = QFrame(MainPage)
        self.viewport.setObjectName("viewport")
        sizePolicy = QSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewport.sizePolicy().hasHeightForWidth())
        self.viewport.setSizePolicy(sizePolicy)
        self.viewport.setMinimumSize(QSize(300, 0))
        self.viewport.setFrameShape(QFrame.StyledPanel)
        self.viewport.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.viewport)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.viewport)

        self.line = QFrame(MainPage)
        self.line.setObjectName("line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QFrame.VLine)

        self.horizontalLayout.addWidget(self.line)

        self.retranslateUi(MainPage)

        QMetaObject.connectSlotsByName(MainPage)
