class BaseScene:
    def __init__(self, name: str, id_: int):
        self.name = name
        self.id_ = id_

    def draw(self, game):
        pass

    def process(self, game, event):
        pass

    def clear(self, game):
        pass
