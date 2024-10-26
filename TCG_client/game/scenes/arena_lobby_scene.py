import pygame

from .base_scene import BaseScene
from game.widgets import LobbyControls, ChatWidget


class ArenaLobbyScene(BaseScene):
    def __init__(self, game, name: str, id_: int = 1):
        super().__init__(game, name, id_)
        self.background = pygame.image.load(r'.\game\assets\art\arena\bg.png')
        self.background = pygame.transform.scale(self.background, self.game.resolution)

        self.rooms_frame = pygame.image.load(r'.\game\assets\art\ui\frame.png')
        self.rooms_frame = pygame.transform.scale(self.rooms_frame, (1000, 700))

        self.chat = ChatWidget()
        self.controls = LobbyControls(game)

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        self.game.screen.blit(self.background, (0, 0))

        self.game.screen.blit(self.rooms_frame, (30, 30))
        self.controls.draw(self.game.screen, mouse_pos)
        self.chat.draw(self.game.screen, mouse_pos)

    def process(self, event):
        self.draw()

        self.controls.handle_event(event)
        self.chat.handle_event(event)

    def clear(self):
        pass
