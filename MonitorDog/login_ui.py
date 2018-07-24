# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QEvent, QRegExp
from PyQt5.QtWidgets import QApplication, QMainWindow


class QMain(QMainWindow):

    def login_button_click(self):
        print (self)



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(675, 498)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login_buttom = QtWidgets.QPushButton(self.centralwidget)
        self.login_buttom.setGeometry(QtCore.QRect(210, 220, 76, 33))
        self.login_buttom.setObjectName("login_buttom")
        self.username_input = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input.setGeometry(QtCore.QRect(281, 70, 171, 31))
        self.username_input.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.username_input.setObjectName("username_input")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(217, 70, 62, 31))
        self.username_label.setMinimumSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.username_label.setFont(font)
        self.username_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.username_label.setTextFormat(QtCore.Qt.PlainText)
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.register_buttom = QtWidgets.QPushButton(self.centralwidget)
        self.register_buttom.setGeometry(QtCore.QRect(340, 220, 81, 31))
        self.register_buttom.setObjectName("register_buttom")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(280, 120, 171, 31))
        self.password_input.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.password_input.setText("")
        self.password_input.setObjectName("password_input")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(210, 120, 62, 31))
        self.password_label.setMinimumSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.password_label.setFont(font)
        self.password_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.password_label.setTextFormat(QtCore.Qt.PlainText)
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.remember_username_password = QtWidgets.QCheckBox(self.centralwidget)
        self.remember_username_password.setGeometry(QtCore.QRect(220, 180, 201, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.remember_username_password.setFont(font)
        self.remember_username_password.setObjectName("remember_username_password")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 675, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.login_buttom.clicked.connect(MainWindow.login_button_click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_buttom.setText(_translate("MainWindow", "登陆"))
        self.username_label.setText(_translate("MainWindow", "用户名"))
        self.register_buttom.setText(_translate("MainWindow", "注册"))
        self.password_label.setText(_translate("MainWindow", "密码"))
        self.remember_username_password.setText(_translate("MainWindow", "记住用户名和密码"))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	MainWindow = QMain()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())