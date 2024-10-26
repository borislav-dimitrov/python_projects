class D2Class:
    def __init__(self, name: str, builds: list[str]):
        self.name = name
        self.builds = builds

    def dump(self):
        return {
            'name': self.name,
            'builds': self.builds
        }
