from PySide6.QtWidgets import QListWidget, QGridLayout, QPushButton, QWidget, QTextEdit, QLabel
from .base_view import BaseView


class MainView(BaseView):
    def __init__(self, views_controller):
        super().__init__(views_controller)
        self._create_widgets()
        self.main_layout.setColumnStretch(2, 1)

    # region BUILD GUI
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
        self.main_layout.addWidget(self.preview_label, 0, 3, 1, 1)
        self.preview_label.setText('Preview')
        self.preview_label.setObjectName('previewLbl')

    def _create_main_tree(self):
        self.main_tree = QListWidget()
        self.main_tree.setMinimumWidth(self.MIN_WIDTH)
        self.main_tree.setMaximumWidth(self.MIN_WIDTH)
        self.main_tree.setMinimumHeight(self.MIN_HEIGHT)
        self.main_tree.setObjectName('mainTree')
        self.main_layout.addWidget(self.main_tree, 1, 0, self.ROWS, 1)

        self.main_tree.itemSelectionChanged.connect(self._on_selection_changed)

    def _create_navigation_bar(self):
        self._navigation_bar_layout = QGridLayout()

        self.add_btn = QPushButton('+', self)
        self._navigation_bar_layout.addWidget(self.add_btn, 1, 0, 1, 1)
        self.add_btn.clicked.connect(self.views_controller.create_program)

        self.rem_btn = QPushButton('-', self)
        self._navigation_bar_layout.addWidget(self.rem_btn, 2, 0, 1, 1)
        self.rem_btn.clicked.connect(self.views_controller.delete_program)

        self.edit_btn = QPushButton('E', self)
        self._navigation_bar_layout.addWidget(self.edit_btn, 3, 0, 1, 1)
        self.edit_btn.clicked.connect(self.views_controller.edit_program)

        self.quit_btn = QPushButton('Q', self)
        self._navigation_bar_layout.addWidget(self.quit_btn, 4, 0, 1, 1)
        self.quit_btn.clicked.connect(self.views_controller.quit)

        self.main_layout.addLayout(self._navigation_bar_layout, 1, 1, 1, 1)

    def _create_preview(self):
        self.preview = QTextEdit()
        self.preview.setMinimumWidth(self.MIN_WIDTH)
        self.preview.setMaximumWidth(self.MIN_WIDTH)
        self.preview.setMinimumHeight(self.MIN_HEIGHT)
        self.preview.setObjectName('preview')
        self.main_layout.addWidget(self.preview, 1, 3, self.ROWS, 1)

        self.preview.setReadOnly(True)

    # endregion

    def _on_selection_changed(self):
        selected_program_name = self.main_tree.selectedItems()[0].text()
        program = self.views_controller.main_controller.programs_controller.get_program_by_name(selected_program_name)
        self.views_controller.current_program = program
        self.preview.setText(program.get_preview())

    def refresh_main_tree_items(self):
        self.views_controller.refresh_main_tree_items()
