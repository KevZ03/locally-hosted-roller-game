# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game2OxfbHL.ui'
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
        MainWindow.resize(1920, 1080)
        MainWindow.setMaximumSize(QSize(1920, 1080))
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        MainWindow.setStyleSheet(u"@font-face {\n"
"    font-family: \"SAOUI\";\n"
"    src: url(\":/icons/assets/font/SAOUI-Regular.otf\");\n"
"}\n"
"\n"
"\n"
"QMainWindow {\n"
"    font-family: \"SAOUI\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.Game_Windows = QWidget(MainWindow)
        self.Game_Windows.setObjectName(u"Game_Windows")
        self.Game_Windows.setMinimumSize(QSize(1920, 1080))
        self.Game_Windows.setMaximumSize(QSize(1920, 1080))
        self.horizontalLayout = QHBoxLayout(self.Game_Windows)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.Game_Windows)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(0, 16777215))
        font = QFont()
        font.setFamily(u"SAO UI")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.widget_3.setFont(font)
        self.widget_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.Game_Windows)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(0, 16777215))
        self.widget_4.setFont(font)
        self.widget_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout.addWidget(self.widget_4)

        self.Content = QStackedWidget(self.Game_Windows)
        self.Content.setObjectName(u"Content")
        self.Content.setMinimumSize(QSize(1280, 0))
        self.Content.setMaximumSize(QSize(1920, 1080))
        self.Content.setFont(font)
        self.Content.setStyleSheet(u"\n"
"color: rgb(255,255,255);")
        self.Content.setLineWidth(0)
        self.HomePage = QWidget()
        self.HomePage.setObjectName(u"HomePage")
        self.HomePage.setStyleSheet(u"QWidget#HomePage {\n"
"background-image: url(:/background/assets/background/background.png);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.HomePage)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.MainWidget = QWidget(self.HomePage)
        self.MainWidget.setObjectName(u"MainWidget")
        font1 = QFont()
        font1.setFamily(u"SAO UI")
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.MainWidget.setFont(font1)
        self.MainWidget.setStyleSheet(u"")
        self.horizontalLayout_29 = QHBoxLayout(self.MainWidget)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.main_screen_buton_widget = QWidget(self.MainWidget)
        self.main_screen_buton_widget.setObjectName(u"main_screen_buton_widget")
        self.main_screen_buton_widget.setMinimumSize(QSize(500, 650))
        self.main_screen_buton_widget.setMaximumSize(QSize(1000, 1080))
        self.main_screen_buton_widget.setFont(font1)
        self.verticalLayout_4 = QVBoxLayout(self.main_screen_buton_widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.GameTitle = QLabel(self.main_screen_buton_widget)
        self.GameTitle.setObjectName(u"GameTitle")
        self.GameTitle.setMinimumSize(QSize(500, 300))
        font2 = QFont()
        font2.setFamily(u"Sans Serif Collection")
        font2.setPointSize(100)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(50)
        self.GameTitle.setFont(font2)
        self.GameTitle.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,200); \n"
"	background-colour: 0;\n"
"	border:0;\n"
"text-align: centre; \n"
"    padding-left: 20px;	\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton::indicator {\n"
"    background-color: #ffffff;\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgba(255,255,255,255);\n"
"    font-size: 105px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   color: rgba(255,255,255,225);\n"
"}\n"
"")
        self.GameTitle.setAlignment(Qt.AlignCenter)
        self.GameTitle.setMargin(0)

        self.verticalLayout_4.addWidget(self.GameTitle)

        self.online_button = QPushButton(self.main_screen_buton_widget)
        self.online_button.setObjectName(u"online_button")
        self.online_button.setMinimumSize(QSize(380, 0))
        self.online_button.setMaximumSize(QSize(313131, 125))
        font3 = QFont()
        font3.setFamily(u"Sans Serif Collection")
        font3.setPointSize(55)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.online_button.setFont(font3)
        self.online_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.online_button.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,200); \n"
"	background-colour: 0;\n"
"	border:0;\n"
"text-align: centre; \n"
"    padding-left: 20px;	\n"
"\n"
"}\n"
"\n"
"QPushButton::indicator {\n"
"    background-color: #ffffff;\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgba(255,255,255,255);\n"
"    font-size: 105px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   color: rgba(255,255,255,225);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.online_button)

        self.local_button = QPushButton(self.main_screen_buton_widget)
        self.local_button.setObjectName(u"local_button")
        self.local_button.setMinimumSize(QSize(380, 0))
        self.local_button.setMaximumSize(QSize(313131, 125))
        self.local_button.setFont(font3)
        self.local_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.local_button.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,200); \n"
"	background-colour: 0;\n"
"	border:0;\n"
"text-align: centre; \n"
"    padding-left: 20px;	\n"
"\n"
"}\n"
"\n"
"QPushButton::indicator {\n"
"    background-color: #ffffff;\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgba(255,255,255,255);\n"
"    font-size: 105px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   color: rgba(255,255,255,225);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.local_button)

        self.settings_button = QPushButton(self.main_screen_buton_widget)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setMinimumSize(QSize(380, 0))
        self.settings_button.setMaximumSize(QSize(313131, 125))
        self.settings_button.setFont(font3)
        self.settings_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_button.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,200); \n"
"	background-colour: 0;\n"
"	border:0;\n"
"text-align: centre; \n"
"    padding-left: 20px;	\n"
"\n"
"}\n"
"\n"
"QPushButton::indicator {\n"
"    background-color: #ffffff;\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgba(255,255,255,255);\n"
"    font-size: 105px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   color: rgba(255,255,255,225);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.settings_button)

        self.about_button = QPushButton(self.main_screen_buton_widget)
        self.about_button.setObjectName(u"about_button")
        self.about_button.setMinimumSize(QSize(380, 0))
        self.about_button.setMaximumSize(QSize(313131, 125))
        self.about_button.setFont(font3)
        self.about_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.about_button.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,200); \n"
"	background-colour: 0;\n"
"	border:0;\n"
"text-align: centre; \n"
"    padding-left: 20px;	\n"
"\n"
"}\n"
"\n"
"QPushButton::indicator {\n"
"    background-color: #ffffff;\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgba(255,255,255,255);\n"
"    font-size: 105px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   color: rgba(255,255,255,225);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.about_button)

        self.quit_button = QPushButton(self.main_screen_buton_widget)
        self.quit_button.setObjectName(u"quit_button")
        self.quit_button.setMinimumSize(QSize(380, 0))
        self.quit_button.setMaximumSize(QSize(313131, 125))
        self.quit_button.setFont(font3)
        self.quit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.quit_button.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,200); \n"
"	background-colour: 0;\n"
"	border:0;\n"
"text-align: centre; \n"
"    padding-left: 20px;	\n"
"\n"
"}\n"
"\n"
"QPushButton::indicator {\n"
"    background-color: #ffffff;\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgba(255,255,255,255);\n"
"    font-size: 105px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   color: rgba(255,255,255,225);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.quit_button)


        self.horizontalLayout_29.addWidget(self.main_screen_buton_widget)


        self.verticalLayout_3.addWidget(self.MainWidget)

        self.BottomWidget = QWidget(self.HomePage)
        self.BottomWidget.setObjectName(u"BottomWidget")
        self.BottomWidget.setMaximumSize(QSize(16777215, 100))
        self.BottomWidget.setFont(font1)
        self.label = QLabel(self.BottomWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1560, 20, 291, 51))
        font4 = QFont()
        font4.setFamily(u"SAO UI")
        font4.setPointSize(18)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.label.setFont(font4)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.BottomWidget)

        self.Content.addWidget(self.HomePage)
        self.PlayPage = QWidget()
        self.PlayPage.setObjectName(u"PlayPage")
        self.PlayPage.setStyleSheet(u"\n"
"QWidget#PlayPage {\n"
"background-image: url(:/background/assets/background/background2);\n"
"}\n"
"\n"
"QWidget {\n"
"color: rgb(0, 0, 0);\n"
"\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.PlayPage)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.TopWidget_4 = QWidget(self.PlayPage)
        self.TopWidget_4.setObjectName(u"TopWidget_4")
        self.TopWidget_4.setMaximumSize(QSize(16777215, 100))
        self.TopWidget_4.setFont(font1)
        self.TopWidget_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.horizontalLayout_16 = QHBoxLayout(self.TopWidget_4)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(30, 15, 0, 0)
        self.server_back_button = QPushButton(self.TopWidget_4)
        self.server_back_button.setObjectName(u"server_back_button")
        self.server_back_button.setMinimumSize(QSize(150, 70))
        self.server_back_button.setMaximumSize(QSize(150, 70))
        font5 = QFont()
        font5.setFamily(u"SAO UI")
        font5.setPointSize(32)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.server_back_button.setFont(font5)
        self.server_back_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.server_back_button.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(0,0,0,150);\n"
"border: 3px solid white;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgba(255,255,255,200);\n"
"border: 3px solid rgba(255,255,255,200);;\n"
"background-color: rgba(0,0,0,200);\n"
"\n"
"}")

        self.horizontalLayout_16.addWidget(self.server_back_button)

        self.widget_18 = QWidget(self.TopWidget_4)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setFont(font1)

        self.horizontalLayout_16.addWidget(self.widget_18)


        self.verticalLayout_9.addWidget(self.TopWidget_4)

        self.PlayPageStackedWidget = QStackedWidget(self.PlayPage)
        self.PlayPageStackedWidget.setObjectName(u"PlayPageStackedWidget")
        self.PlayPageStackedWidget.setFont(font1)
        self.PlayPageStackedWidget.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0,0,0, 0);\n"
"")
        self.ServerListPage = QWidget()
        self.ServerListPage.setObjectName(u"ServerListPage")
        self.ServerListPage.setStyleSheet(u"")
        self.horizontalLayout_35 = QHBoxLayout(self.ServerListPage)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(150, 150, 150, 150)
        self.ServerContainer = QWidget(self.ServerListPage)
        self.ServerContainer.setObjectName(u"ServerContainer")
        self.ServerContainer.setStyleSheet(u"QWidget#ServerContainer {\n"
"background-color: rgba(0,0,0,150);\n"
"border-color: rgb(0, 0, 0);\n"
"border: 10px solid white;\n"
"}")
        self.horizontalLayout_10 = QHBoxLayout(self.ServerContainer)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.ServerContainer)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setFont(font1)
        self.widget_5.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.widget_5)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.server_list_widget = QWidget(self.widget_5)
        self.server_list_widget.setObjectName(u"server_list_widget")
        self.server_list_widget.setFont(font1)
        self.verticalLayout_10 = QVBoxLayout(self.server_list_widget)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(50, 50, 0, 0)
        self.widget_2 = QWidget(self.server_list_widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(20220, 225))
        self.widget_2.setFont(font1)
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, -1, 0)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        font6 = QFont()
        font6.setFamily(u"SAO UI")
        font6.setPointSize(70)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(200, 16777215))
        font7 = QFont()
        font7.setFamily(u"SAO UI")
        font7.setPointSize(20)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(50)
        self.label_3.setFont(font7)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: left;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.create_server_button = QPushButton(self.widget_2)
        self.create_server_button.setObjectName(u"create_server_button")
        self.create_server_button.setMinimumSize(QSize(0, 50))
        self.create_server_button.setMaximumSize(QSize(200, 16777215))
        font8 = QFont()
        font8.setFamily(u"SAO UI")
        font8.setPointSize(20)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setUnderline(True)
        font8.setWeight(50)
        self.create_server_button.setFont(font8)
        self.create_server_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.create_server_button.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,200); /* Normal text color */\n"
