class SurfaceEngine:
    def __init__(self, pygame_instance, game_engine):
        self.game_engine = game_engine
        self.pygame_instance = pygame_instance

        self.main_surface = self.pygame_instance.display.set_mode(self.game_engine.resolution)

    def update_screen(self):
        '''Update screen content'''
        # Ground
        self._update_ground()

        # Decorations over the ground
        self._update_decorations_1()
        self._update_decorations_2()
        self._update_decorations_3()

        # Actors
        self._update_actors()

        # Decorations over actors
        self._update_decorations_4()
        self._update_decorations_5()

        # Collisions
        self._update_collisions()

        # UI
        self._update_ui_1()
        self._update_ui_2()

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

    def _update_actors(self):
        '''Update the Actors content/sprites'''
        pass

    def _update_buildings(self):
        '''Update the buildings content/sprites'''
        pass

    def _update_collisions(self):
        '''Update the collisions content/sprites'''
        pass

    def _update_ui_1(self):
        '''Update the UI[1] content/sprites'''
        pass

    def _update_ui_2(self):
        '''Update the UI[2] content/sprites'''
        pass
