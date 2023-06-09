from prefabs.ui_text import UITextPrefab
from prefabs.button import Button
from .base_scene import BaseScene

class CharacterScreenScene(BaseScene):
    def __init__(self, name, game_engine):
        super().__init__(game_engine)
        self.scene_name = name

        self._instantiate_scene_objects()

    def _instantiate_scene_objects(self):
        super().instantiate_scene_objects()
        game_width = self.game_engine.game_width
        game_height = self.game_engine.game_height

        self.title = UITextPrefab(pygame_instance=self.pygame_instance, x=0, y=50, text='Character Screen')
        self.title.x = self.game_engine.game_width / 2 - self.title.text_width / 2
        self.scene_objects.append(self.title)

        self.create_btn = Button(pygame_instance=self.pygame_instance, x=(game_width / 2) - (game_width / 4), y=game_height - 100,
                                 text='Create', on_click=self._create_btn_onclick)
        self.scene_objects.append(self.create_btn)
        self.interractables.append({
            'object': self.create_btn,
            'x1': self.create_btn.x,
            'x2': self.create_btn.x + self.create_btn.width,
            'y1': self.create_btn.y,
            'y2': self.create_btn.y + self.create_btn.height
            })

        self.delete_btn = Button(pygame_instance=self.pygame_instance, x=game_width / 2, y=game_height - 100,
                                 text='Delete', on_click=self._delete_btn_onclick)
        self.scene_objects.append(self.delete_btn)
        self.interractables.append({
            'object': self.delete_btn,
            'x1': self.delete_btn.x,
            'x2': self.delete_btn.x + self.delete_btn.width,
            'y1': self.delete_btn.y,
            'y2': self.delete_btn.y + self.delete_btn.height
            })

        self.start_btn = Button(pygame_instance=self.pygame_instance, x=(game_width / 2) + (game_width / 4), y=game_height - 100,
                                text=' Start ', on_click=self._start_btn_onclick)
        self.scene_objects.append(self.start_btn)
        self.interractables.append({
            'object': self.start_btn,
            'x1': self.start_btn.x,
            'x2': self.start_btn.x + self.start_btn.width,
            'y1': self.start_btn.y,
            'y2': self.start_btn.y + self.start_btn.height
            })

    def update_scene(self):
        super().update_scene()

    def update_ui_1(self):
        self.main_surface.blit(self.title.surface, (self.title.x, self.title.y))

    def update_ui_2(self):
        pass

    # region Scene Specific
    def _create_btn_onclick(self):
        print('Creating')

    def _delete_btn_onclick(self):
        print('Deleting')

    def _start_btn_onclick(self):
        print('Starting')
        self.game_engine.scene_manager.change_scene('Act1Scene1')
    # endregion

