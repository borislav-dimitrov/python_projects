import pygame
import sys
from .surface_engine import SurfaceEngine


class GameEngine:
    def __init__(self, fps=100, resolution=(1920, 1080), title='My Game') -> None:
        # Initialize pygame
        self.pygame_instance = pygame
        self.pygame_instance.init()

        # Dimensions
        self.resolution = resolution
        self.game_width = resolution[0]
        self.game_height = resolution[1]

        # Settings
        self.title = title
        self.pygame_instance.display.set_caption(self.title)
        self.fps = fps
        self.clock = self.pygame_instance.time.Clock()

        # Surface
        self.surface_engine = SurfaceEngine(self.pygame_instance, self)

    def start(self):
        '''Start the game'''
        self.game_loop()

    def game_loop(self) -> None:
        '''The main game loop'''
        while True:
            for event in self.pygame_instance.event.get():
                if event.type == self.pygame_instance.QUIT:
                    self._on_exit()

            # Update screen content
            self.surface_engine.update_screen()

            self._update()

    def _on_exit(self) -> None:
        '''Execute this when closing the game'''
        # Code before closing the game
        # ....
        # Close the game
        self.pygame_instance.quit()
        sys.exit()

    def _update(self):
        '''Draw all elements. Update everything. And set max FPS'''
        # Draw all elements. Update everything.
        self.pygame_instance.display.update()
        # Set max fps
        self.clock.tick(self.fps)
