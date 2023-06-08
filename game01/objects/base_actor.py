class BaseActor:
    def __init__(self, prefab, id_, name, level=1, max_hp=55, max_mp=25,
                 min_dmg=3, max_dmg=5, max_weight=100):
        self.prefab = prefab
        self.id_ = id_

        self.name = name
        self.level = level
        self.max_hp = max_hp
        self.curr_hp = self.max_hp
        self.max_mp = max_mp
        self.curr_mp = self.max_mp
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg

        self.max_weight = max_weight
        self.curr_weight = 0
