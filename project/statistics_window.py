import sqlite3
import csv
import os
import shutil
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from theme import apply_theme


class StatisticsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WordWise Mini — Статистика")
        self.resize(430, 400)
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
        self.date_label = QLabel()
        self.time_label = QLabel()
        self.average_time_label = QLabel()
        for label in [
            self.words_label,
            self.tests_label,
            self.correct_label,
            self.percent_label,
            self.date_label,
            self.time_label
        ]:
            label.setProperty("class", "card")
            label.setMinimumHeight(45)
        self.close_button = QPushButton("Закрыть")
        self.export_button = QPushButton("Экспортировать статистику")
        self.close_button.clicked.connect(self.close)
        self.export_button.clicked.connect(self.export_statistics)
        layout.addWidget(title)
        layout.addWidget(self.words_label)
        layout.addWidget(self.tests_label)
        layout.addWidget(self.correct_label)
        layout.addWidget(self.percent_label)
        layout.addWidget(self.date_label)
        layout.addWidget(self.time_label)
        layout.addWidget(self.average_time_label)
        layout.addStretch()
        layout.addWidget(self.close_button)
        layout.addWidget(self.export_button)
        self.load_statistics()
        apply_theme(self)

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

        try:
            with open("statistics.csv", "r", encoding="utf-8") as file:
                reader = list(csv.DictReader(file))
                if reader:
                    last_test = reader[-1]
                    self.date_label.setText(
                        f"📅 Последний тест: {last_test['Дата']}")
                    seconds = int(last_test["Время прохождения"])
                    minutes = seconds // 60
                    seconds = seconds % 60
                    self.time_label.setText(
                        f"⏱ Время прохождения: {minutes:02d}:{seconds:02d}"
                    )
                else:
                    self.date_label.setText("📅 Последний тест: нет данных")
                    self.time_label.setText("⏱ Время прохождения: нет данных")

        except FileNotFoundError:
            self.date_label.setText("📅 Последний тест: нет данных")
            self.time_label.setText("⏱ Время прохождения: нет данных")

        if os.path.exists("statistics.csv"):
            with open("statistics.csv", "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                times = [
                    int(row["Время прохождения"])
                    for row in reader
                ]

            if times:
                average = sum(times) // len(times)
                minutes = average // 60
                seconds = average % 60

                self.average_time_label.setText(
                    f"⏱ Среднее время теста: {minutes:02d}:{seconds:02d}"
                )
            else:
                self.average_time_label.setText("⏱ Среднее время теста: —")
        else:
            self.average_time_label.setText("⏱ Среднее время теста: —")

    def export_statistics(self):
        if not os.path.exists("statistics.csv"):
            QMessageBox.warning(
                self,
                "Ошибка",
                "История тестов пока пуста."
            )
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Сохранить статистику",
            "Моя статистика.csv",
            "CSV файлы (*.csv)"
        )

        if file_path:
            try:
                shutil.copyfile("statistics.csv", file_path)
                QMessageBox.information(
                    self,
                    "Успешно",
                    "Статистика сохранена!"
                    )
            except Exception as error:
                QMessageBox.warning(
                    self,
                    "Ошибка сохранения",
                    f"Не удалось сохранить файл: {error}"
                    )