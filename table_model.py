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
            value = self._data[index.row()][index.column()]

            if value >= 5:
                return QtGui.QColor('red')

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])