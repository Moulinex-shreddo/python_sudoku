from PyQt5 import QtWidgets

from libs.item_delegate import item_delegate
from libs.table_model import table_model
import libs.solver as solver
import libs.brute_force as brute_force
import libs.config as config


cell_size = 40


height = config.get_window_height()
width = config.get_window_width()


class main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.create_tool_bar()

        self.create_table_view()

        self.setMinimumSize(width, height)
        self.setWindowTitle("PySudoku")
        self.setCentralWidget(self._table_view)

        self.show()

    def create_table_view(self):
        data = brute_force.generate()

        self._table_view = QtWidgets.QTableView()

        table_item_delegate = item_delegate(self._table_view)

        self._table_model = table_model(data)

        self._table_view.setModel(self._table_model)

        
        self._table_view.setItemDelegate(table_item_delegate)

        #Resize
        for i in range(9):
            self._table_view.setColumnWidth(i, cell_size)
            self._table_view.setRowHeight(i, cell_size)

        #Hide headers
        self._table_view.horizontalHeader().hide()
        self._table_view.verticalHeader().hide()

    def reset_table_view(self, data):
        self._table_view = QtWidgets.QTableView()
        table_item_delegate = item_delegate(self._table_view)
        self._table_model = table_model(data)
        self._table_view.setModel(self._table_model)
        self._table_view.setItemDelegate(table_item_delegate)

        #Resize
        for i in range(9):
            self._table_view.setColumnWidth(i, cell_size)
            self._table_view.setRowHeight(i, cell_size)

        #Hide headers
        self._table_view.horizontalHeader().hide()
        self._table_view.verticalHeader().hide()

    def create_tool_bar(self):
        _new_action = QtWidgets.QAction("&New", self)
        _new_action.setShortcut("Ctrl+N")
        _new_action.setStatusTip("Generate New Grid")
        _new_action.triggered.connect(self.generate_new_grid)

        _exit_action = QtWidgets.QAction("&Exit", self)
        _exit_action.setShortcut("Ctrl+Q")
        _exit_action.setStatusTip("Exit")
        _exit_action.triggered.connect(QtWidgets.qApp.quit)

        _save_action = QtWidgets.QAction("&Save", self)
        _save_action.setShortcut("Ctrl+S")
        _save_action.setStatusTip("Saves the grid")
        _save_action.triggered.connect(self.save_grid)

        _load_action = QtWidgets.QAction("&Load", self)
        _load_action.setShortcut("Ctrl+O")
        _load_action.setStatusTip("Loads a grid")
        _load_action.triggered.connect(self.load_grid)

        _tool_bar = self.menuBar()
        _file_menu = _tool_bar.addMenu("&File")
        _file_menu.addAction(_new_action)
        _file_menu.addSeparator()
        _file_menu.addAction(_save_action)
        _file_menu.addAction(_load_action)
        _file_menu.addSeparator()
        _file_menu.addAction(_exit_action)

    def generate_new_grid(self):
        data = brute_force.generate()
        self.reset_table_view(data)
        self.setCentralWidget(self._table_view)

    def save_grid(self):
        s = QtWidgets.QFileDialog.getSaveFileName(self, "Save Grid", "", "Sudoku (*.sdk)")
        file_name = s[0]
        f = open(file_name, "w")
        for i in range(9):
            for j in range(9):
                f.write(str(self._table_model._data[i][j]))

        f.close()

    def load_grid(self):
        s = QtWidgets.QFileDialog.getOpenFileName(self, "Load Grid", "", "Sudoku (*.sdk)")
        file_name = s[0]
        f = open(file_name, "r")
        s = f.read()

        k = 0

        data = solver.generate_empty_data(9)

        for i in range(9):
            for j in range(9):
                data[i][j] = int(s[k])
                k += 1

        self.reset_table_view(data)
        self.setCentralWidget(self._table_view)

        f.close()
