class ActorPrefab:
    def __init__(self, pygame_instance, sprite_path):
        self.pygame_instance = pygame_instance
        self.sprite = sprite_path

        # Surface[the actor sprite] is being displayed on the screen
        self.surface = self.pygame_instance.image.load(self.sprite)

    @property
    def width(self):
        return self.surface.get_width()

    @property
    def height(self):
        return self.surface.get_height()

    def update(self, surface):
        '''Called each frame in the scene to update the widget'''
        pass
