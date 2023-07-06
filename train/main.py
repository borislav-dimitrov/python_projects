import sys

from controllers import MainController


def main():
    main_controller = MainController(sys.argv)
    main_controller.start_app()


if __name__ == '__main__':
    main()
