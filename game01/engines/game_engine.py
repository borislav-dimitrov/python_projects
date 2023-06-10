import pygame
import sys
import time
from .surface_engine import SurfaceEngine
from managers.game_manager import GameManager
from managers.scene_manager import SceneManager


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

        # Managers
        self.game_manager = None
        self.scene_manager = None

    def start(self):
        '''Start the game'''
        self._init_managers()
        self.game_loop()

    def game_loop(self) -> None:
        '''The main game loop'''
        while True:
            self._handle_pygame_events()

            # Update scene
            self.scene_manager.update_scene()

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

    def _init_managers(self):
        '''Initialise all the managers'''
        self.game_manager = GameManager(self)
        self.scene_manager = SceneManager(self)

    def _handle_pygame_events(self):
        left_click = 1
        right_click = 2
        middle_click = 3
        scroll_up = 4
        scroll_down = 5

        mouse_x, mouse_y = self.pygame_instance.mouse.get_pos()

        for event in self.pygame_instance.event.get():
            if event.type == self.pygame_instance.QUIT:
                self._on_exit()
            elif event.type == self.pygame_instance.MOUSEBUTTONDOWN:
                button = event.button
                for obj in self.scene_manager.active_scene.interractables:
                    if button == left_click:
                        if obj['x1'] <= mouse_x <= obj['x2'] and obj['y1'] <= mouse_y <= obj['y2']:
                            obj['object'].on_click()
