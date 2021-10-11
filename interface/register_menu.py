# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_registro.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(432, 393)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        MainWindow.setIconSize(QtCore.QSize(20, 20))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backgroundAttendance = QtWidgets.QFrame(self.centralwidget)
        self.backgroundAttendance.setMaximumSize(QtCore.QSize(425, 400))
        self.backgroundAttendance.setStyleSheet("image: url(:/Imagens/images/fundo ofc.png);")
        self.backgroundAttendance.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.backgroundAttendance.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backgroundAttendance.setObjectName("backgroundAttendance")
        self.namePerson = QtWidgets.QLineEdit(self.backgroundAttendance)
        self.namePerson.setGeometry(QtCore.QRect(110, 140, 231, 21))
        self.namePerson.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(112, 112, 112);")
        self.namePerson.setObjectName("namePerson")
        self.buttonConfirm = QtWidgets.QPushButton(self.backgroundAttendance)
        self.buttonConfirm.setGeometry(QtCore.QRect(250, 176, 131, 61))
        self.buttonConfirm.setStyleSheet("image: url(:/Buttons/images/btnConfirmar.png);")
        self.buttonConfirm.setText("")
        self.buttonConfirm.setObjectName("buttonConfirm")
        self.buttonCancel = QtWidgets.QPushButton(self.backgroundAttendance)
        self.buttonCancel.setGeometry(QtCore.QRect(90, 170, 131, 71))
        self.buttonCancel.setStyleSheet("image: url(:/Buttons/images/btnCancelar.png);")
        self.buttonCancel.setText("")
        self.buttonCancel.setObjectName("buttonCancel")
        self.horizontalLayout.addWidget(self.backgroundAttendance)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 432, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Attendance Project"))

import Resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

