from PyQt5.QtWidgets import (
    QWidget, 
    QLabel, 
    QPushButton, 
    QVBoxLayout, 
    QHBoxLayout, 
    QStackedWidget, 
    QSpinBox, 
    QCheckBox, 
    QTableWidget, 
    QTableWidgetItem,
    QAbstractItemView,
    QHeaderView,
    QFrame
)
from PyQt5.QtCore import QSize, pyqtSignal
import qtawesome as qta



class editAreaWidget(QFrame):
    sizeChanged = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setObjectName("Area")
        self.setFixedWidth(300)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.pixelButton, self.ratioButton, self.editTabBar = self.createEditTabBar()
        self.widthSpinBox, self.heightSpinBox, self.editTab = self.createEditTab()
        self.widthSpinBox.valueChanged.connect(self.onSizeChanged)
        self.heightSpinBox.valueChanged.connect(self.onSizeChanged)
        self.pixelButton.clicked.connect(lambda: self.editTab.setCurrentIndex(0))
        self.ratioButton.clicked.connect(lambda: self.editTab.setCurrentIndex(1))
        self.addButton = self.createAddButton()
        self.exeButton = self.createExeButton()
        buttonLayout = QHBoxLayout()
        buttonLayout.setContentsMargins(30, 30, 30, 30)
        # buttonLayout.setSpacing(30)
        buttonLayout.addWidget(self.addButton)
        buttonLayout.addWidget(self.exeButton)
        buttonWidget = QWidget()
        buttonWidget.setLayout(buttonLayout)
        layout.addWidget(self.editTabBar)
        layout.addWidget(self.editTab)
        layout.addWidget(buttonWidget)
        self.setLayout(layout)
      
    def createEditTabBar(self):
        pixelButton = QPushButton()
        pixelButton.setObjectName("editTabBarElement")
        pixelButton.setIcon(qta.icon("fa5s.image", color="white"))
        pixelButton.setFixedHeight(60)
        pixelButton.setIconSize(QSize(30,30))
        pixelButton.setToolTip("ピクセルの変更")

        ratioButton = QPushButton()
        ratioButton.setObjectName("editTabBarElement")
        ratioButton.setIcon(qta.icon("fa5s.ruler", color="white"))
        ratioButton.setFixedHeight(60)
        ratioButton.setIconSize(QSize(30,30))
        ratioButton.setToolTip("比率の変更")

        editTabBarLayout = QHBoxLayout()
        editTabBarLayout.setContentsMargins(0, 0, 0, 0)
        editTabBarLayout.setSpacing(0)
        editTabBarLayout.addWidget(pixelButton)
        editTabBarLayout.addWidget(ratioButton)
        editTabBar = QWidget()
        editTabBar.setLayout(editTabBarLayout)
        return pixelButton, ratioButton, editTabBar
    
    def createEditTab(self):
        widthLabel = QLabel("幅（px）")
        widthSpinBox = QSpinBox()
        widthSpinBox.setRange(1, 5000)
        widthSpinBox.setValue(500)
        widthLayout = QHBoxLayout()
        widthLayout.addWidget(widthLabel)
        widthLayout.addWidget(widthSpinBox)

        heightLabel = QLabel("高さ（px）")
        heightSpinBox = QSpinBox()
        heightSpinBox.setRange(1, 5000)
        heightSpinBox.setValue(500)
        heightLayout = QHBoxLayout()
        heightLayout.addWidget(heightLabel)
        heightLayout.addWidget(heightSpinBox)

        ratioCheckBox = QCheckBox("縦横比を維持")
        ratioCheckBox.setChecked(True)

        wholeCheckBox = QCheckBox("全体に適応")
        wholeCheckBox.setChecked(False)

        pixelTabLayout = QVBoxLayout()
        pixelTabLayout.setContentsMargins(30, 30, 30, 30)
        pixelTabLayout.setSpacing(30)
        pixelTabLayout.addLayout(widthLayout)
        pixelTabLayout.addLayout(heightLayout)
        pixelTabLayout.addWidget(ratioCheckBox)
        pixelTabLayout.addWidget(wholeCheckBox)
        pixelTabWidget = QWidget()
        pixelTabWidget.setLayout(pixelTabLayout)

        ratioTable = QTableWidget(4,2)
        ratioTable.verticalHeader().setVisible(False)
        ratioTable.horizontalHeader().setVisible(False)
        ratioTable.setShowGrid(False)
        ratioTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        ratioTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        ratioTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        data = ["25%", "50%", "75%", "カスタム"]

        for row, col in enumerate(data):
            ratioTable.setItem(row, 0, QTableWidgetItem(col))
            ratioTable.setRowHeight(row, 40)

        ratioTabLayout = QVBoxLayout()
        ratioTabLayout.setContentsMargins(30, 30, 30, 30)
        ratioTabLayout.addWidget(ratioTable)
        ratioTabWidget = QWidget()
        ratioTabWidget.setLayout(ratioTabLayout)

        editTab = QStackedWidget()
        editTab.addWidget(pixelTabWidget)
        editTab.addWidget(ratioTabWidget)
        editTab.setCurrentIndex(0)

        return widthSpinBox, heightSpinBox, editTab

    def createAddButton(self):
        addButton = QPushButton()
        addButton.setObjectName("editButton")
        addButton.setIcon(qta.icon("fa5s.plus", color="white"))
        addButton.setFixedSize(60, 60)
        addButton.setIconSize(QSize(30, 30))
        addButton.setToolTip("画像を追加")
        return addButton

    def createExeButton(self):
        exeButton = QPushButton()
        exeButton.setObjectName("editButton")
        exeButton.setIcon(qta.icon("fa5s.edit", color="white"))
        exeButton.setFixedSize(60, 60)
        exeButton.setIconSize(QSize(30, 30))
        exeButton.setToolTip("画像を編集")
        return exeButton

    def onSizeChanged(self):
        width = self.widthSpinBox.value()
        height = self.heightSpinBox.value()
        self.sizeChanged.emit(width, height)

        

        

