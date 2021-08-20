from PyQt5 import QtCore, QtGui, QtWidgets
import internet_test
from multiprocessing import Process

internet = internet_test.InternetTest()

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(434, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.check_download = QtWidgets.QCheckBox(self.centralwidget)
        self.check_download.setGeometry(QtCore.QRect(20, 40, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.check_download.setFont(font)
        self.check_download.setStyleSheet("color: rgb(255, 255, 255);")
        self.check_download.setObjectName("check_download")
        self.check_ping = QtWidgets.QCheckBox(self.centralwidget)
        self.check_ping.setEnabled(True)
        self.check_ping.setGeometry(QtCore.QRect(194, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setUnderline(False)
        font.setKerning(False)
        self.check_ping.setFont(font)
        self.check_ping.setStyleSheet("color: rgb(255, 255, 255);")
        self.check_ping.setObjectName("check_ping")
        self.check_upload = QtWidgets.QCheckBox(self.centralwidget)
        self.check_upload.setEnabled(True)
        self.check_upload.setGeometry(QtCore.QRect(320, 40, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.check_upload.setFont(font)
        self.check_upload.setStyleSheet("color: rgb(255, 255, 255);")
        self.check_upload.setObjectName("check_upload")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(210, 120, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(2)
        self.spinBox.setMaximum(60)
        self.spinBox.setSingleStep(1)
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 110, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 250, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 300, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 110, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, -10, 431, 391))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("mainscreen_back.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.photo.raise_()
        self.check_download.raise_()
        self.check_ping.raise_()
        self.check_upload.raise_()
        self.spinBox.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 434, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.StartTest)

        self.pushButton_2.clicked.connect(self.StopTest)

    def StartTest(self):
            self.testProcess = Process(target = 
            internet.Test, args = 
            (self.check_download.isChecked(), self.check_ping.isChecked(),self.check_upload.isChecked(), self.spinBox.value()))

            self.testProcess.start()

    def StopTest(self):
        if self.testProcess.is_alive():
            self.testProcess.terminate()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Test your internet"))
        self.check_download.setText(_translate("MainWindow", "Download"))
        self.check_ping.setText(_translate("MainWindow", "Ping"))
        self.check_upload.setText(_translate("MainWindow", "Upload"))
        self.label.setText(_translate("MainWindow", "Test each:"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_2.setText(_translate("MainWindow", "STOP"))
        self.label_3.setText(_translate("MainWindow", "minutes"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
