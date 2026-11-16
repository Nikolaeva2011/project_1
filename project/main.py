import sys
import os
from PyQt6.QtWidgets import QApplication, QDialog
from main_window import MyNotes
from profile_window import ProfileWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    if not os.path.exists("profile.csv"):
        profile = ProfileWindow()
        if profile.exec() != QDialog.DialogCode.Accepted:
            sys.exit()
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec())
