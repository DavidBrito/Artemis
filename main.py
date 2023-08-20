import sys
from PyQt5 import QtWidgets

from controllers.login_widget_controller import LoginWidget

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = LoginWidget()
    win.show()
    sys.exit(app.exec())