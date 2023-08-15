import sys
from PyQt5 import QtWidgets

from controllers.login import Login

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Login()
    win.show()
    sys.exit(app.exec())