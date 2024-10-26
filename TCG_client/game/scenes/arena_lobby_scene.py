from .base_scene import BaseScene
import pygame


class ArenaScene(BaseScene):
    def __init__(self, game, name: str, id_: int):
        super().__init__(game, name, id_)
        self.background = pygame.image.load(r'.\game\art\lobby\bg.jpg')
        self.background = pygame.transform.scale(self.background, self.game.resolution)
