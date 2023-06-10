from .base_actor import BaseActor


class Enemy(BaseActor):
    def __init__(self, prefab, id_, name, level=1, max_hp=55, max_mp=25,
                 min_dmg=3, max_dmg=5, max_weight=100):
        super().__init__(prefab, id_, name, level, max_hp, max_mp, min_dmg, max_dmg, max_weight)
