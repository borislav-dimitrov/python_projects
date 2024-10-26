import pygame

from .base_scene import BaseScene
from game.widgets import CharacterPanel, LobbyControls, ChatWidget
from game.prefabs import BaseBuilding, TownHall, Arena


class LobbyScene(BaseScene):
    def __init__(self, game, name: str, id_: int):
        super().__init__(game, name, id_)
        self.background = pygame.image.load(r'.\game\assets\art\lobby\bg.jpg')
        self.background = pygame.transform.scale(self.background, self.game.resolution)

        self.char_panel = None

        self.chat = ChatWidget()
        self.controls = LobbyControls(game)

        # region BUILDINGS
        self.town_hall = TownHall(
            self.game,
            'Town Hall', 1500, 550,
            r'.\game\assets\art\lobby\town_hall.png',
            r'.\game\assets\art\lobby\town_hall_hover.png'
        )
        self.arena = Arena(
            self.game,
            'Arena', 800, 600,
            r'.\game\assets\art\lobby\Arena.bmp',
            r'.\game\assets\art\lobby\Arena_hover.bmp',
            scale=(350, 300)
        )

        self.buildings: list[BaseBuilding] = [
            self.town_hall,
            self.arena,
        ]
        # endregion

    def draw(self):
        if not self.char_panel:
            # self.char_panel = CharacterPanel(self.game.middleware.authorized_user)
            self.char_panel = CharacterPanel()

        mouse_pos = pygame.mouse.get_pos()

        self.game.screen.blit(self.background, (0, 0))
        self.controls.draw(self.game.screen, mouse_pos)
        self.char_panel.draw(self.game.screen, mouse_pos)
        self.chat.draw(self.game.screen, mouse_pos)

        for building in self.buildings:
            building.draw(self.game.screen, mouse_pos)

    def process(self, event):
        self.draw()

        self.controls.handle_event(event)
        self.char_panel.handle_event(event)
        self.chat.handle_event(event)

        for building in self.buildings:
            building.handle_event(event)

    def clear(self):
        pass
