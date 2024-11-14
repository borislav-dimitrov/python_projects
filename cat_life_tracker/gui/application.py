import tkinter as tk
import customtkinter as ctk
import utils

from .tab_view import TabView


class Application:
    def __init__(self) -> None:
        self._root = ctk.CTk()
        self._width = 1360
        self._height = 768
        self._appearance = utils.Appearance.DARK
        self._theme = utils.CtkTheme.GREEN
        self._colors = utils.ColorThemes.Green

        self._configure_app()
        self._create_gui()

    def _configure_app(self) -> None:
        self._root.iconbitmap(r'assets\icon.ico')
        self._root.title('Cats Life Tracker')
        self._root.geometry(f'{self._width}x{self._height}')

        ctk.set_appearance_mode(self._appearance)
        ctk.set_default_color_theme(self._theme)

    def run(self) -> None:
        self._root.mainloop()

    def _create_gui(self) -> None:
        self._title = ctk.CTkLabel(
            self._root, text='Cats Life Tracker \U0001F43E',
            font=utils.Fonts.HEADER_1, text_color=self._colors.NORMAL
        )
        self._title.pack(side=tk.TOP, pady=10)

        self._tab_view = TabView(self._root)
        self._tab_view.pack(
            side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE, padx=10, pady=(0, 10)
        )