"	background-colour: 0;\n"
"	border:0;\n"
"	\n"
"	\n"
"\n"
"}\n"
"\n"
"QPushButton::indicator {\n"
"    background-color: #ffffff; /* Color of the bullet point */\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgba(255,255,255,255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   color: rgba(255,255,255,225);\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.create_server_button)


        self.verticalLayout_10.addWidget(self.widget_2)

        self.widget_10 = QWidget(self.server_list_widget)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setFont(font1)

        self.verticalLayout_10.addWidget(self.widget_10)


        self.verticalLayout_8.addWidget(self.server_list_widget)


        self.horizontalLayout_10.addWidget(self.widget_5)

        self.Server_Widget = QWidget(self.ServerContainer)
        self.Server_Widget.setObjectName(u"Server_Widget")
        self.Server_Widget.setMinimumSize(QSize(500, 700))
        self.Server_Widget.setMaximumSize(QSize(800, 123131))
        self.Server_Widget.setFont(font1)
        self.Server_Widget.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.Server_Widget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Server_top_bar = QWidget(self.Server_Widget)
        self.Server_top_bar.setObjectName(u"Server_top_bar")
        self.Server_top_bar.setMinimumSize(QSize(0, 50))
        self.Server_top_bar.setMaximumSize(QSize(16777215, 100))
        self.Server_top_bar.setFont(font1)
        self.horizontalLayout_8 = QHBoxLayout(self.Server_top_bar)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(100, 0, 0, 0)
        self.refresh_sever = QPushButton(self.Server_top_bar)
        self.refresh_sever.setObjectName(u"refresh_sever")
        self.refresh_sever.setMinimumSize(QSize(100, 50))
        self.refresh_sever.setMaximumSize(QSize(100, 16777215))
        self.refresh_sever.setFont(font7)
        self.refresh_sever.setCursor(QCursor(Qt.PointingHandCursor))
        self.refresh_sever.setStyleSheet(u"QPushButton:hover {\n"
"color: rgba(255,252,255,200);\n"
"}")

        self.horizontalLayout_8.addWidget(self.refresh_sever)

        self.widget_9 = QWidget(self.Server_top_bar)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMaximumSize(QSize(150, 16777215))
        self.widget_9.setFont(font7)
        self.horizontalLayout_9 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_2 = QPushButton(self.widget_9)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(50, 50))
        self.pushButton_2.setMaximumSize(QSize(50, 50))
        font9 = QFont()
        font9.setFamily(u"Comic Sans MS")
        font9.setPointSize(35)
        font9.setBold(False)
        font9.setItalic(False)
        font9.setWeight(50)
        self.pushButton_2.setFont(font9)
        self.pushButton_2.setCursor(QCursor(Qt.BusyCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton:hover {\n"
"color: rgba(255,252,255,200);\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget_9)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(50, 50))
        self.pushButton_3.setMaximumSize(QSize(50, 50))
        self.pushButton_3.setFont(font9)
        self.pushButton_3.setCursor(QCursor(Qt.BusyCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton:hover {\n"
"color: rgba(255,252,255,200);\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_3)


        self.horizontalLayout_8.addWidget(self.widget_9)


        self.verticalLayout_5.addWidget(self.Server_top_bar)

        self.widget_11 = QWidget(self.Server_Widget)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMaximumSize(QSize(16777215, 600))
        self.widget_11.setFont(font1)
        self.widget_11.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.widget_11)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 30, 100)
        self.server_list = QListWidget(self.widget_11)
        QListWidgetItem(self.server_list)
        QListWidgetItem(self.server_list)
        QListWidgetItem(self.server_list)
        QListWidgetItem(self.server_list)
        QListWidgetItem(self.server_list)
        QListWidgetItem(self.server_list)
        QListWidgetItem(self.server_list)
        self.server_list.setObjectName(u"server_list")
        self.server_list.setMaximumSize(QSize(700, 500))
        self.server_list.setFont(font4)
        self.server_list.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.server_list.setFocusPolicy(Qt.StrongFocus)
        self.server_list.setContextMenuPolicy(Qt.NoContextMenu)
#if QT_CONFIG(whatsthis)
        self.server_list.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.server_list.setStyleSheet(u"QListWidget {\n"
"background-color: rgba(0,0,0,0);\n"
"\n"
"color: rgb(255,255,255);\n"
" border: none;\n"
"border-radius: 20px;\n"
"	outline: none;\n"
"\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background-color: rgba(0,0,0,0);\n"
"	border-radius: 7px;\n"
"    border: 3px solid white;\n"
"    padding: 30px;\n"
"    font-size: 16px;\n"
"    outline: none;\n"
"	margin-bottom: 25px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #c5e1a5;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"QListWidget {\n"
"    scrollbar-width: 10px;\n"
"    scrollbar-height: 10px;\n"
"}\n"
"\n"
"QListWidget:::vertical {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QListWidget:::vertical::handle {\n"
"    background: #c0c0c0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QListWidget:::vertical::handle:hover {\n"
"    background: #a0a0a0;\n"
"}\n"
"\n"
"QListWidget:::vertical::add-line:hover,\n"
"QListWidget:::vertical::sub-line:hover {\n"
"    background: #f0f0f0;\n"
"}\n"
""
                        "\n"
"QListWidget:::vertical::add-page:hover,\n"
"QListWidget:::vertical::sub-page:hover {\n"
"    background: #e0e0e0;\n"
"}\n"
"\n"
"QListWidget:::vertical {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"")
        self.server_list.setFrameShape(QFrame.NoFrame)
        self.server_list.setLineWidth(0)
        self.server_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.server_list.setLayoutMode(QListView.SinglePass)
        self.server_list.setViewMode(QListView.ListMode)

        self.verticalLayout_7.addWidget(self.server_list)


        self.verticalLayout_5.addWidget(self.widget_11)


        self.horizontalLayout_10.addWidget(self.Server_Widget)


        self.horizontalLayout_35.addWidget(self.ServerContainer)

        self.PlayPageStackedWidget.addWidget(self.ServerListPage)
        self.ServerCreatePage = QWidget()
        self.ServerCreatePage.setObjectName(u"ServerCreatePage")
        self.horizontalLayout_6 = QHBoxLayout(self.ServerCreatePage)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_7 = QWidget(self.ServerCreatePage)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setFont(font1)

        self.horizontalLayout_6.addWidget(self.widget_7)

        self.ServerCreateFrame = QWidget(self.ServerCreatePage)
        self.ServerCreateFrame.setObjectName(u"ServerCreateFrame")
        self.ServerCreateFrame.setMinimumSize(QSize(300, 100))
        self.ServerCreateFrame.setMaximumSize(QSize(600, 500))
        self.ServerCreateFrame.setFont(font1)
        self.ServerCreateFrame.setStyleSheet(u"QWidget#ServerCreateFrame {\n"
"border: 10px solid white;\n"
"border-radius: 10px;\n"
"background-color: rgba(0,0,0,200);\n"
"}")
        self.verticalLayout_17 = QVBoxLayout(self.ServerCreateFrame)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(50, 50, 50, 50)
        self.widget_46 = QWidget(self.ServerCreateFrame)
        self.widget_46.setObjectName(u"widget_46")
        self.widget_46.setMaximumSize(QSize(16777215, 50))
        self.widget_46.setFont(font1)
        self.horizontalLayout_30 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(25, 0, 0, 0)
        self.hostgame_backbutton = QPushButton(self.widget_46)
        self.hostgame_backbutton.setObjectName(u"hostgame_backbutton")
        self.hostgame_backbutton.setMinimumSize(QSize(50, 50))
        self.hostgame_backbutton.setMaximumSize(QSize(50, 16777215))
        self.hostgame_backbutton.setFont(font7)
        self.hostgame_backbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.hostgame_backbutton.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,200); /* Normal text color */\n"
"	background-colour: 0;\n"
"	border:0;\n"
"	\n"
"\n"
"}\n"
"\n"
"QPushButton::indicator {\n"
"    background-color: #ffffff;\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgba(255,255,255,255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   color: rgba(255,255,255,225);\n"
"}\n"
"")

        self.horizontalLayout_30.addWidget(self.hostgame_backbutton)

        self.widget_47 = QWidget(self.widget_46)
        self.widget_47.setObjectName(u"widget_47")
        self.widget_47.setFont(font1)

        self.horizontalLayout_30.addWidget(self.widget_47)


        self.verticalLayout_17.addWidget(self.widget_46)

        self.label_13 = QLabel(self.ServerCreateFrame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 100))
        self.label_13.setFont(font7)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_13)

        self.widget_35 = QWidget(self.ServerCreateFrame)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setMaximumSize(QSize(600, 300))
        self.widget_35.setFont(font1)
        self.verticalLayout_18 = QVBoxLayout(self.widget_35)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_36 = QWidget(self.widget_35)
        self.widget_36.setObjectName(u"widget_36")
        self.widget_36.setFont(font1)
        self.horizontalLayout_7 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_14 = QLabel(self.widget_36)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font7)

        self.horizontalLayout_7.addWidget(self.label_14)

        self.host_server_name = QLineEdit(self.widget_36)
        self.host_server_name.setObjectName(u"host_server_name")
        self.host_server_name.setMaximumSize(QSize(16777215, 40))
        font10 = QFont()
        font10.setFamily(u"SAO UI")
        font10.setPointSize(15)
        font10.setBold(False)
        font10.setItalic(False)
        font10.setWeight(50)
        self.host_server_name.setFont(font10)
        self.host_server_name.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 5px;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-color: #999;\n"
"}\n"
"QLineEdit:focus {\n"
"    border-color: white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.host_server_name.setMaxLength(50)

        self.horizontalLayout_7.addWidget(self.host_server_name)


        self.verticalLayout_18.addWidget(self.widget_36)

        self.widget_37 = QWidget(self.widget_35)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setFont(font1)
        self.horizontalLayout_24 = QHBoxLayout(self.widget_37)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_15 = QLabel(self.widget_37)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font7)

        self.horizontalLayout_24.addWidget(self.label_15)

        self.host_player_count = QSpinBox(self.widget_37)
        self.host_player_count.setObjectName(u"host_player_count")
        self.host_player_count.setFont(font7)
        self.host_player_count.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.host_player_count.setMinimum(2)
        self.host_player_count.setMaximum(4)

        self.horizontalLayout_24.addWidget(self.host_player_count)


        self.verticalLayout_18.addWidget(self.widget_37)

        self.widget_38 = QWidget(self.widget_35)
        self.widget_38.setObjectName(u"widget_38")
        self.widget_38.setFont(font1)
        self.horizontalLayout_25 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_16 = QLabel(self.widget_38)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font7)

        self.horizontalLayout_25.addWidget(self.label_16)

        self.host_mode = QComboBox(self.widget_38)
        self.host_mode.addItem("")
        self.host_mode.addItem("")
        self.host_mode.addItem("")
        self.host_mode.addItem("")
        self.host_mode.setObjectName(u"host_mode")
        self.host_mode.setFont(font7)
        self.host_mode.setEditable(False)
        self.host_mode.setMaxVisibleItems(5)

        self.horizontalLayout_25.addWidget(self.host_mode)


        self.verticalLayout_18.addWidget(self.widget_38)


        self.verticalLayout_17.addWidget(self.widget_35)

        self.create_game_button = QWidget(self.ServerCreateFrame)
        self.create_game_button.setObjectName(u"create_game_button")
        self.create_game_button.setMaximumSize(QSize(16777215, 150))
        self.create_game_button.setFont(font1)
        self.horizontalLayout_26 = QHBoxLayout(self.create_game_button)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.widget_41 = QWidget(self.create_game_button)
        self.widget_41.setObjectName(u"widget_41")
        self.widget_41.setFont(font1)

        self.horizontalLayout_26.addWidget(self.widget_41)

        self.host_creategame = QPushButton(self.create_game_button)
        self.host_creategame.setObjectName(u"host_creategame")
        self.host_creategame.setMaximumSize(QSize(140, 16777215))
        self.host_creategame.setFont(font7)
        self.host_creategame.setCursor(QCursor(Qt.PointingHandCursor))
        self.host_creategame.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,200);\n"
