import engines.engine_settings as e_settings


class UIText:
    def __init__(self, pygame_instance, text, font_type=None, font_size=50, font_color='white',
                 anti_aliasing=False, bold=False, layer=e_settings.LAYER_MAP[e_settings.UI_1]):
        self.pygame_instance = pygame_instance

        # Settings
        self.font = self.pygame_instance.font.Font(font_type, font_size)
        self.font.bold = bold
        self.text = text
        self.font_color = font_color
        self.anti_aliasing = anti_aliasing

        # Surface[the text picture] is being displayed on the screen
        self.surface = self.font.render(self.text, self.anti_aliasing, self.font_color)
