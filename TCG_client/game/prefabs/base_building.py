import pygame

pygame.mixer.init()


class BaseBuilding:
    def __init__(self, game, name: str, x: int, y: int, image: str, hover_image: str, scale: tuple | None = None):
        self.game = game
        self.x = x
        self.y = y
        self.name = name
        self.image = image
        self.hover_image = hover_image

        self.image = pygame.image.load(image)
        self.hover_image = pygame.image.load(hover_image)

        if scale:
            self.image = pygame.transform.scale(self.image, scale)
            self.hover_image = pygame.transform.scale(self.hover_image, scale)

        self.image_rect = pygame.Rect(
            self.x,
            self.y,
            self.image.get_width(),
            self.image.get_height()
        )

        self.click_sound = pygame.mixer.Sound(r'.\game\assets\sounds\click.ogg')

    def draw(self, screen, mouse_pos):
        if self.image_rect.collidepoint(mouse_pos):
            screen.blit(self.hover_image, (self.x, self.y))
        else:
            screen.blit(self.image, (self.x, self.y))

    def handle_event(self, event):
        pass

    def play_sound(self):
        self.click_sound.play()
