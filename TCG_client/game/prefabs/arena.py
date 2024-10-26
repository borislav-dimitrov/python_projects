import pygame

from .base_building import BaseBuilding


class Arena(BaseBuilding):
    def __init__(self, game, name: str, x: int, y: int, image: str, hover_image: str, scale: tuple | None = None):
        super().__init__(game, name, x, y, image, hover_image, scale)

    def draw(self, screen, mouse_pos):
        super().draw(screen, mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.image_rect.collidepoint(event.pos):
            self.play_sound()
            self.game.scene_manager.change_scene(self.game.scene_manager.arena_lobby_scene)
