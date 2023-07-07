from .views_controller import ViewsController
from .programs_controller import ProgramsController
from PySide6.QtWidgets import QApplication

STYLESHEET = r'utils\style.qss'


class MainController:
    def __init__(self, args):
        self.args = args
        self.app = QApplication(self.args)
        with open(STYLESHEET, 'r') as handler:
            self.app.setStyleSheet(handler.read())

        self.programs_controller = ProgramsController(self)
        self.views_controller = ViewsController(self)

    def start_app(self):
        self.views_controller.initialize()
        self.app.exec()

    def get_all_programs(self):
        return self.programs_controller.programs
