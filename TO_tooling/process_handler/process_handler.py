from typing import Callable

import PySide6.QtWidgets
import psutil
import win32process
import win32gui
import win32con
import win32api

from .process import Process
from memory_reader import MemReader

class ProcessHandler:
    def __init__(self) -> None:
        self._game_process_name = 'client.exe'
        self._game_processes: list[Process] = []
        self._current_game_process: Process | None = None

        self._mem_reader = MemReader()
        self._gather_game_processes_info()

    def on_tick(self, game_hwnd: int, update_hp_mp_callback: Callable) -> None:
        if not game_hwnd:
            return

        selected_process = [p for p in self._game_processes if p.hwnd == game_hwnd][0]

        if selected_process and selected_process != self._current_game_process:
            self._current_game_process = selected_process
            self._mem_reader.set_current_process(self._current_game_process.pid)

        update_hp_mp_callback(self._mem_reader.get_hp_mp())

    def _gather_game_processes_info(self) -> None:
        for proc in psutil.process_iter():
            if proc.name() == self._game_process_name:
                self._game_processes.append(Process(pid=proc.pid, process_name=proc.name()))

        if not self._game_processes:
            raise RuntimeError('Could not find game window!')

        def callback(hwnd, game_processes: list[Process]):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)

            for process in game_processes:
                process_window_name = str(win32gui.GetWindowText(hwnd)).strip()
                if process.pid == found_pid and 'Talisman Online' in process_window_name:
                    process.hwnd = hwnd
                    process.window_name = process_window_name

            return True

        win32gui.EnumWindows(callback, self._game_processes)

    def focus_game_window(self, game_hwnd: int) -> None:
        win32gui.ShowWindow(game_hwnd, win32con.SW_RESTORE)
        win32gui.ShowWindow(game_hwnd, win32con.SW_SHOW)
        win32gui.SetForegroundWindow(game_hwnd)
        win32api.keybd_event(win32con.VK_MENU, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
        win32api.keybd_event(win32con.VK_MENU, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)

        for process in self._game_processes:
            if process.hwnd == game_hwnd:
                self._current_game_process = process
                self._mem_reader.set_current_process(process.pid)

    @property
    def games(self) -> list[Process]:
        return self._game_processes