"	background-colour: 0;\n"
"	border:0;\n"
"	\n"
"\n"
"}\n"
"\n"
"QPushButton::indicator {\n"
"    background-color: #ffffff; /* Color of the bullet point */\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgba(255,255,255,255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   color: rgba(255,255,255,225);\n"
"}\n"
"")

        self.horizontalLayout_26.addWidget(self.host_creategame)

        self.widget_42 = QWidget(self.create_game_button)
        self.widget_42.setObjectName(u"widget_42")
        self.widget_42.setFont(font1)

        self.horizontalLayout_26.addWidget(self.widget_42)


        self.verticalLayout_17.addWidget(self.create_game_button)

        self.server_warning = QLabel(self.ServerCreateFrame)
        self.server_warning.setObjectName(u"server_warning")
        font11 = QFont()
        font11.setFamily(u"OCR-A")
        font11.setPointSize(12)
        font11.setBold(False)
        font11.setItalic(False)
        font11.setWeight(50)
        self.server_warning.setFont(font11)
        self.server_warning.setStyleSheet(u"color: rgb(255, 85, 0);")
        self.server_warning.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.server_warning)


        self.horizontalLayout_6.addWidget(self.ServerCreateFrame)

        self.widget_8 = QWidget(self.ServerCreatePage)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setFont(font1)

        self.horizontalLayout_6.addWidget(self.widget_8)

        self.PlayPageStackedWidget.addWidget(self.ServerCreatePage)
        self.LocalModePage = QWidget()
        self.LocalModePage.setObjectName(u"LocalModePage")
        self.LocalModePage.setStyleSheet(u"")
        self.horizontalLayout_31 = QHBoxLayout(self.LocalModePage)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.widget_48 = QWidget(self.LocalModePage)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setFont(font1)

        self.horizontalLayout_31.addWidget(self.widget_48)

        self.LocalPlayerPage = QWidget(self.LocalModePage)
        self.LocalPlayerPage.setObjectName(u"LocalPlayerPage")
        self.LocalPlayerPage.setMinimumSize(QSize(600, 300))
        self.LocalPlayerPage.setMaximumSize(QSize(700, 450))
        self.LocalPlayerPage.setFont(font1)
        self.LocalPlayerPage.setStyleSheet(u"QWidget#LocalPlayerPage {\n"
"border: 10px solid white;\n"
"border-radius: 15px;\n"
"background-color: rgba(0,0,0,150);\n"
"\n"
"}")
        self.verticalLayout_30 = QVBoxLayout(self.LocalPlayerPage)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.widget_58 = QWidget(self.LocalPlayerPage)
        self.widget_58.setObjectName(u"widget_58")
        self.widget_58.setMaximumSize(QSize(16777215, 123))
        self.verticalLayout_40 = QVBoxLayout(self.widget_58)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 6, 0, 0)
        self.label_21 = QLabel(self.widget_58)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 100))
        font12 = QFont()
        font12.setFamily(u"SAO UI")
        font12.setPointSize(45)
        font12.setBold(False)
        font12.setItalic(False)
        font12.setWeight(50)
        self.label_21.setFont(font12)
        self.label_21.setStyleSheet(u"\n"
"padding: 10px;\n"
"padding-top: 0px;")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.label_21)

        self.label_20 = QLabel(self.widget_58)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font10)
        self.label_20.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_40.addWidget(self.label_20)


        self.verticalLayout_30.addWidget(self.widget_58)

        self.widget_57 = QWidget(self.LocalPlayerPage)
        self.widget_57.setObjectName(u"widget_57")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_57)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.LocalLeft = QWidget(self.widget_57)
        self.LocalLeft.setObjectName(u"LocalLeft")
        self.LocalLeft.setMinimumSize(QSize(300, 300))
        self.LocalLeft.setFont(font1)
        self.verticalLayout_19 = QVBoxLayout(self.LocalLeft)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_43 = QWidget(self.LocalLeft)
        self.widget_43.setObjectName(u"widget_43")
        self.widget_43.setMaximumSize(QSize(23232, 16777215))
        self.widget_43.setFont(font1)
        self.widget_43.setStyleSheet(u"padding-left: 50px;")
        self.verticalLayout_22 = QVBoxLayout(self.widget_43)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 40, 0, 0)
        self.widget_34 = QWidget(self.widget_43)
        self.widget_34.setObjectName(u"widget_34")
        self.widget_34.setFont(font1)
        self.verticalLayout_21 = QVBoxLayout(self.widget_34)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget_45 = QWidget(self.widget_34)
        self.widget_45.setObjectName(u"widget_45")
        self.widget_45.setMinimumSize(QSize(150, 50))
        self.widget_45.setMaximumSize(QSize(250, 50))
        self.widget_45.setFont(font1)
        self.horizontalLayout_28 = QHBoxLayout(self.widget_45)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.widget_45)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font7)
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_17.setMargin(10)

        self.horizontalLayout_28.addWidget(self.label_17)

        self.local_playercount = QSpinBox(self.widget_45)
        self.local_playercount.setObjectName(u"local_playercount")
        self.local_playercount.setMinimumSize(QSize(39, 40))
        self.local_playercount.setMaximumSize(QSize(45, 40))
        self.local_playercount.setFont(font10)
        self.local_playercount.setCursor(QCursor(Qt.PointingHandCursor))
        self.local_playercount.setStyleSheet(u"QSpinBox {\n"
"    border: 2px solid white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    min-width: 25px; \n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #d3d3d3;\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpinBox::down-arrow {\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QSpinBox::up-a\n"
"")
        self.local_playercount.setMinimum(1)
        self.local_playercount.setMaximum(3)

        self.horizontalLayout_28.addWidget(self.local_playercount)


        self.verticalLayout_21.addWidget(self.widget_45)

        self.local_howto_play = QPushButton(self.widget_34)
        self.local_howto_play.setObjectName(u"local_howto_play")
        self.local_howto_play.setMinimumSize(QSize(50, 50))
        self.local_howto_play.setMaximumSize(QSize(213131, 16777215))
        self.local_howto_play.setFont(font)
        self.local_howto_play.setCursor(QCursor(Qt.PointingHandCursor))
        self.local_howto_play.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,150);\n"
