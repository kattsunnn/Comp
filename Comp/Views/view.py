from PyQt5.QtWidgets import (
    QWidget, 
    QHBoxLayout, 
    QVBoxLayout,
    QGridLayout,
    QScrollArea
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from .imgArea import ImgAreaWidget
from . import editArea


class MainView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("Comp")
        self.setObjectName("window")
        self.resize(1067, 600)

        self.imgAreas = []
        self.imgColumns = 5
        self.imgAreaWidget = QWidget()
        self.imgAreaGridLayout = QGridLayout()
        self.imgAreaGridLayout.setContentsMargins(0, 0, 0, 0)
        self.imgAreaWidget.setLayout(self.imgAreaGridLayout)
        self.editArea = editArea.editAreaWidget()

        self.mainLayout = QHBoxLayout()
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.mainLayout.addWidget(self.imgAreaWidget)
        self.mainLayout.addStretch()
        self.mainLayout.addWidget(self.editArea)

        self.setLayout(self.mainLayout)

    def addImgArea(self, model):
        imgAreaWidget = ImgAreaWidget(model)
        self.imgAreas.append(imgAreaWidget)

        index = len(self.imgAreas) - 1
        row = index // self.imgColumns
        col = index % self.imgColumns

        self.imgAreaGridLayout.addWidget(imgAreaWidget, row, col)
        return imgAreaWidget
    
    def removeImgArea(self, widget):
        if widget in self.imgAreas:
            self.imgAreas.remove(widget)
        self.imgAreaGridLayout.removeWidget(widget)
        widget.setParent(None)
        widget.deleteLater()
        self.rebuildImgGridArea()
    
    def rebuildImgGridArea(self):
        for i in reversed(range(self.imgAreaGridLayout.count())):
            item = self.imgAreaGridLayout.itemAt(i)
            w = item.widget()
            if w:
                self.imgAreaGridLayout.removeWidget(w)
                w.setParent(None)
        for i, widget in enumerate(self.imgAreas):
            row = i // self.imgColumns
            col = i % self.imgColumns
            self.imgAreaGridLayout.addWidget(widget, row, col)


    def updateAllImgAreaWidgets(self):
        for widget in self.imgAreas:
            widget.updateCompressedSizeLabel()

# # QTabBarを自前で用意
# tabBar = QTabBar()
# pixelIcon = qta.icon("fa5s.image", color="white")   # ピクセルアイコン
# ratioIcon = qta.icon("fa5s.ruler", color="white")   # 比率アイコン
# tabBar.setIconSize(QSize(30, 30))
# tabBar.addTab(pixelIcon, "")
# tabBar.addTab(ratioIcon, "")
# tabBar.setExpanding(True)  # 均等に広げる
# # tabBar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

# # QStackedWidget（タブの中身）を自前で用意
# self.stacked_widget = QStackedWidget()
# self.stacked_widget.addWidget(QLabel("ピクセルの設定画面"))
# self.stacked_widget.addWidget(QLabel("比率の設定画面"))