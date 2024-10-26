import customtkinter as ctk
import tkinter as tk

class ToolTip:
    def __init__(self, widget, text, theme_color):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self._theme_color = theme_color

        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        # Create a new top-level window for the tooltip
        if self.tooltip_window or not self.text:
            return

        OFFSET_X = 20
        OFFSET_Y = 10
        self.tooltip_window = tk.Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.wm_geometry(
            f"+{event.x_root + OFFSET_X}+{event.y_root + OFFSET_Y}"
        )

        label = tk.Label(
            self.tooltip_window,
            text=self.text,
            background=self._theme_color,
            foreground='white',
            borderwidth=1,
            relief="solid"
        )
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None
