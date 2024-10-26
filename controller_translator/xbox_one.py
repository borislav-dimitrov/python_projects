import controller_map as mapping
from keyboard import Input
import math


class XBoxOneTranslate:
    def __init__(self, right_stick_mouse=True):
        self.right_stick_mouse = right_stick_mouse

        self.arrows_x = {'cmd': 'ABS_HAT0X', 'value': 0}
        self.arrows_y = {'cmd': 'ABS_HAT0Y', 'value': 0}
        self.left_stick_x = {'cmd': 'ABS_X', 'value': 0}
        self.left_stick_y = {'cmd': 'ABS_Y', 'value': 0}
        self.left_stick_click = {'cmd': 'BTN_THUMBL', 'value': 0}
        self.right_stick_x = {'cmd': 'ABS_RX', 'value': 0}
        self.right_stick_y = {'cmd': 'ABS_RY', 'value': 0}
        self.right_stick_click = {'cmd': 'BTN_THUMBR', 'value': 0}
        self.x = {'cmd': 'BTN_WEST', 'value': 0}
        self.a = {'cmd': 'BTN_SOUTH', 'value': 0}
        self.b = {'cmd': 'BTN_EAST', 'value': 0}
        self.y = {'cmd': 'BTN_NORTH', 'value': 0}
        self.lb = {'cmd': 'BTN_TL', 'value': 0}
        self.lt = {'cmd': 'ABS_Z', 'value': 0}
        self.rb = {'cmd': 'BTN_TR', 'value': 0}
        self.rt = {'cmd': 'ABS_RZ', 'value': 0}
        self.minus = {'cmd': 'BTN_START', 'value': 0}
        self.plus = {'cmd': 'BTN_SELECT', 'value': 0}


    def read(self, event_type, event_code, event_state, debug=False):
        if 'Sync' in event_type:
            return

        if debug:
            print(event_type, event_code, event_state)

        if event_code == self.arrows_x['cmd']:
            self.arrows_x['value'] = event_state
            # self._handle_arrows_input_x()
        elif event_code == self.arrows_y['cmd']:
            self.arrows_y['value'] = event_state
            # self._handle_arrows_input_y()
        elif event_code == self.left_stick_x['cmd']:
            self.left_stick_x['value'] = event_state
            # self._handle_left_stick_x()
        elif event_code == self.left_stick_y['cmd']:
            self.left_stick_y['value'] = event_state
            # self._handle_left_stick_y()
        elif event_code == self.left_stick_click['cmd']:
            self.left_stick_click['value'] = event_state
        elif event_code == self.right_stick_x['cmd']:
            self.right_stick_x['value'] = event_state
            # self._handle_right_stick_x()
        elif event_code == self.right_stick_y['cmd']:
            self.right_stick_y['value'] = event_state
            # self._handle_right_stick_y()
        elif event_code == self.right_stick_click['cmd']:
            self.right_stick_click['value'] = event_state
        elif event_code in self.x['cmd']:
            self.x['value'] = event_state
            # self._handle_xaby()
        elif event_code in self.a['cmd']:
            self.a['value'] = event_state
            # self._handle_xaby()
        elif event_code in self.b['cmd']:
            self.b['value'] = event_state
            # self._handle_xaby()
        elif event_code in self.y['cmd']:
            self.y['value'] = event_state
            # self._handle_xaby()
        elif event_code == self.lb['cmd']:
            self.lb['value'] = event_state
            # self._handle_lb()
        elif event_code == self.lt['cmd']:
            self.lt['value'] = event_state
            # self._handle_lt()
        elif event_code == self.rb['cmd']:
            self.rb['value'] = event_state
            # self._handle_rb()
        elif event_code == self.rt['cmd']:
            self.rt['value'] = event_state
            # self._handle_rt()
        elif event_code == self.minus['cmd']:
            self.minus['value'] = event_state
            # self._handle_minus()
        elif event_code == self.plus['cmd']:
            self.plus['value'] = event_state
            # self._handle_plus()

    def handle_input(self):
        # self._handle_arrows_input_x()
        # self._handle_arrows_input_y()

        # self._handle_left_stick_x()
        # self._handle_left_stick_y()
        # self._handle_left_stick_click()

        # self._handle_right_stick_x()
        # self._handle_right_stick_y()
        # self._handle_right_stick_click()

        # self._handle_xaby()

        # self._handle_lb()
        # self._handle_lt()

        self._handle_rb()
        self._handle_rt()

        # self._handle_minus()
        # self._handle_plus()

    def _handle_arrows_input_x(self):
        if self.arrows_x['value'] < 0:
            Input.press_key(mapping.ARROW_LEFT)
        if self.arrows_x['value'] > 0:
            Input.press_key(mapping.ARROW_RIGHT)

    def _handle_arrows_input_y(self):
        if self.arrows_y['value'] > 0:
            Input.press_key(mapping.ARROW_DOWN)
        if self.arrows_y['value'] < 0:
            Input.press_key(mapping.ARROW_UP)

    def _handle_left_stick_x(self):
        self._generic_axis_handle(
            self.left_stick_x['value'], mapping.LEFT_STICK_LEFT, mapping.LEFT_STICK_RIGHT)

    def _handle_left_stick_y(self):
        self._generic_axis_handle(
            self.left_stick_y['value'], mapping.LEFT_STICK_DOWN, mapping.LEFT_STICK_UP)

    def _handle_left_stick_click(self):
        if self.left_stick_click['value']:
            Input.press_key(mapping.LEFT_STICK_CLICK)

    def _handle_right_stick_x(self):
        if self.right_stick_mouse:
            self._mouse_handler(axis='x', value=self.right_stick_x['value'])
        else:
            self._generic_axis_handle(
                self.right_stick_x['value'], mapping.RIGHT_STICK_LEFT, mapping.RIGHT_STICK_RIGHT)

    def _handle_right_stick_y(self):
        if self.right_stick_mouse:
            self._mouse_handler(axis='y', value=self.right_stick_y['value'])
        else:
            self._generic_axis_handle(self.right_stick_y['value'], mapping.RIGHT_STICK_DOWN, mapping.RIGHT_STICK_UP)

    def _handle_right_stick_click(self):
        if self.right_stick_click['value']:
            Input.press_key(mapping.RIGHT_STICK_CLICK)

    def _handle_xaby(self):
        if self.x['value']:
            Input.press_key(mapping.X)
        if self.a['value']:
            Input.press_key(mapping.A)
        if self.b['value']:
            Input.press_key(mapping.B)
        if self.y['value']:
            Input.press_key(mapping.Y)

    def _handle_lb(self):
        if self.lb['value']:
            Input.press_key('s')

    def _handle_lt(self):
        self._generic_trigger_handle(self.lt['value'], mapping.LT)

    def _handle_rb(self):
        if self.rb['value']:
            Input.press_key('l')

    def _handle_rt(self):
        self._generic_trigger_handle(self.rt['value'], mapping.RT)

    def _handle_minus(self):
        if not self.minus['value']:
            return
        Input.press_key(mapping.MINUS)

    def _handle_plus(self):
        if not self.plus['value']:
            return
        Input.press_key(mapping.PLUS)

    @staticmethod
    def _generic_axis_handle(value, key_code_lower, key_code_higher):
        deadzone = 3500
        if value < -deadzone:
            Input.release_key(key_code_higher)
            Input.hold_key(key_code_lower)
        if value > deadzone:
            Input.release_key(key_code_lower)
            Input.hold_key(key_code_higher)
        if -deadzone < value < deadzone:
            Input.release_key(key_code_lower)
            Input.release_key(key_code_higher)

    @staticmethod
    def _mouse_handler(axis, value):
        if value < 0:
            Input.move_mouse(axis)
        if value > 0:
            Input.move_mouse(axis, low=False)

    @staticmethod
    def _generic_trigger_handle(value, key_code):
        if value > 0:
            # Load game 2 ctrl + num 1
            Input.hold_key('alt')
            Input.press_key('num1')
            Input.release_key('alt')
        elif value < 0:
            # Save game 2 alt + num 1
            Input.hold_key('ctrl')
            Input.press_key('num1')
            Input.release_key('ctrl')

    @staticmethod
    def _generic_button_press(key_code):
        Input.press_key(key_code)