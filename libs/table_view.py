from PyQt5 import QtWidgets

class table_view(QtWidgets.QTableView):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.setRowCount(9)
        self.setColumnCount(9)