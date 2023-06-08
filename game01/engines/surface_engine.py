import engines.engine_settings as e_settings

from assets.actor import Actor
from assets.ui_text import UIText


class SurfaceEngine:
    def __init__(self, pygame_instance, game_engine):
        self.game_engine = game_engine
        self.pygame_instance = pygame_instance

        self.main_surface = self.pygame_instance.display.set_mode(self.game_engine.resolution)

        self.sky = self.pygame_instance.image.load('art/graphics/Sky.png')
        self.ground = self.pygame_instance.image.load('art/graphics/ground.png')

        self.test_player = Actor(self.pygame_instance, sprite_path='art/graphics/smile.png', name='smile')
        self.test_text = UIText(self.pygame_instance, 'SOME text', font_type='art/graphics/font/Pixeltype.ttf')


    def update_screen(self):
        '''Update screen content'''
        # Ground
        self._update_ground()

        # Decorations over the ground
        self._update_decorations_1()
        self._update_decorations_2()
        self._update_decorations_3()

        # Actors
        self._update_players()
        self._update_npcs()

        # Decorations over actors
        self._update_decorations_4()
        self._update_decorations_5()

        # Collisions
        self._update_collisions()

        # UI
        self._update_base_ui()
        self._update_ui_windows()

    def _update_ground(self):
        '''Update the ground content/sprites'''
        pass

    def _update_decorations_1(self):
        '''Update the decorations[1] content/sprites'''
        pass

    def _update_decorations_2(self):
        '''Update the decorations[2] content/sprites'''
        pass

    def _update_decorations_3(self):
        '''Update the decorations[3] content/sprites'''
        pass

    def _update_decorations_4(self):
        '''Update the decorations[4] content/sprites'''
        pass

    def _update_decorations_5(self):
        '''Update the decorations[5] content/sprites'''
        pass

    def _update_players(self):
        '''Update the players content/sprites'''
        self.main_surface.blit(self.test_player.surface, (self.game_engine.game_width / 2, self.sky.get_height() - self.test_player.surface.get_height()))

    def _update_npcs(self):
        '''Update the NPCs content/sprites'''
        pass

    def _update_buildings(self):
        '''Update the buildings content/sprites'''
        pass

    def _update_collisions(self):
        '''Update the collisions content/sprites'''
        pass

    def _update_base_ui(self):
        '''Update the base UI content/sprites'''
        self.main_surface.blit(self.test_text.surface,
            ((self.game_engine.game_width / 2) - (self.test_text.surface.get_width() / 2),
             self.test_text.surface.get_height()))

    def _update_ui_windows(self):
        '''Update the UI windows content/sprites'''
        pass
