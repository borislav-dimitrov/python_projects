class ItemBase:
    def __init__(self, base, min_max_def, min_str, durability, sockets, qlvl):
        self.base = base
        self.min_max_def = min_max_def
        self.qlvl = qlvl
        self.sockets = sockets
        self.durability = durability
        self.min_str = min_str
