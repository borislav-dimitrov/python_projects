from .server_settings import FORMAT


class MiddleWare:
    def __init__(self):
        self._messages_history = []
        self.clients = []

    def process(self):
        pass

    def show_global_message(self, sender, message: str) -> None:
        '''Show the global message and keep it in the history'''
        for client in self.clients:
            if client != sender:
                client.send_msg(f'[GLOBAL MESSAGE] {message}'.encode(FORMAT))

        self._messages_history.append(message)


MIDDLEWARE = MiddleWare()
