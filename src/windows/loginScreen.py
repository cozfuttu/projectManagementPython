# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import json
from logging import error
from PyQt5 import QtCore, QtGui, QtWidgets
import pyrebase
import requests
from requests.models import HTTPError
from config.firebase import firebaseConfig
from windows.openWindow import openWindow

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setFixedSize(975, 600)
        MainWindow.setWindowTitle("Login Screen")
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 127);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(520, 260, 221, 31))

        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(520, 320, 221, 31))

        self.UsernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.UsernameLabel.setGeometry(QtCore.QRect(220, 260, 251, 31))
        self.UsernameLabel.setText("Kullanıcı Adı / Email:")
        self.UsernameLabel.setStyleSheet("color: rgb(0, 85, 255);\n" "font-size: 28px;")

        self.PasswordLabel = QtWidgets.QLabel(self.centralwidget)
        self.PasswordLabel.setGeometry(QtCore.QRect(410, 310, 71, 41))
        self.PasswordLabel.setText("Şifre:")
        self.PasswordLabel.setStyleSheet("color: rgb(0, 85, 255);\n"
"font-size: 28px;")

        self.DontHaveAccountLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.DontHaveAccountLabel1.setText("Hesabınız yok mu? ")
        self.DontHaveAccountLabel1.setGeometry(QtCore.QRect(350, 470, 91, 16))

        self.SignUpDirectionLabel = QtWidgets.QLabel(self.centralwidget)
        self.SignUpDirectionLabel.setGeometry(QtCore.QRect(440, 470, 41, 16))
        self.SignUpDirectionLabel.setText("Buraya")
        self.SignUpDirectionLabel.setStyleSheet("color: rgb(0, 85, 255);\n" "text-decoration: underline;")
        self.SignUpDirectionLabel.setCursor(QtCore.Qt.PointingHandCursor)
        self.SignUpDirectionLabel.mousePressEvent = self.openSignUpWindow

        self.DontHaveAccountLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.DontHaveAccountLabel2.setGeometry(QtCore.QRect(480, 470, 121, 16))
        self.DontHaveAccountLabel2.setText("tıklayıp kayıt olabilirsiniz.")

        self.InvalidInfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.InvalidInfoLabel.setGeometry(QtCore.QRect(632, 360, 201, 21))
        self.InvalidInfoLabel.setText("Girilen bilgilere ait hesap bulunmamaktadır.")
        self.InvalidInfoLabel.setStyleSheet("color: rgb(255,0,0);")
        self.InvalidInfoLabel.setVisible(False)

        self.LoginScreenLabel = QtWidgets.QLabel(self.centralwidget)
        self.LoginScreenLabel.setGeometry(QtCore.QRect(350, 110, 241, 91))
        self.LoginScreenLabel.setText("Giriş Ekranı")
        self.LoginScreenLabel.setStyleSheet("color: rgb(0, 85, 255);\n"
"font-size: 48px;")

        self.LoginButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoginButton.setGeometry(QtCore.QRect(630, 390, 111, 31))
        self.LoginButton.setText("Giriş")
        self.LoginButton.setStyleSheet("font-size: 20px;\n"
"border: 2px solid #000000;\n"
"border-radius: 8px;\n"
"color: rgb(0, 85, 255);\n"
"background-color: rgb(223, 255, 10);")
        self.LoginButton.clicked.connect(lambda: self.login())

        MainWindow.setCentralWidget(self.centralwidget)

    def login(self):
        email = self.usernameInput.text()
        password = self.passwordInput.text()
        try:
                print(auth.sign_in_with_email_and_password(email, password))
        except HTTPError as e:
                print("failed")
                self.InvalidInfoLabel.setText("Hata: " + json.loads(e.args[1])["error"]["message"])
                self.InvalidInfoLabel.setVisible(True)
        print("done")

    def openSignUpWindow(self, event):
            print(event)