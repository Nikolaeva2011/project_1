import io
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtCore import Qt


class MyNotes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('WordWise Mini')
        self.setMinimumSize(500, 550)
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
        buttons_layout = QVBoxLayout()
        buttons_layout.setSpacing(12)
        for button in [self.start_button, self.dictionary_button]:
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
        buttons_layout.addWidget(self.start_button, alignment=Qt.AlignmentFlag.AlignCenter)
        buttons_layout.addWidget(self.dictionary_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(buttons_layout)
        layout.addStretch()
        self.start_button.clicked.connect(self.open_test)
        self.dictionary_button.clicked.connect(self.open_dictionary)

    def open_test(self):
        self.test_window = TestWindow()
        self.test_window.show()

    def open_dictionary(self):
            self.test_window = TestWindow()
            self.test_window.show()


class Dictionary(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Мой словарь')
        self.resize(500, 400)
        layout = QVBoxLayout()
        title = QLabel('Мой словарь')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        self.setLayout(layout)


class TestWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Тест')
        self.resize(500, 400)
        layout = QVBoxLayout()
        title = QLabel('Проверка знаний')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec())
