# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\sesa236189\OneDrive - Schneider Electric\Documents\Perso\pop-it\Projects\Zuora\ZTool_clean\ZTool_clean\BillingPreview\UI\qt\ZTools.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 442)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(517, 0))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frameHeader = QtWidgets.QFrame(self.centralwidget)
        self.frameHeader.setStyleSheet("background:white;")
        self.frameHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameHeader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameHeader.setObjectName("frameHeader")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frameHeader)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.titleLabel = QtWidgets.QLabel(self.frameHeader)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.horizontalLayout.addWidget(self.titleLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.toolIconLabel = QtWidgets.QLabel(self.frameHeader)
        self.toolIconLabel.setText("")
        self.toolIconLabel.setPixmap(QtGui.QPixmap(":/Buttons/images/Image1.png"))
        self.toolIconLabel.setObjectName("toolIconLabel")
        self.horizontalLayout.addWidget(self.toolIconLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.descriptionLabel = QtWidgets.QLabel(self.frameHeader)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.horizontalLayout_2.addWidget(self.descriptionLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.toolButton = QtWidgets.QToolButton(self.frameHeader)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Buttons/images/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.startButton = QtWidgets.QCommandLinkButton(self.frameHeader)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.startButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Buttons/images/bigGo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startButton.setIcon(icon1)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_3.addWidget(self.startButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.AllInOneLabel = QtWidgets.QLabel(self.frameHeader)
        self.AllInOneLabel.setStyleSheet("color:green")
        self.AllInOneLabel.setObjectName("AllInOneLabel")
        self.horizontalLayout_3.addWidget(self.AllInOneLabel)
        self.modeChoiceHorizontalSlider = QtWidgets.QSlider(self.frameHeader)
        self.modeChoiceHorizontalSlider.setMaximumSize(QtCore.QSize(35, 16777215))
        self.modeChoiceHorizontalSlider.setStyleSheet("QSlider::handle:horizontal {\n"
"background: #3dcd58;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}")
        self.modeChoiceHorizontalSlider.setMaximum(1)
        self.modeChoiceHorizontalSlider.setSingleStep(1)
        self.modeChoiceHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.modeChoiceHorizontalSlider.setObjectName("modeChoiceHorizontalSlider")
        self.horizontalLayout_3.addWidget(self.modeChoiceHorizontalSlider)
        self.stepBystepLabel = QtWidgets.QLabel(self.frameHeader)
        self.stepBystepLabel.setObjectName("stepBystepLabel")
        self.horizontalLayout_3.addWidget(self.stepBystepLabel)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.loginButton = QtWidgets.QCommandLinkButton(self.frameHeader)
        self.loginButton.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.loginButton.setFont(font)
        self.loginButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.loginButton.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Buttons/images/login_username.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginButton.setIcon(icon2)
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayout_4.addWidget(self.loginButton)
        self.billingButton = QtWidgets.QCommandLinkButton(self.frameHeader)
        self.billingButton.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.billingButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Buttons/images/billng.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.billingButton.setIcon(icon3)
        self.billingButton.setObjectName("billingButton")
        self.horizontalLayout_4.addWidget(self.billingButton)
        self.extendButton = QtWidgets.QCommandLinkButton(self.frameHeader)
        self.extendButton.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.extendButton.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Buttons/images/extend.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.extendButton.setIcon(icon4)
        self.extendButton.setObjectName("extendButton")
        self.horizontalLayout_4.addWidget(self.extendButton)
        self.arrangeButton = QtWidgets.QCommandLinkButton(self.frameHeader)
        self.arrangeButton.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.arrangeButton.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Buttons/images/arrange.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.arrangeButton.setIcon(icon5)
        self.arrangeButton.setObjectName("arrangeButton")
        self.horizontalLayout_4.addWidget(self.arrangeButton)
        self.finalizeButton = QtWidgets.QCommandLinkButton(self.frameHeader)
        self.finalizeButton.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.finalizeButton.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Buttons/images/finalize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.finalizeButton.setIcon(icon6)
        self.finalizeButton.setObjectName("finalizeButton")
        self.horizontalLayout_4.addWidget(self.finalizeButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frameHeader, 0, 0, 1, 1)
        self.frameWizard = QtWidgets.QFrame(self.centralwidget)
        self.frameWizard.setStyleSheet("background:white;")
        self.frameWizard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameWizard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameWizard.setObjectName("frameWizard")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frameWizard)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.wizardStackedWidget = QtWidgets.QStackedWidget(self.frameWizard)
        self.wizardStackedWidget.setStyleSheet("")
        self.wizardStackedWidget.setObjectName("wizardStackedWidget")
        self.loginPage = QtWidgets.QWidget()
        self.loginPage.setStyleSheet("")
        self.loginPage.setObjectName("loginPage")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.loginPage)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.frame = QtWidgets.QFrame(self.loginPage)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setMinimumSize(QtCore.QSize(100, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.userNamelineEdit = QtWidgets.QLineEdit(self.frame)
        self.userNamelineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.userNamelineEdit.setObjectName("userNamelineEdit")
        self.horizontalLayout_6.addWidget(self.userNamelineEdit)
        self.gridLayout_11.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setMinimumSize(QtCore.QSize(100, 0))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.passwordlineEdit = QtWidgets.QLineEdit(self.frame)
        self.passwordlineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordlineEdit.setObjectName("passwordlineEdit")
        self.horizontalLayout_5.addWidget(self.passwordlineEdit)
        self.gridLayout_11.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.directLabel = QtWidgets.QLabel(self.frame)
        self.directLabel.setObjectName("directLabel")
        self.horizontalLayout_7.addWidget(self.directLabel)
        self.proxySlider = QtWidgets.QSlider(self.frame)
        self.proxySlider.setMaximumSize(QtCore.QSize(35, 16777215))
        self.proxySlider.setStyleSheet("QSlider::handle:horizontal {\n"
"background: #3dcd58;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}")
        self.proxySlider.setMaximum(1)
        self.proxySlider.setOrientation(QtCore.Qt.Horizontal)
        self.proxySlider.setObjectName("proxySlider")
        self.horizontalLayout_7.addWidget(self.proxySlider)
        self.seProxyLabel = QtWidgets.QLabel(self.frame)
        self.seProxyLabel.setObjectName("seProxyLabel")
        self.horizontalLayout_7.addWidget(self.seProxyLabel)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.gridLayout_11.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)
        self.gridLayout_12.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.loginPage)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem7 = QtWidgets.QSpacerItem(47, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.frame_2)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Buttons/images/loginBig.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon7)
        self.commandLinkButton.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.horizontalLayout_8.addWidget(self.commandLinkButton)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.gridLayout_6.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.gridLayout_12.addWidget(self.frame_2, 0, 1, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.wizardStackedWidget.addWidget(self.loginPage)
        self.billingPage = QtWidgets.QWidget()
        self.billingPage.setStyleSheet("")
        self.billingPage.setObjectName("billingPage")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.billingPage)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_3 = QtWidgets.QFrame(self.billingPage)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.billingTargetDateEdit = QtWidgets.QDateEdit(self.frame_3)
        self.billingTargetDateEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.billingTargetDateEdit.setCalendarPopup(True)
        self.billingTargetDateEdit.setDate(QtCore.QDate(2018, 12, 7))
        self.billingTargetDateEdit.setObjectName("billingTargetDateEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.billingTargetDateEdit)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.invoiceDateDateEdit = QtWidgets.QDateEdit(self.frame_3)
        self.invoiceDateDateEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.invoiceDateDateEdit.setCalendarPopup(True)
        self.invoiceDateDateEdit.setObjectName("invoiceDateDateEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.invoiceDateDateEdit)
        self.gridLayout_10.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.billingPage)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.batchComboBox = QtWidgets.QComboBox(self.frame_4)
        self.batchComboBox.setObjectName("batchComboBox")
        self.batchComboBox.addItem("")
        self.batchComboBox.addItem("")
        self.batchComboBox.addItem("")
        self.batchComboBox.addItem("")
        self.batchComboBox.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.batchComboBox)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.onetimeCheckBox = QtWidgets.QCheckBox(self.frame_4)
        self.onetimeCheckBox.setObjectName("onetimeCheckBox")
        self.horizontalLayout_11.addWidget(self.onetimeCheckBox)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.recurringCheckBox = QtWidgets.QCheckBox(self.frame_4)
        self.recurringCheckBox.setObjectName("recurringCheckBox")
        self.horizontalLayout_12.addWidget(self.recurringCheckBox)
        self.usageCheckBox = QtWidgets.QCheckBox(self.frame_4)
        self.usageCheckBox.setObjectName("usageCheckBox")
        self.horizontalLayout_12.addWidget(self.usageCheckBox)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_12)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_11)
        self.gridLayout_9.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_4, 0, 1, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.billingPage)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout.setObjectName("gridLayout")
        self.launchBillingCommandLinkButton = QtWidgets.QCommandLinkButton(self.frame_5)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Buttons/images/billingLaunch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.launchBillingCommandLinkButton.setIcon(icon8)
        self.launchBillingCommandLinkButton.setIconSize(QtCore.QSize(40, 40))
        self.launchBillingCommandLinkButton.setObjectName("launchBillingCommandLinkButton")
        self.gridLayout.addWidget(self.launchBillingCommandLinkButton, 0, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 1, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_5, 0, 2, 1, 1)
        self.wizardStackedWidget.addWidget(self.billingPage)
        self.welcomePage = QtWidgets.QWidget()
        self.welcomePage.setObjectName("welcomePage")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.welcomePage)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtWidgets.QLabel(self.welcomePage)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.wizardStackedWidget.addWidget(self.welcomePage)
        self.gridLayout_3.addWidget(self.wizardStackedWidget, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frameWizard, 1, 0, 1, 1)
        self.frameResult = QtWidgets.QFrame(self.centralwidget)
        self.frameResult.setStyleSheet("background:white")
        self.frameResult.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameResult.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameResult.setObjectName("frameResult")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frameResult)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.resultTable = QtWidgets.QTableWidget(self.frameResult)
        self.resultTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.resultTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.resultTable.setTabKeyNavigation(False)
        self.resultTable.setProperty("showDropIndicator", False)
        self.resultTable.setDragDropOverwriteMode(False)
        self.resultTable.setObjectName("resultTable")
        self.resultTable.setColumnCount(0)
        self.resultTable.setRowCount(0)
        self.gridLayout_4.addWidget(self.resultTable, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frameResult, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.wizardStackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ZTools by Stef !"))
        self.titleLabel.setText(_translate("MainWindow", "bDO - Billing forecasting"))
        self.descriptionLabel.setText(_translate("MainWindow", "Generate Billing Preview Run from Zuora and lookup the result with subscription data source"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.startButton.setText(_translate("MainWindow", "Start New Process !"))
        self.AllInOneLabel.setText(_translate("MainWindow", "All in on step"))
        self.stepBystepLabel.setText(_translate("MainWindow", "Step by step mode"))
        self.loginButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Login to your Zuora tenant</p></body></html>"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.billingButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Launch your Billing Preview and import the temporary file</p></body></html>"))
        self.billingButton.setText(_translate("MainWindow", "Billing"))
        self.extendButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Launch Subscription details export and integrate results to billing preview</p></body></html>"))
        self.extendButton.setText(_translate("MainWindow", "Extend info"))
        self.arrangeButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Arrange headers and choose which one to export</p></body></html>"))
        self.arrangeButton.setText(_translate("MainWindow", "Arrange"))
        self.finalizeButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Generate final file (xls, csv, html,...)</p></body></html>"))
        self.finalizeButton.setText(_translate("MainWindow", "Finalize"))
        self.label_5.setText(_translate("MainWindow", "User Name"))
        self.label_6.setText(_translate("MainWindow", "User Password"))
        self.directLabel.setText(_translate("MainWindow", "Direct connexion"))
        self.seProxyLabel.setText(_translate("MainWindow", "Use SE Proxy"))
        self.commandLinkButton.setText(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "Target Date"))
        self.label_3.setText(_translate("MainWindow", "Invoice date"))
        self.label_4.setText(_translate("MainWindow", "Batch"))
        self.batchComboBox.setItemText(0, _translate("MainWindow", "Batch1"))
        self.batchComboBox.setItemText(1, _translate("MainWindow", "Batch2"))
        self.batchComboBox.setItemText(2, _translate("MainWindow", "Batch3"))
        self.batchComboBox.setItemText(3, _translate("MainWindow", "Batch4"))
        self.batchComboBox.setItemText(4, _translate("MainWindow", "Batch5"))
        self.label_7.setText(_translate("MainWindow", "Filters"))
        self.onetimeCheckBox.setText(_translate("MainWindow", "One Time"))
        self.recurringCheckBox.setText(_translate("MainWindow", "Recurring"))
        self.usageCheckBox.setText(_translate("MainWindow", "Usage"))
        self.launchBillingCommandLinkButton.setText(_translate("MainWindow", "Launch Billing Preview"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00aa00;\">Welcome on zpopTool ! Start a new process by pressing the big green arrow.</span></p><p>Choose wheter you want to execute the run in one step (define your preferences in settings) or step by step to control and debug the execution.</p></body></html>"))

import ztools_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
