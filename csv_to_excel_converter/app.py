import pandas as pd
import openpyxl
import os
import webbrowser
import tempfile
import customtkinter as ctk
import tkinter as tk
from listbox import ListBox


class App:
    def __init__(self) -> None:
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('green')

        self._root = ctk.CTk()
        self._root.title('CSV to XLSX converter')
        self._root.geometry('400x250')
        self._root.resizable(False, False)

        initial_output_dir = os.path.join(tempfile.gettempdir(), 'csv_to_xls')
        self._out_dir_var = ctk.StringVar(value=initial_output_dir)

        self._create_gui()

        self._converted_files_ct = 0
        self._root.protocol('WM_DELETE_WINDOW', self.exit)

    def _create_gui(self) -> None:
        '''Create the gui.'''
        self._create_item_list()
        self._create_progress_bar()
        self._create_controls()
        self._create_output()

    def _create_item_list(self) -> None:
        '''Create widgets that holds the files to be converted.'''
        self._item_lst_fr = ctk.CTkFrame(self._root, fg_color='transparent')
        self._item_lst_fr.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        self._items_list = ListBox(self._item_lst_fr)
        self._items_list.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self._item_lst_controls_fr = ctk.CTkFrame(self._item_lst_fr, fg_color='transparent')
        self._item_lst_controls_fr.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)

        self._add_file_btn = ctk.CTkButton(
            master=self._item_lst_controls_fr,
            text='Add file/s',
            width=90,
            command=self._add_file_for_conversion
        )
        self._add_file_btn.pack(
            side=tk.TOP, fill=tk.NONE, expand=tk.FALSE, padx=10, pady=(40, 0)
        )

        self._rem_file_btn = ctk.CTkButton(
            master=self._item_lst_controls_fr,
            text='Remove file',
            width=90,
            command=self._items_list.remove_item
        )
        self._rem_file_btn.pack(
            side=tk.BOTTOM, fill=tk.NONE, expand=tk.FALSE, padx=10, pady=(0, 40)
        )

    def _create_progress_bar(self) -> None:
        '''Create the progressbar widget.'''
        self._progress_fr = ctk.CTkFrame(master=self._root, fg_color='transparent')
        self._progress_fr.pack(side=tk.TOP, fill=tk.X, expand=tk.FALSE)

        self._progress = ctk.CTkProgressBar(self._progress_fr, orientation='horizontal')
        self._progress.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE, padx=10)
        self._reset_progress()

    def _create_output(self) -> None:
        '''Create the output directory widgets.'''
        self._out_fr = ctk.CTkFrame(master=self._root, fg_color='transparent')
        self._out_fr.pack(
            side=tk.BOTTOM, fill=tk.X, expand=tk.FALSE, padx=10, pady=10
        )

        self._out_lbl = ctk.CTkLabel(
            master=self._out_fr,
            text='Output dir:'
        )
        self._out_lbl.pack(side=tk.LEFT, fill=tk.NONE, expand=tk.FALSE)

        self._in_inpt = ctk.CTkEntry(
            master=self._out_fr,
            textvariable=self._out_dir_var,
            state=tk.DISABLED,
            width=230
        )
        self._in_inpt.pack(side=tk.LEFT, fill=tk.NONE, expand=tk.FALSE, padx=10)

        self._out_btn = ctk.CTkButton(
            master=self._out_fr,
            text='Change',
            width=70,
            command=self._change_output_dir
        )
        self._out_btn.pack(side=tk.LEFT, fill=tk.NONE, expand=tk.FALSE)

    def _create_controls(self) -> None:
        '''Create the control widgets.'''
        self._controls_fr = ctk.CTkFrame(master=self._root, fg_color='transparent')
        self._controls_fr.pack(
            side=tk.BOTTOM, fill=tk.X, expand=tk.FALSE, padx=10, pady=10
        )

        self._convert_btn = ctk.CTkButton(
            master=self._controls_fr,
            text='Convert files',
            width=90,
            command=self._convert_files
        )
        self._convert_btn.pack(side=tk.LEFT, fill=tk.NONE, expand=tk.FALSE)

        self._exit_btn = ctk.CTkButton(
            master=self._controls_fr,
            text='Open output dir',
            width=90,
            command=self._open_output_dir
        )
        self._exit_btn.pack(side=tk.LEFT, fill=tk.NONE, expand=tk.FALSE, padx=10)

        self._exit_btn = ctk.CTkButton(
            master=self._controls_fr,
            text='Exit',
            width=90,
            command=self.exit
        )
        self._exit_btn.pack(side=tk.RIGHT, fill=tk.NONE, expand=tk.FALSE, padx=(10, 0))

    def _add_file_for_conversion(self) -> None:
        '''Browse and add file/s for conversion.'''
        filenames = ctk.filedialog.askopenfilenames(
            filetypes=[('CSV files', '.csv')]
        )

        for filename in filenames:
            abs_file = os.path.abspath(filename)

            if os.path.abspath(filename) in self._items_list.items:
                tk.messagebox.showerror(
                    title='Error!',
                    message=f'File is already loaded - {filename}.\nSkipping this file...'
                )
                continue

            if os.path.isfile(abs_file):
                self._items_list.add_item(abs_file)

    def _change_output_dir(self) -> None:
        '''Change the output directory.'''
        directory = ctk.filedialog.askdirectory()
        if directory:
            self._out_dir_var.set(os.path.abspath(directory))

    def _open_output_dir(self) -> None:
        '''Open the output directory in the file explorer.'''
        if not os.path.exists(self._out_dir_var.get()):
            os.mkdir(self._out_dir_var.get())

        webbrowser.open(self._out_dir_var.get())

    def _update_progress(self) -> None:
        '''Update the progressbar state.'''
        percentage = self._converted_files_ct / len(self._items_list.items) * 100
        self._progress.set(percentage / 100)

    def _reset_progress(self) -> None:
        '''Reset the progress of converted files.'''
        self._converted_files_ct = 0
        self._progress.set(0)

    def _convert_files(self) -> None:
        '''Convert the specified files.'''
        self._progress.start()
        self._reset_progress()

        for file_path in self._items_list.items:
            if not os.path.isfile(file_path):
                tk.messagebox.showerror(
                    title='Error!',
                    message=f'File not found - {file_path}!\nSkipping this file...'
                )

            try:
                new_data_frame = pd.read_csv(file_path)
                xls_file_name = f'{file_path.split('.csv')[0]}.xlsx'
                xls_file_name = os.path.join(
                    self._out_dir_var.get(),
                    os.path.basename(xls_file_name)
                )
                with pd.ExcelWriter(xls_file_name, mode='w') as writer:
                    new_data_frame.to_excel(
                        writer,
                        sheet_name='Sheet1',
                        index=False,
                    )

                # Add rows border
                workbook = openpyxl.load_workbook(xls_file_name)
                worksheet = workbook.active
                border = openpyxl.styles.borders.Border(
                    left=openpyxl.styles.Side(border_style='thin'),
                    right=openpyxl.styles.Side(border_style='thin'),
                    top=openpyxl.styles.Side(border_style='thin'),
                    bottom=openpyxl.styles.Side(border_style='thin'),
                )

                for row in worksheet.iter_rows():
                    for cell in row:
                        cell.border = border

                workbook.save(xls_file_name)
                workbook.close()
            except pd.errors.EmptyDataError as _:
                tk.messagebox.showerror(
                    title='Error!',
                    message=f'File is empty - {file_path}!\nSkipping this file...'
                )
            finally:
                self._converted_files_ct += 1
                self._update_progress()

        self._progress.stop()
        tk.messagebox.showinfo(
            title='Info!',
            message=f'Conversion is done!'
        )

    def start(self) -> None:
        '''Start the application.'''
        self._root.mainloop()

    def exit(self) -> None:
        '''Exit the application.'''
        self._root.destroy()
