from inputs import get_gamepad
from controller_map import BUTTON_MAPPING
from keyboard import Input

def main_func():
    print('Running')
    while True:
        events = get_gamepad()
        for event in events:
            key = None
            if event.ev_type == 'Absolute':
                treshold = 30000
                if event.state > treshold:
                    key = BUTTON_MAPPING.get(event.code)[1]
                if event.state < treshold:
                    key = BUTTON_MAPPING.get(event.code)[0]
            if event.ev_type == 'Key' and event.state == 1:
                key = BUTTON_MAPPING.get(event.code)

            if key:
                Input.press_key(key)

if __name__ == '__main__':
    main_func()