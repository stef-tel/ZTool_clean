import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets  import QWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets

from ZToolsUi import Ui_MainWindow
import ztools_rc

from popClasses.popBilling import connectionDetails, ZToken, ZFile

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
        self.modeChoiceHorizontalSlider.valueChanged.connect(self.modeLabelsColorSet)
        self.commandLinkButton.clicked.connect(self.loginProcess)

    def startNewProcess(self):
        print("enfin")
        self.wizardStackedWidget.setCurrentIndex(2)
        self.loginButton.setEnabled(True)
        self.billingButton.setEnabled(False)
        self.extendButton.setEnabled(False)
        self.arrangeButton.setEnabled(False)
        self.finalizeButton.setEnabled(False)

    def startLoginProcess(self):
        print("login")
        self.wizardStackedWidget.setCurrentIndex(0)

    def startBillingProcess(self):
        print("login")
        self.wizardStackedWidget.setCurrentIndex(1)   

    def modeLabelsColorSet(self):
        if self.modeChoiceHorizontalSlider.value() == 0:
            self.AllInOneLabel.setStyleSheet("color:green")
            self.stepBystepLabel.setStyleSheet("color:black")
        else:
            self.AllInOneLabel.setStyleSheet("color:black")
            self.stepBystepLabel.setStyleSheet("color:green")

    def loginProcess(self):
        print("start login")
        myConnectionDetails = connectionDetails("c2bfc320-bb04-413d-8ce6-91886f7b4d9b","xnAH1Foi03IxaybnuBL1",proxy = 'N')
        myZToken = ZToken()
        myZToken.generate(myConnectionDetails)
        print("Token is : " + myZToken.token)

def main(args):
    app = QtWidgets.QApplication(sys.argv)
    w = ZToolsApp()
    w.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":

    main(sys.argv)
    
