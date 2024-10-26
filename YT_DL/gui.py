import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from gui_functionality import *

COLOR_2 = '#5c5b5b'
VERSION = 'Alpha 0.0.2'
LICENSE = 'N/A'


class Application:
    def __init__(self, download_mgr, history_mgr, width=500, height=500):
        self.download_mgr = download_mgr
        self.history_mgr = history_mgr
        self._width = width
        self._height = height

    def run(self):
        '''Run the application'''
        self.root = ThemedTk(theme='equilux')

        self._config_window()
        self._initialize_gui()
        self._create_menu_bar()

        self.root.mainloop()

    def _create_menu_bar(self):
        '''Create the app menu bar'''
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.help_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.help_menu.add_command(label='About', command=self._show_about_window)

        self.menu_bar.add_cascade(label='About', menu=self.help_menu, underline=0)

    def _show_about_window(self):
        '''Show the about window'''
        about = tk.Toplevel(self.root, background=COLOR_2)
        about.title(f'About {self.root.title()}')

        center_window(about, 350, 200)
        about_lbl = ttk.Label(about, text=f'Version: {VERSION}', font=('Arial', 20))
        about_lbl.pack(side=tk.TOP, expand=tk.TRUE)

        license_lbl = ttk.Label(about, text=f'Licensed to: {LICENSE}', font=('Arial', 20))
        license_lbl.pack(side=tk.BOTTOM, expand=tk.TRUE)

    def _config_window(self):
        '''Configure the main window settings'''
        center_window(self.root, self._width, self._height)
        self.root.title('YouTube Downloader')
        self.root.iconbitmap(rf'.\resources\icon.ico')

    def _initialize_gui(self):
        '''Initialize the gui components'''
        self.top_container = tk.Frame(self.root, background=COLOR_2)
        self.top_container.pack(side=tk.TOP, expand=tk.TRUE, fill=tk.BOTH)

        self.left_container = tk.Frame(self.top_container, background=COLOR_2)
        self.left_container.pack(side=tk.LEFT, expand=tk.TRUE, fill=tk.BOTH)
        self.right_container = tk.Frame(self.top_container, background=COLOR_2)
        self.right_container.pack(side=tk.RIGHT, expand=tk.TRUE, fill=tk.BOTH)

        self.bottom_container = tk.Frame(self.root, background=COLOR_2)
        self.bottom_container.pack(side=tk.BOTTOM, expand=tk.TRUE, fill=tk.BOTH)

        self._init_top()
        self._init_bottom()


    def _init_top(self):
        '''Init the top part'''
        self._init_left()
        self._init_right()

    def _init_bottom(self):
        '''Init the bottom part'''
        self.separator_4 = ttk.Label(self.bottom_container, text='', background=COLOR_2)
        self.separator_4.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self.download_btn = ttk.Button(self.bottom_container, text='Download', command=lambda: download(self.videos_list, self.download_mgr, self.history_mgr, self._show_loading_bar, self._hide_loading_bar))
        self.download_btn.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE)

    def _init_left(self):
        '''Init the left part'''
        self._create_format_section()

        self.separator_1 = ttk.Label(self.left_container, text='', background=COLOR_2)
        self.separator_1.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self._create_destination_section()

        self.separator_2 = ttk.Label(self.left_container, text='', background=COLOR_2)
        self.separator_2.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self._create_video_link_section()

        self.separator_3 = ttk.Label(self.left_container, text='', background=COLOR_2)
        self.separator_3.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self._create_load_from_file_section()

        # self.separator_4 = ttk.Label(self.left_container, text='', background=COLOR_2)
        # self.separator_4.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        # self._create_ads_banner_section()

    def _create_format_section(self):
        '''Create the format label / dropdown'''
        self.format_section = tk.Frame(self.left_container)
        self.format_section.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self.format_lbl = ttk.Label(self.format_section, text=' Choose format')
        self.format_lbl.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self.format_var = tk.StringVar()
        self.format_var.set(self.download_mgr.format_)

        self.format_dropdown = ttk.Combobox(self.format_section, textvariable=self.format_var)
        populate_formats(self.format_dropdown, self.download_mgr.AVAILABLE_FORMATS)
        self.format_dropdown.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self.format_dropdown.bind('<<ComboboxSelected>>', lambda event: change_format(self.format_var, self.download_mgr))

    def _create_destination_section(self):
        '''Create the destination label / input'''
        self.download_path_section = tk.Frame(self.left_container)
        self.download_path_section.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self.download_path_lbl = ttk.Label(self.download_path_section, text=' Chose download dir')
        self.download_path_lbl.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self.download_path_inpt = ttk.Entry(self.download_path_section)
        self.download_path_inpt.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self.download_path_btn = ttk.Button(self.download_path_section, text='Browse', command=lambda: chose_download_dir(self.download_path_inpt, self.download_mgr))
        self.download_path_btn.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self.download_path_inpt.insert(0, self.download_mgr.get_abs_download_dir())

    def _create_video_link_section(self):
        '''Create the video link label/input/buttons'''
        self.video_link_section = tk.Frame(self.left_container)
        self.video_link_section.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self.video_link_lbl = ttk.Label(self.video_link_section, text=' Input YouTube video link')
        self.video_link_lbl.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self.video_link_inpt = ttk.Entry(self.video_link_section)
        self.video_link_inpt.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self.add_video_link_btn = ttk.Button(self.video_link_section, text='Add', command=lambda: add_video(self.video_link_inpt, self.videos_list))
        self.add_video_link_btn.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self.rem_video_link_btn = ttk.Button(self.video_link_section, text='Remove', command=lambda: remove_video(self.videos_list))
        self.rem_video_link_btn.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

    def _create_load_from_file_section(self):
        '''Create the load from file label / input / btn'''
        self.load_from_file_section = tk.Frame(self.left_container)
        self.load_from_file_section.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self.load_from_file_lbl = ttk.Label(self.load_from_file_section, text=' Chose file to import from.\n Links separated with " | "!')
        self.load_from_file_lbl.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self.load_from_file_inpt = ttk.Entry(self.load_from_file_section)
        self.load_from_file_inpt.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self.load_from_file_btn = ttk.Button(self.load_from_file_section, text='Browse', command=lambda: chose_file_to_import_from(self.load_from_file_inpt))
        self.load_from_file_btn.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self.load_from_file_btn_2 = ttk.Button(self.load_from_file_section, text='Add to list', command=lambda: load_links_from_file(self.load_from_file_inpt, self.history_mgr, self.videos_list))
        self.load_from_file_btn_2.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

    def _create_ads_banner_section(self):
        '''Create ads banner section'''
        # To be done some day (eventually :D)
        pass

    def _init_right(self):
        '''Init the right part'''
        self.videos_list_lbl = ttk.Label(self.right_container, text=' Video List for download')
        self.videos_list_lbl.pack(side=tk.TOP, fill=tk.X, padx=2, pady=2)

        self.videos_list = tk.Listbox(self.right_container, bg=COLOR_2, selectmode=tk.MULTIPLE)
        self.videos_list.pack(expand=tk.TRUE, fill=tk.BOTH)


    def _show_loading_bar(self):
        '''Create and show the progress bar'''
        self.progress_bar = ttk.Progressbar(self.bottom_container, orient=tk.HORIZONTAL)
        self.progress_bar.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE)
        self.progress_bar.start()
        self.progress_bar['value'] = 25
        self.progress_bar.grab_set()
        self.root.update_idletasks()

        return self.progress_bar

    def _hide_loading_bar(self):
        '''Hide the progress bar'''
        self.progress_bar.grab_release()
        self.progress_bar.pack_forget()
