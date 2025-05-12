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
        self.selected = False
        self.initUi()

    def initUi(self):
        self.cancelButton = self.createCancelButton()
        self.imgLabel = self.createImgLabel()
        self.imgNameLabel = self.createImgNameLabel()
        self.originalSizeLabel = self.createOriginalSizeLabel()
        arrowLabel = self.createArrowLabel()
        self.compressedSizeLabel = self.createCompressedSizeLabel()
        sizeLayout = QHBoxLayout()
        sizeLayout.setContentsMargins(0, 0, 0, 0)  # ← マージンを完全になくす
        sizeLayout.setSpacing(5)  # ← 必要なら間の余白を微調整（お好みで0〜5程度）
        sizeLayout.addWidget(self.originalSizeLabel)
        sizeLayout.addWidget(arrowLabel)
        sizeLayout.addWidget(self.compressedSizeLabel)
        sizeWidget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)
        sizeWidget.setLayout(sizeLayout)
        layout.addWidget(self.cancelButton, alignment=Qt.AlignRight)
        layout.addWidget(self.imgLabel, alignment=Qt.AlignCenter)
        layout.addWidget(self.imgNameLabel, alignment=Qt.AlignCenter)
        layout.addWidget(sizeWidget, alignment=Qt.AlignCenter)
        self.setObjectName("imgArea")
        self.setFixedSize(200, 260)
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
        imgLabel.setFixedSize(160, 160)
        imgLabel.setAlignment(Qt.AlignCenter)
        scaledImg = self.model.img.scaled(
            imgLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        imgLabel.setPixmap(scaledImg)
        return imgLabel
        
    def createImgNameLabel(self):
        imgNameLabel = QLabel()
        imgNameLabel.setObjectName("imgNameLabel")
        imgNameLabel.setFixedHeight(20)
        imgNameLabel.setText(self.model.imgName)
        return imgNameLabel

    def createOriginalSizeLabel(self):
        originalSizeLabel = QLabel()
        originalSizeLabel.setObjectName("sizeLabel")
        size = self.model.originalSize
        sizeStr = f"{size.width()}×{size.height()}"
        originalSizeLabel.setText(sizeStr)
        return originalSizeLabel
    
    def createArrowLabel(self):
        arrowLabel = QLabel()
        arrowIcon = qta.icon('fa5s.arrow-right')
        arrowLabel.setPixmap(arrowIcon.pixmap(10,10))
        return arrowLabel

    def createCompressedSizeLabel(self):
        compressedSizeLabel = QLabel()
        compressedSizeLabel.setObjectName("sizeLabel")
        compressedSizeLabel.setFixedHeight(20)
        size = self.model.compressedSize
        sizeStr = f"{size.width()}×{size.height()}"
        compressedSizeLabel.setText(sizeStr)
        return compressedSizeLabel
    
    def updateCompressedSizeLabel(self):
        size = self.model.compressedSize
        sizeStr = f"{size.width()}×{size.height()}"
        self.compressedSizeLabel.setText(sizeStr)

    def requestRemove(self):
        self.removeRequested.emit(self)  # ← Controllerに「自分（Widget）を削除して」と通知
        
    def mousePressEvent(self, event):
        self.selected = not self.selected
        if self.selected:
            self.setObjectName("imgAreaSelected")
        else:
            self.setObjectName("imgArea")
        self.style().unpolish(self)      
        self.style().polish(self)
        super().mousePressEvent(event)

    

