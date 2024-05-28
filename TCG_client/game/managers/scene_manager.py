from game.scenes import LoginScene, BaseScene


class SceneManager:
    def __init__(self, game):
        self.game = game
        self.active_scene: BaseScene | None = None
        self.login_scene: LoginScene = LoginScene('Login', 1)

    def change_scene(self, scene: BaseScene) -> None:
        if self.active_scene is scene:
            return

        self.clear_scene()
        self.active_scene = scene

    def clear_scene(self):
        if self.active_scene is not None:
            self.active_scene.clear(self.game)

    def process(self, event):
        if self.active_scene:
            self.active_scene.process(self.game, event)
