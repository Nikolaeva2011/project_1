import sqlite3
import random
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


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
        self.word_label.setWordWrap(True)
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
                font-size: 22px;
                font-weight: bold;
                border-radius: 15px;
                padding: 12px;
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
            self.answer_input.clear()
            self.word_label.setText("Поздравляю! Тест завершен.")
            self.answer_input.hide()
            self.check_button.hide()
            self.next_button.hide()
            return
        self.current_word = random.choice(self.test_questions_list)
        self.test_questions_list.remove(self.current_word)
        self.word_label.setText(self.current_word[0])
        self.answer_input.clear()
        self.answer_input.setEnabled(True)
        self.check_button.show()
        self.next_button.setEnabled(False)

    def check_answer(self):
        answer = self.answer_input.text().strip().lower()
        if answer == self.current_word[1].strip().lower():
            self.word_label.setText("Правильно!")
        else:
            self.word_label.setText(
                f"Неправильно! Правильный ответ: {self.current_word[1]}")
        self.answer_input.clear()
        self.answer_input.setEnabled(False)
        self.check_button.hide()
        self.next_button.setEnabled(True)

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