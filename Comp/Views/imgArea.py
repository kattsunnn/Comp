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

class ImgAreaWidget(QFrame):
    def __init__(self):
        super().__init__()
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
            return cancelButton
    
    def createImgLabel(self):
        imgLabel = QLabel()
        imgLabel.setFixedSize(200, 200)
        imgLabel.setAlignment(Qt.AlignCenter)
        return imgLabel
        
    def createOriginalSizeLabel(self):
        originalSizeLabel = QLabel()
        originalSizeLabel.setObjectName("sizeLabel")
        originalSizeLabel.setFixedHeight(30)
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
        return compressedSizeLabel
    
    def setImgArea(self, img: QPixmap, imgSize: QSize):
        scaledImg = img.scaled(
            self.imgLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.imgLabel.setPixmap(scaledImg)
        sizeStr = f"{imgSize.width()}×{imgSize.height()}"
        self.originalSizeLabel.setText(sizeStr)
        self.compressedSizeLabel.setText(sizeStr)