"	background-colour: 0;\n"
"	border:0;\n"
"\n"
"}\n"
"\n"
"QPushButton::indicator {\n"
"    background-color: #ffffff;\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgba(255,255,255,200);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   color: rgba(255,255,255,255);\n"
"}\n"
"")

        self.verticalLayout_21.addWidget(self.local_howto_play)

        self.local_create_game = QPushButton(self.widget_34)
        self.local_create_game.setObjectName(u"local_create_game")
        self.local_create_game.setMinimumSize(QSize(0, 50))
        self.local_create_game.setMaximumSize(QSize(123131, 16777215))
        font13 = QFont()
        font13.setFamily(u"SAO UI")
        font13.setPointSize(25)
        font13.setBold(False)
        font13.setItalic(False)
        font13.setUnderline(True)
        font13.setWeight(50)
        self.local_create_game.setFont(font13)
        self.local_create_game.setCursor(QCursor(Qt.PointingHandCursor))
        self.local_create_game.setStyleSheet(u"QPushButton {\n"
"    color: rgba(255,255,255,150);\n"
"	background-colour: 0;\n"
"	border:0;\n"
"\n"
"}\n"
"\n"
"QPushButton::indicator {\n"
"    background-color: #ffffff;\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgba(255,255,255,200);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   color: rgba(255,255,255,255);\n"
"}\n"
"")
        self.local_create_game.setInputMethodHints(Qt.ImhNone)
        self.local_create_game.setCheckable(False)
        self.local_create_game.setAutoExclusive(False)
        self.local_create_game.setAutoDefault(False)
        self.local_create_game.setFlat(False)

        self.verticalLayout_21.addWidget(self.local_create_game)


        self.verticalLayout_22.addWidget(self.widget_34)

        self.widget_44 = QWidget(self.widget_43)
        self.widget_44.setObjectName(u"widget_44")
        self.widget_44.setFont(font1)
        self.verticalLayout_29 = QVBoxLayout(self.widget_44)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_22.addWidget(self.widget_44)


        self.verticalLayout_19.addWidget(self.widget_43)


        self.horizontalLayout_27.addWidget(self.LocalLeft)

        self.LocalRight = QWidget(self.widget_57)
        self.LocalRight.setObjectName(u"LocalRight")
        self.LocalRight.setMinimumSize(QSize(300, 300))
        font14 = QFont()
        font14.setFamily(u"SAO UI")
        font14.setPointSize(7)
        font14.setBold(False)
        font14.setItalic(False)
        font14.setWeight(50)
        self.LocalRight.setFont(font14)
        self.verticalLayout_20 = QVBoxLayout(self.LocalRight)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.widget_50 = QWidget(self.LocalRight)
        self.widget_50.setObjectName(u"widget_50")
        self.widget_50.setFont(font1)
        self.local_player_image = QLabel(self.widget_50)
        self.local_player_image.setObjectName(u"local_player_image")
        self.local_player_image.setGeometry(QRect(4, 0, 300, 300))
        self.local_player_image.setMaximumSize(QSize(300, 300))
        self.local_player_image.setFont(font1)
        self.local_player_image.setStyleSheet(u"margin:30px;")
        self.local_player_image.setPixmap(QPixmap(u":/Local/assets/background/Local/1.png"))
        self.local_player_image.setScaledContents(True)
        self.local_player_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.widget_50)


        self.horizontalLayout_27.addWidget(self.LocalRight)


        self.verticalLayout_30.addWidget(self.widget_57)


        self.horizontalLayout_31.addWidget(self.LocalPlayerPage)

        self.widget_49 = QWidget(self.LocalModePage)
        self.widget_49.setObjectName(u"widget_49")
        self.widget_49.setFont(font1)

        self.horizontalLayout_31.addWidget(self.widget_49)

        self.PlayPageStackedWidget.addWidget(self.LocalModePage)
        self.ServerWaitPage = QWidget()
        self.ServerWaitPage.setObjectName(u"ServerWaitPage")
        self.horizontalLayout_43 = QHBoxLayout(self.ServerWaitPage)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.widget_59 = QWidget(self.ServerWaitPage)
        self.widget_59.setObjectName(u"widget_59")
        self.widget_59.setFont(font1)

        self.horizontalLayout_43.addWidget(self.widget_59)

        self.ServerWaitFrame = QWidget(self.ServerWaitPage)
        self.ServerWaitFrame.setObjectName(u"ServerWaitFrame")
        self.ServerWaitFrame.setMinimumSize(QSize(300, 100))
        self.ServerWaitFrame.setMaximumSize(QSize(600, 500))
        self.ServerWaitFrame.setFont(font1)
        self.ServerWaitFrame.setStyleSheet(u"QWidget#ServerWaitFrame {\n"
"border: 10px solid white;\n"
"border-radius: 10px;\n"
"background-color: rgba(0,0,0,200);\n"
"}")
        self.verticalLayout_31 = QVBoxLayout(self.ServerWaitFrame)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(50, 50, 50, 50)
        self.widget_60 = QWidget(self.ServerWaitFrame)
        self.widget_60.setObjectName(u"widget_60")
        self.horizontalLayout_38 = QHBoxLayout(self.widget_60)
        self.horizontalLayout_38.setSpacing(20)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.widget_61 = QWidget(self.widget_60)
        self.widget_61.setObjectName(u"widget_61")
        self.verticalLayout_32 = QVBoxLayout(self.widget_61)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.widget_22 = QWidget(self.widget_61)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.widget_22)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(50, 16777215))
        font15 = QFont()
        font15.setFamily(u"SAO UI")
        font15.setPointSize(14)
        font15.setBold(False)
        font15.setItalic(False)
        font15.setWeight(50)
        self.label_32.setFont(font15)
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_32)

        self.LobbyHostName = QLabel(self.widget_22)
        self.LobbyHostName.setObjectName(u"LobbyHostName")
        self.LobbyHostName.setFont(font4)

        self.horizontalLayout_13.addWidget(self.LobbyHostName)


        self.verticalLayout_32.addWidget(self.widget_22)

        self.ServerWaittext_3 = QFrame(self.widget_61)
        self.ServerWaittext_3.setObjectName(u"ServerWaittext_3")
        self.ServerWaittext_3.setMinimumSize(QSize(0, 150))
        self.ServerWaittext_3.setMaximumSize(QSize(16777215, 100))
        font16 = QFont()
        font16.setPointSize(17)
        font16.setBold(False)
        font16.setItalic(False)
        font16.setWeight(50)
        self.ServerWaittext_3.setFont(font16)
        self.ServerWaittext_3.setFrameShape(QFrame.StyledPanel)
        self.ServerWaittext_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.ServerWaittext_3)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.ServerWaittext_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 0))
        self.label_26.setMaximumSize(QSize(16777215, 32131))
        font17 = QFont()
        font17.setFamily(u"SAO UI")
        font17.setPointSize(56)
        font17.setBold(False)
        font17.setItalic(False)
        font17.setWeight(50)
        self.label_26.setFont(font17)
        self.label_26.setStyleSheet(u"")
        self.label_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_41.addWidget(self.label_26)


        self.verticalLayout_32.addWidget(self.ServerWaittext_3)

        self.ServerWaittext_2 = QFrame(self.widget_61)
        self.ServerWaittext_2.setObjectName(u"ServerWaittext_2")
        self.ServerWaittext_2.setMaximumSize(QSize(16777215, 50))
        self.ServerWaittext_2.setFrameShape(QFrame.StyledPanel)
        self.ServerWaittext_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.ServerWaittext_2)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.ServerWaittext_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font10)

        self.horizontalLayout_40.addWidget(self.label_23)

        self.LobbyServerName = QLabel(self.ServerWaittext_2)
        self.LobbyServerName.setObjectName(u"LobbyServerName")
        self.LobbyServerName.setFont(font10)
        self.LobbyServerName.setStyleSheet(u"padding-left: 5px;")

        self.horizontalLayout_40.addWidget(self.LobbyServerName)


        self.verticalLayout_32.addWidget(self.ServerWaittext_2)

        self.ServerWaittext = QFrame(self.widget_61)
        self.ServerWaittext.setObjectName(u"ServerWaittext")
        self.ServerWaittext.setMaximumSize(QSize(16777215, 50))
        self.ServerWaittext.setFrameShape(QFrame.StyledPanel)
        self.ServerWaittext.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.ServerWaittext)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.ServerWaittext)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font7)

        self.horizontalLayout_39.addWidget(self.label_22)

        self.LobbyMaxPlayer = QLabel(self.ServerWaittext)
        self.LobbyMaxPlayer.setObjectName(u"LobbyMaxPlayer")
        self.LobbyMaxPlayer.setFont(font7)
        self.LobbyMaxPlayer.setStyleSheet(u"padding-left: 5px;")

        self.horizontalLayout_39.addWidget(self.LobbyMaxPlayer)


        self.verticalLayout_32.addWidget(self.ServerWaittext)

        self.frame_3 = QFrame(self.widget_61)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 39, 0, 13)
        self.LobbyLeaveGame = QPushButton(self.frame_3)
        self.LobbyLeaveGame.setObjectName(u"LobbyLeaveGame")
        font18 = QFont()
        font18.setFamily(u"SAO UI")
        font18.setPointSize(30)
        font18.setBold(False)
        font18.setItalic(False)
        font18.setWeight(50)
        self.LobbyLeaveGame.setFont(font18)
        self.LobbyLeaveGame.setCursor(QCursor(Qt.PointingHandCursor))
        self.LobbyLeaveGame.setStyleSheet(u"QPushButton {\n"
"color: rgba(255,255,255,225);\n"
"border: 0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgba(255,255,255,200);\n"
"\n"
"\n"
"}")

        self.horizontalLayout_44.addWidget(self.LobbyLeaveGame)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_44.addWidget(self.frame_4)


        self.verticalLayout_32.addWidget(self.frame_3)


        self.horizontalLayout_38.addWidget(self.widget_61)

        self.widget_62 = QWidget(self.widget_60)
        self.widget_62.setObjectName(u"widget_62")
        self.verticalLayout_33 = QVBoxLayout(self.widget_62)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.LobbySlots = QWidget(self.widget_62)
        self.LobbySlots.setObjectName(u"LobbySlots")
        self.verticalLayout_35 = QVBoxLayout(self.LobbySlots)
        self.verticalLayout_35.setSpacing(15)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.LobbyPlayersTab = QListWidget(self.LobbySlots)
        QListWidgetItem(self.LobbyPlayersTab)
        QListWidgetItem(self.LobbyPlayersTab)
        QListWidgetItem(self.LobbyPlayersTab)
        QListWidgetItem(self.LobbyPlayersTab)
        self.LobbyPlayersTab.setObjectName(u"LobbyPlayersTab")
        font19 = QFont()
        font19.setFamily(u"SAO UI")
        font19.setPointSize(17)
        font19.setBold(False)
        font19.setItalic(False)
        font19.setWeight(50)
        self.LobbyPlayersTab.setFont(font19)
        self.LobbyPlayersTab.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.LobbyPlayersTab.setStyleSheet(u"QListWidget {\n"
"background-color: rgba(0,0,0,0);\n"
"\n"
"color: rgb(255,255,255);\n"
" border: none;\n"
"border-radius: 20px;\n"
"	outline: none;\n"
"\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background-color: rgba(0,0,0,0);\n"
"	border-radius: 7px;\n"
"    border: 3px solid white;\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    outline: none;\n"
"	margin-bottom:10px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #c5e1a5;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"QListWidget {\n"
"    scrollbar-width: 10px;\n"
"    scrollbar-height: 10px;\n"
"}\n"
"\n"
"QListWidget:::vertical {\n"
"    background: transparent;\n"
"}\n"
"\n"
"")
        self.LobbyPlayersTab.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.LobbyPlayersTab.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.LobbyPlayersTab.setAutoScroll(False)
        self.LobbyPlayersTab.setAutoScrollMargin(16)
        self.LobbyPlayersTab.setProperty("showDropIndicator", True)

        self.verticalLayout_35.addWidget(self.LobbyPlayersTab)


        self.verticalLayout_33.addWidget(self.LobbySlots)

        self.widget_64 = QWidget(self.widget_62)
        self.widget_64.setObjectName(u"widget_64")
        self.widget_64.setMaximumSize(QSize(16777215, 80))
        self.verticalLayout_34 = QVBoxLayout(self.widget_64)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.LobbyStartGameButton = QPushButton(self.widget_64)
        self.LobbyStartGameButton.setObjectName(u"LobbyStartGameButton")
        self.LobbyStartGameButton.setFont(font18)
        self.LobbyStartGameButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.LobbyStartGameButton.setStyleSheet(u"QPushButton {\n"
"color: rgba(255,255,255,225);\n"
"border: 0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgba(255,255,255,200);\n"
"\n"
"\n"
"}")

        self.verticalLayout_34.addWidget(self.LobbyStartGameButton)


        self.verticalLayout_33.addWidget(self.widget_64)


        self.horizontalLayout_38.addWidget(self.widget_62)


        self.verticalLayout_31.addWidget(self.widget_60)

        self.label_30 = QLabel(self.ServerWaitFrame)
        self.label_30.setObjectName(u"label_30")
        font20 = QFont()
        font20.setFamily(u"SAO UI")
        font20.setPointSize(12)
        font20.setBold(False)
        font20.setItalic(False)
        font20.setWeight(50)
        self.label_30.setFont(font20)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_30)


        self.horizontalLayout_43.addWidget(self.ServerWaitFrame)

        self.widget_33 = QWidget(self.ServerWaitPage)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setFont(font1)

        self.horizontalLayout_43.addWidget(self.widget_33)

        self.PlayPageStackedWidget.addWidget(self.ServerWaitPage)

        self.verticalLayout_9.addWidget(self.PlayPageStackedWidget)

        self.Content.addWidget(self.PlayPage)
        self.SettingPage = QWidget()
        self.SettingPage.setObjectName(u"SettingPage")
        self.SettingPage.setStyleSheet(u"QWidget#SettingPage {\n"
"	background-image: url(:/background/assets/background/background1.png);\n"
"}\n"
"\n"
"QWidget {\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.SettingPage)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.TopWidget_5 = QWidget(self.SettingPage)
        self.TopWidget_5.setObjectName(u"TopWidget_5")
        self.TopWidget_5.setMaximumSize(QSize(16777215, 100))
        self.TopWidget_5.setFont(font1)
        self.TopWidget_5.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.horizontalLayout_18 = QHBoxLayout(self.TopWidget_5)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(30, 10, 0, 0)
        self.setting_back_button = QPushButton(self.TopWidget_5)
        self.setting_back_button.setObjectName(u"setting_back_button")
        self.setting_back_button.setMinimumSize(QSize(150, 70))
        self.setting_back_button.setMaximumSize(QSize(150, 70))
        self.setting_back_button.setFont(font5)
        self.setting_back_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.setting_back_button.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(0,0,0,150);\n"
"border: 3px solid white;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgba(255,255,255,200);\n"
"border: 3px solid rgba(255,255,255,200);;\n"
"background-color: rgba(0,0,0,200);\n"
"\n"
"}")

        self.horizontalLayout_18.addWidget(self.setting_back_button)

        self.widget_20 = QWidget(self.TopWidget_5)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setFont(font1)

        self.horizontalLayout_18.addWidget(self.widget_20)


        self.verticalLayout_11.addWidget(self.TopWidget_5)

        self.widget_12 = QWidget(self.SettingPage)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setFont(font1)
        self.horizontalLayout_11 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setFont(font1)

        self.horizontalLayout_11.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setFont(font1)
        self.horizontalLayout_20 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.widget_19 = QWidget(self.widget_14)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setFont(font1)

        self.horizontalLayout_20.addWidget(self.widget_19)

        self.SettingFrame = QWidget(self.widget_14)
        self.SettingFrame.setObjectName(u"SettingFrame")
        self.SettingFrame.setMinimumSize(QSize(1000, 400))
        self.SettingFrame.setMaximumSize(QSize(1000, 400))
        self.SettingFrame.setFont(font1)
        self.SettingFrame.setStyleSheet(u"\n"
"QWidget#SettingFrame {\n"
"background-color: rgba(0,0,0,150);\n"
"color: white;\n"
"border: 5px solid white;\n"
"border-radius: 10px;\n"
"}\n"
"QWidget {\n"
"color: white;\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.SettingFrame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_4 = QLabel(self.SettingFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 100))
        font21 = QFont()
        font21.setFamily(u"SAO UI")
        font21.setPointSize(35)
        font21.setBold(False)
        font21.setItalic(False)
        font21.setWeight(50)
        self.label_4.setFont(font21)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_4)

        self.widget_17 = QWidget(self.SettingFrame)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMaximumSize(QSize(16777215, 300))
        self.widget_17.setFont(font1)
        self.widget_17.setStyleSheet(u"color: white;")
        self.verticalLayout_14 = QVBoxLayout(self.widget_17)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_21 = QWidget(self.widget_17)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMaximumSize(QSize(16777215, 117))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(150, 0, 150, 0)
        self.label_5 = QLabel(self.widget_21)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)

        self.horizontalLayout_12.addWidget(self.label_5)

        self.logged_in_name = QLabel(self.widget_21)
        self.logged_in_name.setObjectName(u"logged_in_name")
        self.logged_in_name.setFont(font)

        self.horizontalLayout_12.addWidget(self.logged_in_name)

        self.label_8 = QLabel(self.widget_21)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)

        self.horizontalLayout_12.addWidget(self.label_8)

        self.logged_in_ip = QLabel(self.widget_21)
        self.logged_in_ip.setObjectName(u"logged_in_ip")
        self.logged_in_ip.setFont(font)

        self.horizontalLayout_12.addWidget(self.logged_in_ip)


        self.verticalLayout_14.addWidget(self.widget_21)

        self.widget_26 = QWidget(self.widget_17)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setMinimumSize(QSize(500, 100))
        self.widget_26.setMaximumSize(QSize(16777215, 70))
        self.widget_26.setFont(font1)
        self.horizontalLayout_19 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_19.setSpacing(30)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(20, 20, 20, 20)
        self.label_10 = QLabel(self.widget_26)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font18)

        self.horizontalLayout_19.addWidget(self.label_10)

        self.volume_slider_general = QSlider(self.widget_26)
        self.volume_slider_general.setObjectName(u"volume_slider_general")
        self.volume_slider_general.setMinimumSize(QSize(200, 50))
        self.volume_slider_general.setFont(font1)
        self.volume_slider_general.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999; /* Border color of the groove */\n"
