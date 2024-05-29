import pygame

import user.user
from .label import Label
import game.fonts.fonts

FONT_CONSTRUCTOR = game.fonts.fonts.BaseFont


class CharacterPanel:
    def __init__(self, user_obj: user.user.User):
        self.panel_x = 0
        self.panel_y = 0
        self.panel_w = 0
        self.panel_h = 0
        self.row_gap = 10
        self.col_gap = 20

        self.user_name_panel = self._construct_player_name(user_obj.username)

    def _construct_player_name(self, player_name: str) -> Label:
        label_rect = pygame.Rect(self.panel_x + self.col_gap, self.panel_y + self.row_gap, 100, 50)
        font = FONT_CONSTRUCTOR(size=24)
        label = Label(rect=label_rect, text=player_name, font=font)

        self._recalc_dimensions(label_rect)
        return label

    def _recalc_dimensions(self, rect: pygame.Rect):
        self.panel_w += rect.w + self.col_gap
        self.panel_h += rect.h + self.row_gap

    def draw(self, screen, mouse_pos):
        self.user_name_panel.draw(screen, mouse_pos)

    def handle_event(self, event):
        pass
