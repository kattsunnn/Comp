class ImageModel:
    def __init__(self):
        self.file_path = ""
        self.width = 0
        self.height = 0

    def load_image(self, path):
        from PyQt5.QtGui import QPixmap
        pixmap = QPixmap(path)
        self.file_path = path
        self.width = pixmap.width()
        self.height = pixmap.height()
        return pixmap