"    height: 20px; /* Height of the groove */\n"
"     /* Background color of the groove */\n"
"    margin: 2px 0; /* Margin */\n"
"	\n"
"	background-color: rgba(0, 123, 255, 100);\n"
"    border-radius: 4px; /* Border radius */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #007bff; /* Handle color */\n"
"    border: 1px solid #007bff; /* Border color of the handle */\n"
"    width: 30px; /* Width of the handle */\n"
"    margin: -6px  -1px; /* Margin */\n"
"    border-radius: 7px; /* Border radius */\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"	border-radius: 5px;\n"
"    background: rgb(255,255,255,255); /* Backgroun\n"
"}")
        self.volume_slider_general.setMaximum(100)
        self.volume_slider_general.setValue(100)
        self.volume_slider_general.setOrientation(Qt.Horizontal)

        self.horizontalLayout_19.addWidget(self.volume_slider_general)


        self.verticalLayout_14.addWidget(self.widget_26)


        self.verticalLayout_13.addWidget(self.widget_17)


        self.horizontalLayout_20.addWidget(self.SettingFrame)

        self.widget_16 = QWidget(self.widget_14)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setFont(font1)

        self.horizontalLayout_20.addWidget(self.widget_16)


        self.horizontalLayout_11.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.widget_12)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setFont(font1)

        self.horizontalLayout_11.addWidget(self.widget_15)


        self.verticalLayout_11.addWidget(self.widget_12)

        self.Content.addWidget(self.SettingPage)
        self.AboutPage = QWidget()
        self.AboutPage.setObjectName(u"AboutPage")
        self.AboutPage.setStyleSheet(u"QWidget#AboutPage {\n"
"background-image: url(:/background/assets/background/background.png);\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.AboutPage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.TopWidget_6 = QWidget(self.AboutPage)
        self.TopWidget_6.setObjectName(u"TopWidget_6")
        self.TopWidget_6.setMaximumSize(QSize(16777215, 100))
        self.TopWidget_6.setFont(font1)
        self.TopWidget_6.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.horizontalLayout_21 = QHBoxLayout(self.TopWidget_6)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(30, 10, 0, 0)
        self.about_back_button = QPushButton(self.TopWidget_6)
        self.about_back_button.setObjectName(u"about_back_button")
        self.about_back_button.setMinimumSize(QSize(150, 70))
        self.about_back_button.setMaximumSize(QSize(150, 70))
        self.about_back_button.setFont(font5)
        self.about_back_button.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(0,0,0,150);\n"
"border: 3px solid white;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgba(255,255,255,200);\n"
"border: 3px solid rgba(255,255,255,200);;\n"
"background-color: rgba(0,0,0,200);\n"
"\n"
"}")

        self.horizontalLayout_21.addWidget(self.about_back_button)

        self.widget_27 = QWidget(self.TopWidget_6)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setFont(font1)

        self.horizontalLayout_21.addWidget(self.widget_27)


        self.verticalLayout_12.addWidget(self.TopWidget_6)

        self.widget_28 = QWidget(self.AboutPage)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setFont(font1)
        self.horizontalLayout_22 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.widget_29 = QWidget(self.widget_28)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setFont(font1)

        self.horizontalLayout_22.addWidget(self.widget_29)

        self.widget_30 = QWidget(self.widget_28)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setFont(font1)
        self.widget_30.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.widget_31 = QWidget(self.widget_30)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setFont(font1)

        self.horizontalLayout_23.addWidget(self.widget_31)

        self.AboutFrame = QWidget(self.widget_30)
        self.AboutFrame.setObjectName(u"AboutFrame")
        self.AboutFrame.setMinimumSize(QSize(1000, 800))
        self.AboutFrame.setMaximumSize(QSize(1000, 800))
        self.AboutFrame.setFont(font1)
        self.AboutFrame.setStyleSheet(u"\n"
"QWidget#AboutFrame {\n"
"background-color: rgba(0,0,0,150);\n"
"color:white;\n"
"border: 5px solid white;\n"
"border-radius: 10px;\n"
"}\n"
"QWidget {\n"
"color:white;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.AboutFrame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 50, 0, 0)
        self.label_11 = QLabel(self.AboutFrame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 160))
        self.label_11.setFont(font21)
        self.label_11.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_11.setMargin(0)

        self.verticalLayout_15.addWidget(self.label_11)

        self.widget_32 = QWidget(self.AboutFrame)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setFont(font1)
        self.verticalLayout_16 = QVBoxLayout(self.widget_32)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 53)
        self.label_12 = QLabel(self.widget_32)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font7)
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setMargin(50)

        self.verticalLayout_16.addWidget(self.label_12)

        self.widget_67 = QWidget(self.widget_32)
        self.widget_67.setObjectName(u"widget_67")
        self.widget_67.setMinimumSize(QSize(0, 100))
        self.verticalLayout_39 = QVBoxLayout(self.widget_67)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.widget_67)
        self.label_24.setObjectName(u"label_24")
        font22 = QFont()
        font22.setFamily(u"SAO UI")
        font22.setPointSize(33)
        font22.setBold(False)
        font22.setItalic(False)
        font22.setWeight(50)
        self.label_24.setFont(font22)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_24)

        self.widget_68 = QWidget(self.widget_67)
        self.widget_68.setObjectName(u"widget_68")
        self.horizontalLayout_42 = QHBoxLayout(self.widget_68)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_25 = QLabel(self.widget_68)
        self.label_25.setObjectName(u"label_25")
        font23 = QFont()
        font23.setFamily(u"SAO UI")
        font23.setPointSize(19)
        font23.setBold(False)
        font23.setItalic(False)
        font23.setWeight(50)
        self.label_25.setFont(font23)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.label_25)

        self.label_27 = QLabel(self.widget_68)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font23)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.label_27)


        self.verticalLayout_39.addWidget(self.widget_68)


        self.verticalLayout_16.addWidget(self.widget_67)


        self.verticalLayout_15.addWidget(self.widget_32)


        self.horizontalLayout_23.addWidget(self.AboutFrame)

        self.widget_39 = QWidget(self.widget_30)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setFont(font1)

        self.horizontalLayout_23.addWidget(self.widget_39)


        self.horizontalLayout_22.addWidget(self.widget_30)

        self.widget_40 = QWidget(self.widget_28)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setFont(font1)

        self.horizontalLayout_22.addWidget(self.widget_40)


        self.verticalLayout_12.addWidget(self.widget_28)

        self.Content.addWidget(self.AboutPage)
        self.GamePage = QWidget()
        self.GamePage.setObjectName(u"GamePage")
        self.horizontalLayout_32 = QHBoxLayout(self.GamePage)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.GamePagePanel = QStackedWidget(self.GamePage)
        self.GamePagePanel.setObjectName(u"GamePagePanel")
        self.LocalGamePage = QWidget()
        self.LocalGamePage.setObjectName(u"LocalGamePage")
        self.verticalLayout = QVBoxLayout(self.LocalGamePage)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Image_content = QWidget(self.LocalGamePage)
        self.Image_content.setObjectName(u"Image_content")
        self.Image_content.setMinimumSize(QSize(1920, 868))
        self.Image_content.setMaximumSize(QSize(1920, 1080))
        self.Image_content.setFont(font)
        self.Image_content.setStyleSheet(u"QWidget#Image_content {\n"
"	background-image: url(:/background/assets/background/player_pov_local.png);\n"
"}")
        self.setting_button = QPushButton(self.Image_content)
        self.setting_button.setObjectName(u"setting_button")
        self.setting_button.setGeometry(QRect(1820, 30, 50, 50))
        self.setting_button.setFont(font)
        self.setting_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.setting_button.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.current_player = QLabel(self.Image_content)
        self.current_player.setObjectName(u"current_player")
        self.current_player.setGeometry(QRect(680, 20, 551, 41))
        self.current_player.setFont(font)
        self.current_player.setAlignment(Qt.AlignCenter)
        self.InGameSettingWidget = QWidget(self.Image_content)
        self.InGameSettingWidget.setObjectName(u"InGameSettingWidget")
        self.InGameSettingWidget.setEnabled(True)
        self.InGameSettingWidget.setGeometry(QRect(670, 60, 581, 461))
        self.InGameSettingWidget.setFont(font1)
        self.InGameSettingWidget.setStyleSheet(u"QWidget#InGameSettingWidget {\n"
"\n"
"background-color: rgba(25,25,25,250);\n"
"border: 3px solid white;\n"
"border-radius: 30px;\n"
"}")
        self.verticalLayout_24 = QVBoxLayout(self.InGameSettingWidget)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(50, 50, 50, 50)
        self.widget_51 = QWidget(self.InGameSettingWidget)
        self.widget_51.setObjectName(u"widget_51")
        self.widget_51.setEnabled(True)
        self.widget_51.setMinimumSize(QSize(300, 100))
        self.widget_51.setMaximumSize(QSize(16777215, 300))
        self.widget_51.setFont(font1)
        self.verticalLayout_23 = QVBoxLayout(self.widget_51)
        self.verticalLayout_23.setSpacing(15)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.game_return = QPushButton(self.widget_51)
        self.game_return.setObjectName(u"game_return")
        self.game_return.setEnabled(True)
        self.game_return.setMinimumSize(QSize(0, 70))
        self.game_return.setFont(font10)
        self.game_return.setCursor(QCursor(Qt.PointingHandCursor))
        self.game_return.setStyleSheet(u"QPushButton {\n"
"border: 3px solid white;\n"
"border-radius: 10px;\n"
"color: black;\n"
"background-color: rgba(250,250,250,255);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(200,200,200);\n"
"}")

        self.verticalLayout_23.addWidget(self.game_return)

        self.game_leave = QPushButton(self.widget_51)
        self.game_leave.setObjectName(u"game_leave")
        self.game_leave.setMinimumSize(QSize(0, 70))
        self.game_leave.setFont(font10)
        self.game_leave.setCursor(QCursor(Qt.PointingHandCursor))
        self.game_leave.setStyleSheet(u"QPushButton {\n"
"border: 3px solid white;\n"
"border-radius: 10px;\n"
"color: black;\n"
"background-color: rgba(250,250,250,255);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(200,200,200);\n"
"}")

        self.verticalLayout_23.addWidget(self.game_leave)

        self.game_quit = QPushButton(self.widget_51)
        self.game_quit.setObjectName(u"game_quit")
        self.game_quit.setEnabled(True)
        self.game_quit.setMinimumSize(QSize(0, 70))
        self.game_quit.setFont(font10)
        self.game_quit.setCursor(QCursor(Qt.PointingHandCursor))
        self.game_quit.setStyleSheet(u"QPushButton {\n"
"border: 3px solid white;\n"
"border-radius: 10px;\n"
"color: black;\n"
"background-color: rgba(250,250,250,255);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(200,200,200);\n"
"}")

        self.verticalLayout_23.addWidget(self.game_quit)


        self.verticalLayout_24.addWidget(self.widget_51)

        self.LocalStackedTable = QStackedWidget(self.Image_content)
        self.LocalStackedTable.setObjectName(u"LocalStackedTable")
        self.LocalStackedTable.setGeometry(QRect(700, 0, 500, 800))
        self.LocalStackedTable.setMinimumSize(QSize(500, 800))
        font24 = QFont()
        font24.setPointSize(6)
        font24.setBold(False)
        font24.setItalic(False)
        font24.setWeight(50)
        self.LocalStackedTable.setFont(font24)
        self.LocalStackedTable.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.LocalMainTable = QWidget()
        self.LocalMainTable.setObjectName(u"LocalMainTable")
        self.LocalMainTable.setMinimumSize(QSize(500, 900))
        font25 = QFont()
        font25.setPointSize(7)
        font25.setBold(False)
        font25.setItalic(False)
        font25.setWeight(50)
        self.LocalMainTable.setFont(font25)
        self.horizontalLayout_34 = QHBoxLayout(self.LocalMainTable)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.Dice_ring = QWidget(self.LocalMainTable)
        self.Dice_ring.setObjectName(u"Dice_ring")
        self.Dice_ring.setMinimumSize(QSize(400, 800))
        self.Dice_ring.setMaximumSize(QSize(16777215, 800))
        self.Dice_ring.setFont(font1)
        self.Dice_ring.setStyleSheet(u"QWidget#Dice_ring {\n"
"\n"
"\n"
"border-radius: 175px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.Dice_ring)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_56 = QWidget(self.Dice_ring)
        self.widget_56.setObjectName(u"widget_56")
        self.widget_56.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_28 = QVBoxLayout(self.widget_56)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.ingame_timer = QLabel(self.widget_56)
        self.ingame_timer.setObjectName(u"ingame_timer")
        self.ingame_timer.setMinimumSize(QSize(0, 50))
        self.ingame_timer.setFont(font18)
        self.ingame_timer.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.ingame_timer)

        self.local_highest_roll = QLabel(self.widget_56)
        self.local_highest_roll.setObjectName(u"local_highest_roll")
        font26 = QFont()
        font26.setFamily(u"SAO UI")
        font26.setPointSize(13)
        font26.setBold(False)
        font26.setItalic(False)
        font26.setWeight(50)
        self.local_highest_roll.setFont(font26)
        self.local_highest_roll.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.local_highest_roll)

        self.dice_amount = QLabel(self.widget_56)
        self.dice_amount.setObjectName(u"dice_amount")
        self.dice_amount.setMinimumSize(QSize(0, 50))
        self.dice_amount.setFont(font18)
        self.dice_amount.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.dice_amount)

        self.dice_amount_text = QLabel(self.widget_56)
        self.dice_amount_text.setObjectName(u"dice_amount_text")
        self.dice_amount_text.setMaximumSize(QSize(16777215, 50))
        self.dice_amount_text.setFont(font7)
        self.dice_amount_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.dice_amount_text)


        self.verticalLayout_2.addWidget(self.widget_56)

        self.widget_52 = QWidget(self.Dice_ring)
        self.widget_52.setObjectName(u"widget_52")
        self.widget_52.setMinimumSize(QSize(0, 400))
        self.widget_52.setMaximumSize(QSize(16777215, 400))
        self.widget_52.setStyleSheet(u"")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_52)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 50)
        self.widget_53 = QWidget(self.widget_52)
        self.widget_53.setObjectName(u"widget_53")

        self.horizontalLayout_33.addWidget(self.widget_53)

        self.dice_animation_label = QLabel(self.widget_52)
        self.dice_animation_label.setObjectName(u"dice_animation_label")
        self.dice_animation_label.setMinimumSize(QSize(350, 350))
        self.dice_animation_label.setMaximumSize(QSize(350, 350))
        self.dice_animation_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.dice_animation_label)

        self.widget_54 = QWidget(self.widget_52)
        self.widget_54.setObjectName(u"widget_54")

        self.horizontalLayout_33.addWidget(self.widget_54)


        self.verticalLayout_2.addWidget(self.widget_52)


        self.horizontalLayout_34.addWidget(self.Dice_ring)

        self.LocalStackedTable.addWidget(self.LocalMainTable)
        self.LocalFinishTable = QWidget()
        self.LocalFinishTable.setObjectName(u"LocalFinishTable")
        self.LocalFinishTable.setMaximumSize(QSize(16777215, 500))
        self.verticalLayout_26 = QVBoxLayout(self.LocalFinishTable)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 100, 0, 0)
        self.frame = QFrame(self.LocalFinishTable)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_26.addWidget(self.frame)

        self.widget_55 = QWidget(self.LocalFinishTable)
        self.widget_55.setObjectName(u"widget_55")
        self.widget_55.setMinimumSize(QSize(200, 100))
        self.verticalLayout_25 = QVBoxLayout(self.widget_55)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.widget_55)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 50))
        self.label_18.setFont(font19)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_18)

        self.label_19 = QLabel(self.widget_55)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 50))
        self.label_19.setFont(font)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_19)


        self.verticalLayout_26.addWidget(self.widget_55)

        self.frame_2 = QFrame(self.LocalFinishTable)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_2)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.localFirstplace = QLabel(self.frame_2)
        self.localFirstplace.setObjectName(u"localFirstplace")
        self.localFirstplace.setMaximumSize(QSize(16777215, 50))
        self.localFirstplace.setFont(font)
        self.localFirstplace.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.localFirstplace)

        self.localSecondplace = QLabel(self.frame_2)
        self.localSecondplace.setObjectName(u"localSecondplace")
        self.localSecondplace.setMaximumSize(QSize(16777215, 50))
        self.localSecondplace.setFont(font)
        self.localSecondplace.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.localSecondplace)

        self.localThirdplace = QLabel(self.frame_2)
        self.localThirdplace.setObjectName(u"localThirdplace")
        self.localThirdplace.setMaximumSize(QSize(16777215, 50))
        self.localThirdplace.setFont(font)
        self.localThirdplace.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.localThirdplace)

        self.localFourthplace = QLabel(self.frame_2)
        self.localFourthplace.setObjectName(u"localFourthplace")
        self.localFourthplace.setMaximumSize(QSize(16777215, 50))
        self.localFourthplace.setFont(font)
        self.localFourthplace.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.localFourthplace)


        self.verticalLayout_26.addWidget(self.frame_2)

        self.LocalStackedTable.addWidget(self.LocalFinishTable)
        self.setting_button.raise_()
        self.current_player.raise_()
        self.LocalStackedTable.raise_()
        self.InGameSettingWidget.raise_()

        self.verticalLayout.addWidget(self.Image_content)

        self.Interative_Widget = QWidget(self.LocalGamePage)
        self.Interative_Widget.setObjectName(u"Interative_Widget")
        self.Interative_Widget.setFont(font)
        self.Interative_Widget.setStyleSheet(u"background-color: rgb(0,0,0)")
        self.horizontalLayout_2 = QHBoxLayout(self.Interative_Widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.Interative_Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setFont(font)
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.fold_button = QPushButton(self.widget)
        self.fold_button.setObjectName(u"fold_button")
        self.fold_button.setMinimumSize(QSize(0, 60))
        self.fold_button.setMaximumSize(QSize(150, 16777215))
        self.fold_button.setFont(font)
        self.fold_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.fold_button.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(50, 50, 50);\n"
"border: 0px;\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(50, 50, 50, 200);\n"
"colour: rgba(255,255,255,200)\n"
"}")

        self.horizontalLayout_5.addWidget(self.fold_button)

        self.split_bet_button = QPushButton(self.widget)
        self.split_bet_button.setObjectName(u"split_bet_button")
        self.split_bet_button.setMinimumSize(QSize(0, 60))
        self.split_bet_button.setMaximumSize(QSize(150, 16777215))
        self.split_bet_button.setFont(font)
        self.split_bet_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.split_bet_button.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.split_bet_button)

        self.double_bet_button = QPushButton(self.widget)
        self.double_bet_button.setObjectName(u"double_bet_button")
        self.double_bet_button.setMinimumSize(QSize(0, 60))
        self.double_bet_button.setMaximumSize(QSize(150, 16777215))
        self.double_bet_button.setFont(font)
        self.double_bet_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.double_bet_button.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(50, 50, 50);\n"
