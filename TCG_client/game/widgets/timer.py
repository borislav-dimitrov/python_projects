import threading
from typing import Callable


class Timer:
    def __init__(self, seconds: float, callback: Callable):
        timer = threading.Timer(seconds, callback)
        timer.start()
