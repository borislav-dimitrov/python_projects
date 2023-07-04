import sys
from PyQt6 import QtWidgets
from .add_edit_window import AddEditWindow
from .utils import PyQtTable
from config import STYLESHEET
from managers.vault_manager import VaultManager


class Application(QtWidgets.QWidget):
    def __init__(self, width=600, height=800, title='Pwd Mgr'):
        self.app = QtWidgets.QApplication(sys.argv)
        super().__init__()
        self.title = title
        self.left = 0
        self.top = 0
        self.width = width
        self.height = height
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.setStyleSheet(STYLESHEET)

        self._set_layouts()
        self._build_gui()

        # Other Windows
        self.add_window = AddEditWindow(self.table)
        self.add_window.save_hook = self._save_vault
        self.edit_window = AddEditWindow(self.table, edit=True)
        self.edit_window.save_hook = self._save_vault

        # Managers
        self.vault_mgr = VaultManager()

        self.on_load()
        self.show()

    def _set_layouts(self):
        self.layout = QtWidgets.QGridLayout()

        self.top_layout = QtWidgets.QGridLayout()
        self.top_layout.setColumnStretch(0, 1)
        self.top_layout.setColumnStretch(1, 1)


        self.vertical_layout = QtWidgets.QVBoxLayout()

        self.bottom_layout = QtWidgets.QGridLayout()
        self.bottom_layout.addLayout(self.vertical_layout, 0, 1)
        self.bottom_layout.setColumnStretch(0, 1)
        self.bottom_layout.setColumnStretch(2, 1)
        self.bottom_layout.setColumnStretch(3, 30)

        self.setLayout(self.layout)
        self.layout.addLayout(self.top_layout, 0, 0)
        self.layout.addLayout(self.bottom_layout, 1, 0)

    def _build_gui(self):
        # Build SearchBar Section
        self.search_bar = QtWidgets.QLineEdit()
        self.search_btn = QtWidgets.QPushButton(self, text='Search')
        self.top_layout.addWidget(self.search_bar, 0, 1)
        self.top_layout.addWidget(self.search_btn, 0, 2)

        # Build Vertical Buttons
        self.add_btn = QtWidgets.QPushButton(self, text='Add')
        self.add_btn.clicked.connect(self._add_on_click)
        self.vertical_layout.addWidget(self.add_btn, 0)

        self.remove_btn = QtWidgets.QPushButton(self, text='Remove')
        self.remove_btn.clicked.connect(self._remove_on_click)
        self.vertical_layout.addWidget(self.remove_btn, 1)

        self.edit_btn = QtWidgets.QPushButton(self, text='Edit')
        self.edit_btn.clicked.connect(self._edit_on_click)
        self.vertical_layout.addWidget(self.edit_btn, 2)

        self.options_btn = QtWidgets.QPushButton(self, text='Options')
        self.options_btn.clicked.connect(self._options_on_click)
        self.vertical_layout.addWidget(self.options_btn, 3)

        self.exit_btn = QtWidgets.QPushButton(self, text='Exit')
        self.vertical_layout.addWidget(self.exit_btn, 4)
        self.exit_btn.clicked.connect(self._exit_on_click)
        self.vertical_layout.addStretch()

        # Build Table
        self.table = PyQtTable(('Location', 'Password'))
        self.bottom_layout.addWidget(self.table, 0, 3)

    def _search_on_click(self):
        pass

    def _add_on_click(self):
        if self.add_window:
            self.add_window.add()

    def _remove_on_click(self):
        self.table.remove_selected()
        self._save_vault()

    def _edit_on_click(self):
        if self.edit_window and self.table.selected:
            self.edit_window.edit(self.table.selected)

    def _options_on_click(self):
        pass

    def _exit_on_click(self):
        self.app.quit()

    def run(self):
        sys.exit(self.app.exec())

    def before_exit(self):
        print('Before Exit Triggered')
        self._save_vault()

    def closeEvent(self, event):
        self.before_exit()

    def on_load(self):
        self.table.insert_data(self.vault_mgr.get_raw_data())

    def _save_vault(self):
        self.vault_mgr.fill_from_app(self.table.data())
        self.vault_mgr.dump_vault()
