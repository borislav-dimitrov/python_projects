import client.client_obj


class MiddleWare:
    def __init__(self):
        self.client: client.client_obj.Client | None = None


MIDDLEWARE = MiddleWare()
