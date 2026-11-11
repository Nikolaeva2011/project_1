import sys
from PyQt6.QtWidgets import QApplication
from main_window import MyNotes


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec())
