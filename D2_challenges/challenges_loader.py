import json


class Loader:
    def __init__(self, challenges_file=r'challenges.json'):
        self.challenges_file = challenges_file
        self.raw_challenges_data = {}

    def load(self):
        '''Load the challenges'''
        with open(self.challenges_file, 'r') as fh:
            self.raw_challenges_data = json.load(fh)