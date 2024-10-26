import sys

from .client_obj import CLIENT
from threading import Thread
from .middleware import MIDDLEWARE


def connect(username: str, password: str, debug: bool = False) -> bool:
    if debug:
        login_info = {
            'username': 'testUser01',
            'password': 'testPassword01'
        }
    else:
        login_info = {
            'username': username,
            'password': password
        }

    thread = Thread(target=CLIENT.connect, args=(login_info,))
    thread.start()

    # Wait client connection
    while CLIENT.connected is None:
        pass

    # Wait client authorization
    while MIDDLEWARE.authorized_user is None:
        pass

    # Exit if not connected
    if not CLIENT.connected:
        return False

    # Disconnect and exit if not
    if not MIDDLEWARE.authorized_user:
        CLIENT.disconnect()
        return False

    MIDDLEWARE.client = CLIENT
    return True
