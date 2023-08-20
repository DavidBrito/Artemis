# -*- coding: utf-8 -*-
from PyQt5 import QtCore
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QFrame, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
import resources.images

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 550)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint) # type: ignore
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground) # type: ignore

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 20, 421, 501))
        self.frame.setStyleSheet(u"border: none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 381, 461))
        self.label.setStyleSheet(u"background-image: url(:/images/forest-path-1387064.png);\n"
"background-size: contain;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border-radius: 20px;")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 381, 461))
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.71, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop:0.83 rgba(0,0,0,75));\n"
"border-radius: 20px;")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 421, 501))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 381, 461))
        self.label_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.71, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop:0.83 rgba(0,0,0,75));\n"
"border-radius: 20px;")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 30, 361, 421))
        self.label_3.setStyleSheet(u"background-color: rgba(0,0,0,100);\n"
"border-radius: 20px;")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(100, 50, 201, 41))
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 140, 291, 31))
        self.lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(105,118,132,255);\n"
"color: rgba(255,255,255,230);\n"
"padding-bottom: 7px;")
        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(60, 220, 291, 31))
        self.lineEdit_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(105,118,132,255);\n"
"color: rgba(255,255,255,230);\n"
"padding-bottom: 7px;")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 310, 131, 41))
        self.pushButton.setStyleSheet(u"QPushButton#pushButton {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.4, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"  color: rgba(255, 255, 255, 210);\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.4, stop:0 rgba(30, 67, 98, 219), stop:1 rgba(95, 108, 122, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"  padding-left: 5px;\n"
"  padding-top: 5px;\n"
"  background-color: rgba(105, 118, 132, 200);\n"
"}\n"
"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_4.setText("")
        self.label_3.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Projeto Artemis", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Usu\u00e1rio", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Senha", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Entrar", None))
    # retranslateUi

