class BaseScene:
    '''Base Scene Class to be overrided for each different scene'''
    def __init__(self, game_engine):
        self.game_engine = game_engine
        self.pygame_instance = self.game_engine.pygame_instance
        self.main_surface = self.pygame_instance.display.set_mode(self.game_engine.resolution)

        self.scene_objects = []
        self.interractables = []

    def instantiate_scene_objects(self):
        pass

    def update_scene(self):
        '''Update the scene'''
        for obj in self.scene_objects:
            obj.update(self.main_surface)
        self.update()
        self.update_late()
        self.update_screen()

    def update(self):
        '''First update'''
        pass

    def update_late(self):
        '''Late update [after the first update]'''
        pass

    def update_screen(self):
        '''Update screen content'''
        # Ground
        self.update_ground()

        # Decorations over the ground
        self.update_decorations_1()
        self.update_decorations_2()
        self.update_decorations_3()

        # Actors
        self.update_actors()

        # Decorations over actors
        self.update_decorations_4()
        self.update_decorations_5()

        # Collisions
        self.update_collisions()

        # UI
        self.update_ui_1()
        self.update_ui_2()

    def update_ground(self):
        '''Update the ground content/sprites'''
        pass

    def update_decorations_1(self):
        '''Update the decorations[1] content/sprites'''
        pass

    def update_decorations_2(self):
        '''Update the decorations[2] content/sprites'''
        pass

    def update_decorations_3(self):
        '''Update the decorations[3] content/sprites'''
        pass

    def update_decorations_4(self):
        '''Update the decorations[4] content/sprites'''
        pass

    def update_decorations_5(self):
        '''Update the decorations[5] content/sprites'''
        pass

    def update_actors(self):
        '''Update the Actors content/sprites'''
        pass

    def update_buildings(self):
        '''Update the buildings content/sprites'''
        pass

    def update_collisions(self):
        '''Update the collisions content/sprites'''
        pass

    def update_ui_1(self):
        '''Update the UI[1] content/sprites'''
        pass

    def update_ui_2(self):
        '''Update the UI[2] content/sprites'''
        pass

    def leave_scene(self):
        '''Things to do when leaving the scene'''
        self.main_surface.fill('black')
