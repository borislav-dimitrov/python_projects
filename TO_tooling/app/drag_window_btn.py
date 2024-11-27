from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt

class DraggableButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._drag_start_pos = None
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_start_pos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._drag_start_pos is not None:
            delta = event.globalPos() - self._drag_start_pos
            main_window = self.window()
            main_window.move(main_window.pos() + delta)
            self._drag_start_pos = event.globalPos()
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_start_pos = None
            event.accept()
