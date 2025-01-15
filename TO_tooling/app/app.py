import sys
import traceback
from PySide6 import QtWidgets, QtCore

from bot import Bot
from process_handler import ProcessHandler
from .macro_button import MacroButton


class App(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        sys.excepthook = self._handle_exception

        self._main_window = QtWidgets.QWidget()
        self._main_window.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, True)

        self._process_timer = QtCore.QTimer()
        self._bot_timer = QtCore.QTimer()
        self._buff_timer = QtCore.QTimer()
        self._buff_timer.timeout.connect(self._rebuff_reminder)

        self._bot = Bot(self._bot_timer)
        self._process_handler = ProcessHandler()

    def run(self) -> None:
        self._init_ui()
        self._main_window.show()

        self._process_timer.timeout.connect(self._on_process_handler_tick)
        self._process_timer.start(1000)

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
        self._select_game_process_combo = QtWidgets.QComboBox()
        self._select_game_process_combo.addItems([
            f'{game.window_name} | {game.hwnd}' for game in self._process_handler.games
        ])

        self._hp_lbl = QtWidgets.QLabel('Health: ')
        self._hp_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self._hp_value_lbl = QtWidgets.QLabel('-----')
        self._hp_value_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self._mp_lbl = QtWidgets.QLabel('Mana: ')
        self._mp_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self._mp_value_lbl = QtWidgets.QLabel('-----')
        self._mp_value_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self._macro_1 = MacroButton('Macro 1')
        self._macro_1.setFixedHeight(20)
        self._macro_1.macro = '1 2900, r 1000, 2 2000, 2 2000, 2 2000'
        self._macro_1.clicked.connect(self._on_macro_1)
        self._macro_2 = MacroButton('Macro 2')
        self._macro_2.setFixedHeight(20)
        self._macro_2.macro = '2 2400, r 1000, 2 2000, 2 2000'
        self._macro_2.clicked.connect(self._on_macro_2)
        self._buff = MacroButton('Buff')
        self._buff.setFixedHeight(20)
        self._buff.macro = 'f1 1500, 8 1500, z 1500, x 1500, 9'
        self._buff.clicked.connect(self._on_buff)

        self._main_layout = QtWidgets.QGridLayout(self._main_window)

        self._main_layout.addWidget(self._select_game_process_combo, 0, 0, 1, 4)

        self._main_layout.addWidget(self._hp_lbl, 1, 0)
        self._main_layout.addWidget(self._hp_value_lbl, 1, 1)
        self._main_layout.addWidget(self._mp_lbl, 1, 2)
        self._main_layout.addWidget(self._mp_value_lbl, 1, 3)

        self._main_layout.addWidget(self._macro_1, 2, 0)
        self._main_layout.addWidget(self._macro_2, 2, 1)
        self._main_layout.addWidget(self._buff, 2, 3)

    def _on_buff(self):
        self._bot.run_macro(self._buff.macro, self._focus_game_and_get_hwnd())
        self._buff_timer.start(1000 * 60 * 25)

    def _on_macro_1(self) -> None:
        self._bot.run_macro(self._macro_1.macro, self._focus_game_and_get_hwnd())

    def _on_macro_2(self) -> None:
        self._bot.run_macro(self._macro_2.macro, self._focus_game_and_get_hwnd())

    def _focus_game_and_get_hwnd(self) -> int:
        if not self._select_game_process_combo.currentText():
            return 0

        game_hwnd = int(self._select_game_process_combo.currentText().split(' | ')[-1])
        self._process_handler.focus_game_window(game_hwnd)

        return game_hwnd

    def _rebuff_reminder(self) -> None:
        self._buff_timer.stop()

        msg = QtWidgets.QMessageBox()
        msg.setText('Buffs falling off in 5 minutes.')
        msg.setWindowTitle("Rebuff reminder!")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, True)
        msg.exec()

    def _on_process_handler_tick(self) -> None:
        if not self._select_game_process_combo.currentText():
            return

        game_hwnd = int(self._select_game_process_combo.currentText().split(' | ')[-1])
        self._process_handler.on_tick(game_hwnd)
        self._update_hp_mp(self._process_handler.hp_mp)
        print(self._process_handler.target)

    def _update_hp_mp(self, hp_mp: tuple[int, int]) -> None:
        if hp_mp[0] != -1:
            self._hp_value_lbl.setText(str(hp_mp[0]))

        if hp_mp[1] != -1:
            self._mp_value_lbl.setText(str(hp_mp[1]))
