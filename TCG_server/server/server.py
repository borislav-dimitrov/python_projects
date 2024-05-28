import socket

from threading import Thread
from .server_settings import PORT, HEADER
from .connected_client import Client
from .middleware import MIDDLEWARE


class Server:
    def __init__(self):
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = PORT
        self.header = HEADER
        self.running = False

    @property
    def active_connections_ct(self) -> int:
        '''Get the current active connections'''
        return len(MIDDLEWARE.clients)

    @property
    def active_connections_str(self) -> str:
        '''Get the active connections string'''
        return f'[CONNECTIONS STATUS] Active Connections Count: {self.active_connections_ct}'

    def start(self):
        '''Run the server'''
        print(f'[SERVER] Listening on: {self.host}:{self.port}')
        self.running = True

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((self.host, self.port))
            server.listen()

            while self.running:
                connection, address = server.accept()
                self._new_client(connection, address)
                print(self.active_connections_str)

    def _new_client(self, connection: socket.socket, address: tuple[str, int]):
        '''On new client connected'''
        client = Client(self, connection=connection, address=address, header=self.header)
        thread = Thread(target=client.process)
        thread.start()
        print(f'[CLIENT] {address} has been connected!')

    def on_disconnect(self, client: tuple[str, int]) -> None:
        '''When client disconnected'''
        print(f'[CLIENT] {client} has been disconnected!')
        print(self.active_connections_str)


SERVER = Server()
