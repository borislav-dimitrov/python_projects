from game.scenes import BaseScene, LoginScene, LobbyScene


class SceneManager:
    def __init__(self, game):
        self.game = game
        self.active_scene: BaseScene | None = None
        self.login_scene: LoginScene = LoginScene(self.game, 'Login', 1)
        self.lobby_scene: LobbyScene = LobbyScene(self.game, 'Lobby', 2)

    def change_scene(self, scene: BaseScene) -> None:
        if self.active_scene is scene:
            return

        self.clear_scene()
        self.active_scene = scene

    def clear_scene(self):
        if self.active_scene is not None:
            self.active_scene.clear()

    def process(self, event):
        if self.active_scene:
            self.active_scene.process(event)
