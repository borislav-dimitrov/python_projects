import socket
import pickle

from .server_settings import (
    FORMAT, DISCON_MSG, GLOBAL_MSG, OBJECT_MSG, LOGIN_MSG, AUTH_MSG
)
from .middleware import MIDDLEWARE
from .authentication import authenticate
from user.user import User


class Client:
    def __init__(self, server, connection: socket.socket, address: tuple[str, int], header: int):
        self.server = server
        self.connection = connection
        self.address = address
        self.header = header
        self.format = FORMAT
        self.connected = True

        MIDDLEWARE.clients.append(self)

    def process(self):
        '''Process the server-client connection'''
        while self.connected:
            # Read message
            try:
                message_len = self.connection.recv(self.header).decode(self.format)
            except ConnectionError as err:
                # Client disconnected forcefully
                self._disconnect()
                continue

            if not message_len:
                continue

            self._react_on_message(int(message_len))

        self.connection.close()

    def _react_on_message(self, message_len: int):
        '''React on received message'''
        message = pickle.loads(self.connection.recv(message_len))

        if message['CMD'] == DISCON_MSG:
            self._disconnect()
        else:
            if message['CMD'] == GLOBAL_MSG:
                message = message['msg']
                MIDDLEWARE.show_global_message(self, message)
            elif message['CMD'] == OBJECT_MSG:
                print(f'[CLIENT: {self.address}] {message["object"]}')
            elif message['CMD'] == LOGIN_MSG:
                result, user = authenticate(message['login_info'])

                if user:
                    user.ip = self.address[0]
                    user.port = self.address[1]
                    print(f'[SERVER] User "{user.username}" has been successfully authorised!')
                else:
                    print(f'[SERVER] User has failed authorising!\nReason: {result["message"]}')

                self.send_auth_response(result, user)
            else:
                # Unhandled messages are skipped
                return

    def send_msg(self, message: bytes):
        '''Send message to the client'''
        msg_len = len(message)
        send_len = str(msg_len).encode(self.format)
        send_len += b' ' * (self.header - len(send_len))

        self.connection.send(send_len)
        self.connection.send(message)

    def send_auth_response(self, result: dict, user: User):
        '''Respond to the client'''
        obj = {
            'CMD': AUTH_MSG,
            'result': result,
            'user': user
        }

        self.send_msg(pickle.dumps(obj))

    def _disconnect(self):
        '''Handle disconnect'''
        self.connected = False
        MIDDLEWARE.clients.remove(self)
        self.server.on_disconnect(self.address)
