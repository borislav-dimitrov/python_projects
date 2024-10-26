import customtkinter as ctk
import tkinter as tk
from tooltip import ToolTip


NORMAL_COLOR = '#2FA572'
HOVER_COLOR = '#106A43'


class ListBox:
    def __init__(
        self, master, width=200, height=100, fg_color='transparent',
    ) -> None:
        self._frame = ctk.CTkFrame(master=master, fg_color=fg_color, width=width, height=height)
        self._frame.pack_propagate(False)

        self._scrollable = ctk.CTkScrollableFrame(
            master=self._frame,
            scrollbar_button_color=NORMAL_COLOR,
            scrollbar_button_hover_color=HOVER_COLOR
        )
        self._scrollable.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self._items = []
        self._selected_item: ctk.CTkLabel = None

    def pack(self, *args, **kwargs) -> None:
        self._frame.pack(*args, **kwargs)

    def add_item(self, item: str) -> None:
        '''Add item to the listbox.'''
        self._items.append(item)
        self._display_item(item)

    def remove_item(self) -> None:
        '''Remove file from the listbox.'''
        for i, label in enumerate(self._scrollable.winfo_children()):
            if label == self.selected_item:
                self._items.pop(i)
                self._refresh_items()

    def _refresh_items(self) -> None:
        '''Refresh the items view.'''
        for child in self._scrollable.winfo_children():
            child.destroy()

        for item in self._items:
            self._display_item(item)

    def _display_item(self, item: str) -> str:
        '''Display item in the listbox.'''
        label = ctk.CTkLabel(self._scrollable, text=item, bg_color='transparent')
        label.pack(side=tk.TOP, fill=tk.X, expand=tk.TRUE)
        ToolTip(label, item, NORMAL_COLOR)
        label.bind('<Button-1>', lambda _: self._on_select(label))
        label.bind('<Enter>', lambda _: self._on_mouse_enter(label))
        label.bind('<Leave>', lambda _: self._on_mouse_leave(label))

        return item

    def _on_mouse_enter(self, label: ctk.CTkLabel) -> None:
        '''On mouse enter item.'''
        if self._selected_item != label:
            label.configure(bg_color=HOVER_COLOR)

    def _on_mouse_leave(self, label: ctk.CTkLabel) -> None:
        '''On mouse levae item.'''
        if self._selected_item != label:
            label.configure(bg_color='transparent')

    def _on_select(self, label: ctk.CTkLabel) -> None:
        '''On select item.'''
        if label != self._selected_item:
            # Deselect previously selected
            for child in self._scrollable.winfo_children():
                child.configure(bg_color='transparent')

            self._selected_item = label
            self._selected_item.configure(bg_color=NORMAL_COLOR)

    @property
    def items(self) -> list:
        '''Get all items in the listbox.'''
        return self._items

    @property
    def selected_item(self) -> ctk.CTkLabel | None:
        '''Get the currently selected item.'''
        return self._selected_item

    @property
    def selection(self) -> str | None:
        '''Get the current selection'''
        if self._selected_item:
            return self._selected_item.cget('text')
