import tkinter as tk
import customtkinter as ctk

from controller import BrightnessController, Monitor

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('green')


class App:
    def __init__(self):
        self._brightness_controller = BrightnessController()
        self._allowed_monitor_len = 15

        self._root = ctk.CTk()
        self._initial_width = 300
        self._initial_height = 400
        self._monitor_entry_variables: list[ctk.StringVar | None] = []
        self._monitor_slider_variables: list[ctk.IntVar | None] = []
        self._color_primary = 'darkgray'
        self._color_on_primary = '#2CC985'
        self._color_font = 'white'
        self._font = ('Consolas', 14, 'bold')

        self._config_app()
        self._create_widgets()
        self._resize_if_needed()

    def run(self) -> None:
        self._root.mainloop()

    def _config_app(self) -> None:
        self._root.title('Brightness Controller')
        self._root.iconbitmap('icon.ico')
        self._root.resizable(False, False)
        self._root.geometry(f'{self._initial_width}x{self._initial_height}')

    def _create_widgets(self) -> None:
        self._global_frame = ctk.CTkFrame(self._root, fg_color='transparent')
        self._global_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)
        self._refresh_gui_btn = ctk.CTkButton(
            self._global_frame, text='Refresh', font=self._font, command=self._on_refresh_click
        )
        self._refresh_gui_btn.pack(side=tk.TOP, fill=tk.X, expand=tk.FALSE, padx=5, pady=(5, 0))

        self._create_brightness_widgets()

    def _create_brightness_widgets(self):
        self._brightness_widgets_frame = ctk.CTkScrollableFrame(self._global_frame, fg_color='transparent')
        self._brightness_widgets_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self._create_global_brightness_widget()

        for monitor in self._brightness_controller.monitors:
            self._create_monitor_brightness_widget(monitor)

    def _create_monitor_brightness_widget(self, monitor: Monitor):
        def slider_mouse_up_callback(_):
            entry_var.set(str(slider_var.get()))
            self._update_brightness(slider_var.get(), monitor=monitor)

        def entry_return_callback(_):
            slider_var.set(int(entry_var.get()))
            self._update_brightness(slider_var.get(), monitor=monitor)

        slider_var = ctk.IntVar(value=self._brightness_controller.get_monitor_brightness(monitor))
        self._monitor_slider_variables.append(slider_var)
        entry_var = ctk.StringVar(value=str(slider_var.get()))
        self._monitor_entry_variables.append(entry_var)

        frame = ctk.CTkFrame(self._brightness_widgets_frame, fg_color=self._color_primary)
        frame.pack(side=tk.TOP, fill=tk.X, expand=tk.TRUE, pady=10)
        text_frame = ctk.CTkFrame(frame, fg_color='transparent')
        text_frame.pack(side=tk.TOP, fill=tk.NONE, expand=tk.FALSE, anchor=tk.CENTER, pady=(5,))
        label_monitor_name = (
            monitor.monitor_name if len(monitor.monitor_name) <= self._allowed_monitor_len
            else f'{monitor.monitor_name[:self._allowed_monitor_len]}...'
        )
        label1 = ctk.CTkLabel(
            text_frame, text=f'{label_monitor_name} brightness:',
            text_color=self._color_font, font=self._font
        )
        label1.pack(side=tk.LEFT, fill=tk.NONE, expand=tk.FALSE, padx=(10,))
        brightness_input = ctk.CTkEntry(
            text_frame, textvariable=entry_var, width=40, validate=tk.ALL, text_color=self._color_font,
            fg_color=self._color_primary, border_color=self._color_font, font=self._font,
            validatecommand=(self._root.register(self._validate_entry), '%P')
        )
        brightness_input.pack(side=tk.LEFT, fill=tk.NONE, expand=tk.FALSE)
        brightness_input.bind('<Return>', entry_return_callback)
        label3 = ctk.CTkLabel(text_frame, text=' %', text_color=self._color_font, font=self._font)
        label3.pack(side=tk.LEFT, fill=tk.NONE, expand=tk.FALSE, padx=(0, 10))
        slider = ctk.CTkSlider(
            frame, from_=self._brightness_controller.min_brightness,
            to=self._brightness_controller.max_brightness, variable=slider_var
        )
        slider.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE, pady=(0, 5))
        slider.bind('<ButtonRelease-1>', slider_mouse_up_callback)

    def _create_global_brightness_widget(self):
        def slider_mouse_up_callback(_):
            entry_var.set(str(slider_var.get()))
            self._update_brightness(slider_var.get(), is_global=True)

        def entry_return_callback(_):
            slider_var.set(int(entry_var.get()))
            self._update_brightness(slider_var.get(), is_global=True)

        uniq_brightness = set([monitor.brightness for monitor in self._brightness_controller.monitors])
        initial_brightness = next(iter(uniq_brightness)) if len(uniq_brightness) == 1 else 50
        slider_var = ctk.IntVar(value=initial_brightness)
        entry_var = ctk.StringVar(value=str(slider_var.get()))

        frame = ctk.CTkFrame(self._brightness_widgets_frame, fg_color=self._color_primary)
        frame.pack(side=tk.TOP, fill=tk.X, expand=tk.TRUE, pady=(5,))
        text_frame = ctk.CTkFrame(frame, fg_color='transparent')
        text_frame.pack(side=tk.TOP, fill=tk.NONE, expand=tk.FALSE, anchor=tk.CENTER, pady=(5,))
        label1 = ctk.CTkLabel(text_frame, text=f'Global brightness:', text_color=self._color_font, font=self._font)
        label1.pack(side=tk.LEFT, fill=tk.NONE, expand=tk.FALSE, padx=(10,))
        brightness_input = ctk.CTkEntry(
            text_frame, textvariable=entry_var, width=40, validate=tk.ALL, text_color=self._color_font,
            fg_color=self._color_primary, border_color=self._color_font, font=self._font,
            validatecommand=(self._root.register(self._validate_entry), '%P')
        )
        brightness_input.pack(side=tk.LEFT, fill=tk.NONE, expand=tk.FALSE)
        brightness_input.bind('<Return>', entry_return_callback)
        label3 = ctk.CTkLabel(text_frame, text=' %', text_color=self._color_font, font=self._font)
        label3.pack(side=tk.LEFT, fill=tk.NONE, expand=tk.FALSE, padx=(0, 10))
        slider = ctk.CTkSlider(
            frame, from_=self._brightness_controller.min_brightness,
            to=self._brightness_controller.max_brightness, variable=slider_var
        )
        slider.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE, pady=(0, 5))
        slider.bind('<ButtonRelease-1>', slider_mouse_up_callback)

    def _update_brightness(self, brightness_level: int, is_global: bool = False, monitor: Monitor | None = None):
        if is_global:
            self._brightness_controller.set_brightness(brightness_level)
            for entry_var, slider_var in zip(self._monitor_entry_variables, self._monitor_slider_variables):
                entry_var.set(str(brightness_level))
                slider_var.set(brightness_level)
        else:
            self._brightness_controller.set_brightness(brightness_level, monitor)

    def _refresh_gui(self):
        for widget in self._global_frame.winfo_children():
            if isinstance(widget, ctk.CTkButton):
                continue
            widget.destroy()

        self._refresh_monitors()
        self._create_brightness_widgets()
        self._resize_if_needed()

    def _refresh_monitors(self) -> None:
        self._brightness_controller.detected_monitors()

    def _on_refresh_click(self) -> None:
        if self._refresh_gui_btn.cget('state') == tk.DISABLED:
            return

        original_text = self._refresh_gui_btn.cget('text')
        self._refresh_gui_btn.configure(text='...')
        self._refresh_gui_btn.configure(state=tk.DISABLED)
        self._root.update_idletasks()

        self._refresh_gui()

        def complete_refresh():
            self._refresh_gui_btn.configure(text=original_text)
            self._refresh_gui_btn.configure(state=tk.NORMAL)

        self._root.after(300, complete_refresh)

    @staticmethod
    def _validate_entry(value: str) -> bool:
        return value.isdigit() or value == ""

    def _resize_if_needed(self):
        self._root.update_idletasks()
        required_width = 0
        offset = 30

        for widget in self._brightness_widgets_frame.winfo_children():
            required_width = widget.winfo_reqwidth()

        if required_width:
            self._root.geometry(f'{required_width + offset}x{self._initial_height}')