"border: 0px;\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(50, 50, 50, 200);\n"
"colour: rgba(255,255,255,200)\n"
"}")

        self.horizontalLayout_5.addWidget(self.double_bet_button)


        self.horizontalLayout_2.addWidget(self.widget)

        self.Bet_Widget = QWidget(self.Interative_Widget)
        self.Bet_Widget.setObjectName(u"Bet_Widget")
        self.Bet_Widget.setFont(font)
        self.horizontalLayout_3 = QHBoxLayout(self.Bet_Widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bet_amount = QLabel(self.Bet_Widget)
        self.bet_amount.setObjectName(u"bet_amount")
        self.bet_amount.setMaximumSize(QSize(300, 100))
        self.bet_amount.setFont(font)
        self.bet_amount.setStyleSheet(u"background-color: rgb(13, 13, 14);")
        self.bet_amount.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.bet_amount)


        self.horizontalLayout_2.addWidget(self.Bet_Widget)

        self.widget_6 = QWidget(self.Interative_Widget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setFont(font)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.roll_button = QPushButton(self.widget_6)
        self.roll_button.setObjectName(u"roll_button")
        self.roll_button.setMinimumSize(QSize(0, 60))
        self.roll_button.setMaximumSize(QSize(150, 16777215))
        self.roll_button.setFont(font)
        self.roll_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.roll_button.setFocusPolicy(Qt.ClickFocus)
        self.roll_button.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(50, 50, 50);\n"
"border: 0px;\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(50, 50, 50, 200);\n"
"colour: rgba(255,255,255,200)\n"
"}")

        self.horizontalLayout_4.addWidget(self.roll_button)

        self.stay_button = QPushButton(self.widget_6)
        self.stay_button.setObjectName(u"stay_button")
        self.stay_button.setMinimumSize(QSize(0, 60))
        self.stay_button.setMaximumSize(QSize(150, 16777215))
        self.stay_button.setFont(font)
        self.stay_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.stay_button.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(50, 50, 50);\n"
