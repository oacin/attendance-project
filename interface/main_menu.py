from PyQt5 import QtCore, QtGui, QtWidgets
from subprocess import call 
import webbrowser
from PyQt5.QtWidgets import QMessageBox
import cv2

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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backgroundAttendance.sizePolicy().hasHeightForWidth())
        self.backgroundAttendance.setSizePolicy(sizePolicy)
        self.backgroundAttendance.setMaximumSize(QtCore.QSize(1920, 1080))
        self.backgroundAttendance.setStyleSheet("#Teste{\n"
"image: url(:/Imagens/images/fundo ofc.png);\n"
"}")
        self.backgroundAttendance.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.backgroundAttendance.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backgroundAttendance.setObjectName("backgroundAttendance")
        self.gridLayout = QtWidgets.QGridLayout(self.backgroundAttendance)
        self.gridLayout.setObjectName("gridLayout")
        self.startAttendance = QtWidgets.QPushButton(self.backgroundAttendance)
        self.startAttendance.setMinimumSize(QtCore.QSize(365, 125))
        self.startAttendance.setMaximumSize(QtCore.QSize(365, 300))
        self.startAttendance.setStyleSheet("image: url(:/Buttons/images/btnIniciarChamada.png);\n"
"background-position: center;")
        self.startAttendance.setText("")
        self.startAttendance.setObjectName("startAttendance")
        self.gridLayout.addWidget(self.startAttendance, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.registerPerson = QtWidgets.QPushButton(self.backgroundAttendance)
        self.registerPerson.setMinimumSize(QtCore.QSize(365, 125))
        self.registerPerson.setMaximumSize(QtCore.QSize(365, 300))
        self.registerPerson.setStyleSheet("image: url(:/Buttons/images/btnRegistrarPessoa.png);\n"
"background-position: center;")
        self.registerPerson.setText("")
        self.registerPerson.setObjectName("registerPerson")
        self.gridLayout.addWidget(self.registerPerson, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.attendanceList = QtWidgets.QPushButton(self.backgroundAttendance)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attendanceList.sizePolicy().hasHeightForWidth())
        self.attendanceList.setSizePolicy(sizePolicy)
        self.attendanceList.setMinimumSize(QtCore.QSize(365, 125))
        self.attendanceList.setMaximumSize(QtCore.QSize(400, 300))
        self.attendanceList.setStyleSheet("image: url(:/Buttons/images/btnListaChamada.png);\n"
"background-position: center;")
        self.attendanceList.setText("")
        self.attendanceList.setObjectName("attendanceList")
        self.gridLayout.addWidget(self.attendanceList, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.frame = QtWidgets.QFrame(self.backgroundAttendance)
        self.frame.setStyleSheet("image: url(:/Imagens/images/attendance project.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.attendanceList.raise_()
        self.startAttendance.raise_()
        self.registerPerson.raise_()
        self.frame.raise_()
        self.horizontalLayout.addWidget(self.backgroundAttendance)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.registerPerson.clicked.connect(self.callRegisterPerson)

        self.startAttendance.clicked.connect(self.callStartAttendance)

        self.attendanceList.clicked.connect(self.open_webbrowser)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Attendance Project"))

    def callRegisterPerson(self):
        call(["python", "./interface/register_menu.py"])
        

    def callStartAttendance(self):
        cap = cv2.VideoCapture(0)
        success, img = cap.read()

        if not success:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Camera não encontrada.")
            msg.setInformativeText(f'O cadastro não foi possível pois não tem uma camera conectada!')
            msg.setWindowTitle("Camera não encontrada!")
            msg.exec_()

        else:
            call(["python", "./processing/attendance.py"])

    def open_webbrowser(self):
        webbrowser.open('http://127.0.0.1:8085/frontend/index.html')

import Resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())

