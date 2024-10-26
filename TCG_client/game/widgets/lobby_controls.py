import pygame

from .button import Button
from game.fonts import BASE_FONT_BLACK
import game.colors as colors


class LobbyControls:
    def __init__(self, game, width: int = 1000, height: int = 70):
        self.game = game

        # region STYLE
        padding = 10
        c_width = 90
        c_height = height - (padding * 2)
        buttons_bg = colors.BaseColor(0, 255, 0)
        buttons_hover = colors.BaseColor(153, 255, 153)
        shop_bg = colors.BaseColor(255, 125, 0)
        shop_hover = colors.BaseColor(255, 167, 51)
        # endregion
        
        d_info = pygame.display.Info()
        self.x = d_info.current_w - width - padding
        self.y = d_info.current_h - height - padding
        self.controls_size = (width, height)

        self.controls_frame = pygame.image.load(r'.\game\assets\art\ui\frame.png')
        self.controls_frame = pygame.transform.scale(self.controls_frame, self.controls_size)

        tmp_c_x = self.x + (padding * 2)
        self.shop_btn = Button(
            'SHOP', tmp_c_x, self.y + padding, c_width, c_height,
            self.shop, BASE_FONT_BLACK, shop_bg, shop_hover, colors.BLACK
        )

        tmp_c_x += padding + c_width
        self.cards_btn = Button(
            'Cards', tmp_c_x, self.y + padding, c_width, c_height,
            self.cards, BASE_FONT_BLACK, buttons_bg, buttons_hover, colors.BLACK
        )

        self.exit_btn = Button(
            'Logout', d_info.current_w - 120, self.y + padding, c_width, c_height,
            self.log_out, BASE_FONT_BLACK, buttons_bg, buttons_hover, colors.BLACK
        )

    def draw(self, screen, mouse_pos):
        screen.blit(self.controls_frame, (self.x, self.y))
        self.shop_btn.draw(screen, mouse_pos)
        self.cards_btn.draw(screen, mouse_pos)
        self.exit_btn.draw(screen, mouse_pos)

    def handle_event(self, event):
        self.shop_btn.handle_event(event)
        self.cards_btn.handle_event(event)
        self.exit_btn.handle_event(event)

    def log_out(self):
        if not self.game:
            return

        if self.game.middleware.client:
            self.game.middleware.client.disconnect()

        self.game.scene_manager.change_scene(self.game.scene_manager.login_scene)
        self.game.middleware.add_game_client_message('Disconnected from server!')

    @staticmethod
    def shop():
        print('SHOP pressed')

    @staticmethod
    def cards():
        print('Cards pressed')
