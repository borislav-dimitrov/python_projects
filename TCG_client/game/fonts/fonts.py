from pygame.font import Font


class BaseFont(Font):
    def __init__(self, name: str | None = None, size: int = 32):
        super().__init__(name, size)
