from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout
from PySide6.QtGui import QIcon

WIDTH = 1366
HEIGHT = 768
TITLE = 'Trainer'
ICON = r'resources\muscle.png'


class BaseView(QMainWindow):
    def __init__(self, views_controller):
        super().__init__()
        self.views_controller = views_controller
        self.widget = QWidget()
        self.main_layout = QGridLayout()
        self._configure_window()
        self.setCentralWidget(self.widget)
        self.widget.setLayout(self.main_layout)

    def _configure_window(self):
        self.setFixedSize(WIDTH, HEIGHT)
        self.setWindowTitle(TITLE)
        self.setWindowIcon(QIcon(ICON))
