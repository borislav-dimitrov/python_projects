import pygame
from pygame.font import Font
from game.colors import BaseColor, BLACK, WHITE

pygame.font.init()


class BaseFont(Font):
    def __init__(self, name: str | None = None, size: int = 32, color: BaseColor = BLACK):
        super().__init__(name, size)
        self.font_size = size
        self.color = color


BASE_FONT_BLACK = BaseFont()
BASE_FONT_WHITE = BaseFont(color=WHITE)
