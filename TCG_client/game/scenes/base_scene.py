class BaseScene:
    def __init__(self, game, name: str, id_: int):
        self.game = game
        self.name = name
        self.id_ = id_

    def draw(self):
        pass

    def process(self, event):
        self.draw()

    def clear(self):
        pass
