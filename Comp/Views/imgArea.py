from PyQt5.QtWidgets import (
    QWidget, 
    QLabel, 
    QPushButton, 
    QVBoxLayout, 
    QHBoxLayout, 
    QFrame,
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
import qtawesome as qta
from PyQt5.QtCore import pyqtSignal

class ImgAreaWidget(QFrame):
    removeRequested = pyqtSignal(object)  # 自分自身を引数で送る

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.initUi()

    def initUi(self):
        self.setObjectName("Area")
        self.setFixedSize(250, 300)
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        self.cancelButton = self.createCancelButton()
        self.imgLabel = self.createImgLabel()
        self.originalSizeLabel = self.createOriginalSizeLabel()
        arrowLabel = self.createArrowLabel()
        self.compressedSizeLabel = self.createCompressedSizeLabel()
        sizeLayout = QHBoxLayout()
        sizeLayout.addWidget(self.originalSizeLabel)
        sizeLayout.addWidget(arrowLabel)
        sizeLayout.addWidget(self.compressedSizeLabel)
        sizeWidget = QWidget()
        sizeWidget.setLayout(sizeLayout)
        layout.addWidget(self.cancelButton, alignment=Qt.AlignRight)
        layout.addWidget(self.imgLabel, alignment=Qt.AlignCenter)
        layout.addWidget(sizeWidget, alignment=Qt.AlignCenter)
        self.setLayout(layout)

    def createCancelButton(self):
            cancelButton = QPushButton()
            cancelButton = QPushButton()
            cancelButton.setObjectName("cancelButton")
            cancelButton.setIcon(qta.icon("fa5s.times", color="white"))
            cancelButton.setFixedSize(30, 30)
            cancelButton.setIconSize(QSize(15, 15))
            cancelButton.setToolTip("画像を削除")
            cancelButton.clicked.connect(self.requestRemove)
            return cancelButton
    
    def createImgLabel(self):
        imgLabel = QLabel()
        imgLabel.setFixedSize(200, 200)
        imgLabel.setAlignment(Qt.AlignCenter)
        scaledImg = self.model.img.scaled(
            imgLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        imgLabel.setPixmap(scaledImg)
        return imgLabel
        
    def createOriginalSizeLabel(self):
        originalSizeLabel = QLabel()
        originalSizeLabel.setObjectName("sizeLabel")
        originalSizeLabel.setFixedHeight(30)
        sizeStr = f"{self.model.originalSize.width()}×{self.model.originalSize.height()}"
        originalSizeLabel.setText(sizeStr)
        return originalSizeLabel
    
    def createArrowLabel(self):
        arrowLabel = QLabel()
        arrowIcon = qta.icon('fa5s.arrow-right')
        arrowLabel.setPixmap(arrowIcon.pixmap(15,15))
        return arrowLabel

    def createCompressedSizeLabel(self):
        compressedSizeLabel = QLabel()
        compressedSizeLabel.setObjectName("sizeLabel")
        compressedSizeLabel.setFixedHeight(30)
        sizeStr = f"{self.model.compressedSize.width()}×{self.model.compressedSize.height()}"
        compressedSizeLabel.setText(sizeStr)
        return compressedSizeLabel

    def requestRemove(self):
        self.removeRequested.emit(self)  # ← Controllerに「自分（Widget）を削除して」と通知
        
        
        

