import pygame
from game.fonts import BaseFont, BASE_FONT_BLACK


class Label:
    def __init__(self, rect: pygame.Rect, text: str = '', font: BaseFont = BASE_FONT_BLACK):
        self.text = text
        self.font = font
        self.border_color = (0, 0, 0, 255)
        self.rect = rect
        self.txt_surface = font.render(self.text, True, self.font.color())
        self.lbl_surface = pygame.Surface((self.rect.w, self.rect.h), pygame.SRCALPHA)
        self.setup_surface()

    def setup_surface(self):
        self.lbl_surface.fill((0, 0, 0, 0))
        border_rect = self.lbl_surface.get_rect()
        border_rect.inflate(-2, -2)
        pygame.draw.rect(self.lbl_surface, (40, 40, 40, 100), border_rect, border_radius=10)
        pygame.draw.rect(self.lbl_surface, self.border_color, border_rect, 2, border_radius=10)

        self.txt_surface = self.font.render(self.text, True, self.font.color())
        text_rect = self.txt_surface.get_rect(center=self.lbl_surface.get_rect().center)
        self.lbl_surface.blit(self.txt_surface, text_rect.topleft)

    def draw(self, screen, mouse_pos=None):
        screen.blit(self.lbl_surface, (self.rect.x, self.rect.y))
