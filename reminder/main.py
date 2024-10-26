import time
import os
import winsound
from threading import Thread

SOUNDS = {
    'start1': {'file': 'start1.wav', 'len': 4},
    'start2': {'file': 'start2.wav', 'len': 1},
    'end': {'file': 'end.wav', 'len': 1},
}

TIMERS = {
    'abs': {'rest': 15, 'workout': 45},
    'pushups': {'rest': 20, 'workout': 30},
}

def main_func() -> None:
    running = True
    rest = True
    time_passed = 0
    start_sound = SOUNDS['start1']
    end_sound = SOUNDS['end']
    rest_timer = TIMERS['pushups']['rest']
    work_out_timer = TIMERS['pushups']['workout']

    while running:
        os.system('cls')

        time_passed += 1
        print(f'{time_passed}s - {"RESTING" if rest else "WORKING OUT"}')
        time.sleep(1)

        if rest:
            if time_passed == rest_timer - start_sound['len']:
                t = Thread(target=winsound.PlaySound, args=(start_sound['file'], winsound.SND_ALIAS))
                t.start()
            if time_passed >= rest_timer:
                time_passed = 0
                rest = False
        else:
            if time_passed == work_out_timer - end_sound['len']:
                t = Thread(target=winsound.PlaySound, args=(end_sound['file'], winsound.SND_ALIAS))
                t.start()
            if time_passed >= work_out_timer:
                time_passed = 0
                rest = True


if __name__ == '__main__':
    main_func()
