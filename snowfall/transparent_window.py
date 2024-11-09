import random
import tkinter as tk
from ctypes import windll

from drawer import Drawer


class TransparentClickThroughWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.attributes('-fullscreen', True)
        self.attributes('-topmost', True)
        self.wm_attributes('-transparentcolor', 'lightblue')
        self._canvas = tk.Canvas(self, background='lightblue', highlightthickness=0)
        self._canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)
        self._snowflakes = []

        self._make_click_through(self.winfo_id(), 255)
        self._draw_snowflakes()

    def _draw_snowflakes(self):
        for _ in range(25):
            x = random.randint(0, self.winfo_screenwidth())
            y = random.randint(0, self.winfo_screenheight())
            size = random.randint(6, 9)
            speed = random.uniform(.5, 1.5)
            self._create_falling_snowflake(x, y, size, speed)
        self._move_snowflakes()

    def _create_falling_snowflake(self, x, y, size, speed):
        snowflake_ids, image = Drawer.draw_snowflake(self._canvas, x, y)
        self._snowflakes.append((snowflake_ids, speed, image))

    def _move_snowflakes(self):
        for snowflake_id, speed, image in self._snowflakes:
            self._canvas.move(snowflake_id, 0, speed)

            coords = self._canvas.coords(snowflake_id)
            if coords and coords[1] >= self._canvas.winfo_height():
                self._canvas.move(snowflake_id, 0, -self._canvas.winfo_height())

        self._canvas.after(20, self._move_snowflakes)

    @staticmethod
    def _make_click_through(widget_id, transparency: int):
        gwl_ex_style = -20
        ws_ex_layered = 0x00080000
        ws_ex_transparent = 0x00000020
        hwnd = windll.user32.GetParent(widget_id)
        current_style = windll.user32.GetWindowLongW(hwnd, gwl_ex_style)
        new_style = current_style | ws_ex_layered | ws_ex_transparent
        windll.user32.SetWindowLongW(hwnd, gwl_ex_style, new_style)
        windll.user32.SetLayeredWindowAttributes(hwnd, 0, transparency, 0x2)

