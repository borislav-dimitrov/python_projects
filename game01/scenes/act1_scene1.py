from prefabs.ui_text import UITextPrefab
from .base_scene import BaseScene

class Act1Scene1(BaseScene):
    def __init__(self, name, game_engine):
        super().__init__(game_engine)
        self.scene_name = name

        self.title = UITextPrefab(pygame_instance=self.pygame_instance, x=0, y=50, text='Act 1 Scene 1')
        self.title.x = self.game_engine.game_width / 2 - self.title.text_width / 2

    def update_ui_1(self):
        pass

    def update_ui_2(self):
        self.main_surface.blit(self.title.surface, (self.title.x, self.title.y))



