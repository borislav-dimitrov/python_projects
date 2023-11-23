from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QGridLayout, QLabel
from PyQt6.QtGui import QCursor

from .utils import create_button, create_lbl
from utils import exit_app
from .titles import MAIN_WINDOW_TITLE
from .wifi_config import WiFiConfig


class MainWindow(QMainWindow):
    def __init__(self, style_sheet_file=r'.\gui\main.stylesheet'):
        super().__init__()

        # region CONFIG
        self.setWindowTitle(MAIN_WINDOW_TITLE)
        self.setMinimumSize(800, 600)

        self.style_sheet_file = style_sheet_file
        with open(self.style_sheet_file, "r") as fh:
            self.setStyleSheet(fh.read())
        # endregion

        self.wifi_config_window = WiFiConfig()

        self.main_layout = QGridLayout()
        self._init_widgets()

        self.center_widget = QWidget()
        self.center_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.center_widget)

    def _init_widgets(self):
        ''''''
        status_lbl = create_lbl(text='Status')
        wifi_btn = create_button(text='Wi-Fi', cmd=lambda: self.wifi_config_window.show())
        exit_btn = create_button(text='Exit', cmd=exit_app)

        self.main_layout.addWidget(status_lbl, 0, 1)
        self.main_layout.addWidget(wifi_btn, 1, 1)
        self.main_layout.addWidget(exit_btn, 2, 1)


class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.window = MainWindow()
        self.window.show()
