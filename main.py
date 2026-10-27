import io
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *

template = """
"""


class MyNotes(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.setWindowTitle('ord Wise')
        self.addContactBtn.clicked.connect(self.run)

    def run(self):
        self.contactList.addItem(
            f"{self.contactName.text()} {self.contactNumber.text()}")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec())
