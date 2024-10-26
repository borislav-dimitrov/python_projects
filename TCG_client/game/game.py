import sys

import pygame
from .game_settings import GAME_NAME, WIDTH, HEIGHT, FPS
from .managers import SceneManager
from client import connect, MIDDLEWARE

DEBUG = True


class Game:
    def __init__(self):
        self.middleware = MIDDLEWARE

        pygame.init()
        self.width = WIDTH
        self.height = HEIGHT
        self.resolution = (WIDTH, HEIGHT)
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(GAME_NAME)

        self.running = False
        self.scene_manager = SceneManager(self)
        self.scene_manager.active_scene = self.scene_manager.arena_lobby_scene

        self.sleep = 0

    def start(self):
        self.running = True

        while self.running:
            if self.sleep:
                pygame.time.wait(self.sleep * 1000)
                self.sleep = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                    return

                self.scene_manager.process(event)

            if self.running:
                pygame.display.update()
                self.clock.tick(FPS)

    def stop(self):
        self.running = False
        pygame.quit()

        if MIDDLEWARE.client:
            print('Disconnecting client')
            MIDDLEWARE.client.disconnect()

        sys.exit()

    def connect_to_server(self, username: str, password: str):
        if connect(username, password, debug=DEBUG):
            if not self.middleware.client:
                # Unknown Issue as of now
                self.middleware.add_game_client_message('Something went wrong! :(')


GAME = Game()
