import csv
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel,
    QComboBox, QPushButton, QMessageBox
)
from PyQt6.QtCore import Qt
from theme import apply_theme

class ProfileWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WordWise Mini — Профиль")
        self.setFixedSize(400, 350)
        self.profile = {}
        self.setStyleSheet("""
            QDialog {
                background-color: #F5F3E9;
                color: #33382B;
                font-family: Arial;
            }

            QLabel {
                font-size: 15px;
                color: #33382B;
            }

            QComboBox {
                background-color: white;
                border: 1px solid #D8D8CB;
                border-radius: 8px;
                padding: 10px;
                font-size: 14px;
            }

            QPushButton {
                background-color: #68734A;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 12px;
                font-size: 15px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #56613C;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 25, 30, 25)
        layout.setSpacing(15)

        title = QLabel("Добро пожаловать!")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            font-size: 23px;
            font-weight: bold;
            color: #68734A;
        """)

        age_label = QLabel("Выберите возрастную категорию:")

        self.age_combo = QComboBox()
        self.age_combo.addItems([
            "Выберите возраст",
            "До 14 лет",
            "15–17 лет",
            "18–24 года",
            "25 лет и старше"
        ])

        gender_label = QLabel("Выберите пол (необязательно):")

        self.gender_combo = QComboBox()
        self.gender_combo.addItems([
            "Не указывать",
            "Женский",
            "Мужской"
        ])

        self.save_button = QPushButton("Продолжить")
        self.save_button.clicked.connect(self.save_profile)

        layout.addWidget(title)
        layout.addWidget(age_label)
        layout.addWidget(self.age_combo)
        layout.addWidget(gender_label)
        layout.addWidget(self.gender_combo)
        layout.addStretch()
        layout.addWidget(self.save_button)
        apply_theme(self)

    def save_profile(self):
        age = self.age_combo.currentText()

        if age == "Выберите возраст":
            QMessageBox.warning(
                self,
                "Профиль",
                "Пожалуйста, выберите возрастную категорию."
            )
            return

        self.profile = {
            "age": age,
            "gender": self.gender_combo.currentText()
        }

        with open("profile.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["age", "gender"])
            writer.writerow([
                self.age_combo.currentText(),
                self.gender_combo.currentText()
        ])
        self.accept()