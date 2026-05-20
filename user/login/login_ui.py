# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'server_login_uilEToEZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 352)
        MainWindow.setMinimumSize(QSize(700, 352))
        MainWindow.setMaximumSize(QSize(700, 352))
        font = QFont()
        font.setFamily(u"OCR-A")
        MainWindow.setFont(font)
        self.Mainbar = QWidget(MainWindow)
        self.Mainbar.setObjectName(u"Mainbar")
        self.Mainbar.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.Mainbar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.BackgroundWidget = QWidget(self.Mainbar)
        self.BackgroundWidget.setObjectName(u"BackgroundWidget")
        self.BackgroundWidget.setStyleSheet(u"QWidget {\n"
"background-color: rgba(7,40,83,255);\n"
"\n"
"color: #016abf;\n"
"}\n"
"\n"
"QWidget#BackgroundWidget {\n"
"	background-image: url(:/icons/assets/login/background.png);\n"
"border: 2px solid #27a8e0;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.BackgroundWidget)
        self.verticalLayout_3.setSpacing(25)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(25, 25, 25, 0)
        self.stacked_pages = QStackedWidget(self.BackgroundWidget)
        self.stacked_pages.setObjectName(u"stacked_pages")
        self.stacked_pages.setLayoutDirection(Qt.LeftToRight)
        self.stacked_pages.setStyleSheet(u"border: 0px solid;")
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.verticalLayout_6 = QVBoxLayout(self.login_page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.login_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(190, 30, 0, 20)
        self.Login_text = QLabel(self.frame_3)
        self.Login_text.setObjectName(u"Login_text")
        self.Login_text.setMinimumSize(QSize(275, 0))
        self.Login_text.setMaximumSize(QSize(275, 50))
        font1 = QFont()
        font1.setFamily(u"SAO UI")
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setWeight(50)
        self.Login_text.setFont(font1)
        self.Login_text.setFocusPolicy(Qt.StrongFocus)
        self.Login_text.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border: 0px solid;")
        self.Login_text.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.Login_text)

        self.username_input = QLineEdit(self.frame_3)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setMinimumSize(QSize(275, 50))
        self.username_input.setMaximumSize(QSize(275, 50))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.username_input.setFont(font2)
        self.username_input.setStyleSheet(u"QLineEdit { \n"
"	border: 3px solid #0070bf;\n"
"	color: #016abf;\n"
"	background-color: rgba(3,51,99,255);\n"
"	padding-left: 10px; \n"
"	padding-bottom: 10px;\n"
"	padding-top: 10px;\n"
"	image-repeat: no-repeat; \n"
"	image-position: left; \n"
"	image: url(:/icons/assets/icon/user.png);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit[urgent=true] {\n"
"	image: url(:/icons/assets/icon/transparent.png);\n"
"}\n"
"\n"
"QLineEdit[urgent=false] {\n"
"	image: url(:/icons/assets/icon/user.png);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	image: url(:/icons/assets/icon/transparent.png);\n"
"}\n"
"")
        self.username_input.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.username_input.setClearButtonEnabled(False)

        self.verticalLayout_2.addWidget(self.username_input)

        self.widget = QWidget(self.frame_3)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(275, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.password_input = QLineEdit(self.widget)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMinimumSize(QSize(275, 50))
        self.password_input.setMaximumSize(QSize(275, 50))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(12)
        self.password_input.setFont(font3)
        self.password_input.setStyleSheet(u"QLineEdit { \n"
"	border: 3px solid #0070bf;\n"
"	color: #016abf;\n"
"	background-color: rgba(3,51,99,255);\n"
"	padding-left: 10px; \n"
"	padding-bottom: 10px;\n"
"	padding-top: 10px;\n"
"	image-repeat: no-repeat; \n"
"	image-position: left; \n"
"	image: url(:/icons/assets/icon/lock.png);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit[urgent=true] {\n"
"	image: url(:/icons/assets/icon/transparent.png);\n"
"}\n"
"\n"
"QLineEdit[urgent=false] {\n"
"	image: url(:/icons/assets/icon/lock.png);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	image: url(:/icons/assets/icon/transparent.png);\n"
"}\n"
"")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.password_input)

        self.password_enter = QPushButton(self.widget)
        self.password_enter.setObjectName(u"password_enter")
        self.password_enter.setMinimumSize(QSize(50, 50))
        font4 = QFont()
        font4.setFamily(u"OCR-A")
        font4.setPointSize(15)
        font4.setBold(True)
        font4.setWeight(75)
        self.password_enter.setFont(font4)
        self.password_enter.setCursor(QCursor(Qt.PointingHandCursor))
        self.password_enter.setFocusPolicy(Qt.NoFocus)
        self.password_enter.setStyleSheet(u"QPushButton {\n"
"	color:rgba(1, 106, 191,255);\n"
"}\n"
"QPushButton:hover {\n"
"	color:rgba(1, 106, 191,150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.password_enter)


        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.login_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 30))
        self.frame_5.setMaximumSize(QSize(16777215, 70))
        self.frame_5.setStyleSheet(u"text-align:center;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 20)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 30))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(260, 0, 0, 0)
        self.create_account_login = QPushButton(self.frame_6)
        self.create_account_login.setObjectName(u"create_account_login")
        self.create_account_login.setMinimumSize(QSize(0, 30))
        self.create_account_login.setMaximumSize(QSize(130, 16777215))
        font5 = QFont()
        font5.setFamily(u"SAO UI")
        font5.setPointSize(15)
        font5.setBold(False)
        font5.setWeight(50)
        self.create_account_login.setFont(font5)
        self.create_account_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.create_account_login.setFocusPolicy(Qt.NoFocus)
        self.create_account_login.setStyleSheet(u"QPushButton {\n"
"	 background-color: 0; \n"
"	color: rgba(1, 106, 191,150)\n"
" }\n"
"QPushButton:hover {\n"
"	color: rgba(1, 106, 191,255)\n"
"}")
        self.create_account_login.setCheckable(False)

        self.verticalLayout_8.addWidget(self.create_account_login)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.WarningText = QLabel(self.frame_5)
        self.WarningText.setObjectName(u"WarningText")
        self.WarningText.setMaximumSize(QSize(16777215, 30))
        font6 = QFont()
        font6.setFamily(u"OCR-A")
        font6.setPointSize(12)
        self.WarningText.setFont(font6)
        self.WarningText.setStyleSheet(u"padding-top: 10px;\n"
"color: rgb(255, 0, 0);")
        self.WarningText.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.WarningText)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.stacked_pages.addWidget(self.login_page)
        self.create_account_page = QWidget()
        self.create_account_page.setObjectName(u"create_account_page")
        self.horizontalLayout = QHBoxLayout(self.create_account_page)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(115, 0, 0, 0)
        self.frame_2 = QFrame(self.create_account_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(52, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 200)
        self.back_login = QPushButton(self.frame_2)
        self.back_login.setObjectName(u"back_login")
        self.back_login.setMinimumSize(QSize(30, 30))
        self.back_login.setMaximumSize(QSize(30, 30))
        font7 = QFont()
        font7.setFamily(u"OCR-A")
        font7.setPointSize(20)
        font7.setBold(True)
        font7.setItalic(False)
        font7.setUnderline(False)
        font7.setWeight(75)
        font7.setStrikeOut(False)
        font7.setKerning(True)
        font7.setStyleStrategy(QFont.PreferAntialias)
        self.back_login.setFont(font7)
        self.back_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_login.setFocusPolicy(Qt.NoFocus)
        self.back_login.setStyleSheet(u"QPushButton {\n"
"	color:rgba(1, 106, 191,255);\n"
"}\n"
"QPushButton:hover {\n"
"	color:rgba(1, 106, 191,150);\n"
"}")

        self.verticalLayout_5.addWidget(self.back_login)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.create_account_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(23, 25, 0, 2)
        self.create_account_label = QLabel(self.frame)
        self.create_account_label.setObjectName(u"create_account_label")
        self.create_account_label.setMinimumSize(QSize(0, 50))
        self.create_account_label.setMaximumSize(QSize(275, 50))
        font8 = QFont()
        font8.setFamily(u"SAO UI")
        font8.setPointSize(20)
        font8.setBold(False)
        font8.setWeight(50)
        font8.setKerning(True)
        font8.setStyleStrategy(QFont.PreferDefault)
        self.create_account_label.setFont(font8)
        self.create_account_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.create_account_label)

        self.create_account_name = QLineEdit(self.frame)
        self.create_account_name.setObjectName(u"create_account_name")
        self.create_account_name.setMinimumSize(QSize(275, 50))
        self.create_account_name.setMaximumSize(QSize(275, 50))
        self.create_account_name.setFont(font6)
        self.create_account_name.setStyleSheet(u"border: 3px solid #0070bf;\n"
"color: #016abf;\n"
"background-color: rgba(3,51,99,255);\n"
"border-radius: 10px;\n"
"padding-left: 5px;")

        self.verticalLayout_4.addWidget(self.create_account_name)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(275, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.create_account_pass = QLineEdit(self.widget_2)
        self.create_account_pass.setObjectName(u"create_account_pass")
        self.create_account_pass.setMinimumSize(QSize(275, 50))
        self.create_account_pass.setMaximumSize(QSize(275, 50))
        self.create_account_pass.setFont(font6)
        self.create_account_pass.setStyleSheet(u"border: 3px solid #0070bf;\n"
"color: #016abf;\n"
"background-color: rgba(3,51,99,255);\n"
"border-radius: 10px;\n"
"padding-left: 5px;")
        self.create_account_pass.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.create_account_pass)

        self.toggle_show_password = QCheckBox(self.widget_2)
        self.toggle_show_password.setObjectName(u"toggle_show_password")
        self.toggle_show_password.setMinimumSize(QSize(50, 50))
        self.toggle_show_password.setMaximumSize(QSize(50, 50))
        font9 = QFont()
        font9.setPointSize(15)
        font9.setBold(False)
        font9.setWeight(50)
        self.toggle_show_password.setFont(font9)
        self.toggle_show_password.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggle_show_password.setFocusPolicy(Qt.NoFocus)
        self.toggle_show_password.setStyleSheet(u"QCheckBox {\n"
"	color:rgba(1, 106, 191,255);\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	image: url(:/icons/assets/icon/password_show.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icons/assets/icon/password_hide.png);\n"
"}\n"
"QCheckBox::indicator {\n"
"            width: 25px;\n"
"            height: 25px;\n"
"			padding-left: 10px;\n"
"}")
        self.toggle_show_password.setText(u"")

        self.horizontalLayout_3.addWidget(self.toggle_show_password)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 69))
        self.frame_4.setMaximumSize(QSize(275, 70))
        self.frame_4.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(175, 35))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(104, 0, 0, 0)
        self.create_account_button = QPushButton(self.frame_7)
        self.create_account_button.setObjectName(u"create_account_button")
        self.create_account_button.setMinimumSize(QSize(70, 40))
        self.create_account_button.setMaximumSize(QSize(70, 40))
        font10 = QFont()
        font10.setFamily(u"SAO UI")
        font10.setPointSize(16)
        self.create_account_button.setFont(font10)
        self.create_account_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.create_account_button.setFocusPolicy(Qt.NoFocus)
        self.create_account_button.setStyleSheet(u"QPushButton {\n"
"	 background-color: 0; \n"
"	color: rgba(1, 106, 191,150)\n"
" }\n"
"QPushButton:hover {\n"
"	color: rgba(1, 106, 191,255)\n"
"}")

        self.verticalLayout_10.addWidget(self.create_account_button)


        self.verticalLayout_9.addWidget(self.frame_7)

        self.Warning_create_account = QLabel(self.frame_4)
        self.Warning_create_account.setObjectName(u"Warning_create_account")
        self.Warning_create_account.setMinimumSize(QSize(275, 0))
        self.Warning_create_account.setMaximumSize(QSize(300, 200))
        font11 = QFont()
        font11.setFamily(u"OCR-A")
        font11.setPointSize(9)
        self.Warning_create_account.setFont(font11)
        self.Warning_create_account.setStyleSheet(u"padding: 10px;\n"
"color: rgb(0, 255, 162);")
        self.Warning_create_account.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.Warning_create_account)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame)

        self.stacked_pages.addWidget(self.create_account_page)

        self.verticalLayout_3.addWidget(self.stacked_pages)


        self.verticalLayout.addWidget(self.BackgroundWidget)

        MainWindow.setCentralWidget(self.Mainbar)

        self.retranslateUi(MainWindow)

        self.stacked_pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.frame_3.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: rgba(255, 255, 255, 0);\n"
"border: 0px solid;", None))
        self.Login_text.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.username_input.setText("")
        self.username_input.setPlaceholderText("")
        self.password_input.setPlaceholderText("")
        self.password_enter.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.create_account_login.setText(QCoreApplication.translate("MainWindow", u"Create Account", None))
        self.WarningText.setText("")
        self.back_login.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.create_account_label.setText(QCoreApplication.translate("MainWindow", u"Create Account", None))
        self.create_account_name.setText("")
        self.create_account_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.create_account_pass.setText("")
        self.create_account_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"password", None))
        self.create_account_button.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.Warning_create_account.setText("")
    # retranslateUi

