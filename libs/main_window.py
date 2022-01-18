from PyQt5 import QtWidgets

from libs.item_delegate import item_delegate
from libs.table_model import table_model
import libs.solver as solver
import libs.brute_force as brute_force

height = 600
width = 900 

class main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.create_table_view()

        self.setMinimumSize(width, height)
        self.setWindowTitle("PySudoku")
        self.setCentralWidget(self._table_view)

    def create_table_view(self):
        data = brute_force.generate()

        self._table_view = QtWidgets.QTableView()

        table_item_delegate = item_delegate(self._table_view)

        self._table_view.setItemDelegate(table_item_delegate)
        self._table_model = table_model(data)

        self._table_view.setModel(self._table_model)

        #Hide headers
        self._table_view.horizontalHeader().hide()
        self._table_view.verticalHeader().hide()