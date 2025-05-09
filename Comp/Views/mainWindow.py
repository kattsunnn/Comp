from PyQt5.QtWidgets import (
    QWidget, 
    QHBoxLayout, 

)
from . import imgArea
from . import editArea


class ImageView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("Comp")
        self.setObjectName("window")
        self.resize(1067, 600)

        self.imgArea = imgArea.ImgAreaWidget()
        self.editArea = editArea.editAreaWidget()

        self.mainLayout = QHBoxLayout()
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.mainLayout.addWidget(self.imgArea)
        self.mainLayout.addStretch()
        self.mainLayout.addWidget(self.editArea)

        self.setLayout(self.mainLayout)
        

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