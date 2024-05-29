import pygame
from game.fonts import BaseFont, BASE_FONT_WHITE
from game.colors import *
from .label import Label


class InputBox:
    def __init__(
            self, x: int, y: int, w: int, h: int, font: BaseFont,
            text: str = '', max_len: int = 30, border_color: BaseColor = BLACK,
            background_color: BaseColor = GRAY, hover_color: BaseColor = LIGHT_GRAY,
            label: str = '', mask: bool = False, border_width: int = 2,
            border_radius: int = 10
    ):
        self.mask = mask
        self.font = font
        self.max_len = max_len
        self.active = False
        self.text = text

        self.txt_surface = font.render(self.text, True, self.font.color())

        self.rect = pygame.Rect(x, y, w, h)

        self.bg_color = background_color
        self.hover_color = hover_color
        self.color = self.bg_color

        self.border_color = border_color
        self.active_border_color = BLUE
        self.current_border_color = self.border_color
        self.border_width = border_width
        self.border_radius = border_radius

        if label:
            lbl_rect_w = sum([font.font_size * .5 for _ in label])
            lbl_rect = pygame.Rect(self.rect.x - lbl_rect_w - 20, self.rect.y, lbl_rect_w, self.rect.h)
            self.label = Label(lbl_rect, label, BASE_FONT_WHITE)
        else:
            self.label = None

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

            self.current_border_color = self.active_border_color if self.active else self.border_color

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                # TODO - submit
                print(self.text)
            elif event.key == pygame.K_TAB:
                # TODO - submit
                print('Pressed Tab')
            else:
                if len(self.text) < self.max_len:
                    self.text += event.unicode

    def draw(self, screen, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.color = self.hover_color
        else:
            self.color = self.bg_color

        # Draw input box
        pygame.draw.rect(screen, self.color(), self.rect, border_radius=self.border_radius)
        pygame.draw.rect(screen, self.current_border_color(), self.rect, self.border_width, border_radius=self.border_radius)

        # Render text
        text = self.text if not self.mask else '*' * len(self.text)
        self.txt_surface = self.font.render(text, True, self.font.color())
        screen.blit(self.txt_surface, (self.rect.x + 10, self.rect.y + 15))

        # Draw label
        if self.label:
            self.label.draw(screen)
