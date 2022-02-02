from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt

class table_model(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(table_model, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

        if role == Qt.ForegroundRole:
            return QtGui.QColor('blue')

        if role == Qt.BackgroundRole and (index.row()//3 + index.column()//3 == 1 or index.row()//3 + index.column()//3 == 3):
            return QtGui.QColor(252, 227, 171)

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])