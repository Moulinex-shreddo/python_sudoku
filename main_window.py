from PyQt5 import QtWidgets
from table_model import table_model

height = 600
width = 1000 

def generate_empty_data():
    return [[0 for i in range(9)] for j in range(9)]

class main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.create_table_view()

        self.setMinimumSize(width, height)
        self.setWindowTitle("PySudoku")
        self.setCentralWidget(self._table_view)

    def create_table_view(self):
        data = generate_empty_data()

        self._table_view = QtWidgets.QTableView()
        self._table_model = table_model(data)

        self._table_view.setModel(self._table_model)