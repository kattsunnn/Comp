from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt

class ImageController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect_signals()

    def connect_signals(self):
        self.view.addButton.clicked.connect(self.open_image)
        self.view.exeButton.clicked.connect(self.open_image)
        self.view.cancelButton.clicked.connect(self.hide_image_area)

    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.view,
            "画像を開く",
            "",
            "画像ファイル (*.png *.jpg *.jpeg *.bmp *.gif);;すべてのファイル (*)"
        )
        if file_path:
            pixmap = self.model.load_image(file_path)
            scaled = pixmap.scaled(
                self.view.imgLabel.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.view.imgLabel.setPixmap(scaled)
            self.view.sizeLabel.setText(f"{self.model.width} x {self.model.height}")
            self.view.imgArea.show()

    def hide_image_area(self):
        self.view.imgLabel.clear()
        self.view.sizeLabel.setText("")
        self.view.imgArea.hide()
