# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_inicial.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from subprocess import call

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(490, 393)
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
        self.startAttendance = QtWidgets.QPushButton(self.backgroundAttendance)
        self.startAttendance.setGeometry(QtCore.QRect(150, 200, 191, 71))
        self.startAttendance.setMinimumSize(QtCore.QSize(171, 0))
        self.startAttendance.setMaximumSize(QtCore.QSize(365, 300))
        self.startAttendance.setStyleSheet("image: url(:/Buttons/images/btnIniciarChamada.png);\n"
"background-position: center;")
        self.startAttendance.setText("")
        self.startAttendance.setObjectName("startAttendance")
        self.registerPerson = QtWidgets.QPushButton(self.backgroundAttendance)
        self.registerPerson.setGeometry(QtCore.QRect(140, 270, 201, 111))
        self.registerPerson.setMinimumSize(QtCore.QSize(171, 0))
        self.registerPerson.setMaximumSize(QtCore.QSize(365, 300))
        self.registerPerson.setStyleSheet("image: url(:/Buttons/images/btnRegistrarPessoa.png);\n"
"background-position: center;")
        self.registerPerson.setText("")
        self.registerPerson.setObjectName("registerPerson")
        self.attendanceList = QtWidgets.QPushButton(self.backgroundAttendance)
        self.attendanceList.setGeometry(QtCore.QRect(140, 100, 201, 91))
        self.attendanceList.setMinimumSize(QtCore.QSize(0, 0))
        self.attendanceList.setMaximumSize(QtCore.QSize(365, 300))
        self.attendanceList.setStyleSheet("image: url(:/Buttons/images/btnListaChamada.png);\n"
"background-position: center;")
        self.attendanceList.setText("")
        self.attendanceList.setObjectName("attendanceList")
        self.horizontalLayout.addWidget(self.backgroundAttendance)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.registerPerson.clicked.connect(self.callRegisterPerson)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Attendance Project"))
        
    def callRegisterPerson(self):
        call(["python", "./processing/register.py"])

import Resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

