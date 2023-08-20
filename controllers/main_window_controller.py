import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget

from ui.ui_main_window import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.mainwindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mainwindow)

        #self.wtf_widget = WtfWidget()
        #self.ui.stackedWidget.addWidget(self.wtf_widget)

        self.ui.stackedWidget.setCurrentWidget(self.ui.temperature_bar_chart)
        

        self.ui.pushButton.clicked.connect(self.change1)
        self.ui.pushButton_3.clicked.connect(self.change2)

    def show(self):
        self.mainwindow.show()

    def change1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.temperature_bar_chart)

    def change2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.percentage_bar_chart)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

