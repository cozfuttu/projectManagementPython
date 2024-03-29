# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import json
from PyQt5 import QtCore, QtWidgets
from firebase_admin import credentials, firestore, storage
import firebase_admin
import pyrebase
from requests.models import HTTPError
from config.firebase import getFirebaseConfig
from functions.getUserInfo import getUserInfo
from windows.adminWindow import Ui_AdminWindow
from windows.signUpWindow import Ui_SignUpWindow
from windows.developer import Ui_DevWindow

firebase = pyrebase.initialize_app(getFirebaseConfig())
auth = firebase.auth()

cred = credentials.Certificate('src/config/key.json')
app = firebase_admin.initialize_app(cred, { 'storageBucket' : 'task-management-python.appspot.com' })
db = firestore.client()

class Ui_MainWindow(object):
    def openDevWindow(self, userInfo):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DevWindow()
        self.ui.setupUi(self.window, userInfo, storage, db)
        self.window.show()

    def openSignUpWindow(self, event):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SignUpWindow()
        self.ui.setupUi(self.window, auth, db)
        self.window.show()

    def openAdminWindow(self, userInfo):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self.window, userInfo, db)
        self.window.show()

    def setupUi(self, MainWindow):

        MainWindow.setFixedSize(800, 600)
        MainWindow.setWindowTitle("Login Screen")
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 127);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(370, 260, 221, 31))

        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(370, 320, 221, 31))
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)

        self.UsernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.UsernameLabel.setGeometry(QtCore.QRect(250, 260, 75, 31))
        self.UsernameLabel.setText("Email:")
        self.UsernameLabel.setStyleSheet("color: rgb(0, 85, 255);\n" "font-size: 28px;")

        self.PasswordLabel = QtWidgets.QLabel(self.centralwidget)
        self.PasswordLabel.setGeometry(QtCore.QRect(260, 310, 71, 41))
        self.PasswordLabel.setText("Şifre:")
        self.PasswordLabel.setStyleSheet("color: rgb(0, 85, 255);\n"
"font-size: 28px;")

        self.DontHaveAccountLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.DontHaveAccountLabel1.setText("Hesabınız yok mu? ")
        self.DontHaveAccountLabel1.setGeometry(QtCore.QRect(300, 470, 91, 16))

        self.SignUpDirectionLabel = QtWidgets.QLabel(self.centralwidget)
        self.SignUpDirectionLabel.setGeometry(QtCore.QRect(390, 470, 41, 16))
        self.SignUpDirectionLabel.setText("Buraya")
        self.SignUpDirectionLabel.setStyleSheet("color: rgb(0, 85, 255);\n" "text-decoration: underline;")
        self.SignUpDirectionLabel.setCursor(QtCore.Qt.PointingHandCursor)

        # Opening the sign up window after clicking "don't have account" label.
        self.SignUpDirectionLabel.mousePressEvent = self.openSignUpWindow

        self.DontHaveAccountLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.DontHaveAccountLabel2.setGeometry(QtCore.QRect(430, 470, 121, 16))
        self.DontHaveAccountLabel2.setText("tıklayıp kayıt olabilirsiniz.")

        self.InvalidInfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.InvalidInfoLabel.setGeometry(QtCore.QRect(482, 360, 201, 21))
        self.InvalidInfoLabel.setText("Girilen bilgilere ait hesap bulunmamaktadır.")
        self.InvalidInfoLabel.setStyleSheet("color: rgb(255,0,0);")
        self.InvalidInfoLabel.setVisible(False)

        self.LoginScreenLabel = QtWidgets.QLabel(self.centralwidget)
        self.LoginScreenLabel.setGeometry(QtCore.QRect(300, 110, 241, 91))
        self.LoginScreenLabel.setText("Giriş Ekranı")
        self.LoginScreenLabel.setStyleSheet("color: rgb(0, 85, 255);\n"
"font-size: 48px;")

        self.LoginButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoginButton.setGeometry(QtCore.QRect(480, 390, 111, 31))
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
        username = email.replace("@gmail.com", "")
        try:
                auth.sign_in_with_email_and_password(email, password)
                userInfo = getUserInfo(db, username)

                # If the logged user is admin, opens the administrator window. Else, opens the developer window.
                if(userInfo["Admin"]):
                        self.openAdminWindow(userInfo)
                else:
                        self.openDevWindow(userInfo)
        except HTTPError as e:
                print("login failed")
                self.InvalidInfoLabel.setText("Hata: " + json.loads(e.args[1])["error"]["message"])
                self.InvalidInfoLabel.setVisible(True)
        print(username + " olarak giris yapildi.")