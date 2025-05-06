        # 左側の画像表示領域
        self.imgArea = QWidget()
        self.imgLayout = QVBoxLayout()
        self.imgLayout.setContentsMargins(10, 10, 10, 10)

        self.imgLabel = QLabel()
        self.imgLabel.setAlignment(Qt.AlignCenter)
        self.imgLabel.setFixedSize(200, 200)
        
        self.imgLayout.addWidget(self.imgLabel)

        self.imgArea.setLayout(self.imgLayout)
        self.imgArea.hide()