"border: 0px;\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(50, 50, 50, 200);\n"
"colour: rgba(255,255,255,200)\n"
"}")

        self.horizontalLayout_4.addWidget(self.stay_button)


        self.horizontalLayout_2.addWidget(self.widget_6)


        self.verticalLayout.addWidget(self.Interative_Widget)

        self.GamePagePanel.addWidget(self.LocalGamePage)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.GamePagePanel.addWidget(self.page)

        self.horizontalLayout_32.addWidget(self.GamePagePanel)

        self.Content.addWidget(self.GamePage)
        self.OnlineGamePage = QWidget()
        self.OnlineGamePage.setObjectName(u"OnlineGamePage")
        self.verticalLayout_36 = QVBoxLayout(self.OnlineGamePage)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.widget_25 = QWidget(self.OnlineGamePage)
        self.widget_25.setObjectName(u"widget_25")
        self.verticalLayout_37 = QVBoxLayout(self.widget_25)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.OnlineImageContent = QWidget(self.widget_25)
        self.OnlineImageContent.setObjectName(u"OnlineImageContent")
        self.OnlineImageContent.setMinimumSize(QSize(0, 868))
        self.OnlineImageContent.setStyleSheet(u"QWidget#OnlineImageContent {\n"
"background-image: url(:/background/assets/background/backup_background/player_pov_default back up.png);\n"
"}")
        self.TurnNavigator = QWidget(self.OnlineImageContent)
        self.TurnNavigator.setObjectName(u"TurnNavigator")
        self.TurnNavigator.setGeometry(QRect(30, 40, 354, 106))
        self.verticalLayout_38 = QVBoxLayout(self.TurnNavigator)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.widget_66 = QWidget(self.TurnNavigator)
        self.widget_66.setObjectName(u"widget_66")
        self.horizontalLayout_45 = QHBoxLayout(self.widget_66)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_66)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(165, 0))
        self.label_9.setFont(font4)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.label_9)

        self.label_28 = QLabel(self.widget_66)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(165, 0))
        self.label_28.setFont(font4)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.label_28)


        self.verticalLayout_38.addWidget(self.widget_66)

        self.TurnsIndicator = QWidget(self.TurnNavigator)
        self.TurnsIndicator.setObjectName(u"TurnsIndicator")
        self.TurnsIndicator.setMaximumSize(QSize(16777215, 3123131))
        self.horizontalLayout_17 = QHBoxLayout(self.TurnsIndicator)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, -1, 0, 0)
        self.LobbyCurrentTurn = QLabel(self.TurnsIndicator)
        self.LobbyCurrentTurn.setObjectName(u"LobbyCurrentTurn")
        self.LobbyCurrentTurn.setMinimumSize(QSize(80, 0))
        self.LobbyCurrentTurn.setMaximumSize(QSize(3131, 16777215))
        self.LobbyCurrentTurn.setFont(font23)
        self.LobbyCurrentTurn.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.LobbyCurrentTurn)

        self.label_29 = QLabel(self.TurnsIndicator)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(58, 16777215))
        font27 = QFont()
        font27.setFamily(u"Segoe UI Symbol")
        font27.setPointSize(26)
        font27.setBold(False)
        font27.setItalic(False)
        font27.setWeight(50)
        self.label_29.setFont(font27)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_29)

        self.LobbyNextTurn = QLabel(self.TurnsIndicator)
        self.LobbyNextTurn.setObjectName(u"LobbyNextTurn")
        self.LobbyNextTurn.setMinimumSize(QSize(80, 0))
        self.LobbyNextTurn.setMaximumSize(QSize(3131, 16777215))
        self.LobbyNextTurn.setFont(font23)
        self.LobbyNextTurn.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.LobbyNextTurn)


        self.verticalLayout_38.addWidget(self.TurnsIndicator)

        self.OnlinePlayerIndicator = QLabel(self.OnlineImageContent)
        self.OnlinePlayerIndicator.setObjectName(u"OnlinePlayerIndicator")
        self.OnlinePlayerIndicator.setGeometry(QRect(620, 20, 691, 47))
        self.OnlinePlayerIndicator.setMinimumSize(QSize(80, 0))
        self.OnlinePlayerIndicator.setMaximumSize(QSize(3131, 16777215))
        self.OnlinePlayerIndicator.setFont(font)
        self.OnlinePlayerIndicator.setAlignment(Qt.AlignCenter)
        self.OnlineGameTableStacked = QStackedWidget(self.OnlineImageContent)
        self.OnlineGameTableStacked.setObjectName(u"OnlineGameTableStacked")
        self.OnlineGameTableStacked.setGeometry(QRect(100, 140, 1721, 580))
        self.OnlineGameTableStacked.setMinimumSize(QSize(1700, 580))
        self.OnlineGameTableStacked.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.OnlineDiceAnimation = QLabel(self.page_2)
        self.OnlineDiceAnimation.setObjectName(u"OnlineDiceAnimation")
        self.OnlineDiceAnimation.setGeometry(QRect(560, -10, 600, 600))
        self.OnlineDiceAnimation.setMinimumSize(QSize(600, 600))
        self.OnlineDiceAnimation.setMaximumSize(QSize(600, 16777215))
        self.OnlineDiceAnimation.setCursor(QCursor(Qt.ArrowCursor))
        self.OnlineDiceAnimation.setStyleSheet(u"")
        self.OnlineDiceRollNumber = QLabel(self.page_2)
        self.OnlineDiceRollNumber.setObjectName(u"OnlineDiceRollNumber")
        self.OnlineDiceRollNumber.setGeometry(QRect(480, 0, 751, 100))
        self.OnlineDiceRollNumber.setMinimumSize(QSize(100, 100))
        font28 = QFont()
        font28.setFamily(u"SAO UI")
        font28.setPointSize(36)
        font28.setBold(False)
        font28.setItalic(False)
        font28.setWeight(50)
        self.OnlineDiceRollNumber.setFont(font28)
        self.OnlineDiceRollNumber.setStyleSheet(u"")
        self.OnlineDiceRollNumber.setAlignment(Qt.AlignCenter)
        self.OnlineStayAnimation = QLabel(self.page_2)
        self.OnlineStayAnimation.setObjectName(u"OnlineStayAnimation")
        self.OnlineStayAnimation.setGeometry(QRect(640, 80, 450, 450))
        self.OnlineStayAnimation.setMinimumSize(QSize(450, 450))
        self.OnlineStayAnimation.setMaximumSize(QSize(450, 450))
        self.OnlineGameTableStacked.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_31 = QLabel(self.page_3)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(580, 10, 551, 71))
        self.label_31.setMinimumSize(QSize(165, 0))
        font29 = QFont()
        font29.setFamily(u"SAO UI")
        font29.setPointSize(34)
        font29.setBold(False)
        font29.setItalic(False)
        font29.setWeight(50)
        self.label_31.setFont(font29)
        self.label_31.setAlignment(Qt.AlignCenter)
        self.OnlineGameScoreBoard = QListWidget(self.page_3)
        QListWidgetItem(self.OnlineGameScoreBoard)
        QListWidgetItem(self.OnlineGameScoreBoard)
        QListWidgetItem(self.OnlineGameScoreBoard)
        QListWidgetItem(self.OnlineGameScoreBoard)
        self.OnlineGameScoreBoard.setObjectName(u"OnlineGameScoreBoard")
        self.OnlineGameScoreBoard.setGeometry(QRect(710, 120, 295, 311))
        self.OnlineGameScoreBoard.setFont(font19)
        self.OnlineGameScoreBoard.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.OnlineGameScoreBoard.setStyleSheet(u"QListWidget {\n"
"background-color: rgba(0,0,0,0);\n"
"\n"
"color: rgb(255,255,255);\n"
" border: none;\n"
"border-radius: 20px;\n"
"	outline: none;\n"
"	\n"
"\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background-color: rgba(0, 0, 0, 150);\n"
"	border-radius: 7px;\n"
"    border: 3px solid white;\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    outline: none;\n"
"	\n"
"	margin-bottom:10px;\n"
"}\n"
"\n"
"QListWidget {\n"
"    scrollbar-width: 10px;\n"
"    scrollbar-height: 10px;\n"
"}\n"
"\n"
"QListWidget:::vertical {\n"
"    background: transparent;\n"
"}\n"
"\n"
"")
        self.OnlineGameScoreBoard.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.OnlineGameScoreBoard.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.OnlineGameScoreBoard.setAutoScroll(False)
        self.OnlineGameScoreBoard.setAutoScrollMargin(16)
        self.OnlineGameScoreBoard.setProperty("showDropIndicator", True)
        self.OnlineGameScoreBoard.setItemAlignment(Qt.AlignCenter)
        self.label_33 = QLabel(self.page_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(690, 80, 341, 21))
        self.label_33.setMinimumSize(QSize(165, 0))
        self.label_33.setFont(font15)
        self.label_33.setAlignment(Qt.AlignCenter)
        self.OnlineGameEndText = QLabel(self.page_3)
        self.OnlineGameEndText.setObjectName(u"OnlineGameEndText")
        self.OnlineGameEndText.setGeometry(QRect(480, 400, 751, 71))
        font30 = QFont()
        font30.setFamily(u"SAO UI")
        font30.setPointSize(24)
        font30.setBold(False)
        font30.setItalic(False)
        font30.setWeight(50)
        self.OnlineGameEndText.setFont(font30)
        self.OnlineGameEndText.setAlignment(Qt.AlignCenter)
        self.OnlineLeaveGameButton = QPushButton(self.page_3)
        self.OnlineLeaveGameButton.setObjectName(u"OnlineLeaveGameButton")
        self.OnlineLeaveGameButton.setGeometry(QRect(730, 520, 251, 51))
        self.OnlineLeaveGameButton.setFont(font19)
        self.OnlineLeaveGameButton.setFocusPolicy(Qt.ClickFocus)
        self.OnlineLeaveGameButton.setStyleSheet(u"QPushButton {\n"
"border: 3px solid white;\n"
"border-radius: 10px;\n"
"color: black;\n"
"background-color: rgba(250,250,250,255);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(200,200,200);\n"
"}")
        self.OnlineGameTableStacked.addWidget(self.page_3)

        self.verticalLayout_37.addWidget(self.OnlineImageContent)

        self.OnlineWidgetFrame = QWidget(self.widget_25)
        self.OnlineWidgetFrame.setObjectName(u"OnlineWidgetFrame")
        self.OnlineWidgetFrame.setMinimumSize(QSize(0, 212))
        self.OnlineWidgetFrame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.horizontalLayout_47 = QHBoxLayout(self.OnlineWidgetFrame)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 50, 0, 20)
        self.widget_63 = QWidget(self.OnlineWidgetFrame)
        self.widget_63.setObjectName(u"widget_63")
        self.OnlineCurrentRound = QLabel(self.widget_63)
        self.OnlineCurrentRound.setObjectName(u"OnlineCurrentRound")
        self.OnlineCurrentRound.setGeometry(QRect(30, 30, 221, 80))
        self.OnlineCurrentRound.setMaximumSize(QSize(16777215, 80))
        self.OnlineCurrentRound.setFont(font)
        self.OnlineCurrentRound.setStyleSheet(u"border: 3px solid white;\n"
"border-radius: 15px;")
        self.OnlineCurrentRound.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.widget_63)

        self.widget_23 = QWidget(self.OnlineWidgetFrame)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setMinimumSize(QSize(300, 0))
        self.widget_23.setMaximumSize(QSize(300, 16777215))
        self.widget_23.setStyleSheet(u"")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.OnlineWidget = QWidget(self.widget_23)
        self.OnlineWidget.setObjectName(u"OnlineWidget")
        self.OnlineWidget.setMinimumSize(QSize(300, 0))
        self.OnlineWidget.setMaximumSize(QSize(300, 16777215))
        self.horizontalLayout_46 = QHBoxLayout(self.OnlineWidget)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.OnlineRollButton = QPushButton(self.OnlineWidget)
        self.OnlineRollButton.setObjectName(u"OnlineRollButton")
        self.OnlineRollButton.setMinimumSize(QSize(0, 80))
        self.OnlineRollButton.setMaximumSize(QSize(100, 80))
        font31 = QFont()
        font31.setFamily(u"SAO UI")
        font31.setPointSize(23)
        font31.setBold(False)
        font31.setItalic(False)
        font31.setWeight(50)
        self.OnlineRollButton.setFont(font31)
        self.OnlineRollButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.OnlineRollButton.setFocusPolicy(Qt.ClickFocus)
        self.OnlineRollButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #388e3c; \n"
