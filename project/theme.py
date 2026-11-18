def apply_theme(window):
    try:
        with open("settings.txt", "r", encoding="utf-8") as file:
            theme = file.read().strip()
    except FileNotFoundError:
        theme = "Светлая"

    if theme == "Тёмная":
        window.setStyleSheet("""
            QWidget {
                background-color: #252820;
                color: #F5F3E9;
                font-family: Segoe UI;
                font-size: 14px;
            }

            QLabel {
                color: #F5F3E9;
            }

            QLineEdit, QTextEdit {
                background-color: #383D31;
                color: #F5F3E9;
                border: 1px solid #68734A;
                border-radius: 8px;
                padding: 8px;
            }

            QPushButton {
                background-color: #68734A;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 11px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #7C895A;
            }

            QPushButton:disabled {
                background-color: #414638;
                color: #999999;
            }

            QRadioButton {
                color: #F5F3E9;
                spacing: 8px;
            }

            QComboBox, QListWidget, QTableWidget {
                background-color: #383D31;
                color: #F5F3E9;
                border: 1px solid #68734A;
                border-radius: 8px;
                padding: 6px;
            }
        """)