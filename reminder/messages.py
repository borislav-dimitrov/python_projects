import os
import winsound


def play_sound():
    winsound.PlaySound('sound_effect.wav', winsound.SND_ALIAS)


class Reminder:
    def __init__(self, message: str, seconds: int) -> None:
        self.message = message
        self.seconds = seconds
        self.last_message_shown = 0

    def show(self, seconds_passed: int) -> None:
        self.last_message_shown = seconds_passed
        cmd = f'start "" msg %username% {self.message}'
        os.system(cmd)
        play_sound()