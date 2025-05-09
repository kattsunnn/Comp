from PyQt5.QtWidgets import (
    QWidget, 
    QLabel, 
    QPushButton, 
    QVBoxLayout, 
    QHBoxLayout, 
    QTabWidget, 
    QTabBar, 
    QStackedWidget, 
    QSpinBox, 
    QCheckBox, 
    QTableWidget, 
    QTableWidgetItem,
    QAbstractItemView,
    QHeaderView,
    QFrame
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QSize
import qtawesome as qta
from PyQt5.QtWidgets import QSizePolicy

class ImgAreaWidget(QFrame):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setObjectName("Area")
        self.setFixedSize(220, 300)
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        self.cancelButton = self.createCancelButton()
        self.imgLabel = self.createImgLabel()
        self.sizeWidget = self.createSizeWidget()
        layout.addWidget(self.cancelButton, alignment=Qt.AlignRight)
        layout.addWidget(self.imgLabel, alignment=Qt.AlignCenter)
        layout.addWidget(self.sizeWidget, alignment=Qt.AlignCenter)
        self.setLayout(layout)

    def createCancelButton(self):
            cancelButton = QPushButton()
            cancelButton = QPushButton()
            cancelButton.setObjectName("cancelButton")
            cancelButton.setIcon(qta.icon("fa5s.times", color="white"))
            cancelButton.setFixedSize(30, 30)
            cancelButton.setIconSize(QSize(15, 15))
            cancelButton.setToolTip("画像を削除")
            return cancelButton
    
    def createImgLabel(self):
        imgLabel = QLabel()
        imgLabel.setFixedSize(200, 200)
        imgLabel.setAlignment(Qt.AlignCenter)
        return imgLabel
    
    def createSizeWidget(self):
        sizeBeforeLabel = QLabel()
        sizeBeforeLabel.setObjectName("sizeLabel")
        sizeBeforeLabel.setFixedHeight(30)
        arrowLabel = QLabel()
        arrowIcon = qta.icon('fa5s.arrow-right')
        arrowLabel.setPixmap(arrowIcon.pixmap(15,15))
        sizeAfterLabel = QLabel()
        sizeAfterLabel.setObjectName("sizeLabel")
        sizeAfterLabel.setFixedHeight(30)
        sizeLayout = QHBoxLayout()
        sizeLayout.addWidget(sizeBeforeLabel)
        sizeLayout.addWidget(arrowLabel)
        sizeLayout.addWidget(sizeAfterLabel)
        sizeWidget = QWidget()
        sizeWidget.setLayout(sizeLayout)
        return sizeWidget