from PyQt5 import QtWidgets
from table_model import table_model

class main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.create_table_view()

        self.setCentralWidget(self._table)

    def create_table_view(self):
        data = [
            [4, 9, 2],
            [1, 0, 0],
            [3, 5, 0],
            [3, 3, 2],
            [7, 8, 9],
        ]

        self._table = QtWidgets.QTableView()
        self._table_model = table_model(data)

        self._table.setModel(self._table_model)