import pygame
from game.fonts import BaseFont

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)


class InputBox:
    def __init__(
        self, x: int, y: int, w: int, h: int, font: BaseFont,
        text: str = '', color: tuple = GRAY, max_len: int = 30
    ):
        self.max_len = max_len
        self.active = False

        self.txt_surface = font.render(text, True, BLACK)

        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.text = text

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                # self.active = not self.active
                self.active = not self.active
            else:
                self.active = False

            self.color = BLUE if self.active else GRAY

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if len(self.text) < self.max_len:
                    self.text += event.unicode

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
