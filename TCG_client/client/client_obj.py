import socket
import pickle
from .server_settings import (
    HOST, PORT, HEADER, FORMAT, DISCON_MSG, GLOBAL_MSG, OBJECT_MSG, LOGIN_MSG,
    AUTH_MSG,
)


class Client:
    def __init__(self):
        self.login = None

        self.host = HOST
        self.port = PORT
        self.format = FORMAT
        self.header = HEADER

        self.server: socket.socket | None = None
        self.connected = None
        self.authorized = None

    def connect(self, login_info: dict) -> None:
        '''Connect to the server'''
        self.login = login_info
        print('Connecting to server...')

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            try:
                server.connect((self.host, self.port))
                self.connected = True
                self.server = server
                print('Connection established!')
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
                self.authorized = message['user']
                print('You have logged in successfully!\n')
            else:
                self.authorized = False
                print(f'Login Failed!\n    Reason: {message["result"]["message"]}')
                self.disconnect()
        elif message['CMD'] == DISCON_MSG:
            self.disconnect()
        else:
            # Unhandled messages are skipped
            return

    def attempt_login(self):
        print('Logging in...')
        obj = {
            'CMD': LOGIN_MSG,
            'login_info': self.login
        }

        self.send_msg(pickle.dumps(obj))

    def disconnect(self):
        '''Disconnect from the server'''
        print('Disconnecting from server...')
        msg_obj = {
            'CMD': DISCON_MSG,
        }

        self.send_msg(pickle.dumps(msg_obj))
        self.connected = False
        self.authorized = False

    def emergency_exit(self):
        '''Emergency exit on error'''
        print('Server not responding...\nClient shutting down!')
        self.connected = False
        self.authorized = False


CLIENT = Client()
