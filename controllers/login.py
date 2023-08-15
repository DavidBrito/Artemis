import sys
import os
import requests
from PyQt5 import QtWidgets, QtSql

from dotenv import load_dotenv
from ui.login_dialog import LoginDialog
#from ui.home_window import HomeWindow

class Login(QtWidgets.QWidget, LoginDialog):
    def __init__(self):
        super(Login, self).__init__()
        # Carrega variaveis de ambiente do arquivo .env
        load_dotenv()
        try:
            self.api_host = os.environ['API_HOST']
        except Exception as e:
            print(e)
            sys.exit(1)
    
        self.setupUi(self)
        self.pushButton.clicked.connect(self.checkUser)

    def checkUser(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        response = requests.post(self.api_host, json={'username': username, 'password': password})
        if response.status_code == 200:
            access_token = response.json()['access_token']
            self.open_dashboard(access_token)
            self.close()
        else:
            print("Login failed")

    def open_window(self, access_token):
        #self.home = HomeWindow(access_token)
        self.home.show()
        self.hide()
