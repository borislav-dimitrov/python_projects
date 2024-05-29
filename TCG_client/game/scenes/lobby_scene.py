import pygame

import game.colors as colors
from .base_scene import BaseScene
from game.widgets import Button, CharacterPanel
from game.fonts import BASE_FONT_BLACK


class LobbyScene(BaseScene):
    def __init__(self, game, name: str, id_: int):
        super().__init__(game, name, id_)
        self.background = pygame.image.load(r'.\game\art\lobby\bg.jpg')
        self.background = pygame.transform.scale(self.background, self.game.resolution)

        buttons_bg = colors.BaseColor(0, 255, 0)
        buttons_hover = colors.BaseColor(153, 255, 153)

        self.log_out_btn = Button(
            'Exit', self.game.width - 70 - 10, 10, 70, 50, self.log_out, BASE_FONT_BLACK,
            buttons_bg, buttons_hover, colors.BLACK
        )

        self.char_panel = CharacterPanel(self.game.middleware.authorized_user)

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()

        self.game.screen.blit(self.background, (0, 0))
        self.char_panel.draw(self.game.screen, mouse_pos)
        self.log_out_btn.draw(self.game.screen, mouse_pos)

    def process(self, event):
        super().process(event)

        self.log_out_btn.handle_event(event)
        self.char_panel.handle_event(event)

    def clear(self):
        pass

    def log_out(self):
        if self.game.middleware.client:
            self.game.middleware.client.disconnect()

        self.game.scene_manager.change_scene(self.game.scene_manager.login_scene)
