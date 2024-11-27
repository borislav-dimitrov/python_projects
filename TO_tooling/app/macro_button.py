from PySide6 import QtWidgets, QtCore


class MacroButton(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.macro = ''
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.RightButton:
            self._edit_macro()
        else:
            super().mousePressEvent(event)

    def _edit_macro(self) -> None:
        dialog = QtWidgets.QInputDialog()
        dialog.setWindowTitle('Macro Edit')
        dialog.setLabelText('Input new macro.\nExample: key delay, key delay...')
        dialog.setTextValue(self.macro)
        dialog.resize(400, 200)

        if dialog.exec():
            self.macro = dialog.textValue()
