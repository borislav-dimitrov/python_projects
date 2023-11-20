from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt


class BaseView(QMainWindow):
    WIDTH = 1366
    HEIGHT = 768
    TITLE = 'Trainer'
    ICON = r'resources\muscle.png'
    ROWS = 10
    COLS = 10
    MIN_WIDTH = WIDTH // 3
    MIN_HEIGHT = HEIGHT - 50

    def __init__(self, views_controller):
        super().__init__()
        self.views_controller = views_controller
        self.widget = QWidget()
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self._configure_window()
        self.setCentralWidget(self.widget)
        self.widget.setLayout(self.main_layout)

    def _configure_window(self):
        self.setFixedSize(self.WIDTH, self.HEIGHT)
        self.setWindowTitle(self.TITLE)
        self.setWindowIcon(QIcon(self.ICON))
