from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ImgAreaModel:
    def __init__(self):
        self.img: QPixmap = None
        self.originalSize: QSize = None
        self.compressedSize: QSize = None

    def loadImg(self, path):
        img = QPixmap(path)
        if img.isNull():
            raise ValueError("画像が読み込めませんでした")

        self.img = img
        self.originalSize = img.size()
        self.compressedSize = self.originalSize
    