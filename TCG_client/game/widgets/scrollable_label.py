import pygame
from game.fonts import BaseFont, BASE_FONT_BLACK, BASE_FONT_WHITE
from game.colors import *
from .label import Label

pygame.mixer.init()


class ScrollableLabel(Label):
    def __init__(
            self, rect: pygame.Rect, btn_bg: BaseColor,
            btn_hover: BaseColor, font: BaseFont = BASE_FONT_WHITE, text: str = '',
            text_only: bool = False
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
        super().__init__(self.lbl_rect, text, font, text_only)
        self.btn_bg = btn_bg
        self.btn_hover = btn_hover

        self.multiple_messages = []
        self.click_sound = pygame.mixer.Sound(r'.\game\assets\sounds\click.ogg')

    def draw(self, screen, mouse_pos=None):
        screen.blit(self.lbl_surface, (self.rect.x, self.rect.y))

        color_up = self.btn_bg
        color_down = self.btn_bg

        if mouse_pos:
            hover_down = self._check_hover(self.button_down_rect, mouse_pos)
            hover_up = self._check_hover(self.button_up_rect, mouse_pos)
            if hover_up:
                color_up = self.btn_hover
            if hover_down:
                color_down = self.btn_hover

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
        if not self.multiple_messages:
            super().setup_surface()
        else:
            super().setup_surface(blit_text=False)
            self._blit_multiple()

        super().draw(screen, mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_up_rect.collidepoint(event.pos):
                self.click_sound.play()
                self._scroll_up()
            elif self.button_down_rect.collidepoint(event.pos):
                self.click_sound.play()
                self._scroll_down()

    def _blit_multiple(self):
        step = 30
        offset = step
        for message in self.multiple_messages:
            self.txt_surface = self.font.render(message, True, self.font.color())
            text_rect = self.txt_surface.get_rect(center=self.lbl_surface.get_rect().midtop)
            x_y = (text_rect[0], text_rect[1] + offset)
            self.lbl_surface.blit(self.txt_surface, x_y)
            offset += step

    def show_multiple_messages(self, messages: list[str]):
        self.multiple_messages.clear()
        for msg in messages:
            self.multiple_messages.append(msg)

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
