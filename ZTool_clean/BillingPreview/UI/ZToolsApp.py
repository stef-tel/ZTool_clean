from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets  import QWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets

from ZToolsUi import Ui_MainWindow
import ztools_rc
import sys

class ZToolsApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ZToolsApp, self).__init__(parent=parent)
        self.setupUi(self)
        self.startButton.clicked.connect(self.startNewProcess)
        self.loginButton.clicked.connect(self.startLoginProcess)

    def startNewProcess(self):
        print("enfin")

    def startLoginProcess(self):
        print("login")   


def main(args):
    app = QtWidgets.QApplication(sys.argv)
    w = ZToolsApp()
    w.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":

    main(sys.argv)
    
