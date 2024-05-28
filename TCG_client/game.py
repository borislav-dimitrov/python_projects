import sys
import time

from client import connect, MIDDLEWARE
from game import GAME


def main():
    GAME.start()
    # if connect('sky', 'flying_Cat11'):
    #     if not MIDDLEWARE.client:
    #         print('Something went wrong!')
    #         sys.exit()
    #
    #     GAME.start()
    #     time.sleep(5)
    #     GAME.stop()
    # else:
    #     sys.exit()

    print('Game Closed!')


if __name__ == '__main__':
    main()
