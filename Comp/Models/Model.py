from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os
from PyQt5.QtWidgets import (
    QWidget, 
)

class MainModel:
    def __init__(self):
        self.ImgAreaModel = ImgAreaModel
        self.ImgAreasModel = ImgAreasModel()

class ImgAreaModel:
    def __init__(self):
        self.img: QPixmap = None
        self.imgName: str = None
        self.originalSize: QSize = None
        self.compressedSize: QSize = None

    def loadImg(self, path):
        img = QPixmap(path)
        if img.isNull():
            raise ValueError("画像が読み込めませんでした")

        self.img = img
        self.imgName = os.path.basename(path)  # ファイル名だけを取得
        self.originalSize = img.size()
        self.compressedSize = self.originalSize

    def saveImg(self, folderPath):
        savePath = os.path.join(folderPath, self.imgName)
        base, _ = os.path.splitext(savePath)
        savePathJPG = base + ".jpg"
        if not self.img.save(savePathJPG, "jpg"):
            raise IOError(f"画像の保存に失敗しました: {savePath}")

class ImgAreasModel:
    def __init__(self):
        self.imgAreas = []

    def addImgArea(self, imgArea:ImgAreaModel):
        self.imgAreas.append(imgArea)

    def removeImgArea(self, imgArea: ImgAreaModel):
        if imgArea in self.imgAreas:
            self.imgAreas.remove(imgArea)
