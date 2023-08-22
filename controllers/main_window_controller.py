import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

# Import Interface da Tela Principal
from ui.ui_main_window import Ui_MainWindow

# Importando Novas Telas
from controllers.security_control_controller import SecurityControlWidget

class MainWindow:
    def __init__(self):
        self.qwindow = QMainWindow()
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self.qwindow)

        self.security_control_widget = SecurityControlWidget()
        self.main_window.stackedWidget.addWidget(self.security_control_widget)

        self.main_window.stackedWidget.setCurrentWidget(self.main_window.temperature_bar_chart)

        self.main_window.pushButton.clicked.connect(lambda: self.change_stacked_widget(self.main_window.temperature_bar_chart))
        self.main_window.pushButton_3.clicked.connect(lambda: self.change_stacked_widget(self.security_control_widget))

    def show(self):
        self.qwindow.show()

    def change_stacked_widget(self, widget):
        self.main_window.stackedWidget.setCurrentWidget(widget)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
