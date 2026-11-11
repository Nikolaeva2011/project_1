from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtCore import Qt
from test_window import TestWindow
from dictionary import Dictionary
from statistics_window import StatisticsWindow


class MyNotes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('WordWise Mini')
        self.resize(500, 550)
        self.setFixedSize(500, 550)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F5F3E9;
            }
        """)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.addStretch()
        title = QLabel('WordWise Mini')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            color: #33382B;
            font-size: 28px;
            font-weight: bold;
        """)
        subtitle = QLabel('Твой помощник в изучении английского')
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("""
            color: #777B68;
            font-size: 13px;
        """)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(35)
        self.start_button = QPushButton('Начать тест')
        self.dictionary_button = QPushButton('Мой словарь')
        self.statistics_button = QPushButton("Статистика")
        buttons_layout = QVBoxLayout()
        buttons_layout.setSpacing(12)
        for button in [self.start_button, self.dictionary_button, self.statistics_button]:
            button.setMinimumSize(250, 55)
            button.setMaximumWidth(350)
        self.start_button.setStyleSheet("""
            QPushButton {
                background-color: #68734A;
                color: white;
                border: none;
                border-radius: 12px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7C895A;
            }
        """)
        self.dictionary_button.setStyleSheet("""
            QPushButton {
                background-color: #E5E3D4;
                color: #33382B;
                border: none;
                border-radius: 12px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #D8D6C5;
            }
        """)
        self.statistics_button.setStyleSheet("""
            QPushButton {
                background-color: #68734A;
                color: white;
                border: none;
                border-radius: 12px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #56613C;
            }
        """)
        buttons_layout.addWidget(
            self.start_button, alignment=Qt.AlignmentFlag.AlignCenter)
        buttons_layout.addWidget(
            self.dictionary_button, alignment=Qt.AlignmentFlag.AlignCenter)
        buttons_layout.addWidget(
                    self.statistics_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(buttons_layout)
        layout.addStretch()
        image_layout = QHBoxLayout()
        image_layout.addStretch()
        self.image_label = QLabel()
        self.image_label.setMinimumSize(0, 0)
        self.image_label.setMaximumSize(110, 110)
        pixmap = QPixmap('project_foto.jfif')
        self.image_label.setPixmap(
            pixmap.scaled(
                110, 110,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )
        image_layout.addWidget(self.image_label)
        layout.addLayout(image_layout)
        self.start_button.clicked.connect(self.open_test)
        self.dictionary_button.clicked.connect(self.open_dictionary)
        self.statistics_button.clicked.connect(self.open_statistics)

    def open_test(self):
        self.test_window = TestWindow()
        self.test_window.show()

    def open_dictionary(self):
        self.dictionary_window = Dictionary()
        self.dictionary_window.show()

    def open_statistics(self):
        self.statistics_window = StatisticsWindow()
        self.statistics_window.show()

    def closeEvent(self, event):
        enter = QMessageBox.information(self,
                                        "Выход",
                                        "Вы действительно хотите выйти?",
                                        QMessageBox.StandardButton.Yes |
                                        QMessageBox.StandardButton.No
                                        )
        if enter == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()