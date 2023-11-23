from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QLabel


def create_button(text, cmd=None, w=300, h=60, cursor=Qt.CursorShape.PointingHandCursor):
    btn = QPushButton(text=text)
    btn.setFixedSize(w, h)

    if cmd and callable(cmd):
        btn.clicked.connect(cmd)

    btn.setCursor(cursor)

    return btn


def create_lbl(text, w=300, h=60):
    lbl = QLabel(text=text)
    lbl.setFixedSize(w, h)

    return lbl
