import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets  import QWidget, QApplication, QTableWidget,QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

from ZToolsUi import Ui_MainWindow
import ztools_rc

from popClasses.popBilling import connectionDetails, ZToken, ZFile

from datetime import datetime

import time

class ZToolsApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ZToolsApp, self).__init__(parent=parent)
        
        #initialize UI
        self.setupUi(self)
        self.wizardStackedWidget.setCurrentIndex(2)
        self.firstLaunch = True
        
        
        #connect slots
        self.startButton.clicked.connect(self.startNewProcess)
        self.loginButton.clicked.connect(self.startLoginProcess)
        self.billingButton.clicked.connect(self.startBillingProcess)
        self.modeChoiceHorizontalSlider.valueChanged.connect(self.modeSet)
        self.proxySlider.valueChanged.connect(self.proxySet)
        self.commandLinkButton.clicked.connect(self.loginProcess)
        self.launchBillingCommandLinkButton.clicked.connect(self.launchBillingProcess)

    def startNewProcess(self):
        print("enfin")
        
        if self.firstLaunch == False:
            buttonReply = QMessageBox.question(self, 'Re start Process', "Are you sure ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.No:
                return
            
        self.wizardStackedWidget.setCurrentIndex(2)
        self.loginButton.setEnabled(True)
        self.billingButton.setEnabled(False)
        self.extendButton.setEnabled(False)
        self.arrangeButton.setEnabled(False)
        self.finalizeButton.setEnabled(False)
        self.resultsTableInitialize()
        self.firstLaunch = True
        

    def startLoginProcess(self):
        print("login")
        self.proxyChoice = "N"
        self.firstLaunch = False
        self.wizardStackedWidget.setCurrentIndex(0)

    def startBillingProcess(self):
        print("login")
        self.wizardStackedWidget.setCurrentIndex(1)   

    def modeSet(self):
        if self.modeChoiceHorizontalSlider.value() == 0:
            self.AllInOneLabel.setStyleSheet("color:green")
            self.stepBystepLabel.setStyleSheet("color:black")
        else:
            self.AllInOneLabel.setStyleSheet("color:black")
            self.stepBystepLabel.setStyleSheet("color:green")

    def proxySet(self):
        if self.proxySlider.value() == 0:
            self.directLabel.setStyleSheet("color:green")
            self.seProxyLabel.setStyleSheet("color:black")
            self.proxyChoice = "N"
        else:
            self.directLabel.setStyleSheet("color:black")
            self.proxyChoice = "Y"
            self.seProxyLabel.setStyleSheet("color:green")

    def loginProcess(self):
        print("start login")
        self.myConnectionDetails = connectionDetails(self.userNamelineEdit.text(),self.passwordlineEdit.text(),proxy = self.proxyChoice)
        self.myZToken = ZToken()
        self.myZToken.generate(self.myConnectionDetails)
        print("Token is : " + self.myZToken.token)
        rowPosition = self.resultTable.rowCount()
        self.resultTable.setRowCount(rowPosition)
        self.resultTable.insertRow(rowPosition)
        self.resultTable.setItem(rowPosition , 0, QTableWidgetItem("Login"))
        if self.myZToken.status == "Success":          
            self.resultTable.setItem(rowPosition , 1, QTableWidgetItem("token : " + self.myZToken.token + "\nTenant : " + self.myZToken.tenant))
            self.resultTable.setItem(rowPosition , 2, QTableWidgetItem(self.myZToken.status))
            self.loginButton.setEnabled(False)
            self.billingButton.setEnabled(True)
            self.extendButton.setEnabled(True)
            self.wizardStackedWidget.setCurrentIndex(1)
            currentDate = QDate.currentDate()
            self.billingTargetDateEdit.setDate(currentDate)
            self.invoiceDateDateEdit.setDate(currentDate)
             
        else:
            self.resultTable.setItem(rowPosition , 1, QTableWidgetItem(str(self.myZToken.errorMsg)))
            self.resultTable.setItem(rowPosition , 2, QTableWidgetItem(self.myZToken.status))
        

    def resultsTableInitialize(self):
        headers = ["step", "Details (Timestamp, Name,...)", "status", "actions"]
        self.resultTable.setColumnCount(4)
        self.resultTable.setRowCount(0)
        self.resultTable.setHorizontalHeaderLabels(headers)
        header = self.resultTable.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

    def launchBillingProcess(self):
        print("still under construction !")
        #rowPosition = self.resultTable.rowCount()
        #self.resultTable.setRowCount(rowPosition)
        #self.resultTable.insertRow(rowPosition)
        #self.resultTable.setItem(rowPosition , 0, QTableWidgetItem("Billing Preview"))
        #myZbillingPreviewRun = ZFile("BillingPreviewRun")
        #myZbillingPreviewRun.generate(self.myConnectionDetails, self.myZToken)
        #if myZbillingPreviewRun.value == "SUCCESS" :
        #    print("Billing Run Id : " + myZbillingPreviewRun.runId)
        #    myZbillingPreviewRun.value == "Started"            
        #    self.resultTable.setItem(rowPosition , 1, QTableWidgetItem("Billing Run Id : " + myZbillingPreviewRun.runId))
        #    self.resultTable.setItem(rowPosition , 2, QTableWidgetItem(myZbillingPreviewRun.value))
        #    myZbillingPreviewRun.retrieve(myConnectionDetails, myZbillingPreviewRun.runId, myZToken, 100)
        #else:
        #    myZbillingPreviewRun.value == "Launch failed"
        #    self.resultTable.setItem(rowPosition , 1, QTableWidgetItem("coucou"))
        #    self.resultTable.setItem(rowPosition , 2, QTableWidgetItem(myZbillingPreviewRun.value))

def main(args):

    app = QtWidgets.QApplication(sys.argv)

    # Create and display the splash screen
    splash_pix = QtGui.QPixmap(":/Buttons/images/lifeIsOn_black.jpg")
    splash = QtWidgets.QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)

    splash = QtWidgets.QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.setEnabled(False)
    # splash = QSplashScreen(splash_pix)
    # adding progress bar
    progressBar = QtWidgets.QProgressBar(splash)
    progressBar.setMaximum(10)
    progressBar.setGeometry(0, splash_pix.height() - 50, splash_pix.width(), 20)
    splash.show()

    for i in range(1, 50):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.1:
           app.processEvents()
   
    w = ZToolsApp()
    w.show()
    splash.close()
    
    sys.exit(app.exec_())
    

if __name__ == "__main__":

    main(sys.argv)
    
