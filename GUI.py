import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QFileDialog,
    QVBoxLayout, QHBoxLayout, QLabel
)
import qtawesome as qta

class ImageLoader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("画像サイズ変更")
        self.resize(960, 540)

        mainLayout = QHBoxLayout()
        mainLayout.setContentsMargins(10, 10, 10, 10)

        # 左側の画像表示領域
        self.imgArea = QWidget()
        self.imgLayout = QVBoxLayout()
        self.imgLayout.setContentsMargins(10, 10, 10, 10)
        self.imgArea.setLayout(self.imgLayout)
        self.imgArea.setObjectName("Area")

        cancelButton = QPushButton()
        plusIcon = qta.icon("fa5s.times", color="white")
        cancelButton.setIcon(plusIcon)
        cancelButton.setIconSize(QSize(30, 30))
        cancelButton.setFixedSize(70, 70)
        cancelButton.setToolTip("画像を削除")
        # cancelButton.clicked.connect(self.openImage)

        self.imgLabel = QLabel()
        self.imgLabel.setAlignment(Qt.AlignCenter)
        self.imgLabel.setFixedSize(200, 200)

        self.imgLayout.addWidget(cancelButton)
        self.imgLayout.addWidget(self.imgLabel)


        self.imgArea.hide()

        editArea = QWidget()
        editLayout = QVBoxLayout()
        editLayout.setContentsMargins(30, 30, 30, 30)
        editArea.setLayout(editLayout)
        editArea.setObjectName("Area")

        buttonLayout = QHBoxLayout()

        addButton = QPushButton()
        plusIcon = qta.icon("fa5s.plus", color="white")
        addButton.setIcon(plusIcon)
        addButton.setIconSize(QSize(30, 30))
        addButton.setFixedSize(70, 70)
        addButton.setToolTip("画像を追加")
        addButton.clicked.connect(self.openImage)
        
        exeButton = QPushButton()
        exeIcon = qta.icon("fa5s.edit", color="white")
        exeButton.setIcon(exeIcon)
        exeButton.setIconSize(QSize(30, 30))
        exeButton.setFixedSize(70, 70)
        exeButton.setToolTip("画像を編集")
        exeButton.clicked.connect(self.openImage)

        buttonLayout.addWidget(addButton)
        buttonLayout.addWidget(exeButton)

        editLayout.addStretch()
        editLayout.addLayout(buttonLayout)

        mainLayout.addWidget(self.imgArea)
        mainLayout.addStretch()  # 上側を空けてボタンを下に
        mainLayout.addWidget(editArea)

        self.setLayout(mainLayout)

    def openImage(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "画像を開く",
            "",
            "画像ファイル (*.png *.jpg *.jpeg *.bmp *.gif);;すべてのファイル (*)"
        )
        if file_path:
            pixmap = QPixmap(file_path)
            # ラベルを表示＋サイズ指定
            self.imgArea.show()
            # 画像をQLabelのサイズに収まるよう、比率を保ってリサイズ
            scaled_pixmap = pixmap.scaled(
                self.imgLabel.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            self.imgLabel.setPixmap(scaled_pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("style.qss", "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())

    window = ImageLoader()
    window.show()
    sys.exit(app.exec_())
