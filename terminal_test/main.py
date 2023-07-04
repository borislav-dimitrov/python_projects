import os
from ascii_drawer import Drawer


def main():
    drawer = Drawer()
    print(drawer.img_to_ascii(r'.\art\Barbarian.png'))


if __name__ == '__main__':
    main()
