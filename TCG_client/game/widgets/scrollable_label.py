import pygame
from game.fonts import BaseFont, BASE_FONT_BLACK, BASE_FONT_WHITE
from game.colors import *
from .label import Label


class ScrollableLabel(Label):
    def __init__(
            self, rect: pygame.Rect, btn_bg: BaseColor,
            btn_hover: BaseColor, font: BaseFont = BASE_FONT_WHITE, text: str = ''
    ):
        buttons_width = 50
        buttons_height = 50
        lbl_buttons_gap = 10
        self.lbl_rect = pygame.Rect(rect.x, rect.y, rect.w - (buttons_width + lbl_buttons_gap), rect.h)
        self.button_up_rect = pygame.Rect(
            self.lbl_rect.x + self.lbl_rect.w + lbl_buttons_gap,
            self.lbl_rect.y + buttons_height,
            buttons_width,
            buttons_height
        )
        self.button_down_rect = pygame.Rect(
            self.lbl_rect.x + self.lbl_rect.w + lbl_buttons_gap,
            self.lbl_rect.y + self.lbl_rect.h - (buttons_height * 2),
            buttons_width,
            buttons_height
        )
        super().__init__(self.lbl_rect, text, font)
        self.btn_bg = btn_bg
        self.btn_hover = btn_hover

    def draw(self, screen, mouse_pos=None):
        screen.blit(self.lbl_surface, (self.rect.x, self.rect.y))

        hover_up = self._check_hover(self.button_up_rect, mouse_pos)
        color_up = self.btn_bg if not hover_up else self.btn_hover
        hover_down = self._check_hover(self.button_down_rect, mouse_pos)
        color_down = self.btn_bg if not hover_down else self.btn_hover

        pygame.draw.rect(screen, color_up(), self.button_up_rect, border_radius=10)
        pygame.draw.rect(screen, BLACK(), self.button_up_rect, 2, border_radius=10)
        pygame.draw.rect(screen, color_down(), self.button_down_rect, border_radius=10)
        pygame.draw.rect(screen, BLACK(), self.button_down_rect, 2, border_radius=10)

        spacing = 30
        pygame.draw.polygon(
            screen, BLACK(), [
                (self.button_down_rect.x + self.button_down_rect.w // 2, self.button_down_rect.y + spacing),
                (
                    self.button_down_rect.x + self.button_down_rect.w // 4,
                    self.button_down_rect.y + self.button_down_rect.h - spacing
                ),
                (
                    self.button_down_rect.x + 3 * self.button_down_rect.w // 4,
                    self.button_down_rect.y + self.button_down_rect.h - spacing
                )
            ], 0
        )
        pygame.draw.polygon(
            screen, BLACK(), [
                (
                    self.button_up_rect.x + self.button_up_rect.w // 2,
                    self.button_up_rect.y + self.button_up_rect.h - spacing
                ),
                (self.button_up_rect.x + self.button_up_rect.w // 4, self.button_up_rect.y + spacing),
                (self.button_up_rect.x + 3 * self.button_up_rect.w // 4, self.button_up_rect.y + spacing)
            ], 0
        )
        super().setup_surface()
        super().draw(screen, mouse_pos)

    def show_multiple_messages(self, messages: list[str]):
        for msg in messages:
            self.text += f'{msg}\n\n'

    @staticmethod
    def _check_hover(rect: pygame.Rect, mouse_pos) -> bool:
        if rect.collidepoint(mouse_pos):
            return True

        return False

    def _scroll_up(self):
        # TODO
        pass

    def _scroll_down(self):
        # TODO
        pass
