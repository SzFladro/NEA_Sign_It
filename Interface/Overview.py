import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout


'''
Potential code for overview screen with separated left side from the right side
right side may contain a playing video which will be responsive to what user does on left?
have statistics on the left hand side of the screen
'''
   


class HomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Home Screen")
        self.setGeometry(100, 100, 800, 600)

        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout(central_widget)

        # Sidebar
        self.sidebar = QWidget(self)
        self.sidebar_layout = QVBoxLayout(self.sidebar)

        self.add_navigation_button("Screen 1", self.show_screen_1)
        self.add_navigation_button("Screen 2", self.show_screen_2)

        layout.addWidget(self.sidebar)

        # Central Content
        self.central_content = QWidget(self)
        self.central_layout = QVBoxLayout(self.central_content)

        label = QLabel("Welcome to Your App", self)
        label.setAlignment(Qt.AlignCenter)
        self.central_layout.addWidget(label)

        layout.addWidget(self.central_content)

    def add_navigation_button(self, text, on_click):
        button = QPushButton(text, self)
        button.clicked.connect(on_click)
        self.sidebar_layout.addWidget(button)

    def show_screen_1(self):
        self.set_central_widget_message("This is Screen 1")

    def show_screen_2(self):
        self.set_central_widget_message("This is Screen 2")

    def set_central_widget_message(self, message):
        for i in reversed(range(self.central_layout.count())):
            self.central_layout.itemAt(i).widget().setParent(None)

        label = QLabel(message, self)
        label.setAlignment(Qt.AlignCenter)
        self.central_layout.addWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home_screen = HomeScreen()
    home_screen.show()
    sys.exit(app.exec())
