import client.client_obj
import user.user


class MiddleWare:
    def __init__(self):
        self.game_client_messages = []
        self.client: client.client_obj.Client | None = None
        self.authorized_user = user.user.User('test uname', 'pwd')
        self.authorized_user.ip = '1.1.1.1'
        self.authorized_user.port = 4123

    def add_game_client_message(self, message: str) -> None:
        self.game_client_messages.append(message)

    def clear_game_client_messages(self) -> None:
        self.game_client_messages.clear()


MIDDLEWARE = MiddleWare()
