import sqlite3
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
            self.dictionary_window = Dictionary()
            self.dictionary_window.show()
            

class Dictionary(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Мой словарь')
        self.resize(500, 400)
        with sqlite3.connect('my_words_database.db') as con:
            cur = con.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS words (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    english TEXT NOT NULL,
                    translation TEXT NOT NULL
                )
            ''')
        layout = QVBoxLayout()
        title = QLabel('Мой словарь')
        self.english_input = QLineEdit()
        self.english_input.setPlaceholderText('Английское слово')
        self.translation_input = QLineEdit()
        self.translation_input.setPlaceholderText('Перевод')
        self.add_button = QPushButton('Добавить слово')
        self.delete_button = QPushButton('Удалить слово')
        self.words_list = QListWidget()
        layout.addWidget(title)
        layout.addWidget(self.english_input)
        layout.addWidget(self.translation_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.words_list)
        self.setLayout(layout)
        self.setStyleSheet("""
                    QWidget {
                        background-color: #F5F3E9;
                    }
                """)
        layout.addWidget(title)
        self.setLayout(layout)
        self.add_button.clicked.connect(self.add_word)
        self.delete_button.clicked.connect(self.delete_words)
        self.load_words()

    def add_word(self):
        english = self.english_input.text()
        translation = self.translation_input.text()
        if english != "" and translation != "":
            with sqlite3.connect('my_words_database.db') as con:
                cur = con.cursor()
                cur.execute('INSERT INTO words (english, translation) VALUES (?, ?)', (english, translation))
            self.english_input.clear()
            self.translation_input.clear()
            self.load_words()

    def load_words(self):
        self.words_list.clear()
        with sqlite3.connect('my_words_database.db') as con:
            cur = con.cursor()
            cur.execute('SELECT english, translation FROM words')
            words = cur.fetchall()
        for english, translation in words:
            self.words_list.addItem(f'{english} — {translation}')

    # На доработке
    def delete_words(self):
        self.words_list.clear()
        with sqlite3.connect('my_words_database.db') as con:
            cur = con.cursor()
            cur.execute('DELETE english, translation FROM words')
            words = cur.fetchall()

class TestWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Тест')
        self.resize(500, 400)
        self.setStyleSheet("""
                            QWidget {
                                background-color: #F5F3E9;
                            }
                        """)
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
