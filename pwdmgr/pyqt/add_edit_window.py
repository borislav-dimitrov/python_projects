from PyQt6.QtWidgets import QWidget, QGridLayout, QLineEdit, QPushButton, QLabel


class AddEditWindow(QWidget):
    def __init__(self, table, edit=False):
        super().__init__()
        self.table = table
        self.setWindowTitle('Add new password')
        self.styleSheet = """
        background-color:gray
        """
        self.setStyleSheet(self.styleSheet)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.location_lbl = QLabel(text='Location: ')
        self.location_input = QLineEdit()
        self.pwd_lbl = QLabel(text='Password: ')
        self.pwd_input = QLineEdit()

        if not edit:
            self.add_btn = QPushButton(text='Add')
            self.add_btn.clicked.connect(self._add_on_click)
        else:
            self.editing_row = None
            self.add_btn = QPushButton(text='Save')
            self.add_btn.clicked.connect(self._save_on_click)

        self.cancel_btn = QPushButton(text='Cancel')
        self.cancel_btn.clicked.connect(self._cancel_on_click)

        self.layout.addWidget(self.location_lbl, 0, 0)
        self.layout.addWidget(self.location_input, 0, 1)
        self.layout.addWidget(self.pwd_lbl, 1, 0)
        self.layout.addWidget(self.pwd_input, 1, 1)
        self.layout.addWidget(self.add_btn, 2, 0)
        self.layout.addWidget(self.cancel_btn, 2, 1)

    def _add_on_click(self):
        content = (self.location_input.text(), self.pwd_input.text())
        self.table.add_row(content)
        self._clear()
        self.close()

    def _save_on_click(self):
        if not self.editing_row:
            raise Exception('Ooops!')

        content = (self.location_input.text(), self.pwd_input.text())
        self.table.edit_row(self.editing_row, content)
        self._clear()
        self.close()


    def _cancel_on_click(self):
        self._clear()
        self.close()

    def _clear(self):
        self.location_input.clear()
        self.pwd_input.clear()
        self.editing_row = None

    def add(self):
        self.show()

    def edit(self, row_nr):
        self.show()
        self.editing_row = row_nr
