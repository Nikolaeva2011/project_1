from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel,QComboBox, QPushButton
from theme import apply_theme


class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Настройки")
        self.setFixedSize(350, 250)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(15)

        title = QLabel("Настройки приложения")
        title.setStyleSheet("""
            font-size: 21px;
            font-weight: bold;
            color: #68734A;
            font-weight: bold
        """)

        theme_label = QLabel("Выберите тему:")

        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Светлая", "Тёмная"])

        self.save_button = QPushButton("Сохранить")
        self.save_button.clicked.connect(self.save_settings)

        layout.addWidget(title)
        layout.addWidget(theme_label)
        layout.addWidget(self.theme_combo)
        layout.addStretch()
        layout.addWidget(self.save_button)

        self.setStyleSheet("""
            QDialog {
                background-color: #F5F3E9;
                color: #33382B;
            }

            QComboBox {
                padding: 8px;
                border-radius: 8px;
                background-color: white;
            }

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
        apply_theme(self)
        
    def save_settings(self):
        theme = self.theme_combo.currentText()
        with open("settings.txt", "w", encoding="utf-8") as file:
            file.write(theme)
            
        self.accept()