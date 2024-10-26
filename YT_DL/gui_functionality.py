import os
import requests
import tkinter as tk
from tkinter import ttk, filedialog


def populate_formats(widget, available_formats):
    '''Populate all available formats to chose'''
    widget['values'] = [format_ for format_ in available_formats]


def change_format(dropdown_var, download_mgr):
    '''Change the desired format'''
    download_mgr.set_format(dropdown_var.get())


def chose_download_dir(dir_input_filed, download_mgr):
    '''Chose directory to save downloaded videos in it'''
    directory = filedialog.askdirectory()
    if os.path.isdir(directory):
        dir_input_filed.delete(0, tk.END)
        dir_input_filed.insert(0, os.path.normpath(directory))
        download_mgr.set_download_dir(os.path.normpath(directory))
    else:
        raise Exception(f'{os.path.normpath(directory)} is not a valid directory!')


def chose_file_to_import_from(dir_input_field):
    '''Chose file to import video links from'''
    filepath = filedialog.askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
    filepath = os.path.abspath(filepath.name)

    if os.path.isfile(filepath):
        dir_input_field.delete(0, tk.END)
        dir_input_field.insert(0, filepath)
    else:
        raise Exception(f'{os.path.normpath(filepath)} is not a valid text file!')


def load_links_from_file(dir_input_field, history_mgr, videos_list_lbox):
    '''Load the links from the chosen file'''
    filepath = dir_input_field.get()

    if os.path.isfile(filepath):
        content = history_mgr.load_history_file(filepath)
        for link in content:
            add_video(link, videos_list_lbox)
    else:
        raise Exception(f'{os.path.normpath(filepath)} is not a valid text file!')

def add_video(video_url, videos_list_lbox):
    '''Add video to the download list'''
    if isinstance(video_url, str):
        url = video_url
    else:
        url = video_url.get()

    all_items = videos_list_lbox.get(0, 'end')

    if not validate_video_url(url):
        tk.messagebox.showwarning(title='Warning!', message=f'"{url}" is not a valid YouTube URL!')
        return

    if url not in all_items:
        videos_list_lbox.insert('end', url)

        if not isinstance(video_url, str):
            video_url.delete(0, 'end')
    else:
        tk.messagebox.showwarning(title='Warning!', message=f'"{url}" is already in the list!')


def remove_video(videos_list_lbox):
    '''Remove video from the download list'''
    selection = [idx for idx in videos_list_lbox.curselection()]

    for idx in selection[::-1]:
        videos_list_lbox.delete(idx)


def validate_video_url(video_url):
    '''Validate YouTube video url'''
    if 'https://www.youtube.com/' not in video_url:
        return False

    request = requests.get(video_url)
    status_code = request.status_code

    if status_code == 200 and 'video unavailable' not in request.text.lower():
        return True
    return False


def download(videos_list_lbox, download_mgr, history_mgr, pb_show, pb_hide):
    '''Download button pressed'''
    pb_show()
    selection = videos_list_lbox.get(0, 'end')

    result = download_mgr.download_multiple(selection)

    if result is True:
        videos_list_lbox.delete(0, 'end')
        history_mgr.update_daily_history(selection)
        history_mgr.create_temp_history(selection)

    pb_hide()
    tk.messagebox.showinfo(title='Done..', message='Finished downloading.')

def center_window(window, width, height):
    '''Center tkinter window on the screen'''
    window.update_idletasks()

    screen_w = window.winfo_screenwidth()
    screen_h = window.winfo_screenheight()

    x = (screen_w / 2) - (width / 2)
    y = (screen_h / 2) - (height / 2)

    window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    window.update_idletasks()
