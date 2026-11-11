import sqlite3
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


class StatisticsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WordWise Mini — Статистика")
        self.setFixedSize(430, 400)
        self.setStyleSheet("""
            QWidget {
                background-color: #F5F3E9;
                color: #33382B;
                font-family: Arial;
            }
            QLabel#title {
                font-size: 25px;
                font-weight: bold;
                color: #68734A;
            }
            QLabel[class="card"] {
                background-color: #E5E3D4;
                border-radius: 12px;
                padding: 15px;
                font-size: 16px;
            }
            QPushButton {
                background-color: #68734A;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 12px;
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #56613C;
            }
        """)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 25, 30, 25)
        layout.setSpacing(15)
        title = QLabel("Моя статистика")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.words_label = QLabel()
        self.tests_label = QLabel()
        self.correct_label = QLabel()
        self.percent_label = QLabel()
        for label in [
            self.words_label,
            self.tests_label,
            self.correct_label,
            self.percent_label
        ]:
            label.setProperty("class", "card")
            label.setMinimumHeight(45)
        self.close_button = QPushButton("Закрыть")
        self.close_button.clicked.connect(self.close)
        layout.addWidget(title)
        layout.addWidget(self.words_label)
        layout.addWidget(self.tests_label)
        layout.addWidget(self.correct_label)
        layout.addWidget(self.percent_label)
        layout.addStretch()
        layout.addWidget(self.close_button)
        self.load_statistics()

    def load_statistics(self):
        with sqlite3.connect("my_words_database.db") as con:
            cur = con.cursor()
            cur.execute("SELECT COUNT(*) FROM words")
            words = cur.fetchone()[0]
            cur.execute("""
                CREATE TABLE IF NOT EXISTS statistics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    correct_answers INTEGER,
                    total_answers INTEGER
                )
            """)
            cur.execute("""
                SELECT COUNT(*),
                       SUM(correct_answers),
                       SUM(total_answers)
                FROM statistics
            """)
            tests, correct, total = cur.fetchone()
        correct = correct or 0
        total = total or 0
        percent = round(correct / total * 100) if total else 0
        self.words_label.setText(f"📚 Слов в словаре: {words}")
        self.tests_label.setText(f"📝 Пройдено тестов: {tests}")
        self.correct_label.setText(f"✅ Правильных ответов: {correct}")
        self.percent_label.setText(f"📊 Точность: {percent}%")