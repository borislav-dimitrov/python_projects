from gui import App
from screen_brightness_control.exceptions import ScreenBrightnessError
from tkinter import messagebox

def main():
    try:
        app = App()
        app.run()
    except ScreenBrightnessError as _:
        messagebox.showerror(title='Error!', message='Unsupported monitor/s!')

if __name__ == '__main__':
    main()
