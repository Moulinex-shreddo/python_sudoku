import sys
from libs.main_window import main_window
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = main_window()

    window.show()
    sys.exit(app.exec_())