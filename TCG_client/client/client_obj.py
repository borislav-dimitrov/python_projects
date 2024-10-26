import socket
import pickle
from .server_settings import (
    HOST, PORT, HEADER, FORMAT, DISCON_MSG, GLOBAL_MSG, OBJECT_MSG, LOGIN_MSG,
    AUTH_MSG,
)
from client.middleware import MIDDLEWARE


class Client:
    def __init__(self):
        self.login = None

        self.host = HOST
        self.port = PORT
        self.format = FORMAT
        self.header = HEADER

        self.server: socket.socket | None = None
        self.connected = None

    def connect(self, login_info: dict) -> None:
        '''Connect to the server'''
        self.login = login_info
        MIDDLEWARE.add_game_client_message('Connecting to server...')

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            try:
                server.connect((self.host, self.port))
                self.connected = True
                self.server = server
                MIDDLEWARE.add_game_client_message('Connection established!')
            except ConnectionError as _:
                # Server not responding
                self.emergency_exit()
                return

            self.authenticate()
            self.listen()

    def authenticate(self):
        '''Authenticate to the server'''
        self.attempt_login()
        self.process_server_response()

    def listen(self):
        while self.connected:
            self.process_server_response()

    def send_msg(self, message: bytes) -> None:
        '''Send message to the server'''
        msg_len = len(message)
        send_len = str(msg_len).encode(self.format)
        send_len += b' ' * (self.header - len(send_len))

        self.server.send(send_len)
        self.server.send(message)

    def send_global_msg(self, msg: str) -> None:
        send_obj = pickle.dumps({
            'CMD': GLOBAL_MSG,
            'msg': msg
        })

        self.send_msg(send_obj)

    def send_obj(self, obj: object):
        '''Send object to the server'''
        obj_ = {
            'CMD': OBJECT_MSG,
            'object': obj
        }
        obj_ = pickle.dumps(obj_)

        self.send_msg(obj_)

    def process_server_response(self) -> None:
        '''Process the server response'''
        try:
            message_len = self.server.recv(self.header).decode(self.format)
        except ConnectionError as _:
            # Server not responding
            self.emergency_exit()
            return

        if not message_len:
            return

        self.read_server_msg(int(message_len))

    def read_server_msg(self, message_len: int) -> None:
        message = pickle.loads(self.server.recv(message_len))

        if message['CMD'] == AUTH_MSG:
            if message['user']:
                MIDDLEWARE.authorized_user = message['user']
            else:
                MIDDLEWARE.authorized_user = False
                MIDDLEWARE.add_game_client_message(f'Reason: {message["result"]["message"]}')
                self.disconnect()
        elif message['CMD'] == DISCON_MSG:
            self.disconnect()
        else:
            # Unhandled messages are skipped
            return

    def attempt_login(self):
        MIDDLEWARE.add_game_client_message('Logging in...')
        obj = {
            'CMD': LOGIN_MSG,
            'login_info': self.login
        }

        self.send_msg(pickle.dumps(obj))

    def disconnect(self):
        '''Disconnect from the server'''
        msg_obj = {
            'CMD': DISCON_MSG,
        }

        self.send_msg(pickle.dumps(msg_obj))
        self.connected = False
        MIDDLEWARE.authorized_user = False
        MIDDLEWARE.client = None

    def emergency_exit(self):
        '''Emergency exit on error'''
        MIDDLEWARE.add_game_client_message('Server not responding...')
        MIDDLEWARE.add_game_client_message('Connecting failed!')
        self.connected = False
        MIDDLEWARE.authorized_user = False
        MIDDLEWARE.client = None


CLIENT = Client()
