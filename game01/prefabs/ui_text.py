class UITextPrefab:
    def __init__(self, pygame_instance, text, font_type=None, font_size=50, font_color='white',
                 anti_aliasing=False, bold=False):
        self.pygame_instance = pygame_instance

        # Settings
        self.font = self.pygame_instance.font.Font(font_type, font_size)
        self.font.bold = bold
        self.text = text
        self.font_color = font_color
        self.anti_aliasing = anti_aliasing

        # Surface[the text picture] is being displayed on the screen
        self.surface = self.font.render(self.text, self.anti_aliasing, self.font_color)

    @property
    def width(self):
        return self.surface.get_width()

    @property
    def height(self):
        return self.surface.get_height()
