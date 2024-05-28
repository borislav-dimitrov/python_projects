import pygame
from .game_settings import GAME_NAME, WIDTH, HEIGHT, FPS
from .managers import SceneManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.width = WIDTH
        self.height = HEIGHT
        self.resolution = (WIDTH, HEIGHT)
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(GAME_NAME)

        self.running = False
        self.scene_manager = SceneManager(self)
        self.scene_manager.active_scene = self.scene_manager.login_scene

    def start(self):
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                    return

                self.scene_manager.process(event)
            pygame.display.update()
            self.clock.tick(FPS)

    @staticmethod
    def stop():
        pygame.quit()


GAME = Game()
