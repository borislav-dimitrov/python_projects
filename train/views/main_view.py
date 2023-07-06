from PySide6.QtWidgets import QMainWindow, QListWidget, QGridLayout, QPushButton, QWidget, QLabel
from PySide6.QtGui import QIcon

WIDTH = 1366
HEIGHT = 768
TITLE = 'Trainer'
ICON = r'resources\muscle.png'
ROWS = 10
COLS = 10
MIN_WIDTH = WIDTH // 2.2
MIN_HEIGHT = HEIGHT - 50


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        self.main_layout = QGridLayout()

        self._configure_window()
        self._create_widgets()

        self.setCentralWidget(self.widget)
        self.widget.setLayout(self.main_layout)

    # region BUILD GUI
    def _configure_window(self):
        self.setFixedSize(WIDTH, HEIGHT)
        self.setWindowTitle(TITLE)
        self.setWindowIcon(QIcon(ICON))

    def _create_widgets(self):
        self._create_labels()
        self._create_main_tree()
        self._create_navigation_bar()
        self._create_preview()

    def _create_labels(self):
        self.programs_label = QLabel()
        self.main_layout.addWidget(self.programs_label, 0, 0, 1, 1)
        self.programs_label.setText('Programs')
        self.programs_label.setObjectName('programsLbl')

        self.preview_label = QLabel()
        self.main_layout.addWidget(self.preview_label, 0, 2, 1, 1)
        self.preview_label.setText('Preview')
        self.preview_label.setObjectName('previewLbl')

    def _create_main_tree(self):
        self.main_tree = QListWidget()
        self.main_tree.setMinimumWidth(MIN_WIDTH)
        self.main_tree.setMinimumHeight(MIN_HEIGHT)
        self.main_layout.addWidget(self.main_tree, 1, 0, ROWS, 1)

    def _create_navigation_bar(self):
        self._navigation_bar_layout = QGridLayout()

        self.add_btn = QPushButton('+', self)
        self._navigation_bar_layout.addWidget(self.add_btn, 1, 0, 1, 1)

        self.rem_btn = QPushButton('-', self)
        self._navigation_bar_layout.addWidget(self.rem_btn, 2, 0, 1, 1)

        self.edit_btn = QPushButton('E', self)
        self._navigation_bar_layout.addWidget(self.edit_btn, 3, 0, 1, 1)

        self.quit_btn = QPushButton('Q', self)
        self._navigation_bar_layout.addWidget(self.quit_btn, 4, 0, 1, 1)

        self.main_layout.addLayout(self._navigation_bar_layout, 1, 1, 4, 1)

    def _create_preview(self):
        self.preview = QLabel()
        self.preview.setMinimumWidth(MIN_WIDTH)
        self.preview.setMinimumHeight(MIN_HEIGHT)
        self.preview.setObjectName('preview')
        self.main_layout.addWidget(self.preview, 1, 2, ROWS, 1)

    # endregion
