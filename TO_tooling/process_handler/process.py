class Process:
    def __init__(self, pid: int, process_name: str, window_title: str = '', hwnd: int = -1) -> None:
        self.pid = pid
        self.process_name = process_name
        self.window_name = window_title
        self.hwnd = hwnd
