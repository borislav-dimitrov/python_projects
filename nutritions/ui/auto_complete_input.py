from PyQt6 import QtCore, QtWidgets


class AutoCompleteInput(QtWidgets.QLineEdit):
    def __init__(self, initial_auto_complete_values: list[str]) -> None:
        super().__init__()
        self._completing = False
        self._auto_complete_list = initial_auto_complete_values
        self._auto_complete_model = QtCore.QStringListModel(self._auto_complete_list)
        self._auto_completer = QtWidgets.QCompleter(self._auto_complete_model)

        self._auto_completer.setCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self._auto_completer.setFilterMode(QtCore.Qt.MatchFlag.MatchContains)
        self._auto_completer.setWidget(self)
        self._auto_completer.activated.connect(self._handle_completion)
        self.textChanged.connect(self._handle_text_changed)

    def update_auto_complete_list(self, new_list: list[str]) -> None:
        self._auto_complete_list = new_list
        self._auto_complete_model.setStringList(self._auto_complete_list)

    def _handle_completion(self, text: str) -> None:
        if not self._completing:
            self._completing = True
            prefix = self._auto_completer.completionPrefix()
            self.setText(self.text()[:-len(prefix)] + text)
            self._completing = False

    def _handle_text_changed(self, text: str) -> None:
        if not self._completing:
            found = False
            prefix = text.rpartition(',')[-1]

            if len(prefix):
                self._auto_completer.setCompletionPrefix(prefix)

                if self._auto_completer.currentRow() >= 0:
                    found = True

            if found:
                self._auto_completer.complete()
            else:
                self._auto_completer.popup().hide()

