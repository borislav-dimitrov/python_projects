class ActionsManager:
    def __init__(self):
        self._que = []

    def add_action(self, action):
        self._que.insert(0, action)

    @property
    def actions(self):
        return self._que