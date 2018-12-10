import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets  import QWidget, QApplication, QTableWidget,QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets

from ZToolsUi import Ui_MainWindow
import ztools_rc

from popClasses.popBilling import connectionDetails, ZToken, ZFile

from datetime import datetime

class ZToolsApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ZToolsApp, self).__init__(parent=parent)
        
        #initialize UI
        self.setupUi(self)
        self.wizardStackedWidget.setCurrentIndex(2)
        
        
        #connect slots
        self.startButton.clicked.connect(self.startNewProcess)
        self.loginButton.clicked.connect(self.startLoginProcess)
        self.billingButton.clicked.connect(self.startBillingProcess)
        self.modeChoiceHorizontalSlider.valueChanged.connect(self.modeSet)
        self.proxySlider.valueChanged.connect(self.proxySet)
        self.commandLinkButton.clicked.connect(self.loginProcess)

    def startNewProcess(self):
        print("enfin")
        self.wizardStackedWidget.setCurrentIndex(2)
        self.loginButton.setEnabled(True)
        self.billingButton.setEnabled(False)
        self.extendButton.setEnabled(False)
        self.arrangeButton.setEnabled(False)
        self.finalizeButton.setEnabled(False)
        self.resultsTableInitialize()
        

    def startLoginProcess(self):
        print("login")
        self.proxyChoice = "N"
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
        myConnectionDetails = connectionDetails(self.userNamelineEdit.text(),self.passwordlineEdit.text(),proxy = self.proxyChoice)
        myZToken = ZToken()
        myZToken.generate(myConnectionDetails)
        print("Token is : " + myZToken.token)
        rowPosition = self.resultTable.rowCount()
        self.resultTable.setRowCount(rowPosition)
        self.resultTable.insertRow(rowPosition)
        self.resultTable.setItem(rowPosition , 0, QTableWidgetItem("Login"))
        if myZToken.status == "Success":          
            self.resultTable.setItem(rowPosition , 1, QTableWidgetItem("token : " + myZToken.token + "\nTenant : " + myZToken.tenant))
            self.resultTable.setItem(rowPosition , 2, QTableWidgetItem(myZToken.status))
            self.loginButton.setEnabled(False)
            self.billingButton.setEnabled(True)
            self.extendButton.setEnabled(True)
            self.wizardStackedWidget.setCurrentIndex(1)
            currentDate = QDate.currentDate()
            self.billingTargetDateEdit.setDate(currentDate)
            self.invoiceDateDateEdit.setDate(currentDate)
             
        else:
            self.resultTable.setItem(rowPosition , 1, QTableWidgetItem(str(myZToken.errorMsg)))
            self.resultTable.setItem(rowPosition , 2, QTableWidgetItem(myZToken.status))
        

    def resultsTableInitialize(self):
        headers = ["step", "Details (Timestamp, Name,...)", "status", "actions"]
        self.resultTable.setColumnCount(4)
        self.resultTable.setRowCount(0)
        self.resultTable.setHorizontalHeaderLabels(headers)

def main(args):
    app = QtWidgets.QApplication(sys.argv)
    w = ZToolsApp()
    w.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":

    main(sys.argv)
    
