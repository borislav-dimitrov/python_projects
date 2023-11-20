from PySide6.QtWidgets import QGridLayout, QPushButton, QLabel, QLineEdit, QListWidget
from PySide6.QtCore import Qt

from .base_view import BaseView


class CreateEditProgramView(BaseView):
    def __init__(self, views_controller):
        super().__init__(views_controller)
        self.create = True
        self.program = None

        self.main_layout.setColumnStretch(2, 1)

        self.program_content_layout = QGridLayout()

        self.main_layout.addLayout(self.program_content_layout, 1, 0, 1, 1)

        self._create_widgets()

    def show(self):
        super().show()
        # logic for changes for create/edit

    def _create_widgets(self):
        self._create_program_content()
        self._create_nav_pane()

    def _create_program_content(self):
        self._create_program_content_base()
        self._create_program_name()
        self._create_program_exercises()
        self._create_program_exercises_base()

    def _create_program_content_base(self):
        self.preview_label = QLabel()
        self.preview_label.setText('Program Info')
        self.main_layout.addWidget(self.preview_label, 0, 0, 1, 1)

        self.preview = QLabel()
        self.preview.setMinimumWidth(self.MIN_WIDTH)
        self.preview.setMaximumWidth(self.MIN_WIDTH)
        self.preview.setMinimumHeight(self.MIN_HEIGHT)
        self.preview.setObjectName('createEditBase')

        self.main_layout.addWidget(self.preview, 1, 0, self.ROWS, 1)

    def _create_program_name(self):
        self.program_name_lbl = QLabel()
        self.program_name_lbl.setText('Program name:')
        self.program_name_lbl.setObjectName('programNameLbl')
        self.program_content_layout.addWidget(self.program_name_lbl, 1, 0, 1, 1, alignment=Qt.AlignCenter)

        self.program_name_inpt = QLineEdit()
        self.program_name_inpt.setObjectName('programNameInpt')
        self.program_content_layout.addWidget(self.program_name_inpt, 1, 1, 1, 2, alignment=Qt.AlignCenter)
        self.program_content_layout.setColumnStretch(2, 1)

    def _create_nav_pane(self):
        self._navigation_bar_layout = QGridLayout()

        self.add_btn = QPushButton('+', self)
        self._navigation_bar_layout.addWidget(self.add_btn, 1, 0, 1, 1)
        self.add_btn.clicked.connect(lambda: print('add exercise'))

        self.rem_btn = QPushButton('-', self)
        self._navigation_bar_layout.addWidget(self.rem_btn, 2, 0, 1, 1)
        self.rem_btn.clicked.connect(lambda: print('remove exercise'))

        self.edit_btn = QPushButton('S', self)
        self._navigation_bar_layout.addWidget(self.edit_btn, 3, 0, 1, 1)
        self.edit_btn.clicked.connect(lambda: print('save program'))

        self.quit_btn = QPushButton('B', self)
        self._navigation_bar_layout.addWidget(self.quit_btn, 4, 0, 1, 1)
        self.quit_btn.clicked.connect(lambda: print('go back'))

        self.main_layout.addLayout(self._navigation_bar_layout, 1, 1, 1, 1)

        for i in range(4):
            self._navigation_bar_layout.setRowStretch(2 + i, 1)

    def _create_program_exercises(self):
        self.exercises_lb = QListWidget()
        self.exercises_lb.setObjectName('exercisesLb')
        self.exercises_lb.setMinimumHeight((self.HEIGHT // 2) * 1.5)
        self.exercises_lb.setMaximumHeight((self.HEIGHT // 2) * 1.5)
        self.program_content_layout.addWidget(self.exercises_lb, 2, 0, self.ROWS, 3)

    def _create_program_exercises_base(self):
        self.preview_label = QLabel()
        self.preview_label.setText('Exercises')
        self.main_layout.addWidget(self.preview_label, 0, 3, 1, 1)

        self.preview = QLabel()
        self.preview.setMinimumWidth(self.MIN_WIDTH)
        self.preview.setMaximumWidth(self.MIN_WIDTH)
        self.preview.setMinimumHeight(self.MIN_HEIGHT)
        self.preview.setObjectName('exercisesBase')

        self.main_layout.addWidget(self.preview, 1, 3, self.ROWS, 1)

        self.exercises_layout = QGridLayout()
        self.main_layout.addLayout(self.exercises_layout, 1, 0, 1, 1)
