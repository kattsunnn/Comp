import sys
from PyQt5.QtWidgets import QApplication
from Comp.Models.model import MainModel
from Comp.Views.view import MainView
from Comp.Controllers.controller import MainController

if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("Comp\Views\style.qss", "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())

    model = MainModel()
    view = MainView()
    controller = MainController(model, view)
    view.show()
    
    sys.exit(app.exec_())
        