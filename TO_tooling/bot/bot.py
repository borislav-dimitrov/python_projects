import pyautogui
import win32api
import win32con
from PySide6 import QtCore

pyautogui.PAUSE = 0.012


class Bot:
    def __init__(self, timer: QtCore.QTimer):
        self._current_game_hwnd = 0
        self._timer = timer
        self._timer.timeout.connect(self._execute_next_command)
        self._commands = []

    def run_macro(self, macro: str, game_hwnd: int) -> None:
        self._timer.stop()
        self._commands.clear()

        if not game_hwnd:
            raise RuntimeError('Missing game hwnd!')

        self._current_game_hwnd = game_hwnd
        self._parse_macro(macro)
        self._execute_next_command()

    def _execute_next_command(self):
        if not self._commands:
            self._timer.stop()
            return

        self._send_msg(self._commands.pop(0))

    def _parse_macro(self, macro: str) -> None:
        raw_commands = macro.split(', ')

        for command in raw_commands:
            key_time_pair = command.split()
            if len(key_time_pair) == 1:
                key_time_pair.append('0')

            self._commands.append(key_time_pair)

    def _send_msg(self, command: list) -> None:
        key, delay = command[0], int(command[1])

        if key.lower() == 'tab':
            key = win32con.VK_TAB
        elif key.lower() == 'f1':
            key = win32con.VK_F1
        else:
            key = ord(key.upper()) if len(key) == 1 else None

        if key:
            win32api.SendMessage(self._current_game_hwnd, win32con.WM_KEYDOWN, key, 0)
            win32api.SendMessage(self._current_game_hwnd, win32con.WM_KEYUP, key, 0)

        self._timer.start(delay + 200)


    @staticmethod
    def tmp_1() -> None:
        pyautogui.move(850, 525)
        pyautogui.keyDown('shift')
        pyautogui.rightClick(850, 525)
        pyautogui.rightClick(850, 525)
        pyautogui.keyUp('shift')