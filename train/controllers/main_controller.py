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

        self._programs_controller = ProgramsController(self)
        self._views_controller = ViewsController(self)

        self._configure_hooks()

    def start_app(self):
        self._views_controller.initialize()
        self._views_controller.on_get_all_programs()
        self.app.exec()

    def _configure_hooks(self):
        self._views_controller.set_get_all_programs(self._get_all_programs)

    def _get_all_programs(self):
        return self._programs_controller.programs
