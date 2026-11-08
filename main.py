import sqlite3
import sys
import random
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtCore import Qt


class MyNotes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('WordWise Mini')
        self.resize(500, 550)
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
        buttons_layout.addWidget(
            self.start_button, alignment=Qt.AlignmentFlag.AlignCenter)
        buttons_layout.addWidget(
            self.dictionary_button, alignment=Qt.AlignmentFlag.AlignCenter)
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

    def open_test(self):
        self.test_window = TestWindow()
        self.test_window.show()

    def open_dictionary(self):
        self.dictionary_window = Dictionary()
        self.dictionary_window.show()

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


class TestWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Тест')
        self.resize(500, 400)
        layout = QVBoxLayout()
        layout.setContentsMargins(25, 20, 25, 20)
        layout.setSpacing(15)
        title = QLabel('Переведите слово')
        title.setObjectName('titleLabel')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.word_label = QLabel()
        self.word_label.setObjectName('wordLabel')
        self.word_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.answer_input = QLineEdit()
        self.answer_input.setPlaceholderText('Введите перевод')
        self.check_button = QPushButton('Проверить')
        self.check_button.setObjectName('checkButton')
        self.next_button = QPushButton('Следующее слово')
        self.next_button.setObjectName('nextButton')
        self.next_button.setEnabled(False)
        layout.addWidget(title)
        layout.addWidget(self.word_label, 1)
        layout.addWidget(self.answer_input)
        layout.addWidget(self.check_button)
        layout.addWidget(self.next_button)
        self.setLayout(layout)
        self.setStyleSheet("""
            QWidget {
                background-color: #F5F3E9;
                color: #33382B;
                font-family: Segoe UI;
                font-size: 14px;
            }

            QLabel#titleLabel {
                color: #68734A;
                font-size: 22px;
                font-weight: bold;
                padding: 10px;
            }

            QLabel#wordLabel {
                background-color: white;
                color: #68734A;
                font-size: 30px;
                font-weight: bold;
                border-radius: 15px;
                padding: 30px;
            }

            QLineEdit {
                background-color: white;
                border: 1px solid #D8D8C8;
                border-radius: 10px;
                padding: 11px;
            }

            QLineEdit:focus {
                border: 2px solid #68734A;
            }

            QPushButton {
                border: none;
                border-radius: 10px;
                padding: 12px;
                font-weight: bold;
            }

            QPushButton#checkButton {
                background-color: #68734A;
                color: white;
            }

            QPushButton#checkButton:hover {
               background-color: #7C895A;
            }

            QPushButton#nextButton {
                background-color: #E5E3D4;
                color: #33382B;
            }

            QPushButton#nextButton:hover {
                background-color: #D8D5C3;
            }

            QPushButton:disabled {
                background-color: #D8D8D0;
                color: #999999;
            }
        """)
        self.check_button.clicked.connect(self.check_answer)
        self.next_button.clicked.connect(self.next_question)
        self.load_question()

    def load_question(self):
        with sqlite3.connect('my_words_database.db') as con:
            cur = con.cursor()
            cur.execute("""SELECT DISTINCT english, translation FROM words""")
            self.words = cur.fetchall()
        if not self.words:
            QMessageBox.information(self,
                                    "Нет слов",
                                    "Сначала добавьте слова в словарь!")
            self.close()
            return
        self.test_questions_list = self.words.copy()
        self.next_question()

    def next_question(self):
        if not self.test_questions_list:
            self.word_label.setText("Поздравляю! Тест завершен.")
            self.answer_input.setEnabled(False)
            self.check_button.setEnabled(False)
            self.next_button.setEnabled(False)
            return
        self.current_word = random.choice(self.test_questions_list)
        self.test_questions_list.remove(self.current_word)
        self.word_label.setText(self.current_word[0])
        self.answer_input.clear()
        self.answer_input.setEnabled(True)
        self.check_button.setEnabled(True)
        self.next_button.setEnabled(False)

    def check_answer(self):
        answer = self.answer_input.text().strip().lower()
        if answer == self.current_word[1].strip().lower():
            self.word_label.setText("Правильно!")
        else:
            self.word_label.setText(
                f"Неправильно! Правильный ответ: {self.current_word[1]}")
        self.answer_input.setEnabled(False)
        self.check_button.setEnabled(False)
        self.next_button.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec())
