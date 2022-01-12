# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\canoz\Desktop\taskAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_taskAdmin(object):
    def setupUi(self, taskAdmin):
        taskAdmin.setObjectName("taskAdmin")
        taskAdmin.resize(327, 107)
        taskAdmin.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.UsernameLabel = QtWidgets.QLabel(taskAdmin)
        self.UsernameLabel.setGeometry(QtCore.QRect(10, 10, 151, 21))
        self.UsernameLabel.setObjectName("UsernameLabel")
        self.DetailsLabel = QtWidgets.QLabel(taskAdmin)
        self.DetailsLabel.setGeometry(QtCore.QRect(10, 30, 151, 41))
        self.DetailsLabel.setWordWrap(True)
        self.DetailsLabel.setObjectName("DetailsLabel")
        self.DeadlineLabel = QtWidgets.QLabel(taskAdmin)
        self.DeadlineLabel.setGeometry(QtCore.QRect(10, 70, 151, 21))
        self.DeadlineLabel.setObjectName("DeadlineLabel")
        self.DeleteTaskButton = QtWidgets.QPushButton(taskAdmin)
        self.DeleteTaskButton.setGeometry(QtCore.QRect(220, 10, 75, 23))
        self.DeleteTaskButton.setStyleSheet("background-color: rgb(230, 100, 50);")
        self.DeleteTaskButton.setObjectName("DeleteTaskButton")
        self.StatusLabel = QtWidgets.QLabel(taskAdmin)
        self.StatusLabel.setGeometry(QtCore.QRect(210, 40, 101, 21))
        self.StatusLabel.setObjectName("StatusLabel")
        self.UploadedFilesLabel = QtWidgets.QLabel(taskAdmin)
        self.UploadedFilesLabel.setGeometry(QtCore.QRect(200, 60, 111, 21))
        self.UploadedFilesLabel.setStyleSheet("text-decoration: underline;\n"
"color: rgb(0, 80, 255);")
        self.UploadedFilesLabel.setObjectName("UploadedFilesLabel")
        self.line = QtWidgets.QFrame(taskAdmin)
        self.line.setGeometry(QtCore.QRect(0, 90, 325, 3))
        self.line.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(taskAdmin)
        QtCore.QMetaObject.connectSlotsByName(taskAdmin)

    def retranslateUi(self, taskAdmin):
        _translate = QtCore.QCoreApplication.translate
        taskAdmin.setWindowTitle(_translate("taskAdmin", "Frame"))
        self.UsernameLabel.setText(_translate("taskAdmin", "Kullanıcı: Beyefendi"))
        self.DetailsLabel.setText(_translate("taskAdmin", "Açıklama: Çabuk ol"))
        self.DeadlineLabel.setText(_translate("taskAdmin", "Son Teslim Tarihi: 25.01.2022"))
        self.DeleteTaskButton.setText(_translate("taskAdmin", "Görev Sil"))
        self.StatusLabel.setText(_translate("taskAdmin", "Durum: Tamamlandı"))
        self.UploadedFilesLabel.setText(_translate("taskAdmin", "Yüklenen Dosyaları Gör"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    taskAdmin = QtWidgets.QFrame()
    ui = Ui_taskAdmin()
    ui.setupUi(taskAdmin)
    taskAdmin.show()
    sys.exit(app.exec_())