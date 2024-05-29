import pygame
from typing import Callable

from game.fonts import BaseFont
from game.colors import BaseColor, LIGHT_GRAY, DARK_GRAY


class Button:
    def __init__(
            self, text: str, x: int, y: int, w: int, h: int, on_click: Callable,
            font: BaseFont, bg_color: BaseColor, hover_color: BaseColor,
            border_color: BaseColor, border_radius: int = 10, border_width: int = 2
    ):
        self.disabled = False
        self.on_click = on_click
        self.text = text
        self.font = font

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x, y, w, h)

        self.bg_color = bg_color
        self.hover_color = hover_color
        self.color = self.bg_color
        self.border_color = border_color
        self.border_width = border_width
        self.border_radius = border_radius

    def draw(self, screen, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.color = self.hover_color
        else:
            self.color = self.bg_color

        if self.disabled:
            self.color = LIGHT_GRAY
            border_color = DARK_GRAY
        else:
            border_color = self.border_color

        pygame.draw.rect(screen, self.color(), self.rect, border_radius=self.border_radius)
        pygame.draw.rect(screen, border_color(), self.rect, self.border_width, border_radius=self.border_radius)
        text_surface = self.font.render(self.text, True, self.font.color())
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if self.disabled:
            return

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and self.on_click:
                self.on_click()
