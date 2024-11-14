import tkinter as tk
import customtkinter as ctk


class TabView(ctk.CTkTabview):
    def __init__(self, master: ctk.CTk, height: int | None = None) -> None:
        if height:
            super().__init__(master, height=height)
        else:
            super().__init__(master)

        self._create_widgets()

    def _create_widgets(self) -> None:
        self._create_weight_tab()
        self._create_deworming_tab()

    def _create_weight_tab(self) -> None:
        self.add('Тегло')
        weight_tab = self.tab('Тегло')

        # add scrollable frame for the table

        # add static one (not to be scrolled where the plot will live)

    def _create_deworming_tab(self) -> None:
        self.add('Обезпаразитяване')
        deworming_tab = self.tab('Обезпаразитяване')

    def switch_tab_to(self, tab_name: str) -> None:
        self.set(tab_name)

    @property
    def active_tab_name(self) -> str:
        return self.get()
