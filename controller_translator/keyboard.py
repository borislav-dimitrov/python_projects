import pydirectinput

class Input:
    HOLD_PAUSE = 1
    PRESS_PAUSE = 0.01
    MOUSE_PAUSE = 0.00001

    def hold_key(key_code):
        pydirectinput.PAUSE = Input.HOLD_PAUSE
        pydirectinput.keyDown(key_code)

    def release_key(key_code):
        pydirectinput.PAUSE = Input.HOLD_PAUSE
        pydirectinput.keyUp(key_code)

    def press_key(key_code):
        pydirectinput.PAUSE = Input.PRESS_PAUSE
        if key_code == 'MOUSE_LEFT':
            pydirectinput.leftClick()
        elif key_code == 'MOUSE_RIGHT':
            pydirectinput.rightClick()
        else:
            pydirectinput.press(key_code)

    def move_mouse(axis, low=True, value=15):
        pydirectinput.PAUSE = Input.MOUSE_PAUSE
        current_x, current_y = pydirectinput.position()
        if low:
            if axis == 'x':
                pydirectinput.moveTo(current_x - value, current_y)
            elif axis == 'y':
                pydirectinput.moveTo(current_x, current_y + value)
        else:
            if axis == 'x':
                pydirectinput.moveTo(current_x + value, current_y)
            elif axis == 'y':
                pydirectinput.moveTo(current_x, current_y - value)
