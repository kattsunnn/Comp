from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTabWidget, QTabBar, QStackedWidget, QSpinBox, QCheckBox
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QSize
import qtawesome as qta
from PyQt5.QtWidgets import QSizePolicy

class ImageView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Comp")
        self.setObjectName("window")
        self.resize(1067, 600)

        self.init_ui()

    def init_ui(self):
        # メインレイアウト
        mainLayout = QHBoxLayout()
        mainLayout.setContentsMargins(10, 10, 10, 10)

        # 左側の画像表示領域
        self.imgArea = QWidget()
        self.imgArea.setObjectName("Area")
        self.imgArea.setFixedSize(220, 300)
        self.imgLayout = QVBoxLayout()
        self.imgLayout.setContentsMargins(10, 10, 10, 10)
        self.imgArea.setLayout(self.imgLayout)

        self.cancelButton = QPushButton()
        self.cancelButton.setObjectName("imgButton")
        self.cancelButton.setIcon(qta.icon("fa5s.times", color="white"))
        self.cancelButton.setFixedSize(30, 30)
        self.cancelButton.setIconSize(QSize(15, 15))
        self.cancelButton.setToolTip("画像を削除")

        self.imgLabel = QLabel()
        self.imgLabel.setFixedSize(200, 200)
        self.imgLabel.setAlignment(Qt.AlignCenter)

        self.sizeLabel = QLabel("200 x 200")
        self.imgLabel.setObjectName("imgLabel")
        self.sizeLabel.setFixedHeight(30)

        self.imgLayout.addWidget(self.cancelButton, alignment=Qt.AlignRight)
        self.imgLayout.addWidget(self.imgLabel, alignment=Qt.AlignCenter)
        self.imgLayout.addWidget(self.sizeLabel, alignment=Qt.AlignCenter)
        self.imgArea.hide()

        # 右側の操作エリア

        self.pixelButton = QPushButton()
        self.pixelButton.setObjectName("editTabBarElement")
        self.pixelButton.setIcon(qta.icon("fa5s.image", color="white"))
        # self.pixelButton.setFixedSize(100,60)
        self.pixelButton.setFixedHeight(60)
        self.pixelButton.setIconSize(QSize(30,30))
        self.pixelButton.setToolTip("ピクセルの変更")

        self.ratioButton = QPushButton()
        self.ratioButton.setObjectName("editTabBarElement")
        self.ratioButton.setIcon(qta.icon("fa5s.ruler", color="white"))
        self.ratioButton.setFixedHeight(60)
        self.ratioButton.setIconSize(QSize(30,30))
        self.ratioButton.setToolTip("比率の変更")

        editTabBarLayout = QHBoxLayout()
        editTabBarLayout.setContentsMargins(0, 0, 0, 0)
        editTabBarLayout.setSpacing(0)
        editTabBarLayout.addWidget(self.pixelButton)
        editTabBarLayout.addWidget(self.ratioButton)   

        widthLabel = QLabel("幅（px）")
        widthSpinBox = QSpinBox()
        widthSpinBox.setRange(0, 100)
        widthSpinBox.setValue(50)
        widthLayout = QHBoxLayout()
        widthLayout.addWidget(widthLabel)
        widthLayout.addWidget(widthSpinBox)

        heightLabel = QLabel("高さ（px）")
        heightSpinBox = QSpinBox()
        heightSpinBox.setRange(0, 100)
        heightSpinBox.setValue(50)
        heightLayout = QHBoxLayout()
        heightLayout.addWidget(heightLabel)
        heightLayout.addWidget(heightSpinBox)

        ratioCheckBox = QCheckBox("縦横比を維持")
        ratioCheckBox.setChecked(True)

        pixelTabLayout = QVBoxLayout()
        pixelTabLayout.setContentsMargins(30, 30, 30, 30)
        pixelTabLayout.setSpacing(30)
        pixelTabLayout.addLayout(widthLayout)
        pixelTabLayout.addLayout(heightLayout)
        pixelTabLayout.addWidget(ratioCheckBox)
        pixelTabWidget = QWidget()
        pixelTabWidget.setLayout(pixelTabLayout)


        ratioTabLayout = QHBoxLayout()

        editTab = QStackedWidget()
        editTab.addWidget(pixelTabWidget)


        self.addButton = QPushButton()
        self.addButton.setObjectName("editButton")
        self.addButton.setIcon(qta.icon("fa5s.plus", color="white"))
        self.addButton.setFixedSize(60, 60)
        self.addButton.setIconSize(QSize(30, 30))
        self.addButton.setToolTip("画像を追加")

        self.exeButton = QPushButton()
        self.exeButton.setObjectName("editButton")
        self.exeButton.setIcon(qta.icon("fa5s.edit", color="white"))
        self.exeButton.setFixedSize(60, 60)
        self.exeButton.setIconSize(QSize(30, 30))
        self.exeButton.setToolTip("画像を編集")

        buttonLayout = QHBoxLayout()
        buttonLayout.setContentsMargins(30, 30, 30, 30)
        # buttonLayout.setSpacing(30)
        buttonLayout.addWidget(self.addButton)
        buttonLayout.addWidget(self.exeButton)

        editLayout = QVBoxLayout()
        editLayout.setContentsMargins(0, 0, 0, 0)
        editLayout.addLayout(editTabBarLayout)
        editLayout.addWidget(editTab)
        editLayout.addStretch()
        editLayout.addLayout(buttonLayout)
        editArea = QWidget()
        editArea.setFixedWidth(300)
        editArea.setObjectName("Area")
        editArea.setLayout(editLayout)

        mainLayout.addWidget(self.imgArea)
        mainLayout.addStretch()
        mainLayout.addWidget(editArea)

        self.setLayout(mainLayout)


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