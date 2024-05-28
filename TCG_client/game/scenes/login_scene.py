import pygame
from game.scenes.base_scene import BaseScene
from game.widgets import InputBox


class LoginScene(BaseScene):
    def __init__(self, name: str, id_: int):
        super().__init__(name, id_)
        self.uname_input = InputBox(200, 200, 140, 32)
        self.pwd_input = InputBox(200, 300, 140, 32)

    def draw(self, game):
        background = pygame.image.load(r'.\game\art\lobby\bg.jpg')
        background = pygame.transform.scale(background, game.resolution)
        game.screen.blit(background, (0, 0))

        self.uname_input.draw(game.screen)
        self.pwd_input.draw(game.screen)

    def process(self, game, event):
        self.draw(game)
        self.uname_input.handle_event(event)
        self.pwd_input.handle_event(event)

    def clear(self, game):
        pass
