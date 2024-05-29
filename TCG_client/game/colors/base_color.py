class BaseColor:
    def __init__(self, r: int = 0, g: int = 0, b: int = 0, a: int = 255) -> None:
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __call__(self, *args, **kwargs) -> tuple:
        return self.r, self.g, self.b, self.a
