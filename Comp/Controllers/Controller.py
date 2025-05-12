from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QSize


class MainController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect_signals()

    def connect_signals(self):
        self.view.editArea.addButton.clicked.connect(self.openImg)
        self.view.editArea.exeButton.clicked.connect(self.saveImg)
        self.view.editArea.sizeChanged.connect(self.updateCompressedSizes)
        # self.view.imgArea.cancelButton.clicked.connect(self.hideImgArea)

    def openImg(self):
        filePaths, _ = QFileDialog.getOpenFileNames(
            self.view,
            "画像を開く",
            "",
            "画像ファイル (*.png *.jpg *.jpeg *.bmp *.gif);;すべてのファイル (*)"
        )
        for path in filePaths:
            if path:
                imgAreaModel = self.model.ImgAreaModel()
                imgAreaModel.loadImg(path)
                self.model.ImgAreasModel.addImgArea(imgAreaModel)
                imgAreaWidget = self.view.addImgArea(imgAreaModel)
                imgAreaWidget.removeRequested.connect(self.removeImgArea)

    def saveImg(self):
        folderPath = QFileDialog.getExistingDirectory(
            self.view,
            "保存先フォルダを選択"
        )
        if not folderPath:
            return
        
        for ImgAreaModel in self.model.ImgAreasModel.imgAreas:
            ImgAreaModel.saveImg(folderPath)

    def removeImgArea(self, widget):
        self.view.removeImgArea(widget)
        self.model.ImgAreasModel.removeImgArea(widget.model)

    def updateCompressedSizes(self, width, height):
        for model in self.model.ImgAreasModel.imgAreas:
            model.compressedSize = QSize(width, height)
            self.view.updateAllImgAreaWidgets()
            