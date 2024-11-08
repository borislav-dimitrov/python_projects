import os
import sys


def resource_path(relative_path) -> str:
    try:
        # sys._MEIPASS is the files directory when opened from pyinstaller exe
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)