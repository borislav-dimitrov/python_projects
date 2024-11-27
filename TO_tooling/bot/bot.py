import psutil
import pyautogui
import win32api
import win32con
import win32gui
import win32process
from PySide6 import QtCore


class Bot:
    def __init__(self, timer: QtCore.QTimer):
        self._process_name = 'client.exe'
        self._game_hwnd = self._get_window_hwnd()
        self._timer = timer
        self._timer.timeout.connect(self._execute_next_command)
        self._commands = []

    def run_macro(self, macro: str, interval: int = 2000) -> None:
        self._focus_game_window()

        self._timer.stop()
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

    @staticmethod
    def get_mouse_pos() -> tuple[int, int]:
        x, y = pyautogui.position()
        return x, y

    @staticmethod
    def get_hp_mp_state() -> tuple[str, str]:
        hp_color = ((173, 0, 2),)
        mp_color = ((0, 77, 149), (0, 76, 148))
        low_hp_threshold = (155, 73)
        low_mp_threshold = (158, 83)

        screenshot = pyautogui.screenshot()
        hp = 'GOOD' if screenshot.getpixel(low_hp_threshold) in hp_color else 'LOW'
        mp = 'GOOD' if screenshot.getpixel(low_mp_threshold) in mp_color else 'LOW'
        return hp, mp

    def _focus_game_window(self) -> None:
        win32gui.ShowWindow(self._game_hwnd, win32con.SW_SHOW)
        win32gui.SetForegroundWindow(self._game_hwnd)
        win32api.keybd_event(win32con.VK_MENU, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
        win32api.keybd_event(win32con.VK_MENU, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)

    def _get_window_hwnd(self) -> int:
        hwnd = self._get_hwnd_from_proc_name()

        if not hwnd:
            raise RuntimeError('Could not find process window!')

        return hwnd

    def _get_hwnd_from_proc_name(self) -> int:
        for proc in psutil.process_iter():
            if proc.name() == self._process_name:
                pid = proc.pid
                break
        else:
            raise RuntimeError('Couldn\'t find game window!')

        def callback(hwnd, hwnds):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
            return True

        hwnds = []
        win32gui.EnumWindows(callback, hwnds)
        return hwnds[0]

    def _send_msg(self, command: list) -> None:
        key, delay = command[0], int(command[1])

        if key.lower() == 'tab':
            key = win32con.VK_TAB
        elif key.lower() == 'f1':
            key = win32con.VK_F1
        else:
            key = ord(key.upper()) if len(key) == 1 else None

        if key:
            win32api.SendMessage(self._game_hwnd, win32con.WM_KEYDOWN, key, 0)
            win32api.SendMessage(self._game_hwnd, win32con.WM_KEYUP, key, 0)

        self._timer.start(delay + 200)

