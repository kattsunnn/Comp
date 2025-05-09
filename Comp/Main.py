import sys
from PyQt5.QtWidgets import QApplication
from Models.Model import ImgAreaModel
from Views.mainWindow import ImageView
from Controllers.Controller import ImageController

if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("style.qss", "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())

    model = ImgAreaModel()
    view = ImageView()
    controller = ImageController(model, view)

    view.show()
    sys.exit(app.exec_())
    