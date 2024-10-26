import pygame

from .base_building import BaseBuilding


class TownHall(BaseBuilding):
    def __init__(self, game, name: str, x: int, y: int, image: str, hover_image: str, scale: tuple | None = None):
        super().__init__(game, name, x, y, image, hover_image, scale)
        self.image_rect = pygame.Rect(
            self.image_rect.x + 110,
            self.image_rect.y + 30,
            self.image_rect.width - 140,
            self.image_rect.height - 70
        )

    def draw(self, screen, mouse_pos):
        super().draw(screen, mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.image_rect.collidepoint(event.pos):
            self.play_sound()
            print('Town Hall Clicked!')
