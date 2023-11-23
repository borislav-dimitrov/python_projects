from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QGridLayout, QLabel, QListWidget, \
    QListWidgetItem
from .titles import WIFI_CONFIG_TITLE
from .utils import create_lbl, create_button


class WiFiConfig(QMainWindow):
    def __init__(self, style_sheet_file=r'.\gui\main.stylesheet'):
        super().__init__()

        # region CONFIG
        self.setWindowTitle(WIFI_CONFIG_TITLE)
        self.setMinimumSize(800, 600)

        self.style_sheet_file = style_sheet_file
        with open(self.style_sheet_file, "r") as fh:
            self.setStyleSheet(fh.read())
        # endregion

        # region WiFi
        self.wifi_networks = [('netwk1', '-50'), ('netwk111', '-55')]
        # endregion

        self.main_layout = QGridLayout()
        self._init_widgets()

        self.center_widget = QWidget()
        self.center_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.center_widget)

    def _init_widgets(self):
        ''''''
        self.wifi_lbox = QListWidget()
        self.wifi_lbox.setMaximumSize(300, 300)
        connect_btn = create_button(text='Connect')
        back_btn = create_button(text='Close', cmd=lambda: self.hide())

        for network in self.wifi_networks:
            self.wifi_lbox.addItem(QListWidgetItem(f'{network[0]}    [{network[1]}]'))

        self.main_layout.addWidget(self.wifi_lbox, 1, 1)
        self.main_layout.addWidget(connect_btn, 2, 1)
        self.main_layout.addWidget(back_btn, 3, 1)
