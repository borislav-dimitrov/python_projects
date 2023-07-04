from PyQt6 import QtWidgets


class ReadOnlyDelegate(QtWidgets.QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        return


class PyQtTable(QtWidgets.QTableWidget):
    def __init__(self, headers, rows=0, cols=2, readonly=True):
        super().__init__(rows, cols)
        self.headers = headers
        self.rows = rows
        self.cols = cols
        self.readonly = readonly

        self.setHorizontalHeaderLabels(headers)
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        self._readonly()

    def _create_row(self):
        new_row_idx = self.currentRow() + 1
        self.insertRow(new_row_idx)
        return new_row_idx

    def remove_selected(self):
        if self.rowCount():
            self.removeRow(self.currentRow())

    # def copy_row(self):
    #     self.insertRow(self.currentRow())

    #     for col in range(self.columnCount()):
    #         if not self.item(self.currentRow() + 1, col) is None:
    #             self.setItem(self.rowCount() + 1, col, QtWidgets.QTableWidgetItem(self.item(self.rowCount() + 1, col).text()))

    def _readonly(self):
        if self.readonly:
            delegate = ReadOnlyDelegate(self)
            self.setItemDelegate(delegate)

    def _validate_row_content(self, row_content):
        if len(row_content) != len(self.headers):
            raise Exception(f'Invalid row content length - {len(row_content)}. Must be - {len(self.headers)}')

    def _duplicate_check(self, new_row):
        for idx in range(self.rowCount()):
            for i in range(self.columnCount()):
                text = self.item(idx, i)
                if text.text() == new_row[i]:
                    return True


    def add_row(self, row_content):
        self._validate_row_content(row_content)
        if self._duplicate_check(row_content):
            return
        row_nr = self._create_row()
        for idx in range(len(self.headers)):
            self.setItem(row_nr, idx, QtWidgets.QTableWidgetItem(row_content[idx]))

    def edit_row(self, row_nr, row_content):
        self._validate_row_content(row_content)
        if self._duplicate_check(row_content):
            return
        for idx in range(len(self.headers)):
            self.setItem(row_nr - 1, idx, QtWidgets.QTableWidgetItem(row_content[idx]))

    def data(self):
        result = []
        for row in range(self.rowCount()):
            row_content = []
            for col in range(self.columnCount()):
                row_content.append(self.item(row, col).text())
            result.append(row_content)
        return result

    def insert_data(self, data):
        for row in data:
            self.add_row(row)

    @property
    def selected(self):
        return self.currentRow() + 1
