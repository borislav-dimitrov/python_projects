import tkinter as tk
from tkinter import ttk
import tkinterdnd2 as tk_dnd

def main():
    root = tk_dnd.Tk()
    root.geometry('300x50')

    lbl = ttk.Label(root, text='some label', width=25)
    lbl.pack()

    lbl.drop_target_register(tk_dnd.DND_FILES)
    lbl.dnd_bind('<<Drop>>', drop)

    root.mainloop()


def drop(event):
    drop_info = event.data
    if '{' in drop_info and '}' in drop_info:
        path_info = handle_path_with_spaces(drop_info)
    else:
        path_info = handle_path_without_spaces(drop_info)

    print(path_info)


def handle_path_with_spaces(drop_info):
    '''
    When there are paths including spaces in them the drag and drop module
    encloses them in parentheses {} so the info needs to be cleaned up first.

    :param drop_info: str
    :return: list(str)
    '''
    cleanup = [i.strip() for i in drop_info.split('}') if i]
    cleanup = [i[1:] if i[0] == '{' else i for i in cleanup]
    return cleanup


def handle_path_without_spaces(drop_info):
    '''
    When there are no spaces in the paths the drag and drop module separates them by spaces.
    So just split the string and return it.

    :param a: str
    :return: list(str)
    '''
    return drop_info.split(' ')


if __name__ == '__main__':
    main()
