# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_registroV2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QMessageBox

import sys

sys.path.insert(1, './processing')

import register

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        MainWindow.setIconSize(QtCore.QSize(20, 20))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backgroundAttendance = QtWidgets.QFrame(self.centralwidget)
        self.backgroundAttendance.setMaximumSize(QtCore.QSize(1920, 1080))
        self.backgroundAttendance.setStyleSheet("color: rgb(0, 0, 0);")
        self.backgroundAttendance.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.backgroundAttendance.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backgroundAttendance.setObjectName("backgroundAttendance")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.backgroundAttendance)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.backgroundAttendance)
        self.frame.setMaximumSize(QtCore.QSize(1920, 186))
        self.frame.setStyleSheet("image: url(:/Imagens/images/attendance project.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.namePerson = QtWidgets.QLineEdit(self.backgroundAttendance)
        self.namePerson.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.namePerson.sizePolicy().hasHeightForWidth())
        self.namePerson.setSizePolicy(sizePolicy)
        self.namePerson.setMinimumSize(QtCore.QSize(201, 19))
        self.namePerson.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.namePerson.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.namePerson.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(112, 112, 112);")
        self.namePerson.setText("")
        self.namePerson.setObjectName("namePerson")
        self.verticalLayout.addWidget(self.namePerson)
        self.buttonConfirm = QtWidgets.QPushButton(self.backgroundAttendance)
        self.buttonConfirm.setMinimumSize(QtCore.QSize(200, 115))
        self.buttonConfirm.setStyleSheet("image: url(:/Buttons/images/btnConfirmar.png);")
        self.buttonConfirm.setText("")
        self.buttonConfirm.setObjectName("buttonConfirm")
        self.verticalLayout.addWidget(self.buttonConfirm)
        self.buttonCancel = QtWidgets.QPushButton(self.backgroundAttendance)
        self.buttonCancel.setMinimumSize(QtCore.QSize(200, 115))
        self.buttonCancel.setStyleSheet("image: url(:/Buttons/images/btnCancelar.png);")
        self.buttonCancel.setText("")
        self.buttonCancel.setObjectName("buttonCancel")
        self.verticalLayout.addWidget(self.buttonCancel)
        self.horizontalLayout.addWidget(self.backgroundAttendance)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 432, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.buttonConfirm.clicked.connect(self.callRegisterPerson)

        self.buttonCancel.clicked.connect(self.cancelButton)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Attendance Project"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Attendance Project"))

    def callRegisterPerson(self):
        if self.namePerson.text():
            register.registrar(self.namePerson.text())
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Preencha o nome da pessoa que deseja registrar")
            msg.setInformativeText('É necessário digitar o nome completo da pessoa para que consiga registra-la.')
            msg.setWindowTitle("Campo não preenchido")
            msg.exec_()
            return

        sys.exit(app.exec_())

    def cancelButton(self):
        sys.exit(app.exec_())

import Resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

