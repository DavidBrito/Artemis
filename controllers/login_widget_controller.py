import sys
import os
import requests
from PyQt5 import QtWidgets
from dotenv import load_dotenv
from ui.ui_login_widget import Ui_Form

from controllers.main_window_controller import MainWindow

class LoginWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(LoginWidget, self).__init__()
        load_dotenv()
        try:
            self.api_host = os.environ['API_HOST']
        except Exception as e:
            print(e)
            sys.exit(1)

        self.main_window = None

        self.setupUi(self)
        self.pushButton.clicked.connect(self.checkUser)        
        self.lineEdit_2.returnPressed.connect(self.checkUser)

    def checkUser(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        response = requests.post(f"{self.api_host}/login", json={'username': username, 'password': password})
        print(response)
        if response.status_code == 200:
            access_token = response.json()['access_token']
            print("Login OK!")
            print(access_token)
            self.open_window()
            self.close()
        else:
            print("Login FALHOU!")

    def open_window(self):
        self.hide()
        self.main_window = MainWindow()
        self.main_window.show()
