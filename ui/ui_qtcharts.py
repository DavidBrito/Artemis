# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qtchartsPoWTda.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resources.icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"* {\n"
"color: #fff;\n"
"font-family: Arial;\n"
"font-size: 12px;\n"
"border: none;\n"
"background: none;\n"
"}\n"
"\n"
"#centralwidget {\n"
"background-color: rgb(33,43,51);\n"
"}\n"
"\n"
"#left_menu_widget, #percentage_bar_chart, #temperature_bar_chart{\n"
"background-color: rgba(61, 80, 95, 100)\n"
"}\n"
"\n"
"#header_frame, #frame_3, frame_5{\n"
"background-color: rgb(61, 80, 95)\n"
"}\n"
"\n"
"#frame_4 QPushButton {\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background-color: rgba(33,43,51,100)\n"
"}\n"
"\n"
"#header_nav QPushButton {\n"
"background-color: rgb(61, 80, 95);\n"
"border-radius: 15px;\n"
"border: 3px solid rgb(120,157,186);\n"
"}\n"
"\n"
"#header_nav QPushButton:hover{\n"
"background-color: rgb(120, 157, 186) \n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_widget = QWidget(self.centralwidget)
        self.left_menu_widget.setObjectName(u"left_menu_widget")
        self.verticalLayout = QVBoxLayout(self.left_menu_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.left_menu_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.chart_icon = QLabel(self.frame_3)
        self.chart_icon.setObjectName(u"chart_icon")
        self.chart_icon.setMinimumSize(QSize(30, 30))
        self.chart_icon.setMaximumSize(QSize(30, 30))
        self.chart_icon.setPixmap(QPixmap(u":/icons-png/icons-png/pie-chart.png"))
        self.chart_icon.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.chart_icon)

        self.app_label_2 = QLabel(self.frame_3)
        self.app_label_2.setObjectName(u"app_label_2")
        font = QFont()
        font.setFamily(u"Arial")
        font.setBold(True)
        font.setWeight(75)
        self.app_label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.app_label_2)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignTop) # type: ignore

        self.frame_4 = QFrame(self.left_menu_widget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/icons-png/icons-png/bar-chart-2.png", QSize(), QIcon.Normal, QIcon.Off) # type: ignore
        self.pushButton.setIcon(icon)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon1 = QIcon()
        icon1.addFile(u":/icons-png/icons-png/thermometer.png", QSize(), QIcon.Normal, QIcon.Off) # type: ignore
        self.pushButton_3.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.left_menu_widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(61, 80, 95)\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(30, 30))
        self.label_13.setMaximumSize(QSize(30, 30))
        self.label_13.setPixmap(QPixmap(u":/icons-png/icons-png/meh.png"))
        self.label_13.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_13)

        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame_6, 0, Qt.AlignBottom) # type: ignore

        self.frame_5 = QFrame(self.left_menu_widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.left_menu_widget)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.header_frame = QFrame(self.frame)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMaximumSize(QSize(16777215, 50))
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.header_frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_6 = QPushButton(self.frame_11)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(30, 30))
        self.pushButton_6.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icons-png/icons-png/align-left.png", QSize(), QIcon.Normal, QIcon.Off) # type: ignore
        self.pushButton_6.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.pushButton_6)

        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)


        self.horizontalLayout_4.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.header_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)


        self.horizontalLayout_4.addWidget(self.frame_10)

        self.header_nav = QFrame(self.header_frame)
        self.header_nav.setObjectName(u"header_nav")
        self.header_nav.setFrameShape(QFrame.StyledPanel)
        self.header_nav.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.header_nav)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_8 = QPushButton(self.header_nav)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(30, 30))
        self.pushButton_8.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icons-png/icons-png/minus.png", QSize(), QIcon.Normal, QIcon.Off) # type: ignore
        self.pushButton_8.setIcon(icon3)

        self.horizontalLayout_7.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.header_nav)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(30, 30))
        self.pushButton_7.setMaximumSize(QSize(30, 30))
        icon4 = QIcon()
        icon4.addFile(u":/icons-png/icons-png/maximize-2.png", QSize(), QIcon.Normal, QIcon.Off) # type: ignore
        self.pushButton_7.setIcon(icon4)

        self.horizontalLayout_7.addWidget(self.pushButton_7)

        self.pushButton_9 = QPushButton(self.header_nav)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(30, 30))
        self.pushButton_9.setMaximumSize(QSize(30, 30))
        icon5 = QIcon()
        icon5.addFile(u":/icons-png/icons-png/x.png", QSize(), QIcon.Normal, QIcon.Off) # type: ignore
        self.pushButton_9.setIcon(icon5)

        self.horizontalLayout_7.addWidget(self.pushButton_9)


        self.horizontalLayout_4.addWidget(self.header_nav, 0, Qt.AlignRight) # type: ignore


        self.verticalLayout_4.addWidget(self.header_frame, 0, Qt.AlignTop) # type: ignore

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_8)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.percentage_bar_chart = QWidget()
        self.percentage_bar_chart.setObjectName(u"percentage_bar_chart")
        self.verticalLayout_6 = QVBoxLayout(self.percentage_bar_chart)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_16 = QFrame(self.percentage_bar_chart)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_16)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_9 = QLabel(self.frame_16)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter) # type: ignore

        self.verticalLayout_7.addWidget(self.label_9, 0, Qt.AlignTop) # type: ignore


        self.verticalLayout_6.addWidget(self.frame_16, 0, Qt.AlignTop) # type: ignore

        self.frame_17 = QFrame(self.percentage_bar_chart)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy1)
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_17)
        self.gridLayout.setObjectName(u"gridLayout")

        self.verticalLayout_6.addWidget(self.frame_17)

        self.stackedWidget.addWidget(self.percentage_bar_chart)
        self.temperature_bar_chart = QWidget()
        self.temperature_bar_chart.setObjectName(u"temperature_bar_chart")
        self.verticalLayout_9 = QVBoxLayout(self.temperature_bar_chart)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_18 = QFrame(self.temperature_bar_chart)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_18)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_10 = QLabel(self.frame_18)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter) # type: ignore

        self.verticalLayout_8.addWidget(self.label_10, 0, Qt.AlignTop) # type: ignore


        self.verticalLayout_9.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.temperature_bar_chart)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy1.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy1)
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_19)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.verticalLayout_9.addWidget(self.frame_19)

        self.stackedWidget.addWidget(self.temperature_bar_chart)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(90, 100, 57, 15))

        self.horizontalLayout_8.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(90, 60, 120, 80))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_13)


        self.verticalLayout_4.addWidget(self.frame_9)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.chart_icon.setText("")
        self.app_label_2.setText(QCoreApplication.translate("MainWindow", u"QT CHARTS", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Percent Bar Chart", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Temperature Records", None))
        self.label_13.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Support Me", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Patreon", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Subscribe", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PayPal", None))
        self.pushButton_6.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.pushButton_8.setText("")
        self.pushButton_7.setText("")
        self.pushButton_9.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Percentage Bar Chart", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Temperature Bar Chart", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Copyright", None))
    # retranslateUi

