# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'invitation.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets

from functions.acceptInvitation import acceptInvitation
from functions.rejectInvitation import rejectInvitation


class Ui_InvitationFrame(object):
    def acceptInvite(self, InvitationFrame, invitation, db, updateDavetSayisi):
        result = acceptInvitation(db, invitation)

        InvitationFrame.setVisible(False)
        updateDavetSayisi(result)

    def rejectInvite(self, InvitationFrame, invitation, db, updateDavetSayisi):
        result = rejectInvitation(db, invitation)

        InvitationFrame.setVisible(False)
        updateDavetSayisi(result)

    def setupUi(self, InvitationFrame, invitation, db, updateDavetSayisi):
        InvitationFrame.setObjectName("InvitationFrame")
        InvitationFrame.resize(265, 72)
        InvitationFrame.setStyleSheet("background-color: rgb(255, 255, 127);")

        self.FromLabel = QtWidgets.QLabel(InvitationFrame)
        self.FromLabel.setGeometry(QtCore.QRect(20, 10, 141, 21))
        self.FromLabel.setObjectName("FromLabel")

        self.DetailsLabel = QtWidgets.QLabel(InvitationFrame)
        self.DetailsLabel.setGeometry(QtCore.QRect(20, 30, 151, 41))
        self.DetailsLabel.setWordWrap(True)
        self.DetailsLabel.setObjectName("DetailsLabel")

        self.line_7 = QtWidgets.QFrame(InvitationFrame)
        self.line_7.setGeometry(QtCore.QRect(0, 70, 269, 3))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")

        self.AcceptButton = QtWidgets.QPushButton(InvitationFrame)
        self.AcceptButton.setGeometry(QtCore.QRect(170, 10, 75, 23))
        self.AcceptButton.setObjectName("AcceptButton")
        self.AcceptButton.clicked.connect(lambda: self.acceptInvite(InvitationFrame, invitation, db, updateDavetSayisi))

        self.RejectButton = QtWidgets.QPushButton(InvitationFrame)
        self.RejectButton.setGeometry(QtCore.QRect(170, 40, 75, 23))
        self.RejectButton.setObjectName("RejectButton")
        self.RejectButton.clicked.connect(lambda: self.rejectInvite(db, invitation, updateDavetSayisi))

        self.retranslateUi(InvitationFrame, invitation)
        QtCore.QMetaObject.connectSlotsByName(InvitationFrame)

    def retranslateUi(self, InvitationFrame, invitation):
        _translate = QtCore.QCoreApplication.translate
        InvitationFrame.setWindowTitle(_translate("InvitationFrame", "Frame"))
        self.FromLabel.setText(_translate("InvitationFrame", "Kimden: " + invitation["From"]))
        self.DetailsLabel.setText(_translate("InvitationFrame", "Açıklama: " + invitation["Details"]))
        self.AcceptButton.setText(_translate("InvitationFrame", "Kabul Et"))
        self.RejectButton.setText(_translate("InvitationFrame", "Reddet"))