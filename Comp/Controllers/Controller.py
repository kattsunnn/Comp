from PyQt5.QtWidgets import QFileDialog



class ImageController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect_signals()

    def connect_signals(self):
        self.view.editArea.addButton.clicked.connect(self.openImg)
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
                self.model.loadImg(path)
                self.view.addImgArea(self.model.img, self.model.originalSize)
        
        


    def hideImgArea(self):
        self.view.imgArea.hide()
    
    def showImgArea(self):
        self.view.imgArea.show()
