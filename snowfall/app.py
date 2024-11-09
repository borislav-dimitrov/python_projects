import tkinter as tk
import customtkinter as ctk
from transparent_window import TransparentClickThroughWindow


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x100")
        self._snowfall_windows: list[TransparentClickThroughWindow] = []

        self._snowfall_is_on = False
        button = ctk.CTkButton(self, text='Magic', command=self._show_snowfall)
        button.pack(side=tk.TOP, fill=tk.NONE, expand=tk.FALSE, pady=30)

    def run(self):
        self.mainloop()

    def _show_snowfall(self):
        if self._snowfall_is_on:
            self._snowfall_is_on = False
            for snowfall in self._snowfall_windows:
                snowfall.destroy()
            return

        self._snowfall_is_on = True
        snowfall = TransparentClickThroughWindow(self)
        self._snowfall_windows.append(snowfall)