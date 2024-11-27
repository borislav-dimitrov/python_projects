import sys
import traceback
from bot import Bot

from PySide6 import QtWidgets, QtGui, QtCore
from memory_reader import MemReader
from .drag_window_btn import DraggableButton
from .macro_button import MacroButton


BTN_STYLESHEET = 'background-color: rgba(0, 255, 0, 0.5); color: white; text-align: center; font-weight: bold; border-radius: 5px;'


class App(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        sys.excepthook = self._handle_exception

        self._main_window = QtWidgets.QWidget()
        self._main_window.setWindowFlags(self._main_window.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self._main_window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self._main_window.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, True)
        self._mem_reader = MemReader('client.exe')
        self._timer = QtCore.QTimer()
        self._buff_timer = QtCore.QTimer()
        self._buff_timer.timeout.connect(self._rebuff_reminder)
        self._bot = Bot(self._timer)


    def run(self) -> None:
        self._init_ui()
        self._main_window.show()
        # self._timer.start(1000)
        self.exec()

    def _handle_exception(self, exc_type: Exception, exc_value: Exception, exc_traceback: traceback):
        raise exc_value

    def _init_ui(self):
        self._main_window.setWindowTitle('TO tools')
        x = self.primaryScreen().geometry().width()
        y = self.primaryScreen().geometry().height()
        w, h = self._main_window.geometry().width(), self._main_window.geometry().height()
        self._main_window.move((x // 2) - (w // 2), (y // 2) - (h // 2))

        self._create_widgets()

    def _create_widgets(self) -> None:
        self._macro_1 = MacroButton('Macro 1')
        self._macro_1.setFixedHeight(20)
        self._macro_1.macro = '1 2900, r 1000, 2 2000, 2 2000, 2 2000, 6'
        self._macro_1.clicked.connect(lambda: self._bot.run_macro(self._macro_1.macro))
        self._macro_1.setStyleSheet(BTN_STYLESHEET)

        self._macro_2 = MacroButton('Macro 2')
        self._macro_2.setFixedHeight(20)
        self._macro_2.macro = '2 2400, r 1000, 2 2000, 2 2000, 6'
        self._macro_2.clicked.connect(lambda: self._bot.run_macro(self._macro_2.macro))
        self._macro_2.setStyleSheet(BTN_STYLESHEET)

        self._buff = MacroButton('Buff')
        self._buff.setFixedHeight(20)
        self._buff.macro = 'f1 1500, 8 1500, z 1500, x 1500, 9'
        self._buff.clicked.connect(self._on_buff)
        self._buff.setStyleSheet(BTN_STYLESHEET)

        self._exit = QtWidgets.QPushButton('X')
        self._exit.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        self._exit.clicked.connect(lambda: self.quit())
        self._exit.setStyleSheet(BTN_STYLESHEET)

        self._move_window = DraggableButton('M')
        self._move_window.setStyleSheet(BTN_STYLESHEET)

        self._main_layout = QtWidgets.QGridLayout(self._main_window)
        self._main_layout.setColumnMinimumWidth(0, 55)
        self._main_layout.setColumnMinimumWidth(1, 55)
        self._main_layout.setColumnMinimumWidth(2, 55)
        self._controls_layout = QtWidgets.QHBoxLayout()
        self._main_layout.addLayout(self._controls_layout, 1, 2)
        self._main_layout.addWidget(self._macro_1, 0, 0)
        self._main_layout.addWidget(self._macro_2, 0, 1)
        self._main_layout.addWidget(self._buff, 0, 2)
        self._controls_layout.addWidget(self._move_window)
        self._controls_layout.addWidget(self._exit)

    def _on_buff(self):
        self._bot.run_macro(self._buff.macro)
        self._buff_timer.start(1000 * 60 * 25)

    def _rebuff_reminder(self):
        self._buff_timer.stop()
        msg = QtWidgets.QMessageBox()
        msg.setText('Buffs falling off in 5 minutes.')
        msg.setWindowTitle("Rebuff reminder!")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, True)
        msg.exec()
