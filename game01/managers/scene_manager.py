from scenes.character_screen_scene import CharacterScreenScene
from scenes.act1_scene1 import Act1Scene1


class SceneManager:
    def __init__(self, game_engine):
        self.game_engine = game_engine

        self.scenes = [
            CharacterScreenScene(name='CharacterScreen', game_engine=self.game_engine),
            Act1Scene1(name='Act1Scene1', game_engine=self.game_engine),
            ]
        self.active_scene = None

        self.change_scene('CharacterScreen')

    def update_scene(self):
        self.active_scene.update_scene()

    def change_scene(self, new_scene):
        '''Change the current scene'''
        scene = self.get_scene(new_scene)
        if scene and self.active_scene != scene:
            if self.active_scene:
                self.active_scene.leave_scene()
            print(f'Changing scene to {new_scene}.')
            self.active_scene = scene

    def get_scene(self, scene_name):
        '''Get scene by its name'''
        for scene in self.scenes:
            if scene_name == scene.scene_name:
                return scene
