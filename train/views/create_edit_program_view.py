from PySide6.QtWidgets import QMainWindow, QListWidget, QGridLayout, QPushButton, QWidget, QTextEdit, QLabel
from .base_view import BaseView, WIDTH, HEIGHT


class CreateEditProgramView(BaseView):
    def __init__(self, views_controller):
        super().__init__(views_controller)
        self.create = True
        self.program = None

        self._create_widgets()

    def show(self):
        super().show()
        # logic for changes for create/edit

    def _create_widgets(self):
        pass
