import sqlite3
import random
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from theme import apply_theme


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
        self.answer_buttons = []
        self.answer_group = QButtonGroup(self)

        for i in range(4):
            button = QRadioButton()
            self.answer_buttons.append(button)
            self.answer_group.addButton(button)

        self.correct_answers = 0
        self.total_answers = 0

        self.check_button = QPushButton('Проверить')
        self.check_button.setObjectName('checkButton')
        self.next_button = QPushButton('Следующее слово')
        self.next_button.setObjectName('nextButton')
        self.next_button.setEnabled(False)

        layout.addWidget(title)
        layout.addWidget(self.word_label, 1)
        for button in self.answer_buttons:
            layout.addWidget(button)
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
        apply_theme(self)

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
            with sqlite3.connect("my_words_database.db") as con:
                cur = con.cursor()
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS statistics (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        correct_answers INTEGER,
                        total_answers INTEGER
                    ) 
                """)
                # print("сохраняем", self.correct_answers, self.total_answers)
                cur.execute(
                    'INSERT INTO statistics (correct_answers, total_answers) VALUES (?, ?)',
                    (self.correct_answers, self.total_answers)
                )
            # self.answer_input.clear()
            self.word_label.setText("Поздравляю! Тест завершен.")
            # self.answer_input.hide()
            self.check_button.hide()
            self.next_button.hide()
            return
        self.current_word = random.choice(self.test_questions_list)
        self.test_questions_list.remove(self.current_word)
        self.word_label.setText(self.current_word[0])
        correct_answer = self.current_word[1]
        options = [correct_answer]
        other_words = [
            word[1] for word in self.words
            if word[1] != correct_answer
        ]

        correct_answer = self.current_word[1]
        options = [correct_answer]
        other_words = [
            word[1] for word in self.words
            if word[1] != correct_answer
        ]
        random.shuffle(other_words)
        options.extend(other_words[:3])
        random.shuffle(options)
        for button, option in zip(self.answer_buttons, options):
            button.setText(option)
            button.setChecked(False)
            button.setEnabled(True)
            button.show()

        for button in self.answer_buttons[len(options):]:
            button.hide()

        # self.answer_input.clear()
        # self.answer_input.setEnabled(True)
        self.check_button.show()
        self.next_button.setEnabled(False)

    def check_answer(self):
        selected_button = self.answer_group.checkedButton()
        if selected_button is None:
            QMessageBox.warning(self, "Внимание", "Выберите вариант ответа!")
            return
        answer = selected_button.text().strip().lower()
        self.total_answers += 1
        if answer == self.current_word[1].strip().lower():
            self.correct_answers += 1
            self.word_label.setText("Правильно!")
        else:
            self.word_label.setText(
                f"Неправильно! Правильный ответ: {self.current_word[1]}"
            )
        for button in self.answer_buttons:
            button.setEnabled(False)
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
