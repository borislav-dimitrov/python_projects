import engines.engine_settings as e_settings

class Actor:
    def __init__(self, pygame_instance, sprite_path, name, layer=e_settings.LAYER_MAP[e_settings.NPCS]):
        self.pygame_instance = pygame_instance
        self.sprite = sprite_path
        self.name = name
        self.layer = layer


        # Surface[the actor sprite] is being displayed on the screen
        self.surface = self.pygame_instance.image.load(self.sprite)


