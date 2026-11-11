import sqlite3
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class Dictionary(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Мой словарь")
        self.resize(500, 400)
        with sqlite3.connect('my_words_database.db') as con:
            cur = con.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS words (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    english TEXT NOT NULL,
                    translation TEXT NOT NULL
                )
            """)
        layout = QVBoxLayout()
        layout.setContentsMargins(25, 20, 25, 20)
        layout.setSpacing(12)
        title = QLabel('Мой словарь')
        title.setObjectName('titleLabel')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.english_input = QLineEdit()
        self.english_input.setPlaceholderText('Английское слово')
        self.translation_input = QLineEdit()
        self.translation_input.setPlaceholderText('Перевод')
        self.add_button = QPushButton('Добавить слово')
        self.add_button.setObjectName('addButton')
        self.delete_button = QPushButton('Удалить слово')
        self.delete_button.setObjectName('deleteButton')
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
                color: #33382B;
                font-family: Segoe UI;
                font-size: 14px;
            }

            QLabel#titleLabel {
                font-size: 25px;
                font-weight: bold;
                color: #68734A;
                padding: 10px;
            }

            QLineEdit {
                background-color: #FFFFFF;
                border: 1px solid #D8D8C8;
                border-radius: 10px;
                padding: 10px;
            }

            QLineEdit:focus {
                border: 2px solid #68734A;
            }

            QPushButton {
                border: none;
                border-radius: 10px;
                padding: 11px;
                font-weight: bold;
            }

            QPushButton#addButton {
                background-color: #68734A;
                color: white;
            }

            QPushButton#addButton:hover {
                background-color: #7C895A;
            }

            QPushButton#deleteButton {
                background-color: #E5E3D4;
                color: #33382B;
            }

            QPushButton#deleteButton:hover {
                background-color: #D8D5C3;
            }

            QListWidget {
                background-color: white;
                border: none;
                border-radius: 12px;
                padding: 8px;
            }

            QListWidget::item {
                padding: 10px;
                border-bottom: 1px solid #E5E3D4;
            }

            QListWidget::item:selected {
                background-color: #E5E8D9;
                color: #33382B;
                border-radius: 5px;
            }
    """)
        self.add_button.clicked.connect(self.add_word)
        self.delete_button.clicked.connect(self.delete_words)
        self.load_words()

    def add_word(self):
        english = self.english_input.text()
        translation = self.translation_input.text()
        if english != "" and translation != "":
            with sqlite3.connect('my_words_database.db') as con:
                cur = con.cursor()
                cur.execute(
                    'INSERT INTO words (english, translation) VALUES (?, ?)', (english, translation))
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
            self.words_list.addItem(f'{english} - {translation}')

    def delete_words(self):
        item = self.words_list.currentItem()
        if item is None:
            return
        english, translation = item.text().split(" - ", 1)
        with sqlite3.connect('my_words_database.db') as con:
            cur = con.cursor()
            cur.execute("""DELETE FROM words
                        WHERE english = ? AND translation = ?""", (english, translation))
        self.load_words()

    def closeEvent(self, event):
        enter = QMessageBox.information(self,
                                        "Выход",
                                        "Вы действительно хотите закрыть окно?",
                                        QMessageBox.StandardButton.Yes |
                                        QMessageBox.StandardButton.No
                                        )
        if enter == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

