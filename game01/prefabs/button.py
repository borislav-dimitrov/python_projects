from .ui_text import UITextPrefab

class Button(UITextPrefab):
    def __init__(self, pygame_instance, x, y, text, color='white', hover_color='gray', on_click=None, font_type=None, font_size=50,
                 font_color='black', anti_aliasing=False, bold=False):
        super().__init__(pygame_instance, x, y, text, font_type, font_size, font_color, anti_aliasing, bold)
        self.color = color
        self.hover_color = hover_color

        self.text_x = x
        self.text_y = y
        self.x = x - 10
        self.y = y - 10
        self.width = self.text_width + 20
        self.height = self.text_height + 20

        self.on_click = on_click

    def draw(self, surface):
        rect = self.pygame_instance.draw.rect(
            surface, self.color, self.pygame_instance.Rect(self.x, self.y, self.width, self.height))
        surface.fill(self.color, rect)
        surface.blit(self.surface, (self.text_x, self.text_y))
        self.pygame_instance.display.flip()

    def highlight(self, surface):
        rect = self.pygame_instance.draw.rect(
            surface, self.hover_color, self.pygame_instance.Rect(self.x, self.y, self.width, self.height))
        surface.fill(self.hover_color, rect)
        surface.blit(self.surface, (self.text_x, self.text_y))
        self.pygame_instance.display.flip()

    def update(self, surface):
        '''Called each frame in the scene to update the widget'''
        mouse_pos = self.pygame_instance.mouse.get_pos()
        x1 = self.x
        x2 = self.x + self.width
        y1 = self.y
        y2 = self.y + self.height

        if x1 <= mouse_pos[0] <= x2 and y1 <= mouse_pos[1] <= y2:
            self.highlight(surface)
        else:
            self.draw(surface)


