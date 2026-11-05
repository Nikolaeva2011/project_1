from PyQt6.QtWidgets import QTabWidget, QWidget, QLabel, QVBoxLayout, QMainWindow, QApplication, QTableView, QStackedWidget, QPushButton

class StackApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Стековый переключатель")
        self.resize(400, 300)
        
        # Создаём стек
        self.stack = QStackedWidget()
        
        # Страница 1
        self.page1 = QWidget()
        page1_layout = QVBoxLayout()
        self.label1 = QLabel("Добро пожаловать на страницу 1!")
        self.btn_to_page2 = QPushButton("На страницу 2")
        page1_layout.addWidget(self.label1)
        page1_layout.addWidget(self.btn_to_page2)
        self.page1.setLayout(page1_layout)
        
        # Страница 2
        self.page2 = QWidget()
        page2_layout = QVBoxLayout()
        self.label2 = QLabel("Вы на секретной странице 2!")
        self.btn_to_page1 = QPushButton("Назад")
        page2_layout.addWidget(self.label2)
        page2_layout.addWidget(self.btn_to_page1)
        self.page2.setLayout(page2_layout)
        
        # Добавляем страницы в стек
        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)
        
        # Подключаем кнопки
        self.btn_to_page2.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.btn_to_page1.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        
        self.setCentralWidget(self.stack)

if __name__ == "__main__":
    app = QApplication([])
    w = StackApp()
    w.resize(900, 600)
    w.show()
    app.exec()