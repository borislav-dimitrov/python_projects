import diff_match_patch as dmp_module
import tkinter as tk
from tkinter import ttk


def get_diff():
    file1 = 'file1.txt'
    file2 = 'file2.txt'
    file3 = 'diff.html'

    with open(file1, 'r') as handler1, open(file2, 'r') as handler2:
            lines1 = handler1.readlines()
            lines2 = handler2.readlines()

    dmp = dmp_module.diff_match_patch()
    dmp.Diff_Timeout = 60
    diff = dmp.diff_main(''.join(lines1), ''.join(lines2))
    # html = dmp.diff_prettyHtml(diff)
    dmp.diff_cleanupSemantic(diff)

    # with open(file3, 'w') as output:
    #     # output.writelines(html)
    #     for line in diff:
    #         output.write(str(line[0]).rstrip() + ' ' + str(line[1]).rstrip() + '\n')
    return diff


def add_text(text_obj, new_text, last_pos, last_line, prev_line):
    text_obj.insert(tk.END, new_text[1])
    if last_line != prev_line:
        last_pos = 0
    content = text_obj.get(f'{last_line}.{last_pos}', tk.END)

    if new_text[0] == 0:
        text_obj.tag_add('ori', f'{last_line}.{last_pos}', f'{last_line}.{len(new_text[1])}')
        text_obj.tag_config('ori', background='lightblue')
    elif new_text[0] == -1:
        text_obj.tag_add('rem', f'{last_line}.{last_pos}', f'{last_line}.{len(new_text[1])}')
        text_obj.tag_config('rem', background='red')
    elif new_text[0] == 1:
        text_obj.tag_add('add', f'{last_line}.{last_pos}', f'{last_line}.{len(new_text[1])}')
        text_obj.tag_config('add', background='lime')

    prev_line = last_line
    last_pos = len(content)
    last_line += content.count('\n') - 1

    return last_pos, last_line, prev_line

def main_func():
    last_pos = 0
    last_line = 1
    prev_line = 1

    root = tk.Tk()

    text = tk.Text(root, width=100, height=50)
    text.pack(side=tk.TOP, expand=tk.TRUE, fill=tk.BOTH)

    text1 = (0, 'original\n')
    text2 = (-1, 'removed\n')
    text3 = (1, 'added\n')
    diff = [text1, text2, text3]
    # diff = get_diff()

    for t in diff:
        last_pos, last_line, prev_line = add_text(text, t, last_pos, last_line, prev_line)


    root.mainloop()

if __name__ == '__main__':
    main_func()
