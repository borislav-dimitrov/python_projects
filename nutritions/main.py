import sys
import traceback
from PyQt6 import QtWidgets
from ui import Window


def handle_exception(exc_type: Exception, exc_value: Exception, exc_traceback: traceback):
    raise exc_value


def main() -> None:
    sys.excepthook = handle_exception
    app = QtWidgets.QApplication(['Test'])
    window = Window(app)
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
