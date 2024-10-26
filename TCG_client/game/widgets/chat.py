import pygame

from .button import Button
from .input_box import InputBox
from .scrollable_label import ScrollableLabel


class ChatWidget:
    def __init__(self):
        self.w = 700
        self.h = 300
        d_info = pygame.display.Info()
        self.x = 10
        self.y = d_info.current_h - self.h - 10

        self.chat_main_frame = pygame.image.load(r'.\game\assets\art\ui\frame.png')
        self.chat_main_frame = pygame.transform.scale(self.chat_main_frame, (self.w, self.h))

    def draw(self, screen, mouse_pos):
        screen.blit(self.chat_main_frame, (self.x, self.y))

    def handle_event(self, event):
        pass
