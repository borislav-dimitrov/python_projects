import pygame

import user.user
from .label import Label
import game.fonts.fonts
import game.colors.colors

FONT_CONSTRUCTOR = game.fonts.fonts.BaseFont
COLOR_CONSTRUCTOR = game.colors.colors.BaseColor


class CharacterPanel:
    def __init__(self, user_obj: user.user.User = None):
        self.panel_w = 450
        self.panel_h = 200

        self.bg_img = pygame.image.load(r'.\game\assets\art\lobby\CharacterPanel_v0.1.png')
        self.bg_img = pygame.transform.scale(self.bg_img, (self.panel_w, self.panel_h))

        # self._construct_char_panel_sub_parts(user_obj.username)
        self._construct_char_panel_sub_parts('test_user')

    def _construct_char_panel_sub_parts(self, player_name: str) -> None:
        label_rect = pygame.Rect(190, 5, 250, 50)
        font = FONT_CONSTRUCTOR(size=24, color=COLOR_CONSTRUCTOR(164, 56, 25))
        self.user_name = Label(rect=label_rect, text=player_name, font=font, text_only=True)

    def draw(self, screen, mouse_pos=None):
        screen.blit(self.bg_img, (0, 0))
        self.user_name.draw(screen)

    def handle_event(self, event):
        pass
