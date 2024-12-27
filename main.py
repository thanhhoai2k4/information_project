from radix_tree import Radix_Tree, LOADDATATXT
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
import asyncio


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1007, 600)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/icons8-write-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gbProcess = QtWidgets.QGroupBox(self.centralwidget)
        self.gbProcess.setGeometry(QtCore.QRect(60, 80, 841, 381))
        self.gbProcess.setObjectName("gbProcess")
        self.listWidget = QtWidgets.QListWidget(self.gbProcess)
        self.listWidget.setGeometry(QtCore.QRect(170, 80, 311, 141))
        self.listWidget.setObjectName("listWidget")
        # item = QtWidgets.QListWidgetItem()
        # self.listWidget.addItem(item)

        ###
        self.lbInformation = QtWidgets.QLabel(self.gbProcess)
        self.lbInformation.setGeometry(QtCore.QRect(510, 110, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbInformation.setFont(font)
        self.lbInformation.setObjectName("lbInformation")
        self.pbAdditon = QtWidgets.QPushButton(self.gbProcess)
        self.pbAdditon.setGeometry(QtCore.QRect(700, 170, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.pbAdditon.setFont(font)
        self.pbAdditon.setMouseTracking(False)
        self.pbAdditon.setObjectName("pbAdditon")
        self.pbAdditon.clicked.connect(self.insert)
        self.lineEdit = QtWidgets.QLineEdit(self.gbProcess)
        self.lineEdit.setGeometry(QtCore.QRect(700, 110, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.leInput = QtWidgets.QLineEdit(self.gbProcess)
        self.leInput.setGeometry(QtCore.QRect(170, 260, 651, 91))
        self.leInput.setObjectName("leInput")
        self.lbInput = QtWidgets.QLabel(self.gbProcess)
        self.lbInput.setGeometry(QtCore.QRect(0, 290, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.lbInput.setFont(font)
        self.lbInput.setObjectName("lbInput")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.index = 0

        self.currrntWord = ""
        self.passlist = []
        # Load du lieu tu file txt ngang cap
        self.data = LOADDATATXT("data/data.txt").load()
        self.root = Radix_Tree()
        self.root.insertManyWord(self.data)
        sleep(1)

        #remove push button
        self.removepushtton = QtWidgets.QPushButton(self.gbProcess)
        self.removepushtton.setGeometry(QtCore.QRect(500, 170, 200, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.removepushtton.setFont(font)
        self.removepushtton.setMouseTracking(False)
        self.removepushtton.setObjectName("removepushtton")
        self.removepushtton.clicked.connect(self.remove)
        self.removepushtton.setText("Remove")



        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.CheckkingString)
        self.timer.start()

        self.time1 = QtCore.QTimer()
        self.time1.setInterval(500)
        self.time1.timeout.connect(self.PridictWord)
        self.time1.start()


        self.listWidget.itemClicked.connect(self.slotOrLambdaFunction)

    def remove(self):
        self.root.delete(self.currrntWord)


    def insert(self):
        try:
            self.root.insertWord(self.currrntWord)
            with open("data/data.txt", "a+") as f:
                f.write(self.currrntWord+"\n")
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText("complete !")
            msg.setWindowTitle("THANH HOAI")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel)
            retval = msg.exec()
        except:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText("Error !")
            msg.setWindowTitle("THANH HOAI")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel)
            retval = msg.exec()

    def slotOrLambdaFunction(self,clickedItem):
        stringCurrent = self.leInput.text().split()
        textTotal = clickedItem.text()
        stringCurrent[-1] = textTotal
        stringCurrent = " ".join(stringCurrent)
        self.leInput.setText(stringCurrent)
        self.leInput.setFocus()

    def CheckkingString(self):
        if True:
            self.currrntWord = self.getCurrentWord(self.leInput.text())
            self.lineEdit.setText(self.currrntWord)

    def getCurrentWord(self, sequence: str):
        if (sequence != ""):
            sequence = sequence.split()
            return sequence[-1]
        else:
            return ""
    def PridictWord(self):
        listProposal = self.root.predictWord(self.currrntWord,string="", result=[]) if self.currrntWord!="" else []
        if listProposal != self.passlist:
            self.listWidget.clear()
            self.passlist = listProposal
            for item in listProposal:
                self.listWidget.addItem(item)
            self.listWidget.setCurrentRow(self.index)
            self.index = self.listWidget.currentRow() if self.listWidget.currentRow() != -1 else 0
        else:
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Radix_Tree"))
        self.gbProcess.setTitle(_translate("MainWindow", "Process"))
        self.lbInformation.setText(_translate("MainWindow", "current word :"))
        self.pbAdditon.setText(_translate("MainWindow", "Add"))
        self.lbInput.setText(_translate("MainWindow", "Input :"))

if __name__ == "__main__":

    import sys
    app = QtWidgets .QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow=MainWindow)
    MainWindow.show()
    sys.exit(app.exec())