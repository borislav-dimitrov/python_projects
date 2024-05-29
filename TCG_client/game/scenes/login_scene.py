import pygame
from game.scenes.base_scene import BaseScene
from game.widgets import InputBox, Button, ScrollableLabel, Timer
from game.fonts import BASE_FONT_BLACK
import game.colors as colors


class LoginScene(BaseScene):
    def __init__(self, game, name: str, id_: int):
        super().__init__(game, name, id_)
        self.background = pygame.image.load(r'.\game\art\lobby\bg.jpg')
        self.background = pygame.transform.scale(self.background, self.game.resolution)

        self.uname_input = InputBox(800, 400, 500, 50, font=BASE_FONT_BLACK, label='UserName: ')
        self.pwd_input = InputBox(800, 500, 500, 50, font=BASE_FONT_BLACK, label='Password: ', mask=True)

        buttons_bg = colors.BaseColor(0, 255, 0)
        buttons_hover = colors.BaseColor(153, 255, 153)
        self.output = ScrollableLabel(pygame.Rect(620, 600, 680, 250), buttons_bg, buttons_hover)

        self.submit_btn = Button(
            'Login', 550, 900, 200, 100, self.login, BASE_FONT_BLACK,
            buttons_bg, buttons_hover, colors.BLACK
        )

        self.exit_btn = Button(
            'Exit', 1200, 900, 200, 100, self.exit, BASE_FONT_BLACK,
            buttons_bg, buttons_hover, colors.BLACK
        )

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()

        self.game.screen.blit(self.background, (0, 0))
        self.uname_input.draw(self.game.screen, mouse_pos)
        self.pwd_input.draw(self.game.screen, mouse_pos)
        self.submit_btn.draw(self.game.screen, mouse_pos)
        self.exit_btn.draw(self.game.screen, mouse_pos)
        self.output.draw(self.game.screen, mouse_pos)

    def process(self, event):
        self._check_for_client_messages()

        super().process(event)
        self.uname_input.handle_event(event)
        self.pwd_input.handle_event(event)
        self.submit_btn.handle_event(event)
        self.exit_btn.handle_event(event)

    def clear(self):
        pass

    def exit(self):
        self.game.stop()

    def login(self):
        self.submit_btn.disabled = True
        self.exit_btn.disabled = True

        self.game.connect_to_server(self.uname_input.text, self.pwd_input.text)
        self.output.show_multiple_messages(self.game.middleware.game_client_messages)
        self.game.middleware.clear_game_client_messages()

        if self.game.middleware.authorized_user:
            def tmp():
                self.submit_btn.disabled = False
                self.exit_btn.disabled = False
                self.game.scene_manager.change_scene(self.game.scene_manager.lobby_scene)

            Timer(3, tmp)
        else:
            self.submit_btn.disabled = False
            self.exit_btn.disabled = False

    def _check_for_client_messages(self):
        if self.game.middleware.game_client_messages:
            self.output.show_multiple_messages(self.game.middleware.game_client_messages)
            self.game.middleware.clear_game_client_messages()
