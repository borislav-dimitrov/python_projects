from prefabs.ui_text import UITextPrefab
from .base_scene import BaseScene

class CharacterScreenScene(BaseScene):
    def __init__(self, name, game_engine):
        super().__init__(game_engine)
        self.scene_name = name

        self.title = UITextPrefab(pygame_instance=self.pygame_instance, text='Character Screen')

    def update_ui_1(self):
        pass

    def update_ui_2(self):
        self.main_surface.blit(self.title.surface, (self.game_engine.game_width / 2 - self.title.width / 2, 50))



