# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'developer.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyrebase.pyrebase import Database, Storage
from UIcomponents.invitation import Ui_InvitationFrame
from UIcomponents.taskDev import Ui_TaskDevFrame


class Ui_DevWindow(object):
    def setupUi(self, MainWindow, userInfo, storage: Storage, db: Database):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 127);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.ProfileLabel = QtWidgets.QLabel(self.centralwidget)
        self.ProfileLabel.setGeometry(QtCore.QRect(20, 20, 51, 51))
        self.ProfileLabel.setText("")
        self.ProfileLabel.setPixmap(QtGui.QPixmap("src/img/profile.png"))
        self.ProfileLabel.setObjectName("ProfileLabel")

        self.ProfileTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.ProfileTextLabel.setGeometry(QtCore.QRect(80, 30, 151, 21))
        self.ProfileTextLabel.setObjectName("ProfileTextLabel")

        self.TaskWaitingLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.TaskWaitingLabel1.setGeometry(QtCore.QRect(30, 100, 211, 51))
        self.TaskWaitingLabel1.setStyleSheet("font-size: 24px;\n"
"")
        self.TaskWaitingLabel1.setObjectName("TaskWaitingLabel1")

        self.TaskWaitingLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.TaskWaitingLabel2.setGeometry(QtCore.QRect(250, 100, 21, 51))
        self.TaskWaitingLabel2.setStyleSheet("font-size: 28px;\n"
"color: rgb(0, 80, 255)")
        self.TaskWaitingLabel2.setObjectName("TaskWaitingLabel2")

        self.TaskWaitingLabel3 = QtWidgets.QLabel(self.centralwidget)
        self.TaskWaitingLabel3.setGeometry(QtCore.QRect(280, 100, 151, 51))
        self.TaskWaitingLabel3.setStyleSheet("font-size: 24px;\n"
"")
        self.TaskWaitingLabel3.setObjectName("TaskWaitingLabel3")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 170, 401, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.TasksLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.TasksLayout.setContentsMargins(0, 0, 0, 0)
        self.TasksLayout.setObjectName("TasksLayout")

        for task in userInfo["Tasks"]:
            self.TaskFrame = QtWidgets.QFrame(self.verticalLayoutWidget)
            Ui_TaskDevFrame().setupUi(self.TaskFrame, task, storage, db)
            self.TasksLayout.addWidget(self.TaskFrame)
        
        self.InvitationsLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.InvitationsLabel1.setGeometry(QtCore.QRect(560, 110, 111, 31))
        self.InvitationsLabel1.setStyleSheet("font-size: 28px;")
        self.InvitationsLabel1.setObjectName("InvitationsLabel1")

        self.InvitationsLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.InvitationsLabel2.setGeometry(QtCore.QRect(680, 100, 21, 51))
        self.InvitationsLabel2.setStyleSheet("font-size: 28px;\n"
"color: rgb(0, 80, 255)")
        self.InvitationsLabel2.setObjectName("InvitationsLabel2")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(490, 170, 271, 291))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.InvitationsLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.InvitationsLayout.setContentsMargins(0, 0, 0, 0)
        self.InvitationsLayout.setSpacing(6)
        self.InvitationsLayout.setObjectName("InvitationsLayout")

        for invitation in userInfo["Invitations"]:
            self.InvitationFrame = QtWidgets.QFrame(self.verticalLayoutWidget_2)
            Ui_InvitationFrame().setupUi(self.InvitationFrame, invitation, db)
            self.InvitationsLayout.addWidget(self.InvitationFrame)

        self.TaskerrLabel = QtWidgets.QLabel(self.centralwidget)
        self.TaskerrLabel.setGeometry(QtCore.QRect(480, 20, 231, 51))
        self.TaskerrLabel.setStyleSheet("font-size: 48px;")
        self.TaskerrLabel.setObjectName("TaskerrLabel")

        self.VersionLabel = QtWidgets.QLabel(self.centralwidget)
        self.VersionLabel.setGeometry(QtCore.QRect(720, 40, 61, 31))
        self.VersionLabel.setStyleSheet("font-size: 24px;")
        self.VersionLabel.setObjectName("VersionLabel")

        self.CompletedTasksLabel = QtWidgets.QLabel(self.centralwidget)
        self.CompletedTasksLabel.setGeometry(QtCore.QRect(490, 470, 269, 75))
        self.CompletedTasksLabel.setMaximumSize(QtCore.QSize(16777215, 75))
        self.CompletedTasksLabel.setStyleSheet("font-size: 24px;")
        self.CompletedTasksLabel.setTextFormat(QtCore.Qt.AutoText)
        self.CompletedTasksLabel.setScaledContents(False)
        self.CompletedTasksLabel.setWordWrap(True)
        self.CompletedTasksLabel.setObjectName("CompletedTasksLabel")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(443, 90, 20, 491))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow, userInfo["Username"], len(userInfo["Tasks"]), len(userInfo["Invitations"]), userInfo["CompletedTaskAmount"])
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, username, beklenenGorevSayisi, davetSayisi, tamamlananGorevSayisi):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        usernameText = "Hoşgeldiniz, " + username
        self.ProfileTextLabel.setText(_translate("MainWindow", usernameText))
        self.TaskWaitingLabel1.setText(_translate("MainWindow", "Yapılmayı Bekleyen"))
        self.TaskWaitingLabel2.setText(_translate("MainWindow", str(beklenenGorevSayisi)))
        self.TaskWaitingLabel3.setText(_translate("MainWindow", "Göreviniz Var."))
        self.InvitationsLabel1.setText(_translate("MainWindow", "Davetler: "))
        self.InvitationsLabel2.setText(_translate("MainWindow", str(davetSayisi)))
        self.TaskerrLabel.setText(_translate("MainWindow", "𝓣𝓪𝓼𝓴𝓮𝓻𝓻"))
        self.VersionLabel.setText(_translate("MainWindow", "v0.1"))
        self.CompletedTasksLabel.setText(_translate("MainWindow", "Şu ana kadar " + str(tamamlananGorevSayisi) + " görev tamamladınız!"))