"    color: white;\n"
"    border: none;\n"
"    cursor: pointer;\n"
"	border-radius: 15px;\n"
"\n"
"	border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4CAF50; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2e7d32;  \n"
"}")

        self.horizontalLayout_46.addWidget(self.OnlineRollButton)

        self.OnlineStayButton = QPushButton(self.OnlineWidget)
        self.OnlineStayButton.setObjectName(u"OnlineStayButton")
        self.OnlineStayButton.setMinimumSize(QSize(0, 80))
        self.OnlineStayButton.setMaximumSize(QSize(100, 80))
        self.OnlineStayButton.setFont(font31)
        self.OnlineStayButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.OnlineStayButton.setFocusPolicy(Qt.ClickFocus)
        self.OnlineStayButton.setStyleSheet(u"QPushButton {\n"
"    \n"
"	background-color: rgb(255, 0, 0);\n"
"    color: white;\n"
"    border: none;\n"
"    cursor: pointer;\n"
"	border-radius: 15px;\n"
"	\n"
"	border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(200, 0, 0, 200);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(200, 0, 0, 150);\n"
"}")

        self.horizontalLayout_46.addWidget(self.OnlineStayButton)


        self.horizontalLayout_14.addWidget(self.OnlineWidget)


        self.horizontalLayout_47.addWidget(self.widget_23)

        self.widget_65 = QWidget(self.OnlineWidgetFrame)
        self.widget_65.setObjectName(u"widget_65")
        self.widget_65.setMinimumSize(QSize(800, 0))
        self.widget_65.setMaximumSize(QSize(800, 800))
        self.OnlineCurrentPlayerNameLabel = QLabel(self.widget_65)
        self.OnlineCurrentPlayerNameLabel.setObjectName(u"OnlineCurrentPlayerNameLabel")
        self.OnlineCurrentPlayerNameLabel.setGeometry(QRect(530, 30, 220, 80))
        self.OnlineCurrentPlayerNameLabel.setMaximumSize(QSize(16777215, 80))
        self.OnlineCurrentPlayerNameLabel.setFont(font)
        self.OnlineCurrentPlayerNameLabel.setStyleSheet(u"border: 3px solid white;\n"
"border-radius: 15px;")
        self.OnlineCurrentPlayerNameLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.widget_65)


        self.verticalLayout_37.addWidget(self.OnlineWidgetFrame)


        self.verticalLayout_36.addWidget(self.widget_25)

        self.Content.addWidget(self.OnlineGamePage)

        self.horizontalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.Game_Windows)

        self.retranslateUi(MainWindow)

        self.Content.setCurrentIndex(0)
        self.PlayPageStackedWidget.setCurrentIndex(2)
        self.local_create_game.setDefault(False)
        self.LocalStackedTable.setCurrentIndex(0)
        self.OnlineGameTableStacked.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.GameTitle.setText(QCoreApplication.translate("MainWindow", u"DUEL TO 26", None))
        self.online_button.setText(QCoreApplication.translate("MainWindow", u"PLAY ONLINE", None))
        self.local_button.setText(QCoreApplication.translate("MainWindow", u"TUTORIAL", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.about_button.setText(QCoreApplication.translate("MainWindow", u"ABOUT", None))
        self.quit_button.setText(QCoreApplication.translate("MainWindow", u"QUIT ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Game made by Kev", None))
        self.server_back_button.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SERVERS", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"0 Players Online", None))
        self.create_server_button.setText(QCoreApplication.translate("MainWindow", u"CREATE SERVER", None))
        self.refresh_sever.setText(QCoreApplication.translate("MainWindow", u"REFRESH", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u">", None))

        __sortingEnabled = self.server_list.isSortingEnabled()
        self.server_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.server_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem1 = self.server_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem2 = self.server_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem3 = self.server_list.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem4 = self.server_list.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem5 = self.server_list.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem6 = self.server_list.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.server_list.setSortingEnabled(__sortingEnabled)

        self.hostgame_backbutton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Host Online Game", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Server Name: ", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Player Count:", None))
        self.host_player_count.setPrefix("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Difficulty Mode", None))
        self.host_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"Poor", None))
        self.host_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"Middle Class", None))
        self.host_mode.setItemText(2, QCoreApplication.translate("MainWindow", u"Rich", None))
        self.host_mode.setItemText(3, QCoreApplication.translate("MainWindow", u"Mafia Boss", None))

        self.host_mode.setCurrentText(QCoreApplication.translate("MainWindow", u"Poor", None))
        self.host_creategame.setText(QCoreApplication.translate("MainWindow", u"Create Game", None))
        self.server_warning.setText(QCoreApplication.translate("MainWindow", u"Server Name already Exist!", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Single Player", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"(Tutorial will only last one round)", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Bot Count:", None))
        self.local_playercount.setPrefix("")
        self.local_howto_play.setText(QCoreApplication.translate("MainWindow", u"How to play?", None))
        self.local_create_game.setText(QCoreApplication.translate("MainWindow", u"Create Game", None))
        self.local_player_image.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Host:  ", None))
        self.LobbyHostName.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Lobby", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Server Name:", None))
        self.LobbyServerName.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Max Players: ", None))
        self.LobbyMaxPlayer.setText("")
        self.LobbyLeaveGame.setText(QCoreApplication.translate("MainWindow", u"Leave Game", None))

        __sortingEnabled1 = self.LobbyPlayersTab.isSortingEnabled()
        self.LobbyPlayersTab.setSortingEnabled(False)
        ___qlistwidgetitem7 = self.LobbyPlayersTab.item(0)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Player 1", None));
        ___qlistwidgetitem8 = self.LobbyPlayersTab.item(1)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Player 2", None));
        ___qlistwidgetitem9 = self.LobbyPlayersTab.item(2)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Player 3", None));
        ___qlistwidgetitem10 = self.LobbyPlayersTab.item(3)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Player 4", None));
        self.LobbyPlayersTab.setSortingEnabled(__sortingEnabled1)

        self.LobbyStartGameButton.setText(QCoreApplication.translate("MainWindow", u"Start Game", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"(Game requires a minimum of 2 players to start)", None))
        self.setting_back_button.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"SETTINGS (AUDIO)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"LOGGED IN AS: ", None))
        self.logged_in_name.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ADDRESS: ", None))
        self.logged_in_ip.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"General", None))
        self.about_back_button.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"ABOUT", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Duel to 26 is a twist on the simple concept of rolling dice; up to four players will compete in a game where the objective is to be the one closest to 26. If you go over, you're out.\n"
"\n"
"Each game consists of 5 turns, and begins with each player taking a roll. This number is their current roll, and when the next turn happens, they can choose to either play it safe and keep their current roll, or risk it to roll a different number. \n"
"\n"
"If you roll above 26, you immediately lose. This means the more you roll, the higher of a chance you have to lose. If you roll a 26, you win. Otherwise, the winner is the player with the highest number.\n"
"\n"
"Players can choose to raise the bet: if the bet is raised, every player can choose to either match the bet (put in more of their own money), or fold, losing the money they have already invested, but removing the chance to lose more.\n"
"\n"
"This is a game to test your mental abilities, risk factors and luck. Good luck.", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Credits", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Design & Support: Chonlawat Mahasuvirachai", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Programming & Implementation: Kev Le", None))
        self.setting_button.setText(QCoreApplication.translate("MainWindow", u"\u2699\ufe0f", None))
        self.current_player.setText(QCoreApplication.translate("MainWindow", u"YOU", None))
        self.game_return.setText(QCoreApplication.translate("MainWindow", u"Return to Game", None))
        self.game_leave.setText(QCoreApplication.translate("MainWindow", u"Leave Game", None))
        self.game_quit.setText(QCoreApplication.translate("MainWindow", u"Quit to Desktop", None))
        self.ingame_timer.setText(QCoreApplication.translate("MainWindow", u"60", None))
        self.local_highest_roll.setText(QCoreApplication.translate("MainWindow", u"Highest Roll: ", None))
        self.dice_amount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.dice_amount_text.setText(QCoreApplication.translate("MainWindow", u"YOU HAVE ROLLED", None))
        self.dice_animation_label.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Pratice Round Finish! Leave to play online!", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Highest Rolls:", None))
        self.localFirstplace.setText(QCoreApplication.translate("MainWindow", u"1: Aenb1 [25]", None))
        self.localSecondplace.setText(QCoreApplication.translate("MainWindow", u"2: player 5 [21]", None))
        self.localThirdplace.setText(QCoreApplication.translate("MainWindow", u"3: sunjin who [17]", None))
        self.localFourthplace.setText(QCoreApplication.translate("MainWindow", u"4: gojo [2]", None))
        self.fold_button.setText(QCoreApplication.translate("MainWindow", u"FOLD", None))
        self.split_bet_button.setText("")
        self.double_bet_button.setText(QCoreApplication.translate("MainWindow", u"DOUBLE", None))
        self.bet_amount.setText(QCoreApplication.translate("MainWindow", u"$0", None))
        self.roll_button.setText(QCoreApplication.translate("MainWindow", u"ROLL", None))
        self.stay_button.setText(QCoreApplication.translate("MainWindow", u"STAY", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Currently Playing ", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Next Turn ", None))
        self.LobbyCurrentTurn.setText(QCoreApplication.translate("MainWindow", u"player1", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u27a4", None))
        self.LobbyNextTurn.setText(QCoreApplication.translate("MainWindow", u"player2", None))
        self.OnlinePlayerIndicator.setText("")
        self.OnlineDiceAnimation.setText("")
        self.OnlineDiceRollNumber.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.OnlineStayAnimation.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"SCORE BOARD", None))

        __sortingEnabled2 = self.OnlineGameScoreBoard.isSortingEnabled()
        self.OnlineGameScoreBoard.setSortingEnabled(False)
        ___qlistwidgetitem11 = self.OnlineGameScoreBoard.item(0)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Aenb1 (You) [26]", None));
        ___qlistwidgetitem12 = self.OnlineGameScoreBoard.item(1)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Player 3 ~ 22", None));
        ___qlistwidgetitem13 = self.OnlineGameScoreBoard.item(2)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Player 2 [15]", None));
        ___qlistwidgetitem14 = self.OnlineGameScoreBoard.item(3)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Player 4 [OUT]", None));
        self.OnlineGameScoreBoard.setSortingEnabled(__sortingEnabled2)

        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Highest to Lowest", None))
        self.OnlineGameEndText.setText(QCoreApplication.translate("MainWindow", u"GG Well Play!", None))
        self.OnlineLeaveGameButton.setText(QCoreApplication.translate("MainWindow", u"Leave Game", None))
        self.OnlineCurrentRound.setText(QCoreApplication.translate("MainWindow", u"Round: 0/3", None))
        self.OnlineRollButton.setText(QCoreApplication.translate("MainWindow", u"ROLL", None))
        self.OnlineStayButton.setText(QCoreApplication.translate("MainWindow", u"STAY", None))
        self.OnlineCurrentPlayerNameLabel.setText("")
    # retranslateUi

