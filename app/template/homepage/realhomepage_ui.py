# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'realhomepage.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QListWidget, QListWidgetItem, QPlainTextEdit,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QVBoxLayout,
    QWidget)

import app.assets.realsourceimg.real

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(1280, 720)
        Main.setMinimumSize(QSize(1280, 720))
        Main.setMaximumSize(QSize(1280, 720))
        Main.setStyleSheet(u"background-color: #FAF9F6;")
        self.stackedWidget = QStackedWidget(Main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1280, 720))
        self.settings_admin = QWidget()
        self.settings_admin.setObjectName(u"settings_admin")
        self.stackedWidget_settingadmin = QStackedWidget(self.settings_admin)
        self.stackedWidget_settingadmin.setObjectName(u"stackedWidget_settingadmin")
        self.stackedWidget_settingadmin.setGeometry(QRect(0, 0, 1280, 720))
        self.settingsadminmainpage = QWidget()
        self.settingsadminmainpage.setObjectName(u"settingsadminmainpage")
        self.backbutton_settingsadmin = QPushButton(self.settingsadminmainpage)
        self.backbutton_settingsadmin.setObjectName(u"backbutton_settingsadmin")
        self.backbutton_settingsadmin.setGeometry(QRect(20, 30, 20, 31))
        self.backbutton_settingsadmin.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/backhomoe.png);")
        self.settingsadmincontainer = QWidget(self.settingsadminmainpage)
        self.settingsadmincontainer.setObjectName(u"settingsadmincontainer")
        self.settingsadmincontainer.setGeometry(QRect(60, 60, 1160, 630))
        self.settingsadmincontainer.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.verticalLayout_23 = QVBoxLayout(self.settingsadmincontainer)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.scrollArea_settingsadmin = QScrollArea(self.settingsadmincontainer)
        self.scrollArea_settingsadmin.setObjectName(u"scrollArea_settingsadmin")
        self.scrollArea_settingsadmin.setWidgetResizable(True)
        self.scrollAreaWidgetContents_16 = QWidget()
        self.scrollAreaWidgetContents_16.setObjectName(u"scrollAreaWidgetContents_16")
        self.scrollAreaWidgetContents_16.setGeometry(QRect(0, 0, 1127, 1018))
        self.verticalLayout_28 = QVBoxLayout(self.scrollAreaWidgetContents_16)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_settingsadmin = QFrame(self.scrollAreaWidgetContents_16)
        self.frame_settingsadmin.setObjectName(u"frame_settingsadmin")
        self.frame_settingsadmin.setMinimumSize(QSize(0, 1000))
        self.frame_settingsadmin.setFrameShape(QFrame.StyledPanel)
        self.frame_settingsadmin.setFrameShadow(QFrame.Raised)
        self.accsettingslabel_4 = QLabel(self.frame_settingsadmin)
        self.accsettingslabel_4.setObjectName(u"accsettingslabel_4")
        self.accsettingslabel_4.setGeometry(QRect(417, 10, 290, 61))
        self.accsettingslabel_4.setStyleSheet(u"color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 32px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.accsettingslabel_4.setAlignment(Qt.AlignCenter)
        self.myacclabel_4 = QLabel(self.frame_settingsadmin)
        self.myacclabel_4.setObjectName(u"myacclabel_4")
        self.myacclabel_4.setGeometry(QRect(30, 70, 131, 61))
        self.myacclabel_4.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.settingslabel_4 = QLabel(self.frame_settingsadmin)
        self.settingslabel_4.setObjectName(u"settingslabel_4")
        self.settingslabel_4.setGeometry(QRect(30, 210, 131, 61))
        self.settingslabel_4.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.helplabel_4 = QLabel(self.frame_settingsadmin)
        self.helplabel_4.setObjectName(u"helplabel_4")
        self.helplabel_4.setGeometry(QRect(30, 350, 131, 61))
        self.helplabel_4.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.ruleadminbutton = QPushButton(self.frame_settingsadmin)
        self.ruleadminbutton.setObjectName(u"ruleadminbutton")
        self.ruleadminbutton.setGeometry(QRect(30, 420, 1051, 61))
        self.ruleadminbutton.setStyleSheet(u"QPushButton {\n"
"                background-color: #D9D9D9;\n"
"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }")
        self.logoutsettingsadminbutton = QPushButton(self.frame_settingsadmin)
        self.logoutsettingsadminbutton.setObjectName(u"logoutsettingsadminbutton")
        self.logoutsettingsadminbutton.setGeometry(QRect(30, 650, 1051, 61))
        self.logoutsettingsadminbutton.setStyleSheet(u"QPushButton {\n"
"                background-color: #cd4662;\n"
"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }")
        self.shopaccountbutton = QPushButton(self.frame_settingsadmin)
        self.shopaccountbutton.setObjectName(u"shopaccountbutton")
        self.shopaccountbutton.setGeometry(QRect(30, 140, 1051, 61))
        self.shopaccountbutton.setStyleSheet(u"QPushButton {\n"
"                background-color: #D9D9D9;\n"
"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }")
        self.exitshopbutton = QPushButton(self.frame_settingsadmin)
        self.exitshopbutton.setObjectName(u"exitshopbutton")
        self.exitshopbutton.setGeometry(QRect(30, 550, 1051, 61))
        self.exitshopbutton.setStyleSheet(u"QPushButton {\n"
"                background-color: #cd4662;\n"
"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }")
        self.editshopbutton = QPushButton(self.frame_settingsadmin)
        self.editshopbutton.setObjectName(u"editshopbutton")
        self.editshopbutton.setGeometry(QRect(30, 280, 1051, 61))
        self.editshopbutton.setStyleSheet(u"QPushButton {\n"
"                background-color: #D9D9D9;\n"
"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }")

        self.verticalLayout_28.addWidget(self.frame_settingsadmin)

        self.scrollArea_settingsadmin.setWidget(self.scrollAreaWidgetContents_16)

        self.verticalLayout_23.addWidget(self.scrollArea_settingsadmin)

        self.stackedWidget_settingadmin.addWidget(self.settingsadminmainpage)
        self.shopaccountadminpage = QWidget()
        self.shopaccountadminpage.setObjectName(u"shopaccountadminpage")
        self.adminregistercontainer_3 = QWidget(self.shopaccountadminpage)
        self.adminregistercontainer_3.setObjectName(u"adminregistercontainer_3")
        self.adminregistercontainer_3.setGeometry(QRect(60, 60, 1160, 630))
        self.adminregistercontainer_3.setStyleSheet(u"background: #FAF9F6;")
        self.textboxeditcontainer_10 = QWidget(self.adminregistercontainer_3)
        self.textboxeditcontainer_10.setObjectName(u"textboxeditcontainer_10")
        self.textboxeditcontainer_10.setGeometry(QRect(29, 0, 1101, 600))
        self.textboxeditcontainer_10.setStyleSheet(u"border-radius: 20px;\n"
"background: #F4DBDB;")
        self.shopnamelabel_3 = QLabel(self.textboxeditcontainer_10)
        self.shopnamelabel_3.setObjectName(u"shopnamelabel_3")
        self.shopnamelabel_3.setGeometry(QRect(40, 260, 141, 31))
        self.shopnamelabel_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.fisrtnamelabel_admin_3 = QLabel(self.textboxeditcontainer_10)
        self.fisrtnamelabel_admin_3.setObjectName(u"fisrtnamelabel_admin_3")
        self.fisrtnamelabel_admin_3.setGeometry(QRect(40, 310, 121, 31))
        self.fisrtnamelabel_admin_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.lastnamelabel_admin_3 = QLabel(self.textboxeditcontainer_10)
        self.lastnamelabel_admin_3.setObjectName(u"lastnamelabel_admin_3")
        self.lastnamelabel_admin_3.setGeometry(QRect(450, 310, 121, 31))
        self.lastnamelabel_admin_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.addresslabel_admin_3 = QLabel(self.textboxeditcontainer_10)
        self.addresslabel_admin_3.setObjectName(u"addresslabel_admin_3")
        self.addresslabel_admin_3.setGeometry(QRect(40, 360, 121, 31))
        self.addresslabel_admin_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.phonelabel_admin_3 = QLabel(self.textboxeditcontainer_10)
        self.phonelabel_admin_3.setObjectName(u"phonelabel_admin_3")
        self.phonelabel_admin_3.setGeometry(QRect(820, 260, 71, 31))
        self.phonelabel_admin_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.emaillabel_admin_3 = QLabel(self.textboxeditcontainer_10)
        self.emaillabel_admin_3.setObjectName(u"emaillabel_admin_3")
        self.emaillabel_admin_3.setGeometry(QRect(40, 540, 61, 31))
        self.emaillabel_admin_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.shopdescriptionlabel_3 = QLabel(self.textboxeditcontainer_10)
        self.shopdescriptionlabel_3.setObjectName(u"shopdescriptionlabel_3")
        self.shopdescriptionlabel_3.setGeometry(QRect(450, 260, 141, 31))
        self.shopdescriptionlabel_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.shoplogolabel_3 = QLabel(self.textboxeditcontainer_10)
        self.shoplogolabel_3.setObjectName(u"shoplogolabel_3")
        self.shoplogolabel_3.setGeometry(QRect(470, 10, 181, 41))
        self.shoplogolabel_3.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.shoplogolabel_3.setAlignment(Qt.AlignCenter)
        self.editshoppic_3 = QLabel(self.textboxeditcontainer_10)
        self.editshoppic_3.setObjectName(u"editshoppic_3")
        self.editshoppic_3.setGeometry(QRect(480, 70, 160, 160))
        self.editshoppic_3.setStyleSheet(u"border: none;\n"
"border-radius: 80px;\n"
"background: #cd4662;")
        self.shopdescriptionlabel_4 = QLabel(self.textboxeditcontainer_10)
        self.shopdescriptionlabel_4.setObjectName(u"shopdescriptionlabel_4")
        self.shopdescriptionlabel_4.setGeometry(QRect(610, 260, 141, 31))
        self.shopdescriptionlabel_4.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.phonelabel_admin_4 = QLabel(self.textboxeditcontainer_10)
        self.phonelabel_admin_4.setObjectName(u"phonelabel_admin_4")
        self.phonelabel_admin_4.setGeometry(QRect(930, 260, 151, 31))
        self.phonelabel_admin_4.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.emaillabel_admin_4 = QLabel(self.textboxeditcontainer_10)
        self.emaillabel_admin_4.setObjectName(u"emaillabel_admin_4")
        self.emaillabel_admin_4.setGeometry(QRect(220, 540, 341, 31))
        self.emaillabel_admin_4.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.fisrtnamelabel_admin_4 = QLabel(self.textboxeditcontainer_10)
        self.fisrtnamelabel_admin_4.setObjectName(u"fisrtnamelabel_admin_4")
        self.fisrtnamelabel_admin_4.setGeometry(QRect(220, 310, 131, 31))
        self.fisrtnamelabel_admin_4.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.lastnamelabel_admin_4 = QLabel(self.textboxeditcontainer_10)
        self.lastnamelabel_admin_4.setObjectName(u"lastnamelabel_admin_4")
        self.lastnamelabel_admin_4.setGeometry(QRect(610, 310, 131, 31))
        self.lastnamelabel_admin_4.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.shopnamelabel_4 = QLabel(self.textboxeditcontainer_10)
        self.shopnamelabel_4.setObjectName(u"shopnamelabel_4")
        self.shopnamelabel_4.setGeometry(QRect(220, 260, 151, 31))
        self.shopnamelabel_4.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.addresslabel_admin_4 = QLabel(self.textboxeditcontainer_10)
        self.addresslabel_admin_4.setObjectName(u"addresslabel_admin_4")
        self.addresslabel_admin_4.setGeometry(QRect(220, 360, 791, 161))
        self.addresslabel_admin_4.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.addresslabel_admin_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.backbutton_settingsadmin_7 = QPushButton(self.shopaccountadminpage)
        self.backbutton_settingsadmin_7.setObjectName(u"backbutton_settingsadmin_7")
        self.backbutton_settingsadmin_7.setGeometry(QRect(20, 30, 20, 31))
        self.backbutton_settingsadmin_7.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/backhomoe.png);")
        self.stackedWidget_settingadmin.addWidget(self.shopaccountadminpage)
        self.editshopaccountadminpage = QWidget()
        self.editshopaccountadminpage.setObjectName(u"editshopaccountadminpage")
        self.backbutton_settingsadmin_6 = QPushButton(self.editshopaccountadminpage)
        self.backbutton_settingsadmin_6.setObjectName(u"backbutton_settingsadmin_6")
        self.backbutton_settingsadmin_6.setGeometry(QRect(20, 30, 20, 31))
        self.backbutton_settingsadmin_6.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/backhomoe.png);")
        self.adminregistercontainer_2 = QWidget(self.editshopaccountadminpage)
        self.adminregistercontainer_2.setObjectName(u"adminregistercontainer_2")
        self.adminregistercontainer_2.setGeometry(QRect(60, 60, 1160, 630))
        self.adminregistercontainer_2.setStyleSheet(u"background: #FAF9F6;")
        self.textboxeditcontainer_9 = QWidget(self.adminregistercontainer_2)
        self.textboxeditcontainer_9.setObjectName(u"textboxeditcontainer_9")
        self.textboxeditcontainer_9.setGeometry(QRect(300, 0, 830, 600))
        self.textboxeditcontainer_9.setStyleSheet(u"border-radius: 20px;\n"
"background: #F4DBDB;")
        self.shopregisterationlabel_2 = QLabel(self.textboxeditcontainer_9)
        self.shopregisterationlabel_2.setObjectName(u"shopregisterationlabel_2")
        self.shopregisterationlabel_2.setGeometry(QRect(43, 34, 281, 51))
        self.shopregisterationlabel_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.shopnamelabel_2 = QLabel(self.textboxeditcontainer_9)
        self.shopnamelabel_2.setObjectName(u"shopnamelabel_2")
        self.shopnamelabel_2.setGeometry(QRect(43, 100, 141, 31))
        self.shopnamelabel_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.fisrtnamelabel_admin_2 = QLabel(self.textboxeditcontainer_9)
        self.fisrtnamelabel_admin_2.setObjectName(u"fisrtnamelabel_admin_2")
        self.fisrtnamelabel_admin_2.setGeometry(QRect(43, 200, 121, 31))
        self.fisrtnamelabel_admin_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.lastnamelabel_admin_2 = QLabel(self.textboxeditcontainer_9)
        self.lastnamelabel_admin_2.setObjectName(u"lastnamelabel_admin_2")
        self.lastnamelabel_admin_2.setGeometry(QRect(40, 300, 121, 31))
        self.lastnamelabel_admin_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.addresslabel_admin_2 = QLabel(self.textboxeditcontainer_9)
        self.addresslabel_admin_2.setObjectName(u"addresslabel_admin_2")
        self.addresslabel_admin_2.setGeometry(QRect(450, 250, 121, 31))
        self.addresslabel_admin_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.phonelabel_admin_2 = QLabel(self.textboxeditcontainer_9)
        self.phonelabel_admin_2.setObjectName(u"phonelabel_admin_2")
        self.phonelabel_admin_2.setGeometry(QRect(43, 400, 121, 31))
        self.phonelabel_admin_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.emaillabel_admin_2 = QLabel(self.textboxeditcontainer_9)
        self.emaillabel_admin_2.setObjectName(u"emaillabel_admin_2")
        self.emaillabel_admin_2.setGeometry(QRect(450, 400, 121, 31))
        self.emaillabel_admin_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.shopnamebox_2 = QLineEdit(self.textboxeditcontainer_9)
        self.shopnamebox_2.setObjectName(u"shopnamebox_2")
        self.shopnamebox_2.setGeometry(QRect(43, 150, 341, 31))
        self.shopnamebox_2.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.firstnamebox_admin_2 = QLineEdit(self.textboxeditcontainer_9)
        self.firstnamebox_admin_2.setObjectName(u"firstnamebox_admin_2")
        self.firstnamebox_admin_2.setGeometry(QRect(43, 250, 341, 31))
        self.firstnamebox_admin_2.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.phonebox_admin_2 = QLineEdit(self.textboxeditcontainer_9)
        self.phonebox_admin_2.setObjectName(u"phonebox_admin_2")
        self.phonebox_admin_2.setGeometry(QRect(43, 450, 341, 31))
        self.phonebox_admin_2.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.lastnamebox_admin_2 = QLineEdit(self.textboxeditcontainer_9)
        self.lastnamebox_admin_2.setObjectName(u"lastnamebox_admin_2")
        self.lastnamebox_admin_2.setGeometry(QRect(40, 350, 341, 31))
        self.lastnamebox_admin_2.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.emailbox_admin_2 = QLineEdit(self.textboxeditcontainer_9)
        self.emailbox_admin_2.setObjectName(u"emailbox_admin_2")
        self.emailbox_admin_2.setGeometry(QRect(450, 450, 341, 31))
        self.emailbox_admin_2.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.adminregisterbutton_2 = QPushButton(self.textboxeditcontainer_9)
        self.adminregisterbutton_2.setObjectName(u"adminregisterbutton_2")
        self.adminregisterbutton_2.setGeometry(QRect(590, 530, 201, 41))
        self.adminregisterbutton_2.setStyleSheet(u"color: #FFF;\n"
"background: #AEC289;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border-radius: 10px;")
        self.descriptionbox_admin_2 = QLineEdit(self.textboxeditcontainer_9)
        self.descriptionbox_admin_2.setObjectName(u"descriptionbox_admin_2")
        self.descriptionbox_admin_2.setGeometry(QRect(450, 150, 341, 81))
        self.descriptionbox_admin_2.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.shopdescriptionlabel_2 = QLabel(self.textboxeditcontainer_9)
        self.shopdescriptionlabel_2.setObjectName(u"shopdescriptionlabel_2")
        self.shopdescriptionlabel_2.setGeometry(QRect(450, 100, 141, 31))
        self.shopdescriptionlabel_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.addressbox_admin_2 = QLineEdit(self.textboxeditcontainer_9)
        self.addressbox_admin_2.setObjectName(u"addressbox_admin_2")
        self.addressbox_admin_2.setGeometry(QRect(450, 300, 341, 81))
        self.addressbox_admin_2.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.deleteaccbutton_5 = QPushButton(self.textboxeditcontainer_9)
        self.deleteaccbutton_5.setObjectName(u"deleteaccbutton_5")
        self.deleteaccbutton_5.setGeometry(QRect(380, 530, 201, 41))
        self.deleteaccbutton_5.setStyleSheet(u"color: #FFF;\n"
"background: #cd4662;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border-radius: 10px;")
        self.editshoppic_2 = QLabel(self.adminregistercontainer_2)
        self.editshoppic_2.setObjectName(u"editshoppic_2")
        self.editshoppic_2.setGeometry(QRect(40, 0, 160, 160))
        self.editshoppic_2.setStyleSheet(u"border: none;\n"
"border-radius: 80px;\n"
"background: #cd4662;")
        self.shoplogolabel_2 = QLabel(self.adminregistercontainer_2)
        self.shoplogolabel_2.setObjectName(u"shoplogolabel_2")
        self.shoplogolabel_2.setGeometry(QRect(40, 190, 171, 41))
        self.shoplogolabel_2.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.shoplogolabel_2.setAlignment(Qt.AlignCenter)
        self.stackedWidget_settingadmin.addWidget(self.editshopaccountadminpage)
        self.ruleadminpage = QWidget()
        self.ruleadminpage.setObjectName(u"ruleadminpage")
        self.ruleofusecontainer_3 = QWidget(self.ruleadminpage)
        self.ruleofusecontainer_3.setObjectName(u"ruleofusecontainer_3")
        self.ruleofusecontainer_3.setGeometry(QRect(60, 60, 1160, 630))
        self.ruleofusecontainer_3.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}\n"
"")
        self.verticalLayout_29 = QVBoxLayout(self.ruleofusecontainer_3)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.scrollArea_ruleofuse_3 = QScrollArea(self.ruleofusecontainer_3)
        self.scrollArea_ruleofuse_3.setObjectName(u"scrollArea_ruleofuse_3")
        self.scrollArea_ruleofuse_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_19 = QWidget()
        self.scrollAreaWidgetContents_19.setObjectName(u"scrollAreaWidgetContents_19")
        self.scrollAreaWidgetContents_19.setGeometry(QRect(0, 0, 1127, 1518))
        self.verticalLayout_30 = QVBoxLayout(self.scrollAreaWidgetContents_19)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_ruleofuse_3 = QFrame(self.scrollAreaWidgetContents_19)
        self.frame_ruleofuse_3.setObjectName(u"frame_ruleofuse_3")
        self.frame_ruleofuse_3.setMinimumSize(QSize(0, 1500))
        self.frame_ruleofuse_3.setFrameShape(QFrame.StyledPanel)
        self.frame_ruleofuse_3.setFrameShadow(QFrame.Raised)
        self.ruleofuselabel_3 = QLabel(self.frame_ruleofuse_3)
        self.ruleofuselabel_3.setObjectName(u"ruleofuselabel_3")
        self.ruleofuselabel_3.setGeometry(QRect(417, 10, 290, 61))
        self.ruleofuselabel_3.setStyleSheet(u"color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 32px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.ruleofuselabel_3.setAlignment(Qt.AlignCenter)
        self.ruleofusecontentlabel_3 = QLabel(self.frame_ruleofuse_3)
        self.ruleofusecontentlabel_3.setObjectName(u"ruleofusecontentlabel_3")
        self.ruleofusecontentlabel_3.setGeometry(QRect(40, 100, 1040, 531))
        self.ruleofusecontentlabel_3.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_30.addWidget(self.frame_ruleofuse_3)

        self.scrollArea_ruleofuse_3.setWidget(self.scrollAreaWidgetContents_19)

        self.verticalLayout_29.addWidget(self.scrollArea_ruleofuse_3)

        self.backbutton_settingsadmin_2 = QPushButton(self.ruleadminpage)
        self.backbutton_settingsadmin_2.setObjectName(u"backbutton_settingsadmin_2")
        self.backbutton_settingsadmin_2.setGeometry(QRect(20, 30, 20, 31))
        self.backbutton_settingsadmin_2.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/backhomoe.png);")
        self.stackedWidget_settingadmin.addWidget(self.ruleadminpage)
        self.nouse_4 = QWidget()
        self.nouse_4.setObjectName(u"nouse_4")
        self.backbutton_settingsadmin_4 = QPushButton(self.nouse_4)
        self.backbutton_settingsadmin_4.setObjectName(u"backbutton_settingsadmin_4")
        self.backbutton_settingsadmin_4.setGeometry(QRect(20, 30, 20, 31))
        self.backbutton_settingsadmin_4.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/backhomoe.png);")
        self.changepasswordcontainer_3 = QWidget(self.nouse_4)
        self.changepasswordcontainer_3.setObjectName(u"changepasswordcontainer_3")
        self.changepasswordcontainer_3.setGeometry(QRect(60, 60, 1160, 630))
        self.changepasswordcontainer_3.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}\n"
"")
        self.verticalLayout_31 = QVBoxLayout(self.changepasswordcontainer_3)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.scrollArea_changepassword_3 = QScrollArea(self.changepasswordcontainer_3)
        self.scrollArea_changepassword_3.setObjectName(u"scrollArea_changepassword_3")
        self.scrollArea_changepassword_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_20 = QWidget()
        self.scrollAreaWidgetContents_20.setObjectName(u"scrollAreaWidgetContents_20")
        self.scrollAreaWidgetContents_20.setGeometry(QRect(0, 0, 1127, 1518))
        self.verticalLayout_32 = QVBoxLayout(self.scrollAreaWidgetContents_20)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_changepassword_3 = QFrame(self.scrollAreaWidgetContents_20)
        self.frame_changepassword_3.setObjectName(u"frame_changepassword_3")
        self.frame_changepassword_3.setMinimumSize(QSize(0, 1500))
        self.frame_changepassword_3.setFrameShape(QFrame.StyledPanel)
        self.frame_changepassword_3.setFrameShadow(QFrame.Raised)
        self.changepasswordlabel_3 = QLabel(self.frame_changepassword_3)
        self.changepasswordlabel_3.setObjectName(u"changepasswordlabel_3")
        self.changepasswordlabel_3.setGeometry(QRect(417, 10, 290, 61))
        self.changepasswordlabel_3.setStyleSheet(u"color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 32px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.changepasswordlabel_3.setAlignment(Qt.AlignCenter)
        self.currentpasslabel_3 = QLabel(self.frame_changepassword_3)
        self.currentpasslabel_3.setObjectName(u"currentpasslabel_3")
        self.currentpasslabel_3.setGeometry(QRect(40, 100, 221, 51))
        self.currentpasslabel_3.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.savechangebutton_8 = QPushButton(self.frame_changepassword_3)
        self.savechangebutton_8.setObjectName(u"savechangebutton_8")
        self.savechangebutton_8.setGeometry(QRect(860, 510, 201, 41))
        self.savechangebutton_8.setStyleSheet(u"color: #FFF;\n"
"background: #AEC289;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border-radius: 10px;")
        self.newpasslabel_3 = QLabel(self.frame_changepassword_3)
        self.newpasslabel_3.setObjectName(u"newpasslabel_3")
        self.newpasslabel_3.setGeometry(QRect(40, 270, 221, 51))
        self.newpasslabel_3.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.curpasstextbox_3 = QLineEdit(self.frame_changepassword_3)
        self.curpasstextbox_3.setObjectName(u"curpasstextbox_3")
        self.curpasstextbox_3.setGeometry(QRect(40, 180, 481, 41))
        self.curpasstextbox_3.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.newpasstextbox_3 = QLineEdit(self.frame_changepassword_3)
        self.newpasstextbox_3.setObjectName(u"newpasstextbox_3")
        self.newpasstextbox_3.setGeometry(QRect(40, 350, 481, 41))
        self.newpasstextbox_3.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")

        self.verticalLayout_32.addWidget(self.frame_changepassword_3)

        self.scrollArea_changepassword_3.setWidget(self.scrollAreaWidgetContents_20)

        self.verticalLayout_31.addWidget(self.scrollArea_changepassword_3)

        self.stackedWidget_settingadmin.addWidget(self.nouse_4)
        self.nouse_3 = QWidget()
        self.nouse_3.setObjectName(u"nouse_3")
        self.backbutton_settingsadmin_5 = QPushButton(self.nouse_3)
        self.backbutton_settingsadmin_5.setObjectName(u"backbutton_settingsadmin_5")
        self.backbutton_settingsadmin_5.setGeometry(QRect(20, 30, 20, 31))
        self.backbutton_settingsadmin_5.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/backhomoe.png);")
        self.editprofilecontainer_7 = QWidget(self.nouse_3)
        self.editprofilecontainer_7.setObjectName(u"editprofilecontainer_7")
        self.editprofilecontainer_7.setGeometry(QRect(60, 60, 1160, 630))
        self.editprofilecontainer_7.setStyleSheet(u"background: #FAF9F6;")
        self.textboxeditcontainer_8 = QWidget(self.editprofilecontainer_7)
        self.textboxeditcontainer_8.setObjectName(u"textboxeditcontainer_8")
        self.textboxeditcontainer_8.setGeometry(QRect(29, 0, 1101, 600))
        self.textboxeditcontainer_8.setStyleSheet(u"border-radius: 20px;\n"
"background: #F4DBDB;")
        self.profilelabel_3 = QLabel(self.textboxeditcontainer_8)
        self.profilelabel_3.setObjectName(u"profilelabel_3")
        self.profilelabel_3.setGeometry(QRect(470, 10, 160, 51))
        self.profilelabel_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.profilelabel_3.setAlignment(Qt.AlignCenter)
        self.usernameprofile_3 = QLabel(self.textboxeditcontainer_8)
        self.usernameprofile_3.setObjectName(u"usernameprofile_3")
        self.usernameprofile_3.setGeometry(QRect(763, 350, 121, 31))
        self.usernameprofile_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.fisrtnameprofile_3 = QLabel(self.textboxeditcontainer_8)
        self.fisrtnameprofile_3.setObjectName(u"fisrtnameprofile_3")
        self.fisrtnameprofile_3.setGeometry(QRect(40, 270, 121, 31))
        self.fisrtnameprofile_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.lastnameprofile_3 = QLabel(self.textboxeditcontainer_8)
        self.lastnameprofile_3.setObjectName(u"lastnameprofile_3")
        self.lastnameprofile_3.setGeometry(QRect(230, 460, 121, 31))
        self.lastnameprofile_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.genderprofile_3 = QLabel(self.textboxeditcontainer_8)
        self.genderprofile_3.setObjectName(u"genderprofile_3")
        self.genderprofile_3.setGeometry(QRect(43, 490, 121, 31))
        self.genderprofile_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.birthprofile_3 = QLabel(self.textboxeditcontainer_8)
        self.birthprofile_3.setObjectName(u"birthprofile_3")
        self.birthprofile_3.setGeometry(QRect(450, 300, 121, 31))
        self.birthprofile_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.phoneprofile_3 = QLabel(self.textboxeditcontainer_8)
        self.phoneprofile_3.setObjectName(u"phoneprofile_3")
        self.phoneprofile_3.setGeometry(QRect(43, 400, 121, 31))
        self.phoneprofile_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.emailprofile_3 = QLabel(self.textboxeditcontainer_8)
        self.emailprofile_3.setObjectName(u"emailprofile_3")
        self.emailprofile_3.setGeometry(QRect(450, 400, 121, 31))
        self.emailprofile_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.pictureprofile_3 = QLabel(self.textboxeditcontainer_8)
        self.pictureprofile_3.setObjectName(u"pictureprofile_3")
        self.pictureprofile_3.setGeometry(QRect(470, 70, 160, 160))
        self.pictureprofile_3.setStyleSheet(u"border: none;\n"
"border-radius: 80px;\n"
"background: #cd4662;")
        self.username_3 = QLabel(self.textboxeditcontainer_8)
        self.username_3.setObjectName(u"username_3")
        self.username_3.setGeometry(QRect(770, 390, 165, 41))
        self.username_3.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.username_3.setAlignment(Qt.AlignCenter)
        self.firstname_3 = QLabel(self.textboxeditcontainer_8)
        self.firstname_3.setObjectName(u"firstname_3")
        self.firstname_3.setGeometry(QRect(780, 490, 165, 41))
        self.firstname_3.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.firstname_3.setAlignment(Qt.AlignCenter)
        self.gender_3 = QLabel(self.textboxeditcontainer_8)
        self.gender_3.setObjectName(u"gender_3")
        self.gender_3.setGeometry(QRect(40, 530, 165, 41))
        self.gender_3.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.gender_3.setAlignment(Qt.AlignCenter)
        self.phone_3 = QLabel(self.textboxeditcontainer_8)
        self.phone_3.setObjectName(u"phone_3")
        self.phone_3.setGeometry(QRect(40, 450, 165, 41))
        self.phone_3.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.phone_3.setAlignment(Qt.AlignCenter)
        self.lastname_3 = QLabel(self.textboxeditcontainer_8)
        self.lastname_3.setObjectName(u"lastname_3")
        self.lastname_3.setGeometry(QRect(240, 500, 165, 41))
        self.lastname_3.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.lastname_3.setAlignment(Qt.AlignCenter)
        self.birthday_3 = QLabel(self.textboxeditcontainer_8)
        self.birthday_3.setObjectName(u"birthday_3")
        self.birthday_3.setGeometry(QRect(430, 350, 165, 41))
        self.birthday_3.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.birthday_3.setAlignment(Qt.AlignCenter)
        self.email_3 = QLabel(self.textboxeditcontainer_8)
        self.email_3.setObjectName(u"email_3")
        self.email_3.setGeometry(QRect(430, 450, 165, 41))
        self.email_3.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.email_3.setAlignment(Qt.AlignCenter)
        self.stackedWidget_settingadmin.addWidget(self.nouse_3)
        self.nouse_5 = QWidget()
        self.nouse_5.setObjectName(u"nouse_5")
        self.backbutton_settingsadmin_3 = QPushButton(self.nouse_5)
        self.backbutton_settingsadmin_3.setObjectName(u"backbutton_settingsadmin_3")
        self.backbutton_settingsadmin_3.setGeometry(QRect(20, 30, 20, 31))
        self.backbutton_settingsadmin_3.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/backhomoe.png);")
        self.editprofilecontainer_6 = QWidget(self.nouse_5)
        self.editprofilecontainer_6.setObjectName(u"editprofilecontainer_6")
        self.editprofilecontainer_6.setGeometry(QRect(60, 60, 1160, 630))
        self.editprofilecontainer_6.setStyleSheet(u"background: #FAF9F6;")
        self.textboxeditcontainer_7 = QWidget(self.editprofilecontainer_6)
        self.textboxeditcontainer_7.setObjectName(u"textboxeditcontainer_7")
        self.textboxeditcontainer_7.setGeometry(QRect(300, 0, 830, 600))
        self.textboxeditcontainer_7.setStyleSheet(u"border-radius: 20px;\n"
"background: #F4DBDB;")
        self.editlabel_4 = QLabel(self.textboxeditcontainer_7)
        self.editlabel_4.setObjectName(u"editlabel_4")
        self.editlabel_4.setGeometry(QRect(43, 34, 171, 51))
        self.editlabel_4.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.userabel_4 = QLabel(self.textboxeditcontainer_7)
        self.userabel_4.setObjectName(u"userabel_4")
        self.userabel_4.setGeometry(QRect(43, 100, 121, 31))
        self.userabel_4.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.fisrtlabel_4 = QLabel(self.textboxeditcontainer_7)
        self.fisrtlabel_4.setObjectName(u"fisrtlabel_4")
        self.fisrtlabel_4.setGeometry(QRect(43, 200, 121, 31))
        self.fisrtlabel_4.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.lastlabel_4 = QLabel(self.textboxeditcontainer_7)
        self.lastlabel_4.setObjectName(u"lastlabel_4")
        self.lastlabel_4.setGeometry(QRect(450, 200, 121, 31))
        self.lastlabel_4.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.genlabel_4 = QLabel(self.textboxeditcontainer_7)
        self.genlabel_4.setObjectName(u"genlabel_4")
        self.genlabel_4.setGeometry(QRect(43, 300, 121, 31))
        self.genlabel_4.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.birthlabel_4 = QLabel(self.textboxeditcontainer_7)
        self.birthlabel_4.setObjectName(u"birthlabel_4")
        self.birthlabel_4.setGeometry(QRect(450, 300, 121, 31))
        self.birthlabel_4.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.pholabel_4 = QLabel(self.textboxeditcontainer_7)
        self.pholabel_4.setObjectName(u"pholabel_4")
        self.pholabel_4.setGeometry(QRect(43, 400, 121, 31))
        self.pholabel_4.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.emaillabel_5 = QLabel(self.textboxeditcontainer_7)
        self.emaillabel_5.setObjectName(u"emaillabel_5")
        self.emaillabel_5.setGeometry(QRect(450, 400, 121, 31))
        self.emaillabel_5.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.userbox_4 = QLineEdit(self.textboxeditcontainer_7)
        self.userbox_4.setObjectName(u"userbox_4")
        self.userbox_4.setGeometry(QRect(43, 150, 341, 31))
        self.userbox_4.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.firstnamebox_4 = QLineEdit(self.textboxeditcontainer_7)
        self.firstnamebox_4.setObjectName(u"firstnamebox_4")
        self.firstnamebox_4.setGeometry(QRect(43, 250, 341, 31))
        self.firstnamebox_4.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.genderbox_4 = QLineEdit(self.textboxeditcontainer_7)
        self.genderbox_4.setObjectName(u"genderbox_4")
        self.genderbox_4.setGeometry(QRect(43, 350, 341, 31))
        self.genderbox_4.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.phonebox_4 = QLineEdit(self.textboxeditcontainer_7)
        self.phonebox_4.setObjectName(u"phonebox_4")
        self.phonebox_4.setGeometry(QRect(43, 450, 341, 31))
        self.phonebox_4.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.lastnamebox_4 = QLineEdit(self.textboxeditcontainer_7)
        self.lastnamebox_4.setObjectName(u"lastnamebox_4")
        self.lastnamebox_4.setGeometry(QRect(450, 250, 341, 31))
        self.lastnamebox_4.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.emailbox_4 = QLineEdit(self.textboxeditcontainer_7)
        self.emailbox_4.setObjectName(u"emailbox_4")
        self.emailbox_4.setGeometry(QRect(450, 450, 341, 31))
        self.emailbox_4.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.savechangebutton_7 = QPushButton(self.textboxeditcontainer_7)
        self.savechangebutton_7.setObjectName(u"savechangebutton_7")
        self.savechangebutton_7.setGeometry(QRect(590, 530, 201, 41))
        self.savechangebutton_7.setStyleSheet(u"color: #FFF;\n"
"background: #AEC289;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border-radius: 10px;")
        self.deleteaccbutton_4 = QPushButton(self.textboxeditcontainer_7)
        self.deleteaccbutton_4.setObjectName(u"deleteaccbutton_4")
        self.deleteaccbutton_4.setGeometry(QRect(350, 530, 201, 41))
        self.deleteaccbutton_4.setStyleSheet(u"color: #FFF;\n"
"background: #cd4662;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border-radius: 10px;")
        self.birthdaydateEdit_4 = QDateEdit(self.textboxeditcontainer_7)
        self.birthdaydateEdit_4.setObjectName(u"birthdaydateEdit_4")
        self.birthdaydateEdit_4.setGeometry(QRect(450, 350, 341, 31))
        self.birthdaydateEdit_4.setStyleSheet(u"QDateTimeEdit {\n"
"	background-color: #F4F2EF; \n"
"	font-size: 16px;\n"
"	border: 2px solid #CD4662; \n"
"	padding: 5px;\n"
"	border-radius: 5px; \n"
"}\n"
"QDateTimeEdit::down-button, QDateTimeEdit::up-button {\n"
"	width: 20px; \n"
"	height: 13px;\n"
"	background-color: #F4F2EF; \n"
"	border: 2px solid #CD4662; \n"
"	font-size: 16px;\n"
"}\n"
"QDateTimeEdit::down-button {\n"
"	subcontrol-origin: border;\n"
"	subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QDateTimeEdit::up-button {\n"
"	subcontrol-origin: border;\n"
"	subcontrol-position: top right;\n"
"}\n"
"    \n"
"QDateTimeEdit::down-button:pressed, QDateTimeEdit::up-button:pressed {\n"
"	background-color: #CD4662;\n"
"}\n"
"    \n"
"QDateTimeEdit::down-arrow, QDateTimeEdit::up-arrow {\n"
"	image: url(arrow.png); \n"
"}")
        self.birthdaydateEdit_4.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.editprofilepic_4 = QLabel(self.editprofilecontainer_6)
        self.editprofilepic_4.setObjectName(u"editprofilepic_4")
        self.editprofilepic_4.setGeometry(QRect(40, 0, 160, 160))
        self.editprofilepic_4.setStyleSheet(u"border: none;\n"
"border-radius: 80px;\n"
"background: #cd4662;")
        self.editnameprofile_4 = QLabel(self.editprofilecontainer_6)
        self.editnameprofile_4.setObjectName(u"editnameprofile_4")
        self.editnameprofile_4.setGeometry(QRect(40, 190, 165, 41))
        self.editnameprofile_4.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.editnameprofile_4.setAlignment(Qt.AlignCenter)
        self.stackedWidget_settingadmin.addWidget(self.nouse_5)
        self.stackedWidget.addWidget(self.settings_admin)
        self.nouse = QWidget()
        self.nouse.setObjectName(u"nouse")
        self.verticalLayout_5 = QVBoxLayout(self.nouse)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget.addWidget(self.nouse)
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.gridLayoutWidget = QWidget(self.main)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(-1, -1, 251, 721))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.navbar = QWidget(self.gridLayoutWidget)
        self.navbar.setObjectName(u"navbar")
        self.navbar.setCursor(QCursor(Qt.ArrowCursor))
        self.navbar.setStyleSheet(u"background-color: #FAF9F6;")
        self.Logolabel = QLabel(self.navbar)
        self.Logolabel.setObjectName(u"Logolabel")
        self.Logolabel.setGeometry(QRect(30, 40, 191, 51))
        font = QFont()
        font.setFamilies([u"Supermercado"])
        font.setBold(True)
        self.Logolabel.setFont(font)
        self.Logolabel.setStyleSheet(u"font-family: Supermercado;\n"
"                font-size: 36px;\n"
"                font-weight: 700;\n"
"                line-height: normal;\n"
"                text-align: center;\n"
"                color: #000000;")
        self.homebutton = QPushButton(self.navbar)
        self.homebutton.setObjectName(u"homebutton")
        self.homebutton.setGeometry(QRect(40, 130, 171, 67))
        self.homebutton.setStyleSheet(u"QPushButton{\n"
"	color: #FAF9F6;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 16px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                background-color: #AEC289;\n"
"                border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }\n"
"")
        self.homebutton.setCheckable(True)
        self.homebutton.setAutoExclusive(True)
        self.favbutton = QPushButton(self.navbar)
        self.favbutton.setObjectName(u"favbutton")
        self.favbutton.setGeometry(QRect(40, 240, 171, 67))
        self.favbutton.setStyleSheet(u"QPushButton{\n"
"	color: #000;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 16px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                background-color: #E1E3E7;\n"
"                border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }")
        self.favbutton.setCheckable(True)
        self.favbutton.setAutoExclusive(True)
        self.orderbutton = QPushButton(self.navbar)
        self.orderbutton.setObjectName(u"orderbutton")
        self.orderbutton.setGeometry(QRect(40, 350, 171, 67))
        self.orderbutton.setStyleSheet(u"QPushButton{\n"
"	color: #000;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 16px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                background-color: #E1E3E7;\n"
"                border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }")
        self.orderbutton.setCheckable(True)
        self.orderbutton.setAutoExclusive(True)
        self.messbutton = QPushButton(self.navbar)
        self.messbutton.setObjectName(u"messbutton")
        self.messbutton.setGeometry(QRect(40, 460, 171, 67))
        self.messbutton.setStyleSheet(u"QPushButton{\n"
"	color: #000;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 16px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                background-color: #E1E3E7;\n"
"                border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }")
        self.messbutton.setCheckable(True)
        self.messbutton.setAutoExclusive(True)
        self.settingbutton = QPushButton(self.navbar)
        self.settingbutton.setObjectName(u"settingbutton")
        self.settingbutton.setGeometry(QRect(110, 630, 30, 30))
        self.settingbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingbutton.setStyleSheet(u"image: url(:/pic/realimages/settingpic.png);\n"
"border: none;")
        self.settingbutton.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.navbar, 0, 0, 1, 1)

        self.searchcontainer = QWidget(self.main)
        self.searchcontainer.setObjectName(u"searchcontainer")
        self.searchcontainer.setGeometry(QRect(250, 0, 1031, 109))
        self.searchcontainer.setStyleSheet(u"background-color: #FAF9F6;")
        self.searchbox = QLineEdit(self.searchcontainer)
        self.searchbox.setObjectName(u"searchbox")
        self.searchbox.setGeometry(QRect(60, 50, 684, 31))
        self.searchbox.setStyleSheet(u"				border-radius: 15px;\n"
"                background-color: #EDEDED;\n"
"                color: #CD4662;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 16px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"				padding-left: 20px;\n"
"")
        self.loginsignoutbutton = QPushButton(self.searchcontainer)
        self.loginsignoutbutton.setObjectName(u"loginsignoutbutton")
        self.loginsignoutbutton.setGeometry(QRect(900, 50, 71, 31))
        self.loginsignoutbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginsignoutbutton.setStyleSheet(u"color: #000;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 20px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                border: none;\n"
"				text-align: center;")
        self.cartbutton = QPushButton(self.searchcontainer)
        self.cartbutton.setObjectName(u"cartbutton")
        self.cartbutton.setGeometry(QRect(770, 50, 34, 31))
        self.cartbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cartbutton.setStyleSheet(u"image: url(:/pic/realimages/cartpic.png);\n"
"border: none;")
        self.cartbutton.setIconSize(QSize(34, 31))
        self.profilebutton = QPushButton(self.searchcontainer)
        self.profilebutton.setObjectName(u"profilebutton")
        self.profilebutton.setGeometry(QRect(840, 50, 31, 31))
        self.profilebutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.profilebutton.setStyleSheet(u"image: url(:/pic/realimages/profilepic.png);\n"
"border: none;")
        self.profilebutton.setIconSize(QSize(31, 31))
        self.stackedWidget_main = QStackedWidget(self.main)
        self.stackedWidget_main.setObjectName(u"stackedWidget_main")
        self.stackedWidget_main.setGeometry(QRect(250, 110, 1031, 611))
        self.stackedWidget_main.setMinimumSize(QSize(1031, 611))
        self.stackedWidget_main.setStyleSheet(u"background-color: #FAF9F6;")
        self.viewshoppage = QWidget()
        self.viewshoppage.setObjectName(u"viewshoppage")
        self.scrollArea_homepage_admin_2 = QScrollArea(self.viewshoppage)
        self.scrollArea_homepage_admin_2.setObjectName(u"scrollArea_homepage_admin_2")
        self.scrollArea_homepage_admin_2.setGeometry(QRect(0, 0, 1021, 611))
        self.scrollArea_homepage_admin_2.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_homepage_admin_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_30 = QWidget()
        self.scrollAreaWidgetContents_30.setObjectName(u"scrollAreaWidgetContents_30")
        self.scrollAreaWidgetContents_30.setGeometry(QRect(0, 0, 1006, 1118))
        self.verticalLayout_35 = QVBoxLayout(self.scrollAreaWidgetContents_30)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_homepage_admin_2 = QFrame(self.scrollAreaWidgetContents_30)
        self.frame_homepage_admin_2.setObjectName(u"frame_homepage_admin_2")
        self.frame_homepage_admin_2.setMinimumSize(QSize(0, 1100))
        self.frame_homepage_admin_2.setFrameShape(QFrame.StyledPanel)
        self.frame_homepage_admin_2.setFrameShadow(QFrame.Raised)
        self.homepage_admin_container_3 = QWidget(self.frame_homepage_admin_2)
        self.homepage_admin_container_3.setObjectName(u"homepage_admin_container_3")
        self.homepage_admin_container_3.setGeometry(QRect(40, 24, 913, 221))
        self.homepage_admin_container_3.setStyleSheet(u"border-radius: 10px;\n"
"background: #F4F2EF;")
        self.profilepic_admin_2 = QLabel(self.homepage_admin_container_3)
        self.profilepic_admin_2.setObjectName(u"profilepic_admin_2")
        self.profilepic_admin_2.setGeometry(QRect(47, 50, 130, 130))
        self.profilepic_admin_2.setStyleSheet(u"border: none;\n"
"border-radius: 65px;\n"
"background: #cd4662;")
        self.shopnamelabel_admin_2 = QLabel(self.homepage_admin_container_3)
        self.shopnamelabel_admin_2.setObjectName(u"shopnamelabel_admin_2")
        self.shopnamelabel_admin_2.setGeometry(QRect(213, 93, 171, 41))
        self.shopnamelabel_admin_2.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.numreviews_2 = QLabel(self.homepage_admin_container_3)
        self.numreviews_2.setObjectName(u"numreviews_2")
        self.numreviews_2.setGeometry(QRect(480, 50, 49, 16))
        self.numreviews_2.setStyleSheet(u"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numreviews_2.setAlignment(Qt.AlignCenter)
        self.numreviewlabel_2 = QLabel(self.homepage_admin_container_3)
        self.numreviewlabel_2.setObjectName(u"numreviewlabel_2")
        self.numreviewlabel_2.setGeometry(QRect(560, 50, 61, 16))
        self.numreviewlabel_2.setStyleSheet(u"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numproducts_2 = QLabel(self.homepage_admin_container_3)
        self.numproducts_2.setObjectName(u"numproducts_2")
        self.numproducts_2.setGeometry(QRect(480, 140, 49, 16))
        self.numproducts_2.setStyleSheet(u"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numproducts_2.setAlignment(Qt.AlignCenter)
        self.numproductslebel_2 = QLabel(self.homepage_admin_container_3)
        self.numproductslebel_2.setObjectName(u"numproductslebel_2")
        self.numproductslebel_2.setGeometry(QRect(560, 140, 61, 16))
        self.numproductslebel_2.setStyleSheet(u"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numsolds_2 = QLabel(self.homepage_admin_container_3)
        self.numsolds_2.setObjectName(u"numsolds_2")
        self.numsolds_2.setGeometry(QRect(680, 50, 49, 16))
        self.numsolds_2.setStyleSheet(u"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numsolds_2.setAlignment(Qt.AlignCenter)
        self.numyearregisteredlabel_2 = QLabel(self.homepage_admin_container_3)
        self.numyearregisteredlabel_2.setObjectName(u"numyearregisteredlabel_2")
        self.numyearregisteredlabel_2.setGeometry(QRect(760, 140, 121, 21))
        self.numyearregisteredlabel_2.setStyleSheet(u"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numyearregisteredlabel_2.setAlignment(Qt.AlignCenter)
        self.numsoldslabel_2 = QLabel(self.homepage_admin_container_3)
        self.numsoldslabel_2.setObjectName(u"numsoldslabel_2")
        self.numsoldslabel_2.setGeometry(QRect(750, 50, 49, 16))
        self.numsoldslabel_2.setStyleSheet(u"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numsoldslabel_2.setAlignment(Qt.AlignCenter)
        self.numyearregistered_2 = QLabel(self.homepage_admin_container_3)
        self.numyearregistered_2.setObjectName(u"numyearregistered_2")
        self.numyearregistered_2.setGeometry(QRect(680, 140, 49, 16))
        self.numyearregistered_2.setStyleSheet(u"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numyearregistered_2.setAlignment(Qt.AlignCenter)
        self.productcontainer_admin_3 = QWidget(self.frame_homepage_admin_2)
        self.productcontainer_admin_3.setObjectName(u"productcontainer_admin_3")
        self.productcontainer_admin_3.setGeometry(QRect(40, 570, 913, 440))
        self.productcontainer_admin_3.setMinimumSize(QSize(913, 440))
        self.productcontainer_admin_3.setMaximumSize(QSize(16777215, 16777215))
        self.productcontainer_admin_3.setStyleSheet(u"border-bottom: 3px solid #CD4662;\n"
"background: #FAF9F6;\n"
"height: auto;")
        self.verticalLayout_36 = QVBoxLayout(self.productcontainer_admin_3)
        self.verticalLayout_36.setSpacing(6)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 5)
        self.frame_4 = QFrame(self.frame_homepage_admin_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(40, 270, 909, 49))
        self.frame_4.setMinimumSize(QSize(909, 49))
        self.frame_4.setMaximumSize(QSize(909, 49))
        self.frame_4.setStyleSheet(u"border: none;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.productslabel_admin_4 = QLabel(self.frame_4)
        self.productslabel_admin_4.setObjectName(u"productslabel_admin_4")
        self.productslabel_admin_4.setStyleSheet(u"color: #000;\n"
"border: none;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")

        self.horizontalLayout_21.addWidget(self.productslabel_admin_4)

        self.horizontalSpacer_10 = QSpacerItem(618, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_10)

        self.viewallproductbutton_admin_2 = QPushButton(self.frame_4)
        self.viewallproductbutton_admin_2.setObjectName(u"viewallproductbutton_admin_2")
        self.viewallproductbutton_admin_2.setStyleSheet(u"color:  #CD4662;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")

        self.horizontalLayout_21.addWidget(self.viewallproductbutton_admin_2)

        self.frame_products_admin_2 = QFrame(self.frame_homepage_admin_2)
        self.frame_products_admin_2.setObjectName(u"frame_products_admin_2")
        self.frame_products_admin_2.setGeometry(QRect(40, 340, 913, 435))
        self.frame_products_admin_2.setMinimumSize(QSize(913, 380))
        self.frame_products_admin_2.setMaximumSize(QSize(913, 16777215))
        self.frame_products_admin_2.setStyleSheet(u"border: none;")
        self.frame_products_admin_2.setFrameShape(QFrame.StyledPanel)
        self.frame_products_admin_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_products_admin_2 = QGridLayout(self.frame_products_admin_2)
        self.gridLayout_products_admin_2.setObjectName(u"gridLayout_products_admin_2")

        self.verticalLayout_35.addWidget(self.frame_homepage_admin_2)

        self.scrollArea_homepage_admin_2.setWidget(self.scrollAreaWidgetContents_30)
        self.stackedWidget_main.addWidget(self.viewshoppage)
        self.homepage = QWidget()
        self.homepage.setObjectName(u"homepage")
        self.scrollArea_homepage = QScrollArea(self.homepage)
        self.scrollArea_homepage.setObjectName(u"scrollArea_homepage")
        self.scrollArea_homepage.setGeometry(QRect(-1, -1, 1021, 611))
        self.scrollArea_homepage.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_homepage.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1006, 900))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(1006, 900))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(1006, 16777215))
        self.frame_homepage = QFrame(self.scrollAreaWidgetContents)
        self.frame_homepage.setObjectName(u"frame_homepage")
        self.frame_homepage.setGeometry(QRect(0, 0, 1031, 900))
        self.frame_homepage.setMinimumSize(QSize(1031, 900))
        self.frame_homepage.setMaximumSize(QSize(1031, 16777215))
        self.frame_homepage.setFrameShape(QFrame.StyledPanel)
        self.frame_homepage.setFrameShadow(QFrame.Raised)
        self.stylelabbutton = QPushButton(self.frame_homepage)
        self.stylelabbutton.setObjectName(u"stylelabbutton")
        self.stylelabbutton.setGeometry(QRect(60, 20, 911, 221))
        self.stylelabbutton.setStyleSheet(u"color: #FFF;\n"
"                text-align: center;\n"
"                font-family: Supermercado;\n"
"                font-size: 48px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                border-radius: 10px;\n"
"                background-color: #CD4662;")
        self.newarrivalbutton = QPushButton(self.frame_homepage)
        self.newarrivalbutton.setObjectName(u"newarrivalbutton")
        self.newarrivalbutton.setGeometry(QRect(60, 290, 179, 40))
        self.newarrivalbutton.setStyleSheet(u"QPushButton{\n"
"border-radius: 10px;\n"
"                border: 1px solid #000;\n"
"                opacity: 0.1;\n"
"                background-color: #F7F2EB;\n"
"                color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 20px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: #FAF9F6;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/pic/images/newres/newarrival.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newarrivalbutton.setIcon(icon)
        self.newarrivalbutton.setIconSize(QSize(17, 18))
        self.onsalesbutton = QPushButton(self.frame_homepage)
        self.onsalesbutton.setObjectName(u"onsalesbutton")
        self.onsalesbutton.setGeometry(QRect(300, 290, 179, 40))
        self.onsalesbutton.setStyleSheet(u"QPushButton{\n"
"border-radius: 10px;\n"
"                border: 1px solid #000;\n"
"                opacity: 0.1;\n"
"                background-color: #F7F2EB;\n"
"                color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 20px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: #FAF9F6;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/pic/images/newres/onsales.png", QSize(), QIcon.Normal, QIcon.Off)
        self.onsalesbutton.setIcon(icon1)
        self.onsalesbutton.setIconSize(QSize(22, 22))
        self.buyagainbutton = QPushButton(self.frame_homepage)
        self.buyagainbutton.setObjectName(u"buyagainbutton")
        self.buyagainbutton.setGeometry(QRect(550, 290, 179, 40))
        self.buyagainbutton.setStyleSheet(u"QPushButton{\n"
"border-radius: 10px;\n"
"                border: 1px solid #000;\n"
"                opacity: 0.1;\n"
"                background-color: #F7F2EB;\n"
"                color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 20px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: #FAF9F6;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/pic/images/newres/buyagain.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buyagainbutton.setIcon(icon2)
        self.buyagainbutton.setIconSize(QSize(18, 18))
        self.bestsellingbutton = QPushButton(self.frame_homepage)
        self.bestsellingbutton.setObjectName(u"bestsellingbutton")
        self.bestsellingbutton.setGeometry(QRect(790, 290, 179, 40))
        self.bestsellingbutton.setStyleSheet(u"QPushButton{\n"
"border-radius: 10px;\n"
"                border: 1px solid #000;\n"
"                opacity: 0.1;\n"
"                background-color: #F7F2EB;\n"
"                color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 20px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: #FAF9F6;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/pic/images/newres/bestselling.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bestsellingbutton.setIcon(icon3)
        self.bestsellingbutton.setIconSize(QSize(18, 20))
        self.suggestlabel = QLabel(self.frame_homepage)
        self.suggestlabel.setObjectName(u"suggestlabel")
        self.suggestlabel.setGeometry(QRect(60, 390, 201, 41))
        self.suggestlabel.setStyleSheet(u"color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 32px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.frame_homepage_product = QFrame(self.frame_homepage)
        self.frame_homepage_product.setObjectName(u"frame_homepage_product")
        self.frame_homepage_product.setGeometry(QRect(60, 460, 911, 380))
        self.frame_homepage_product.setMinimumSize(QSize(911, 380))
        self.frame_homepage_product.setMaximumSize(QSize(911, 16777215))
        self.frame_homepage_product.setFrameShape(QFrame.StyledPanel)
        self.frame_homepage_product.setFrameShadow(QFrame.Raised)
        self.scrollArea_homepage.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget_main.addWidget(self.homepage)
        self.cartpage = QWidget()
        self.cartpage.setObjectName(u"cartpage")
        self.gridLayout_11 = QGridLayout(self.cartpage)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.scrollArea_cart = QScrollArea(self.cartpage)
        self.scrollArea_cart.setObjectName(u"scrollArea_cart")
        self.scrollArea_cart.setMinimumSize(QSize(0, 593))
        self.scrollArea_cart.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_cart.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1013, 593))
        self.scrollAreaWidgetContents_4.setMinimumSize(QSize(0, 320))
        self.frame_cartpage = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_cartpage.setObjectName(u"frame_cartpage")
        self.frame_cartpage.setGeometry(QRect(9, 9, 995, 441))
        self.frame_cartpage.setMinimumSize(QSize(995, 320))
        self.frame_cartpage.setMaximumSize(QSize(995, 16777215))
        self.frame_cartpage.setFrameShape(QFrame.StyledPanel)
        self.frame_cartpage.setFrameShadow(QFrame.Raised)
        self.gridLayout_cartpage = QGridLayout(self.frame_cartpage)
        self.gridLayout_cartpage.setObjectName(u"gridLayout_cartpage")
        self.gridLayout_cartpage.setHorizontalSpacing(10)
        self.gridLayout_cartpage.setVerticalSpacing(35)
        self.gridLayout_cartpage.setContentsMargins(40, 0, 60, 16)
        self.cartlabel = QLabel(self.frame_cartpage)
        self.cartlabel.setObjectName(u"cartlabel")
        self.cartlabel.setMinimumSize(QSize(911, 21))
        self.cartlabel.setMaximumSize(QSize(911, 21))
        self.cartlabel.setStyleSheet(u"font-size: 24px;\n"
"font-weight: 700;")

        self.gridLayout_cartpage.addWidget(self.cartlabel, 0, 0, 1, 2)

        self.frame_cartshop = QFrame(self.frame_cartpage)
        self.frame_cartshop.setObjectName(u"frame_cartshop")
        self.frame_cartshop.setMinimumSize(QSize(911, 289))
        self.frame_cartshop.setMaximumSize(QSize(911, 16777215))
        self.frame_cartshop.setFrameShape(QFrame.StyledPanel)
        self.frame_cartshop.setFrameShadow(QFrame.Raised)
        self.verticalLayout_cartshop = QVBoxLayout(self.frame_cartshop)
        self.verticalLayout_cartshop.setSpacing(11)
        self.verticalLayout_cartshop.setObjectName(u"verticalLayout_cartshop")
        self.verticalLayout_cartshop.setContentsMargins(0, 0, 0, 17)

        self.gridLayout_cartpage.addWidget(self.frame_cartshop, 1, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_cartpage.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.horizontalSpacer_36 = QSpacerItem(724, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_cartpage.addItem(self.horizontalSpacer_36, 3, 0, 1, 1)

        self.purchaseallcartbutton = QPushButton(self.frame_cartpage)
        self.purchaseallcartbutton.setObjectName(u"purchaseallcartbutton")
        self.purchaseallcartbutton.setMinimumSize(QSize(156, 42))
        self.purchaseallcartbutton.setMaximumSize(QSize(156, 42))
        self.purchaseallcartbutton.setStyleSheet(u"color: #FFF;\n"
"background-color: #AEC289;\n"
"border: none;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border-radius: 5px;")

        self.gridLayout_cartpage.addWidget(self.purchaseallcartbutton, 3, 1, 1, 1)

        self.scrollArea_cart.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_11.addWidget(self.scrollArea_cart, 0, 0, 1, 1)

        self.stackedWidget_main.addWidget(self.cartpage)
        self.favpage = QWidget()
        self.favpage.setObjectName(u"favpage")
        self.favpage.setStyleSheet(u"favpage")
        self.scrollArea_favpage = QScrollArea(self.favpage)
        self.scrollArea_favpage.setObjectName(u"scrollArea_favpage")
        self.scrollArea_favpage.setGeometry(QRect(-1, -1, 1021, 611))
        self.scrollArea_favpage.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_favpage.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1006, 1000))
        self.scrollAreaWidgetContents_2.setMinimumSize(QSize(0, 1000))
        self.frame_favpage = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_favpage.setObjectName(u"frame_favpage")
        self.frame_favpage.setGeometry(QRect(-1, -1, 1031, 611))
        self.frame_favpage.setFrameShape(QFrame.StyledPanel)
        self.frame_favpage.setFrameShadow(QFrame.Raised)
        self.product_7 = QWidget(self.frame_favpage)
        self.product_7.setObjectName(u"product_7")
        self.product_7.setGeometry(QRect(720, 520, 251, 320))
        self.product_7.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1_12 = QPushButton(self.product_7)
        self.picproduct1_12.setObjectName(u"picproduct1_12")
        self.picproduct1_12.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_12.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_8 = QWidget(self.frame_favpage)
        self.product_8.setObjectName(u"product_8")
        self.product_8.setGeometry(QRect(60, 120, 251, 320))
        self.product_8.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1_6 = QPushButton(self.product_8)
        self.picproduct1_6.setObjectName(u"picproduct1_6")
        self.picproduct1_6.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_6.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_9 = QWidget(self.frame_favpage)
        self.product_9.setObjectName(u"product_9")
        self.product_9.setGeometry(QRect(720, 120, 251, 320))
        self.product_9.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1_7 = QPushButton(self.product_9)
        self.picproduct1_7.setObjectName(u"picproduct1_7")
        self.picproduct1_7.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_7.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_10 = QWidget(self.frame_favpage)
        self.product_10.setObjectName(u"product_10")
        self.product_10.setGeometry(QRect(390, 120, 251, 320))
        self.product_10.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1_8 = QPushButton(self.product_10)
        self.picproduct1_8.setObjectName(u"picproduct1_8")
        self.picproduct1_8.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_8.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_11 = QWidget(self.frame_favpage)
        self.product_11.setObjectName(u"product_11")
        self.product_11.setGeometry(QRect(390, 520, 251, 320))
        self.product_11.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1_13 = QPushButton(self.product_11)
        self.picproduct1_13.setObjectName(u"picproduct1_13")
        self.picproduct1_13.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_13.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_12 = QWidget(self.frame_favpage)
        self.product_12.setObjectName(u"product_12")
        self.product_12.setGeometry(QRect(60, 520, 251, 320))
        self.product_12.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1_14 = QPushButton(self.product_12)
        self.picproduct1_14.setObjectName(u"picproduct1_14")
        self.picproduct1_14.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_14.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.suggestlabel_2 = QLabel(self.frame_favpage)
        self.suggestlabel_2.setObjectName(u"suggestlabel_2")
        self.suggestlabel_2.setGeometry(QRect(60, 10, 201, 41))
        self.suggestlabel_2.setStyleSheet(u"color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 32px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.scrollArea_favpage.setWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget_main.addWidget(self.favpage)
        self.myorderspage = QWidget()
        self.myorderspage.setObjectName(u"myorderspage")
        self.myordersnavcontainer = QWidget(self.myorderspage)
        self.myordersnavcontainer.setObjectName(u"myordersnavcontainer")
        self.myordersnavcontainer.setGeometry(QRect(0, 0, 1031, 139))
        self.myordersnavcontainer.setStyleSheet(u"background-color: #FAF9F6;")
        self.myorderslabel = QLabel(self.myordersnavcontainer)
        self.myorderslabel.setObjectName(u"myorderslabel")
        self.myorderslabel.setGeometry(QRect(60, 0, 180, 51))
        self.myorderslabel.setStyleSheet(u"color: #545454;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.tobeshippedbutton = QPushButton(self.myordersnavcontainer)
        self.tobeshippedbutton.setObjectName(u"tobeshippedbutton")
        self.tobeshippedbutton.setGeometry(QRect(60, 85, 320, 50))
        self.tobeshippedbutton.setStyleSheet(u"QPushButton{\n"
"	color: #CD4662;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border: none;\n"
"border-bottom: 3px solid #CD4662;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #F4DBDB;\n"
"	color: #545454;\n"
"border: none;\n"
"}\n"
"\n"
"")
        self.toberecievedbutton = QPushButton(self.myordersnavcontainer)
        self.toberecievedbutton.setObjectName(u"toberecievedbutton")
        self.toberecievedbutton.setGeometry(QRect(382, 85, 320, 50))
        self.toberecievedbutton.setStyleSheet(u"QPushButton{\n"
"	color: #545454;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #F4DBDB;\n"
"	color: #545454;\n"
"}\n"
"\n"
"")
        self.completedbutton = QPushButton(self.myordersnavcontainer)
        self.completedbutton.setObjectName(u"completedbutton")
        self.completedbutton.setGeometry(QRect(704, 85, 320, 50))
        self.completedbutton.setStyleSheet(u"QPushButton{\n"
"	color: #545454;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #F4DBDB;\n"
"	color: #545454;\n"
"}")
        self.stackedWidget_myorders = QStackedWidget(self.myorderspage)
        self.stackedWidget_myorders.setObjectName(u"stackedWidget_myorders")
        self.stackedWidget_myorders.setGeometry(QRect(0, 140, 1031, 471))
        self.stackedWidget_myorders.setStyleSheet(u"border: none;")
        self.tobeshippedpage = QWidget()
        self.tobeshippedpage.setObjectName(u"tobeshippedpage")
        self.scrollArea_tobeshipped = QScrollArea(self.tobeshippedpage)
        self.scrollArea_tobeshipped.setObjectName(u"scrollArea_tobeshipped")
        self.scrollArea_tobeshipped.setGeometry(QRect(0, 0, 1031, 471))
        self.scrollArea_tobeshipped.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_tobeshipped.setWidgetResizable(True)
        self.scrollAreaWidgetContents_tobeshipped = QWidget()
        self.scrollAreaWidgetContents_tobeshipped.setObjectName(u"scrollAreaWidgetContents_tobeshipped")
        self.scrollAreaWidgetContents_tobeshipped.setGeometry(QRect(0, 0, 1031, 471))
        self.scrollAreaWidgetContents_tobeshipped.setMinimumSize(QSize(0, 300))
        self.frame_tobeshipped = QFrame(self.scrollAreaWidgetContents_tobeshipped)
        self.frame_tobeshipped.setObjectName(u"frame_tobeshipped")
        self.frame_tobeshipped.setGeometry(QRect(0, 0, 1031, 300))
        self.frame_tobeshipped.setMinimumSize(QSize(1031, 300))
        self.frame_tobeshipped.setMaximumSize(QSize(1031, 16777215))
        self.frame_tobeshipped.setFrameShape(QFrame.StyledPanel)
        self.frame_tobeshipped.setFrameShadow(QFrame.Raised)
        self.verticalLayout_shiporder = QVBoxLayout(self.frame_tobeshipped)
        self.verticalLayout_shiporder.setObjectName(u"verticalLayout_shiporder")
        self.verticalLayout_shiporder.setContentsMargins(60, 0, -1, -1)
        self.scrollArea_tobeshipped.setWidget(self.scrollAreaWidgetContents_tobeshipped)
        self.stackedWidget_myorders.addWidget(self.tobeshippedpage)
        self.toberecievedpage = QWidget()
        self.toberecievedpage.setObjectName(u"toberecievedpage")
        self.scrollArea_toberecieved = QScrollArea(self.toberecievedpage)
        self.scrollArea_toberecieved.setObjectName(u"scrollArea_toberecieved")
        self.scrollArea_toberecieved.setGeometry(QRect(0, 0, 1031, 471))
        self.scrollArea_toberecieved.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_toberecieved.setWidgetResizable(True)
        self.scrollAreaWidgetContents_toberecieved = QWidget()
        self.scrollAreaWidgetContents_toberecieved.setObjectName(u"scrollAreaWidgetContents_toberecieved")
        self.scrollAreaWidgetContents_toberecieved.setGeometry(QRect(0, 0, 1016, 500))
        self.scrollAreaWidgetContents_toberecieved.setMinimumSize(QSize(0, 500))
        self.frame_toberecieved = QFrame(self.scrollAreaWidgetContents_toberecieved)
        self.frame_toberecieved.setObjectName(u"frame_toberecieved")
        self.frame_toberecieved.setGeometry(QRect(0, 0, 1031, 471))
        self.frame_toberecieved.setFrameShape(QFrame.StyledPanel)
        self.frame_toberecieved.setFrameShadow(QFrame.Raised)
        self.receiveordercontainer = QWidget(self.frame_toberecieved)
        self.receiveordercontainer.setObjectName(u"receiveordercontainer")
        self.receiveordercontainer.setGeometry(QRect(41, 0, 912, 269))
        self.receiveordercontainer.setStyleSheet(u"border-bottom: 1px solid #CD4662;\n"
"background: #FAF9F6;\n"
"")
        self.shopnameforcart_3 = QLabel(self.receiveordercontainer)
        self.shopnameforcart_3.setObjectName(u"shopnameforcart_3")
        self.shopnameforcart_3.setGeometry(QRect(43, 0, 131, 41))
        self.shopnameforcart_3.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.cartorderpic_3 = QLabel(self.receiveordercontainer)
        self.cartorderpic_3.setObjectName(u"cartorderpic_3")
        self.cartorderpic_3.setGeometry(QRect(43, 51, 134, 134))
        self.cartorderpic_3.setStyleSheet(u"border: none;\n"
"border-radius: 70px;\n"
"background: #cd4662;")
        self.productcartname_3 = QLabel(self.receiveordercontainer)
        self.productcartname_3.setObjectName(u"productcartname_3")
        self.productcartname_3.setGeometry(QRect(240, 51, 672, 28))
        self.productcartname_3.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.productcartdescrip_3 = QLabel(self.receiveordercontainer)
        self.productcartdescrip_3.setObjectName(u"productcartdescrip_3")
        self.productcartdescrip_3.setGeometry(QRect(240, 104, 672, 28))
        self.productcartdescrip_3.setStyleSheet(u"border: none;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.productnum_3 = QLabel(self.receiveordercontainer)
        self.productnum_3.setObjectName(u"productnum_3")
        self.productnum_3.setGeometry(QRect(240, 157, 672, 28))
        self.productnum_3.setStyleSheet(u"border: none;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.totalpricecartlabel_3 = QLabel(self.receiveordercontainer)
        self.totalpricecartlabel_3.setObjectName(u"totalpricecartlabel_3")
        self.totalpricecartlabel_3.setGeometry(QRect(700, 157, 81, 28))
        self.totalpricecartlabel_3.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.totalpricecartnumlabel_3 = QLabel(self.receiveordercontainer)
        self.totalpricecartnumlabel_3.setObjectName(u"totalpricecartnumlabel_3")
        self.totalpricecartnumlabel_3.setGeometry(QRect(850, 157, 49, 28))
        self.totalpricecartnumlabel_3.setStyleSheet(u"border: none;\n"
"color: #cd4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.checkstatusreceivebutton = QPushButton(self.receiveordercontainer)
        self.checkstatusreceivebutton.setObjectName(u"checkstatusreceivebutton")
        self.checkstatusreceivebutton.setGeometry(QRect(757, 210, 156, 42))
        self.checkstatusreceivebutton.setStyleSheet(u"color: #FFF;\n"
"background-color: #cd4662;\n"
"border: none;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border-radius: 5px;")
        self.scrollArea_toberecieved.setWidget(self.scrollAreaWidgetContents_toberecieved)
        self.stackedWidget_myorders.addWidget(self.toberecievedpage)
        self.completedpage = QWidget()
        self.completedpage.setObjectName(u"completedpage")
        self.scrollArea_completed = QScrollArea(self.completedpage)
        self.scrollArea_completed.setObjectName(u"scrollArea_completed")
        self.scrollArea_completed.setGeometry(QRect(0, 0, 1031, 471))
        self.scrollArea_completed.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_completed.setWidgetResizable(True)
        self.scrollAreaWidgetContents_completed = QWidget()
        self.scrollAreaWidgetContents_completed.setObjectName(u"scrollAreaWidgetContents_completed")
        self.scrollAreaWidgetContents_completed.setGeometry(QRect(0, 0, 1016, 500))
        self.scrollAreaWidgetContents_completed.setMinimumSize(QSize(0, 500))
        self.frame_completed = QFrame(self.scrollAreaWidgetContents_completed)
        self.frame_completed.setObjectName(u"frame_completed")
        self.frame_completed.setGeometry(QRect(0, 0, 1031, 471))
        self.frame_completed.setFrameShape(QFrame.StyledPanel)
        self.frame_completed.setFrameShadow(QFrame.Raised)
        self.completeordercontainer = QWidget(self.frame_completed)
        self.completeordercontainer.setObjectName(u"completeordercontainer")
        self.completeordercontainer.setGeometry(QRect(41, 0, 912, 269))
        self.completeordercontainer.setStyleSheet(u"border-bottom: 1px solid #CD4662;\n"
"background: #FAF9F6;\n"
"")
        self.shopnameforcart_4 = QLabel(self.completeordercontainer)
        self.shopnameforcart_4.setObjectName(u"shopnameforcart_4")
        self.shopnameforcart_4.setGeometry(QRect(43, 0, 131, 41))
        self.shopnameforcart_4.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.cartorderpic_4 = QLabel(self.completeordercontainer)
        self.cartorderpic_4.setObjectName(u"cartorderpic_4")
        self.cartorderpic_4.setGeometry(QRect(43, 51, 134, 134))
        self.cartorderpic_4.setStyleSheet(u"border: none;\n"
"border-radius: 70px;\n"
"background: #cd4662;")
        self.productcartname_4 = QLabel(self.completeordercontainer)
        self.productcartname_4.setObjectName(u"productcartname_4")
        self.productcartname_4.setGeometry(QRect(240, 51, 672, 28))
        self.productcartname_4.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.productcartdescrip_4 = QLabel(self.completeordercontainer)
        self.productcartdescrip_4.setObjectName(u"productcartdescrip_4")
        self.productcartdescrip_4.setGeometry(QRect(240, 104, 672, 28))
        self.productcartdescrip_4.setStyleSheet(u"border: none;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.productnum_4 = QLabel(self.completeordercontainer)
        self.productnum_4.setObjectName(u"productnum_4")
        self.productnum_4.setGeometry(QRect(240, 157, 672, 28))
        self.productnum_4.setStyleSheet(u"border: none;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.totalpricecartlabel_4 = QLabel(self.completeordercontainer)
        self.totalpricecartlabel_4.setObjectName(u"totalpricecartlabel_4")
        self.totalpricecartlabel_4.setGeometry(QRect(700, 157, 81, 28))
        self.totalpricecartlabel_4.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.totalpricecartnumlabel_4 = QLabel(self.completeordercontainer)
        self.totalpricecartnumlabel_4.setObjectName(u"totalpricecartnumlabel_4")
        self.totalpricecartnumlabel_4.setGeometry(QRect(850, 157, 49, 28))
        self.totalpricecartnumlabel_4.setStyleSheet(u"border: none;\n"
"color: #cd4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.buyagaincompletebutton = QPushButton(self.completeordercontainer)
        self.buyagaincompletebutton.setObjectName(u"buyagaincompletebutton")
        self.buyagaincompletebutton.setGeometry(QRect(757, 210, 156, 42))
        self.buyagaincompletebutton.setStyleSheet(u"color: #FFF;\n"
"background-color: #cd4662;\n"
"border: none;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border-radius: 5px;")
        self.scrollArea_completed.setWidget(self.scrollAreaWidgetContents_completed)
        self.stackedWidget_myorders.addWidget(self.completedpage)
        self.stackedWidget_main.addWidget(self.myorderspage)
        self.productviewpage = QWidget()
        self.productviewpage.setObjectName(u"productviewpage")
        self.verticalLayout_11 = QVBoxLayout(self.productviewpage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scrollArea_productviewpage = QScrollArea(self.productviewpage)
        self.scrollArea_productviewpage.setObjectName(u"scrollArea_productviewpage")
        self.scrollArea_productviewpage.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_productviewpage.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 67, 1300))
        self.scrollAreaWidgetContents_9.setMinimumSize(QSize(0, 1300))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_productviewpage = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_productviewpage.setObjectName(u"frame_productviewpage")
        self.frame_productviewpage.setMinimumSize(QSize(0, 1300))
        self.frame_productviewpage.setStyleSheet(u"background-color: #FAF9F6;")
        self.frame_productviewpage.setFrameShape(QFrame.StyledPanel)
        self.frame_productviewpage.setFrameShadow(QFrame.Raised)
        self.productcontainer = QWidget(self.frame_productviewpage)
        self.productcontainer.setObjectName(u"productcontainer")
        self.productcontainer.setGeometry(QRect(46, 0, 910, 700))
        self.productcontainer.setStyleSheet(u"background-color: #FAF9F6;\n"
"border-radius: 10px 10px 0px 0px;")
        self.mainpic = QLabel(self.productcontainer)
        self.mainpic.setObjectName(u"mainpic")
        self.mainpic.setGeometry(QRect(47, 34, 352, 352))
        self.mainpic.setStyleSheet(u"\n"
"background-color: #D9D9D9;")
        self.mainpic.setAlignment(Qt.AlignCenter)
        self.productname = QLabel(self.productcontainer)
        self.productname.setObjectName(u"productname")
        self.productname.setGeometry(QRect(534, 24, 281, 41))
        self.productname.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"background-color: red;\n"
"background-color: #FAF9F6;")
        self.buynowbutton = QPushButton(self.productcontainer)
        self.buynowbutton.setObjectName(u"buynowbutton")
        self.buynowbutton.setGeometry(QRect(726, 420, 160, 38))
        self.buynowbutton.setMinimumSize(QSize(160, 38))
        self.buynowbutton.setMaximumSize(QSize(160, 38))
        self.buynowbutton.setStyleSheet(u"border-radius: 19px;\n"
"background-color: #CD4662;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"")
        self.addtocartbutton = QPushButton(self.productcontainer)
        self.addtocartbutton.setObjectName(u"addtocartbutton")
        self.addtocartbutton.setGeometry(QRect(534, 420, 160, 38))
        self.addtocartbutton.setMinimumSize(QSize(160, 38))
        self.addtocartbutton.setMaximumSize(QSize(160, 38))
        self.addtocartbutton.setStyleSheet(u"border-radius: 19px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4DBDB;\n"
"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.shopprofile = QLabel(self.productcontainer)
        self.shopprofile.setObjectName(u"shopprofile")
        self.shopprofile.setGeometry(QRect(47, 540, 120, 120))
        self.shopprofile.setStyleSheet(u"background-color: #D9D9D9;\n"
"border-radius: 60px;")
        self.shopname = QLabel(self.productcontainer)
        self.shopname.setObjectName(u"shopname")
        self.shopname.setGeometry(QRect(210, 540, 201, 21))
        self.shopname.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.shopfollower = QLabel(self.productcontainer)
        self.shopfollower.setObjectName(u"shopfollower")
        self.shopfollower.setGeometry(QRect(210, 580, 277, 21))
        self.shopfollower.setStyleSheet(u"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.star1 = QLabel(self.productcontainer)
        self.star1.setObjectName(u"star1")
        self.star1.setGeometry(QRect(534, 110, 21, 21))
        self.star1.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star2 = QLabel(self.productcontainer)
        self.star2.setObjectName(u"star2")
        self.star2.setGeometry(QRect(555, 110, 21, 21))
        self.star2.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star3 = QLabel(self.productcontainer)
        self.star3.setObjectName(u"star3")
        self.star3.setGeometry(QRect(576, 110, 21, 21))
        self.star3.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star4 = QLabel(self.productcontainer)
        self.star4.setObjectName(u"star4")
        self.star4.setGeometry(QRect(597, 110, 21, 21))
        self.star4.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star5 = QLabel(self.productcontainer)
        self.star5.setObjectName(u"star5")
        self.star5.setGeometry(QRect(618, 110, 21, 21))
        self.star5.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.numberofstar = QLabel(self.productcontainer)
        self.numberofstar.setObjectName(u"numberofstar")
        self.numberofstar.setGeometry(QRect(645, 110, 21, 21))
        self.numberofstar.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.numberofsold = QLabel(self.productcontainer)
        self.numberofsold.setObjectName(u"numberofsold")
        self.numberofsold.setGeometry(QRect(710, 110, 101, 21))
        self.numberofsold.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.currencypic = QLabel(self.productcontainer)
        self.currencypic.setObjectName(u"currencypic")
        self.currencypic.setGeometry(QRect(534, 73, 21, 21))
        self.currencypic.setStyleSheet(u"image: url(:/pic/images/baht.png);\n"
"border: none;")
        self.productprice = QLabel(self.productcontainer)
        self.productprice.setObjectName(u"productprice")
        self.productprice.setGeometry(QRect(555, 73, 261, 21))
        self.productprice.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.review_3 = QLabel(self.productcontainer)
        self.review_3.setObjectName(u"review_3")
        self.review_3.setGeometry(QRect(550, 540, 61, 16))
        self.review_3.setStyleSheet(u"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numyearregis_3 = QLabel(self.productcontainer)
        self.numyearregis_3.setObjectName(u"numyearregis_3")
        self.numyearregis_3.setGeometry(QRect(690, 630, 49, 16))
        self.numyearregis_3.setStyleSheet(u"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numyearregis_3.setAlignment(Qt.AlignCenter)
        self.numreview_3 = QLabel(self.productcontainer)
        self.numreview_3.setObjectName(u"numreview_3")
        self.numreview_3.setGeometry(QRect(470, 540, 49, 16))
        self.numreview_3.setStyleSheet(u"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numreview_3.setAlignment(Qt.AlignCenter)
        self.yearregis_3 = QLabel(self.productcontainer)
        self.yearregis_3.setObjectName(u"yearregis_3")
        self.yearregis_3.setGeometry(QRect(750, 630, 141, 16))
        self.yearregis_3.setStyleSheet(u"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.yearregis_3.setAlignment(Qt.AlignCenter)
        self.numproduct_3 = QLabel(self.productcontainer)
        self.numproduct_3.setObjectName(u"numproduct_3")
        self.numproduct_3.setGeometry(QRect(470, 630, 49, 16))
        self.numproduct_3.setStyleSheet(u"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numproduct_3.setAlignment(Qt.AlignCenter)
        self.numsold_3 = QLabel(self.productcontainer)
        self.numsold_3.setObjectName(u"numsold_3")
        self.numsold_3.setGeometry(QRect(690, 540, 49, 16))
        self.numsold_3.setStyleSheet(u"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numsold_3.setAlignment(Qt.AlignCenter)
        self.sold_3 = QLabel(self.productcontainer)
        self.sold_3.setObjectName(u"sold_3")
        self.sold_3.setGeometry(QRect(770, 540, 49, 16))
        self.sold_3.setStyleSheet(u"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.sold_3.setAlignment(Qt.AlignCenter)
        self.product_35 = QLabel(self.productcontainer)
        self.product_35.setObjectName(u"product_35")
        self.product_35.setGeometry(QRect(550, 630, 61, 16))
        self.product_35.setStyleSheet(u"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.frame_sizeoption_productviewpage = QFrame(self.productcontainer)
        self.frame_sizeoption_productviewpage.setObjectName(u"frame_sizeoption_productviewpage")
        self.frame_sizeoption_productviewpage.setGeometry(QRect(534, 160, 372, 231))
        self.frame_sizeoption_productviewpage.setMinimumSize(QSize(372, 231))
        self.frame_sizeoption_productviewpage.setMaximumSize(QSize(372, 16777215))
        self.frame_sizeoption_productviewpage.setFrameShape(QFrame.StyledPanel)
        self.frame_sizeoption_productviewpage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_sizeoption_productviewpage = QVBoxLayout(self.frame_sizeoption_productviewpage)
        self.verticalLayout_sizeoption_productviewpage.setSpacing(0)
        self.verticalLayout_sizeoption_productviewpage.setObjectName(u"verticalLayout_sizeoption_productviewpage")
        self.verticalLayout_sizeoption_productviewpage.setContentsMargins(0, 0, 0, 0)
        self.sizelabel = QLabel(self.frame_sizeoption_productviewpage)
        self.sizelabel.setObjectName(u"sizelabel")
        self.sizelabel.setMinimumSize(QSize(49, 21))
        self.sizelabel.setMaximumSize(QSize(49, 21))
        self.sizelabel.setStyleSheet(u"color:#545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_sizeoption_productviewpage.addWidget(self.sizelabel)

        self.frame_size_productviewpage = QFrame(self.frame_sizeoption_productviewpage)
        self.frame_size_productviewpage.setObjectName(u"frame_size_productviewpage")
        self.frame_size_productviewpage.setMinimumSize(QSize(381, 80))
        self.frame_size_productviewpage.setMaximumSize(QSize(381, 80))
        self.frame_size_productviewpage.setFrameShape(QFrame.StyledPanel)
        self.frame_size_productviewpage.setFrameShadow(QFrame.Raised)
        self.gridLayout_size_productviewpage = QGridLayout(self.frame_size_productviewpage)
        self.gridLayout_size_productviewpage.setObjectName(u"gridLayout_size_productviewpage")
        self.gridLayout_size_productviewpage.setHorizontalSpacing(25)
        self.gridLayout_size_productviewpage.setVerticalSpacing(10)
        self.gridLayout_size_productviewpage.setContentsMargins(0, -1, 0, -1)

        self.verticalLayout_sizeoption_productviewpage.addWidget(self.frame_size_productviewpage)

        self.optionslabel = QLabel(self.frame_sizeoption_productviewpage)
        self.optionslabel.setObjectName(u"optionslabel")
        self.optionslabel.setMinimumSize(QSize(61, 21))
        self.optionslabel.setMaximumSize(QSize(61, 21))
        self.optionslabel.setStyleSheet(u"color:#545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_sizeoption_productviewpage.addWidget(self.optionslabel)

        self.frame_option_productviewpage = QFrame(self.frame_sizeoption_productviewpage)
        self.frame_option_productviewpage.setObjectName(u"frame_option_productviewpage")
        self.frame_option_productviewpage.setMinimumSize(QSize(381, 80))
        self.frame_option_productviewpage.setMaximumSize(QSize(381, 80))
        self.frame_option_productviewpage.setFrameShape(QFrame.StyledPanel)
        self.frame_option_productviewpage.setFrameShadow(QFrame.Raised)
        self.gridLayout_option_productviewpage = QGridLayout(self.frame_option_productviewpage)
        self.gridLayout_option_productviewpage.setObjectName(u"gridLayout_option_productviewpage")
        self.gridLayout_option_productviewpage.setHorizontalSpacing(25)
        self.gridLayout_option_productviewpage.setVerticalSpacing(10)
        self.gridLayout_option_productviewpage.setContentsMargins(0, -1, 0, -1)

        self.verticalLayout_sizeoption_productviewpage.addWidget(self.frame_option_productviewpage)

        self.prevpicbutton = QPushButton(self.productcontainer)
        self.prevpicbutton.setObjectName(u"prevpicbutton")
        self.prevpicbutton.setGeometry(QRect(0, 190, 21, 39))
        icon4 = QIcon()
        icon4.addFile(u":/pic/realimages/backhomoe.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prevpicbutton.setIcon(icon4)
        self.prevpicbutton.setIconSize(QSize(21, 39))
        self.nextpicbutton = QPushButton(self.productcontainer)
        self.nextpicbutton.setObjectName(u"nextpicbutton")
        self.nextpicbutton.setGeometry(QRect(420, 190, 21, 39))
        icon5 = QIcon()
        icon5.addFile(u":/pic/images/newres/rightarrow_pink.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nextpicbutton.setIcon(icon5)
        self.nextpicbutton.setIconSize(QSize(21, 39))
        self.pushButton = QPushButton(self.productcontainer)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(830, 100, 38, 38))
        self.pushButton.setStyleSheet(u"border: none;\n"
"image:url(:/pic/realimages/fav.png)")
        self.descriptionlabel_productviewpage = QLabel(self.frame_productviewpage)
        self.descriptionlabel_productviewpage.setObjectName(u"descriptionlabel_productviewpage")
        self.descriptionlabel_productviewpage.setGeometry(QRect(50, 750, 171, 31))
        self.descriptionlabel_productviewpage.setStyleSheet(u"font-size: 24px;\n"
"font-weight: 400;")
        self.frame_description_productviewpage = QFrame(self.frame_productviewpage)
        self.frame_description_productviewpage.setObjectName(u"frame_description_productviewpage")
        self.frame_description_productviewpage.setGeometry(QRect(50, 800, 901, 481))
        self.frame_description_productviewpage.setFrameShape(QFrame.StyledPanel)
        self.frame_description_productviewpage.setFrameShadow(QFrame.Raised)
        self.descriptioninfolabel_productviewpage = QLabel(self.frame_description_productviewpage)
        self.descriptioninfolabel_productviewpage.setObjectName(u"descriptioninfolabel_productviewpage")
        self.descriptioninfolabel_productviewpage.setGeometry(QRect(0, 10, 901, 471))
        self.descriptioninfolabel_productviewpage.setStyleSheet(u"font-size: 14px;\n"
"border-bottom: 2px solid #CD4662;")
        self.descriptioninfolabel_productviewpage.setTextFormat(Qt.AutoText)
        self.descriptioninfolabel_productviewpage.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.descriptioninfolabel_productviewpage.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.frame_productviewpage)

        self.scrollArea_productviewpage.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_11.addWidget(self.scrollArea_productviewpage)

        self.stackedWidget_main.addWidget(self.productviewpage)
        self.stackedWidget.addWidget(self.main)
        self.purchasepage = QWidget()
        self.purchasepage.setObjectName(u"purchasepage")
        self.purchasepage.setStyleSheet(u"background-color: #FAF9F6;")
        self.stackedWidget_purchase = QStackedWidget(self.purchasepage)
        self.stackedWidget_purchase.setObjectName(u"stackedWidget_purchase")
        self.stackedWidget_purchase.setGeometry(QRect(0, 0, 1280, 720))
        self.stackedWidget_purchase.setStyleSheet(u" QRadioButton{\n"
"                color: #CD4662;\n"
"            }\n"
"                           \n"
"            QRadioButton::indicator {\n"
"                border-radius: 3px;\n"
"                background-color: #F4DBDB;\n"
"                width: 26px;\n"
"                height: 26px;\n"
"                border: none;\n"
"            }\n"
"\n"
"            QRadioButton::indicator:checked {\n"
"                background-color: #CD4662;\n"
"            }\n"
"            QRadioButton::indicator:unchecked {\n"
"                background-color: #F4DBDB;\n"
"            }")
        self.choosingtypeofpurchase = QWidget()
        self.choosingtypeofpurchase.setObjectName(u"choosingtypeofpurchase")
        self.choosingtypeofpurchase.setStyleSheet(u"background-color: #FAF9F6;")
        self.backtocartbutton = QPushButton(self.choosingtypeofpurchase)
        self.backtocartbutton.setObjectName(u"backtocartbutton")
        self.backtocartbutton.setGeometry(QRect(20, 30, 20, 31))
        self.backtocartbutton.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/backhomoe.png);")
        self.textboxeditcontainer_11 = QWidget(self.choosingtypeofpurchase)
        self.textboxeditcontainer_11.setObjectName(u"textboxeditcontainer_11")
        self.textboxeditcontainer_11.setGeometry(QRect(60, 60, 1101, 171))
        self.textboxeditcontainer_11.setStyleSheet(u"border-radius: 20px;\n"
"background: #F4DBDB;")
        self.addressdisplaylabel_2 = QLabel(self.textboxeditcontainer_11)
        self.addressdisplaylabel_2.setObjectName(u"addressdisplaylabel_2")
        self.addressdisplaylabel_2.setGeometry(QRect(470, 10, 160, 51))
        self.addressdisplaylabel_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.addressdisplaylabel_2.setAlignment(Qt.AlignCenter)
        self.fisrtnameaddress_2 = QLabel(self.textboxeditcontainer_11)
        self.fisrtnameaddress_2.setObjectName(u"fisrtnameaddress_2")
        self.fisrtnameaddress_2.setGeometry(QRect(30, 60, 121, 31))
        self.fisrtnameaddress_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.lastnameaddress_2 = QLabel(self.textboxeditcontainer_11)
        self.lastnameaddress_2.setObjectName(u"lastnameaddress_2")
        self.lastnameaddress_2.setGeometry(QRect(410, 60, 101, 31))
        self.lastnameaddress_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.homenumaddress_2 = QLabel(self.textboxeditcontainer_11)
        self.homenumaddress_2.setObjectName(u"homenumaddress_2")
        self.homenumaddress_2.setGeometry(QRect(30, 90, 71, 41))
        self.homenumaddress_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.phoneaddress_2 = QLabel(self.textboxeditcontainer_11)
        self.phoneaddress_2.setObjectName(u"phoneaddress_2")
        self.phoneaddress_2.setGeometry(QRect(760, 60, 61, 31))
        self.phoneaddress_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.firstnameaddressdisplay_2 = QLabel(self.textboxeditcontainer_11)
        self.firstnameaddressdisplay_2.setObjectName(u"firstnameaddressdisplay_2")
        self.firstnameaddressdisplay_2.setGeometry(QRect(180, 60, 121, 31))
        self.firstnameaddressdisplay_2.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.firstnameaddressdisplay_2.setAlignment(Qt.AlignCenter)
        self.phoneaddressdisplay_2 = QLabel(self.textboxeditcontainer_11)
        self.phoneaddressdisplay_2.setObjectName(u"phoneaddressdisplay_2")
        self.phoneaddressdisplay_2.setGeometry(QRect(870, 60, 201, 31))
        self.phoneaddressdisplay_2.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.phoneaddressdisplay_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lastnameaddressdisplay_2 = QLabel(self.textboxeditcontainer_11)
        self.lastnameaddressdisplay_2.setObjectName(u"lastnameaddressdisplay_2")
        self.lastnameaddressdisplay_2.setGeometry(QRect(520, 60, 101, 31))
        self.lastnameaddressdisplay_2.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.lastnameaddressdisplay_2.setAlignment(Qt.AlignCenter)
        self.homenumaddressdisplay_2 = QLabel(self.textboxeditcontainer_11)
        self.homenumaddressdisplay_2.setObjectName(u"homenumaddressdisplay_2")
        self.homenumaddressdisplay_2.setGeometry(QRect(180, 100, 801, 61))
        self.homenumaddressdisplay_2.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.homenumaddressdisplay_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.orderlabel = QLabel(self.choosingtypeofpurchase)
        self.orderlabel.setObjectName(u"orderlabel")
        self.orderlabel.setGeometry(QRect(60, 240, 121, 41))
        self.orderlabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.choosemethodlabel = QLabel(self.choosingtypeofpurchase)
        self.choosemethodlabel.setObjectName(u"choosemethodlabel")
        self.choosemethodlabel.setGeometry(QRect(60, 500, 271, 41))
        self.choosemethodlabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.promptpaybutton = QRadioButton(self.choosingtypeofpurchase)
        self.promptpaybutton.setObjectName(u"promptpaybutton")
        self.promptpaybutton.setGeometry(QRect(60, 560, 131, 31))
        self.promptpaybutton.setStyleSheet(u"QRadioButton::indicator {\n"
"                width: 20px;\n"
"                height: 20px;\n"
"            }\n"
"            QRadioButton {\n"
"                color: #333;\n"
"                font-size: 20px;\n"
"            }\n"
"            QRadioButton::indicator:checked {\n"
"                background-color: #2196F3;\n"
"                border: 1px solid #2196F3;\n"
"            }")
        self.cashdeliverybutton = QRadioButton(self.choosingtypeofpurchase)
        self.cashdeliverybutton.setObjectName(u"cashdeliverybutton")
        self.cashdeliverybutton.setGeometry(QRect(220, 560, 171, 31))
        self.cashdeliverybutton.setStyleSheet(u"QRadioButton::indicator {\n"
"                width: 20px;\n"
"                height: 20px;\n"
"            }\n"
"            QRadioButton {\n"
"                color: #333;\n"
"                font-size: 20px;\n"
"            }\n"
"            QRadioButton::indicator:checked {\n"
"                background-color: #2196F3;\n"
"                border: 1px solid #2196F3;\n"
"            }")
        self.purchasebutton = QPushButton(self.choosingtypeofpurchase)
        self.purchasebutton.setObjectName(u"purchasebutton")
        self.purchasebutton.setGeometry(QRect(1000, 660, 151, 41))
        self.purchasebutton.setStyleSheet(u"color: #FFF;\n"
"background-color: #AEC289;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;\n"
"border-radius: 10px;")
        self.totalpricelabel = QLabel(self.choosingtypeofpurchase)
        self.totalpricelabel.setObjectName(u"totalpricelabel")
        self.totalpricelabel.setGeometry(QRect(880, 610, 121, 41))
        self.totalpricelabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.totalprice = QLabel(self.choosingtypeofpurchase)
        self.totalprice.setObjectName(u"totalprice")
        self.totalprice.setGeometry(QRect(1040, 610, 71, 41))
        self.totalprice.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.pickupstorebutton = QRadioButton(self.choosingtypeofpurchase)
        self.pickupstorebutton.setObjectName(u"pickupstorebutton")
        self.pickupstorebutton.setGeometry(QRect(420, 560, 201, 31))
        self.pickupstorebutton.setStyleSheet(u"QRadioButton::indicator {\n"
"                width: 20px;\n"
"                height: 20px;\n"
"            }\n"
"            QRadioButton {\n"
"                color: #333;\n"
"                font-size: 20px;\n"
"            }\n"
"            QRadioButton::indicator:checked {\n"
"                background-color: #2196F3;\n"
"                border: 1px solid #2196F3;\n"
"            }")
        self.listWidget = QListWidget(self.choosingtypeofpurchase)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(60, 300, 1091, 191))
        self.stackedWidget_purchase.addWidget(self.choosingtypeofpurchase)
        self.purchasecomplete = QWidget()
        self.purchasecomplete.setObjectName(u"purchasecomplete")
        self.purchasecomplete.setStyleSheet(u"background-color: #FAF9F6;")
        self.orderlabel_9 = QLabel(self.purchasecomplete)
        self.orderlabel_9.setObjectName(u"orderlabel_9")
        self.orderlabel_9.setGeometry(QRect(450, 130, 380, 221))
        self.orderlabel_9.setStyleSheet(u"border:none;\n"
"image: url(:/pic/realimages/purchasecomplete.png);\n"
"background-color: #FAF9F6;")
        self.orderlabel_10 = QLabel(self.purchasecomplete)
        self.orderlabel_10.setObjectName(u"orderlabel_10")
        self.orderlabel_10.setGeometry(QRect(390, 420, 500, 81))
        self.orderlabel_10.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 49px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.backtohomebutton = QPushButton(self.purchasecomplete)
        self.backtohomebutton.setObjectName(u"backtohomebutton")
        self.backtohomebutton.setGeometry(QRect(565, 570, 150, 41))
        self.backtohomebutton.setStyleSheet(u"color: #FFF;\n"
"background-color: #AEC289;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;\n"
"border-radius: 10px;")
        self.stackedWidget_purchase.addWidget(self.purchasecomplete)
        self.promppaymethod = QWidget()
        self.promppaymethod.setObjectName(u"promppaymethod")
        self.promppaymethod.setStyleSheet(u"background-color: #FAF9F6;")
        self.backtochoosingtypebutton = QPushButton(self.promppaymethod)
        self.backtochoosingtypebutton.setObjectName(u"backtochoosingtypebutton")
        self.backtochoosingtypebutton.setGeometry(QRect(20, 30, 20, 31))
        self.backtochoosingtypebutton.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/backhomoe.png);")
        self.orderlabel_6 = QLabel(self.promppaymethod)
        self.orderlabel_6.setObjectName(u"orderlabel_6")
        self.orderlabel_6.setGeometry(QRect(480, 40, 121, 41))
        self.orderlabel_6.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.orderlabel_7 = QLabel(self.promppaymethod)
        self.orderlabel_7.setObjectName(u"orderlabel_7")
        self.orderlabel_7.setGeometry(QRect(650, 40, 71, 41))
        self.orderlabel_7.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.orderlabel_8 = QLabel(self.promppaymethod)
        self.orderlabel_8.setObjectName(u"orderlabel_8")
        self.orderlabel_8.setGeometry(QRect(430, 100, 350, 350))
        self.orderlabel_8.setStyleSheet(u"color: #000;\n"
"background: red;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.orderlabel_8.setAlignment(Qt.AlignCenter)
        self.purchasebutton_2 = QPushButton(self.promppaymethod)
        self.purchasebutton_2.setObjectName(u"purchasebutton_2")
        self.purchasebutton_2.setGeometry(QRect(890, 630, 151, 41))
        self.purchasebutton_2.setStyleSheet(u"color: #FFF;\n"
"background-color: #AEC289;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;\n"
"border-radius: 10px;")
        self.orderlabel_11 = QLabel(self.promppaymethod)
        self.orderlabel_11.setObjectName(u"orderlabel_11")
        self.orderlabel_11.setGeometry(QRect(380, 480, 441, 31))
        self.orderlabel_11.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.orderlabel_11.setAlignment(Qt.AlignCenter)
        self.orderlabel_12 = QLabel(self.promppaymethod)
        self.orderlabel_12.setObjectName(u"orderlabel_12")
        self.orderlabel_12.setGeometry(QRect(420, 520, 361, 31))
        self.orderlabel_12.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.orderlabel_12.setAlignment(Qt.AlignCenter)
        self.orderlabel_13 = QLabel(self.promppaymethod)
        self.orderlabel_13.setObjectName(u"orderlabel_13")
        self.orderlabel_13.setGeometry(QRect(420, 550, 321, 31))
        self.orderlabel_13.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.orderlabel_13.setAlignment(Qt.AlignCenter)
        self.orderlabel_14 = QLabel(self.promppaymethod)
        self.orderlabel_14.setObjectName(u"orderlabel_14")
        self.orderlabel_14.setGeometry(QRect(420, 580, 241, 31))
        self.orderlabel_14.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.orderlabel_14.setAlignment(Qt.AlignCenter)
        self.stackedWidget_purchase.addWidget(self.promppaymethod)
        self.stackedWidget.addWidget(self.purchasepage)
        self.adminwidget = QWidget()
        self.adminwidget.setObjectName(u"adminwidget")
        self.gridLayoutWidget_2 = QWidget(self.adminwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(-1, -1, 1281, 721))
        self.gridLayout_adminwidget = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_adminwidget.setObjectName(u"gridLayout_adminwidget")
        self.gridLayout_adminwidget.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_adminwidget = QStackedWidget(self.gridLayoutWidget_2)
        self.stackedWidget_adminwidget.setObjectName(u"stackedWidget_adminwidget")
        self.adminregisterpage = QWidget()
        self.adminregisterpage.setObjectName(u"adminregisterpage")
        self.backbutton_adminregister = QPushButton(self.adminregisterpage)
        self.backbutton_adminregister.setObjectName(u"backbutton_adminregister")
        self.backbutton_adminregister.setGeometry(QRect(20, 30, 20, 31))
        self.backbutton_adminregister.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/backhomoe.png);")
        self.adminregistercontainer = QWidget(self.adminregisterpage)
        self.adminregistercontainer.setObjectName(u"adminregistercontainer")
        self.adminregistercontainer.setGeometry(QRect(60, 60, 1160, 630))
        self.adminregistercontainer.setStyleSheet(u"background: #FAF9F6;")
        self.textboxeditcontainer_2 = QWidget(self.adminregistercontainer)
        self.textboxeditcontainer_2.setObjectName(u"textboxeditcontainer_2")
        self.textboxeditcontainer_2.setGeometry(QRect(300, 0, 830, 600))
        self.textboxeditcontainer_2.setStyleSheet(u"border-radius: 20px;\n"
"background: #F4DBDB;")
        self.shopregisterationlabel = QLabel(self.textboxeditcontainer_2)
        self.shopregisterationlabel.setObjectName(u"shopregisterationlabel")
        self.shopregisterationlabel.setGeometry(QRect(43, 34, 281, 51))
        self.shopregisterationlabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.shopnamelabel = QLabel(self.textboxeditcontainer_2)
        self.shopnamelabel.setObjectName(u"shopnamelabel")
        self.shopnamelabel.setGeometry(QRect(43, 100, 141, 31))
        self.shopnamelabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.fisrtnamelabel_admin = QLabel(self.textboxeditcontainer_2)
        self.fisrtnamelabel_admin.setObjectName(u"fisrtnamelabel_admin")
        self.fisrtnamelabel_admin.setGeometry(QRect(43, 200, 121, 31))
        self.fisrtnamelabel_admin.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.lastnamelabel_admin = QLabel(self.textboxeditcontainer_2)
        self.lastnamelabel_admin.setObjectName(u"lastnamelabel_admin")
        self.lastnamelabel_admin.setGeometry(QRect(40, 300, 121, 31))
        self.lastnamelabel_admin.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.addresslabel_admin = QLabel(self.textboxeditcontainer_2)
        self.addresslabel_admin.setObjectName(u"addresslabel_admin")
        self.addresslabel_admin.setGeometry(QRect(450, 250, 121, 31))
        self.addresslabel_admin.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.phonelabel_admin = QLabel(self.textboxeditcontainer_2)
        self.phonelabel_admin.setObjectName(u"phonelabel_admin")
        self.phonelabel_admin.setGeometry(QRect(43, 400, 121, 31))
        self.phonelabel_admin.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.emaillabel_admin = QLabel(self.textboxeditcontainer_2)
        self.emaillabel_admin.setObjectName(u"emaillabel_admin")
        self.emaillabel_admin.setGeometry(QRect(450, 400, 121, 31))
        self.emaillabel_admin.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.shopnamebox = QLineEdit(self.textboxeditcontainer_2)
        self.shopnamebox.setObjectName(u"shopnamebox")
        self.shopnamebox.setGeometry(QRect(43, 150, 341, 31))
        self.shopnamebox.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.firstnamebox_admin = QLineEdit(self.textboxeditcontainer_2)
        self.firstnamebox_admin.setObjectName(u"firstnamebox_admin")
        self.firstnamebox_admin.setGeometry(QRect(43, 250, 341, 31))
        self.firstnamebox_admin.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.phonebox_admin = QLineEdit(self.textboxeditcontainer_2)
        self.phonebox_admin.setObjectName(u"phonebox_admin")
        self.phonebox_admin.setGeometry(QRect(43, 450, 341, 31))
        self.phonebox_admin.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.lastnamebox_admin = QLineEdit(self.textboxeditcontainer_2)
        self.lastnamebox_admin.setObjectName(u"lastnamebox_admin")
        self.lastnamebox_admin.setGeometry(QRect(40, 350, 341, 31))
        self.lastnamebox_admin.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.emailbox_admin = QLineEdit(self.textboxeditcontainer_2)
        self.emailbox_admin.setObjectName(u"emailbox_admin")
        self.emailbox_admin.setGeometry(QRect(450, 450, 341, 31))
        self.emailbox_admin.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.adminregisterbutton = QPushButton(self.textboxeditcontainer_2)
        self.adminregisterbutton.setObjectName(u"adminregisterbutton")
        self.adminregisterbutton.setGeometry(QRect(590, 530, 201, 41))
        self.adminregisterbutton.setStyleSheet(u"color: #FFF;\n"
"background: #AEC289;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border-radius: 10px;")
        self.descriptionbox_admin = QLineEdit(self.textboxeditcontainer_2)
        self.descriptionbox_admin.setObjectName(u"descriptionbox_admin")
        self.descriptionbox_admin.setGeometry(QRect(450, 150, 341, 81))
        self.descriptionbox_admin.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.shopdescriptionlabel = QLabel(self.textboxeditcontainer_2)
        self.shopdescriptionlabel.setObjectName(u"shopdescriptionlabel")
        self.shopdescriptionlabel.setGeometry(QRect(450, 100, 141, 31))
        self.shopdescriptionlabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.addressbox_admin = QLineEdit(self.textboxeditcontainer_2)
        self.addressbox_admin.setObjectName(u"addressbox_admin")
        self.addressbox_admin.setGeometry(QRect(450, 300, 341, 81))
        self.addressbox_admin.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.editshoppic = QLabel(self.adminregistercontainer)
        self.editshoppic.setObjectName(u"editshoppic")
        self.editshoppic.setGeometry(QRect(40, 0, 160, 160))
        self.editshoppic.setStyleSheet(u"border: none;\n"
"border-radius: 80px;\n"
"background: #cd4662;")
        self.shoplogolabel = QLabel(self.adminregistercontainer)
        self.shoplogolabel.setObjectName(u"shoplogolabel")
        self.shoplogolabel.setGeometry(QRect(40, 190, 171, 41))
        self.shoplogolabel.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.shoplogolabel.setAlignment(Qt.AlignCenter)
        self.stackedWidget_adminwidget.addWidget(self.adminregisterpage)
        self.adminmain = QWidget()
        self.adminmain.setObjectName(u"adminmain")
        self.searchcontainer_adminmain = QWidget(self.adminmain)
        self.searchcontainer_adminmain.setObjectName(u"searchcontainer_adminmain")
        self.searchcontainer_adminmain.setGeometry(QRect(250, 0, 1031, 109))
        self.searchcontainer_adminmain.setStyleSheet(u"background-color: #FAF9F6;")
        self.loginsignoutbutton_admin = QPushButton(self.searchcontainer_adminmain)
        self.loginsignoutbutton_admin.setObjectName(u"loginsignoutbutton_admin")
        self.loginsignoutbutton_admin.setGeometry(QRect(900, 50, 71, 31))
        self.loginsignoutbutton_admin.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginsignoutbutton_admin.setStyleSheet(u"color: #000;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 20px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                border: none;\n"
"				text-align: center;")
        self.profilebutton_admin = QPushButton(self.searchcontainer_adminmain)
        self.profilebutton_admin.setObjectName(u"profilebutton_admin")
        self.profilebutton_admin.setGeometry(QRect(840, 50, 31, 31))
        self.profilebutton_admin.setCursor(QCursor(Qt.PointingHandCursor))
        self.profilebutton_admin.setStyleSheet(u"image: url(:/pic/realimages/profilepic.png);\n"
"border: none;")
        self.profilebutton_admin.setIconSize(QSize(31, 31))
        self.navbar_adminmain = QWidget(self.adminmain)
        self.navbar_adminmain.setObjectName(u"navbar_adminmain")
        self.navbar_adminmain.setGeometry(QRect(0, 0, 249, 719))
        self.navbar_adminmain.setCursor(QCursor(Qt.ArrowCursor))
        self.navbar_adminmain.setStyleSheet(u"background-color: #FAF9F6;")
        self.Logolabel_admin = QLabel(self.navbar_adminmain)
        self.Logolabel_admin.setObjectName(u"Logolabel_admin")
        self.Logolabel_admin.setGeometry(QRect(30, 40, 191, 51))
        self.Logolabel_admin.setStyleSheet(u"font-family: Supermercado;\n"
"                font-size: 36px;\n"
"                font-weight: 700;\n"
"                line-height: normalpx;\n"
"                text-align: center;\n"
"                color: #000000;")
        self.homebutton_admin = QPushButton(self.navbar_adminmain)
        self.homebutton_admin.setObjectName(u"homebutton_admin")
        self.homebutton_admin.setGeometry(QRect(40, 130, 171, 67))
        self.homebutton_admin.setStyleSheet(u"QPushButton{\n"
"	color: #FAF9F6;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 16px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                background-color: #AEC289;\n"
"                border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }\n"
"")
        self.homebutton_admin.setCheckable(True)
        self.homebutton_admin.setAutoExclusive(True)
        self.orderstatusbutton_admin = QPushButton(self.navbar_adminmain)
        self.orderstatusbutton_admin.setObjectName(u"orderstatusbutton_admin")
        self.orderstatusbutton_admin.setGeometry(QRect(40, 240, 171, 67))
        self.orderstatusbutton_admin.setStyleSheet(u"QPushButton{\n"
"	color: #000;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 16px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                background-color: #E1E3E7;\n"
"                border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }")
        self.orderstatusbutton_admin.setCheckable(True)
        self.orderstatusbutton_admin.setAutoExclusive(True)
        self.productsbutton_admin = QPushButton(self.navbar_adminmain)
        self.productsbutton_admin.setObjectName(u"productsbutton_admin")
        self.productsbutton_admin.setGeometry(QRect(40, 350, 171, 67))
        self.productsbutton_admin.setStyleSheet(u"QPushButton{\n"
"	color: #000;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 16px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                background-color: #E1E3E7;\n"
"                border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }")
        self.productsbutton_admin.setCheckable(True)
        self.productsbutton_admin.setAutoExclusive(True)
        self.messbutton_admin = QPushButton(self.navbar_adminmain)
        self.messbutton_admin.setObjectName(u"messbutton_admin")
        self.messbutton_admin.setGeometry(QRect(40, 460, 171, 67))
        self.messbutton_admin.setStyleSheet(u"QPushButton{\n"
"	color: #000;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 16px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                background-color: #E1E3E7;\n"
"                border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }")
        self.messbutton_admin.setCheckable(True)
        self.messbutton_admin.setAutoExclusive(True)
        self.settingbutton_admin = QPushButton(self.navbar_adminmain)
        self.settingbutton_admin.setObjectName(u"settingbutton_admin")
        self.settingbutton_admin.setGeometry(QRect(110, 630, 30, 30))
        self.settingbutton_admin.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingbutton_admin.setStyleSheet(u"image: url(:/pic/realimages/settingpic.png);\n"
"border: none;")
        self.settingbutton_admin.setIconSize(QSize(30, 30))
        self.stackedWidget_adminmain = QStackedWidget(self.adminmain)
        self.stackedWidget_adminmain.setObjectName(u"stackedWidget_adminmain")
        self.stackedWidget_adminmain.setGeometry(QRect(250, 110, 1031, 3000))
        self.homepage_admin = QWidget()
        self.homepage_admin.setObjectName(u"homepage_admin")
        self.scrollArea_homepage_admin = QScrollArea(self.homepage_admin)
        self.scrollArea_homepage_admin.setObjectName(u"scrollArea_homepage_admin")
        self.scrollArea_homepage_admin.setGeometry(QRect(0, 0, 1021, 611))
        self.scrollArea_homepage_admin.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_homepage_admin.setWidgetResizable(True)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 1006, 1118))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_11)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_homepage_admin = QFrame(self.scrollAreaWidgetContents_11)
        self.frame_homepage_admin.setObjectName(u"frame_homepage_admin")
        self.frame_homepage_admin.setMinimumSize(QSize(0, 1100))
        self.frame_homepage_admin.setFrameShape(QFrame.StyledPanel)
        self.frame_homepage_admin.setFrameShadow(QFrame.Raised)
        self.homepage_admin_container_2 = QWidget(self.frame_homepage_admin)
        self.homepage_admin_container_2.setObjectName(u"homepage_admin_container_2")
        self.homepage_admin_container_2.setGeometry(QRect(40, 24, 913, 221))
        self.homepage_admin_container_2.setStyleSheet(u"border-radius: 10px;\n"
"background: #F4F2EF;")
        self.profilepic_admin = QLabel(self.homepage_admin_container_2)
        self.profilepic_admin.setObjectName(u"profilepic_admin")
        self.profilepic_admin.setGeometry(QRect(47, 50, 130, 130))
        self.profilepic_admin.setStyleSheet(u"border: none;\n"
"border-radius: 65px;\n"
"background: #cd4662;")
        self.shopnamelabel_admin = QLabel(self.homepage_admin_container_2)
        self.shopnamelabel_admin.setObjectName(u"shopnamelabel_admin")
        self.shopnamelabel_admin.setGeometry(QRect(213, 93, 171, 41))
        self.shopnamelabel_admin.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.numreviews = QLabel(self.homepage_admin_container_2)
        self.numreviews.setObjectName(u"numreviews")
        self.numreviews.setGeometry(QRect(480, 50, 49, 16))
        self.numreviews.setStyleSheet(u"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numreviews.setAlignment(Qt.AlignCenter)
        self.numreviewlabel = QLabel(self.homepage_admin_container_2)
        self.numreviewlabel.setObjectName(u"numreviewlabel")
        self.numreviewlabel.setGeometry(QRect(560, 50, 61, 16))
        self.numreviewlabel.setStyleSheet(u"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numproducts = QLabel(self.homepage_admin_container_2)
        self.numproducts.setObjectName(u"numproducts")
        self.numproducts.setGeometry(QRect(480, 140, 49, 16))
        self.numproducts.setStyleSheet(u"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numproducts.setAlignment(Qt.AlignCenter)
        self.numproductslebel = QLabel(self.homepage_admin_container_2)
        self.numproductslebel.setObjectName(u"numproductslebel")
        self.numproductslebel.setGeometry(QRect(560, 140, 61, 16))
        self.numproductslebel.setStyleSheet(u"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numsolds = QLabel(self.homepage_admin_container_2)
        self.numsolds.setObjectName(u"numsolds")
        self.numsolds.setGeometry(QRect(680, 50, 49, 16))
        self.numsolds.setStyleSheet(u"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numsolds.setAlignment(Qt.AlignCenter)
        self.numyearregisteredlabel = QLabel(self.homepage_admin_container_2)
        self.numyearregisteredlabel.setObjectName(u"numyearregisteredlabel")
        self.numyearregisteredlabel.setGeometry(QRect(760, 140, 121, 21))
        self.numyearregisteredlabel.setStyleSheet(u"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numyearregisteredlabel.setAlignment(Qt.AlignCenter)
        self.numsoldslabel = QLabel(self.homepage_admin_container_2)
        self.numsoldslabel.setObjectName(u"numsoldslabel")
        self.numsoldslabel.setGeometry(QRect(750, 50, 49, 16))
        self.numsoldslabel.setStyleSheet(u"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numsoldslabel.setAlignment(Qt.AlignCenter)
        self.numyearregistered = QLabel(self.homepage_admin_container_2)
        self.numyearregistered.setObjectName(u"numyearregistered")
        self.numyearregistered.setGeometry(QRect(680, 140, 49, 16))
        self.numyearregistered.setStyleSheet(u"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numyearregistered.setAlignment(Qt.AlignCenter)
        self.orderstatuscontainer_admin = QWidget(self.frame_homepage_admin)
        self.orderstatuscontainer_admin.setObjectName(u"orderstatuscontainer_admin")
        self.orderstatuscontainer_admin.setGeometry(QRect(40, 380, 913, 161))
        self.orderstatuscontainer_admin.setStyleSheet(u"border-bottom: 3px solid #CD4662;\n"
"background: #FAF9F6;\n"
"")
        self.tobeshippedbutton_admin = QPushButton(self.orderstatuscontainer_admin)
        self.tobeshippedbutton_admin.setObjectName(u"tobeshippedbutton_admin")
        self.tobeshippedbutton_admin.setGeometry(QRect(100, 50, 90, 90))
        self.tobeshippedbutton_admin.setStyleSheet(u"image: url(:/pic/images/newres/tobeshipped.png);\n"
"border: none;")
        self.toberevievedbutton_admin = QPushButton(self.orderstatuscontainer_admin)
        self.toberevievedbutton_admin.setObjectName(u"toberevievedbutton_admin")
        self.toberevievedbutton_admin.setGeometry(QRect(300, 50, 90, 90))
        self.toberevievedbutton_admin.setStyleSheet(u"image: url(:/pic/images/newres/toberecieved.png);\n"
"border: none;")
        self.completedbutton_admin = QPushButton(self.orderstatuscontainer_admin)
        self.completedbutton_admin.setObjectName(u"completedbutton_admin")
        self.completedbutton_admin.setGeometry(QRect(500, 50, 90, 90))
        self.completedbutton_admin.setStyleSheet(u"image: url(:/pic/images/newres/completed.png);\n"
"border: none;")
        self.reviewsbutton_admin = QPushButton(self.orderstatuscontainer_admin)
        self.reviewsbutton_admin.setObjectName(u"reviewsbutton_admin")
        self.reviewsbutton_admin.setGeometry(QRect(700, 40, 90, 90))
        self.reviewsbutton_admin.setStyleSheet(u"image: url(:/pic/images/newres/reviews.png);\n"
"border: none;")
        self.allorderstatusbutton_admin = QPushButton(self.orderstatuscontainer_admin)
        self.allorderstatusbutton_admin.setObjectName(u"allorderstatusbutton_admin")
        self.allorderstatusbutton_admin.setGeometry(QRect(730, 0, 181, 24))
        self.allorderstatusbutton_admin.setStyleSheet(u"color:  #CD4662;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.frame_2 = QFrame(self.orderstatuscontainer_admin)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 909, 49))
        self.frame_2.setStyleSheet(u"border: none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.productslabel_admin_2 = QLabel(self.frame_2)
        self.productslabel_admin_2.setObjectName(u"productslabel_admin_2")
        self.productslabel_admin_2.setStyleSheet(u"color: #000;\n"
"border: none;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")

        self.horizontalLayout_5.addWidget(self.productslabel_admin_2)

        self.horizontalSpacer_4 = QSpacerItem(618, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.vieworderstatusbutton_admin = QPushButton(self.frame_2)
        self.vieworderstatusbutton_admin.setObjectName(u"vieworderstatusbutton_admin")
        self.vieworderstatusbutton_admin.setStyleSheet(u"color:  #CD4662;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.vieworderstatusbutton_admin)

        self.productcontainer_admin = QWidget(self.frame_homepage_admin)
        self.productcontainer_admin.setObjectName(u"productcontainer_admin")
        self.productcontainer_admin.setGeometry(QRect(40, 570, 913, 440))
        self.productcontainer_admin.setMinimumSize(QSize(913, 440))
        self.productcontainer_admin.setMaximumSize(QSize(16777215, 16777215))
        self.productcontainer_admin.setStyleSheet(u"border-bottom: 3px solid #CD4662;\n"
"background: #FAF9F6;\n"
"height: auto;")
        self.verticalLayout_33 = QVBoxLayout(self.productcontainer_admin)
        self.verticalLayout_33.setSpacing(6)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 5)
        self.frame = QFrame(self.productcontainer_admin)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(909, 49))
        self.frame.setMaximumSize(QSize(909, 49))
        self.frame.setStyleSheet(u"border: none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.productslabel_admin = QLabel(self.frame)
        self.productslabel_admin.setObjectName(u"productslabel_admin")
        self.productslabel_admin.setStyleSheet(u"color: #000;\n"
"border: none;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")

        self.horizontalLayout_4.addWidget(self.productslabel_admin)

        self.horizontalSpacer_3 = QSpacerItem(618, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.viewallproductbutton_admin = QPushButton(self.frame)
        self.viewallproductbutton_admin.setObjectName(u"viewallproductbutton_admin")
        self.viewallproductbutton_admin.setStyleSheet(u"color:  #CD4662;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.viewallproductbutton_admin)


        self.verticalLayout_33.addWidget(self.frame)

        self.frame_products_admin = QFrame(self.productcontainer_admin)
        self.frame_products_admin.setObjectName(u"frame_products_admin")
        self.frame_products_admin.setMinimumSize(QSize(913, 380))
        self.frame_products_admin.setMaximumSize(QSize(913, 16777215))
        self.frame_products_admin.setStyleSheet(u"border: none;")
        self.frame_products_admin.setFrameShape(QFrame.StyledPanel)
        self.frame_products_admin.setFrameShadow(QFrame.Raised)
        self.gridLayout_products_admin = QGridLayout(self.frame_products_admin)
        self.gridLayout_products_admin.setObjectName(u"gridLayout_products_admin")

        self.verticalLayout_33.addWidget(self.frame_products_admin)

        self.addproduct_admin = QPushButton(self.frame_homepage_admin)
        self.addproduct_admin.setObjectName(u"addproduct_admin")
        self.addproduct_admin.setGeometry(QRect(40, 270, 913, 77))
        self.addproduct_admin.setCursor(QCursor(Qt.PointingHandCursor))
        self.addproduct_admin.setStyleSheet(u"QPushButton {\n"
"	background: #CD4662;\n"
"	color: white;\n"
"	font-size: 24px;\n"
"	border-radius: 10px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/pic/images/newres/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addproduct_admin.setIcon(icon6)
        self.addproduct_admin.setIconSize(QSize(20, 20))

        self.verticalLayout_15.addWidget(self.frame_homepage_admin)

        self.scrollArea_homepage_admin.setWidget(self.scrollAreaWidgetContents_11)
        self.stackedWidget_adminmain.addWidget(self.homepage_admin)
        self.orderstatus_admin = QWidget()
        self.orderstatus_admin.setObjectName(u"orderstatus_admin")
        self.myordersnavcontainer_2 = QWidget(self.orderstatus_admin)
        self.myordersnavcontainer_2.setObjectName(u"myordersnavcontainer_2")
        self.myordersnavcontainer_2.setGeometry(QRect(0, 0, 1031, 139))
        self.myordersnavcontainer_2.setStyleSheet(u"background-color: #FAF9F6;")
        self.myorderslabel_2 = QLabel(self.myordersnavcontainer_2)
        self.myorderslabel_2.setObjectName(u"myorderslabel_2")
        self.myorderslabel_2.setGeometry(QRect(60, 0, 180, 51))
        self.myorderslabel_2.setStyleSheet(u"color: #545454;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.toshipadminbutton = QPushButton(self.myordersnavcontainer_2)
        self.toshipadminbutton.setObjectName(u"toshipadminbutton")
        self.toshipadminbutton.setGeometry(QRect(60, 85, 240, 50))
        self.toshipadminbutton.setStyleSheet(u"QPushButton{\n"
"	color: #CD4662;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border: none;\n"
"border-bottom: 3px solid #CD4662;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #F4DBDB;\n"
"	color: #545454;\n"
"border: none;\n"
"}\n"
"\n"
"")
        self.canceladminvutton = QPushButton(self.myordersnavcontainer_2)
        self.canceladminvutton.setObjectName(u"canceladminvutton")
        self.canceladminvutton.setGeometry(QRect(300, 85, 240, 50))
        self.canceladminvutton.setStyleSheet(u"QPushButton{\n"
"	color: #545454;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #F4DBDB;\n"
"	color: #545454;\n"
"}\n"
"\n"
"")
        self.completedadminbutton = QPushButton(self.myordersnavcontainer_2)
        self.completedadminbutton.setObjectName(u"completedadminbutton")
        self.completedadminbutton.setGeometry(QRect(540, 85, 240, 50))
        self.completedadminbutton.setStyleSheet(u"QPushButton{\n"
"	color: #545454;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #F4DBDB;\n"
"	color: #545454;\n"
"}")
        self.reviewsadminvutton = QPushButton(self.myordersnavcontainer_2)
        self.reviewsadminvutton.setObjectName(u"reviewsadminvutton")
        self.reviewsadminvutton.setGeometry(QRect(780, 85, 240, 50))
        self.reviewsadminvutton.setStyleSheet(u"QPushButton{\n"
"	color: #545454;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #F4DBDB;\n"
"	color: #545454;\n"
"}")
        self.stackedWidget_orderadmin = QStackedWidget(self.orderstatus_admin)
        self.stackedWidget_orderadmin.setObjectName(u"stackedWidget_orderadmin")
        self.stackedWidget_orderadmin.setGeometry(QRect(0, 140, 1031, 471))
        self.stackedWidget_orderadmin.setStyleSheet(u"background-color: #FAF9F6;")
        self.tobeshipadminpage = QWidget()
        self.tobeshipadminpage.setObjectName(u"tobeshipadminpage")
        self.shipordercontainer_2 = QWidget(self.tobeshipadminpage)
        self.shipordercontainer_2.setObjectName(u"shipordercontainer_2")
        self.shipordercontainer_2.setGeometry(QRect(41, 0, 912, 269))
        self.shipordercontainer_2.setStyleSheet(u"border-bottom: 1px solid #CD4662;\n"
"background: #FAF9F6;\n"
"")
        self.tobeshipproductnameadmin = QLabel(self.shipordercontainer_2)
        self.tobeshipproductnameadmin.setObjectName(u"tobeshipproductnameadmin")
        self.tobeshipproductnameadmin.setGeometry(QRect(43, 0, 141, 41))
        self.tobeshipproductnameadmin.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.tobeshipadminpic = QLabel(self.shipordercontainer_2)
        self.tobeshipadminpic.setObjectName(u"tobeshipadminpic")
        self.tobeshipadminpic.setGeometry(QRect(43, 51, 134, 134))
        self.tobeshipadminpic.setStyleSheet(u"border: none;\n"
"border-radius: 70px;\n"
"background: #cd4662;")
        self.tobeshipcustomernameadmin = QLabel(self.shipordercontainer_2)
        self.tobeshipcustomernameadmin.setObjectName(u"tobeshipcustomernameadmin")
        self.tobeshipcustomernameadmin.setGeometry(QRect(240, 51, 672, 28))
        self.tobeshipcustomernameadmin.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.tobeshipordernumadmin = QLabel(self.shipordercontainer_2)
        self.tobeshipordernumadmin.setObjectName(u"tobeshipordernumadmin")
        self.tobeshipordernumadmin.setGeometry(QRect(240, 104, 672, 28))
        self.tobeshipordernumadmin.setStyleSheet(u"border: none;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.tobeshipproductnumadmin = QLabel(self.shipordercontainer_2)
        self.tobeshipproductnumadmin.setObjectName(u"tobeshipproductnumadmin")
        self.tobeshipproductnumadmin.setGeometry(QRect(240, 157, 672, 28))
        self.tobeshipproductnumadmin.setStyleSheet(u"border: none;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.tobeshiptotalpriceadmin = QLabel(self.shipordercontainer_2)
        self.tobeshiptotalpriceadmin.setObjectName(u"tobeshiptotalpriceadmin")
        self.tobeshiptotalpriceadmin.setGeometry(QRect(700, 157, 81, 28))
        self.tobeshiptotalpriceadmin.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.totalpricecartnumlabel_5 = QLabel(self.shipordercontainer_2)
        self.totalpricecartnumlabel_5.setObjectName(u"totalpricecartnumlabel_5")
        self.totalpricecartnumlabel_5.setGeometry(QRect(850, 157, 49, 28))
        self.totalpricecartnumlabel_5.setStyleSheet(u"border: none;\n"
"color: #cd4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.shippedadminbutton = QPushButton(self.shipordercontainer_2)
        self.shippedadminbutton.setObjectName(u"shippedadminbutton")
        self.shippedadminbutton.setGeometry(QRect(757, 210, 156, 42))
        self.shippedadminbutton.setStyleSheet(u"color: #FFF;\n"
"background-color: #cd4662;\n"
"border: none;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border-radius: 5px;")
        self.stackedWidget_orderadmin.addWidget(self.tobeshipadminpage)
        self.canceladminpage = QWidget()
        self.canceladminpage.setObjectName(u"canceladminpage")
        self.shipordercontainer_5 = QWidget(self.canceladminpage)
        self.shipordercontainer_5.setObjectName(u"shipordercontainer_5")
        self.shipordercontainer_5.setGeometry(QRect(41, 0, 912, 269))
        self.shipordercontainer_5.setStyleSheet(u"border-bottom: 1px solid #CD4662;\n"
"background: #FAF9F6;\n"
"")
        self.cancelproductnameadmin_4 = QLabel(self.shipordercontainer_5)
        self.cancelproductnameadmin_4.setObjectName(u"cancelproductnameadmin_4")
        self.cancelproductnameadmin_4.setGeometry(QRect(43, 0, 141, 41))
        self.cancelproductnameadmin_4.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.canceladminpic_4 = QLabel(self.shipordercontainer_5)
        self.canceladminpic_4.setObjectName(u"canceladminpic_4")
        self.canceladminpic_4.setGeometry(QRect(43, 51, 134, 134))
        self.canceladminpic_4.setStyleSheet(u"border: none;\n"
"border-radius: 70px;\n"
"background: #cd4662;")
        self.cancelcustomernameadmin_4 = QLabel(self.shipordercontainer_5)
        self.cancelcustomernameadmin_4.setObjectName(u"cancelcustomernameadmin_4")
        self.cancelcustomernameadmin_4.setGeometry(QRect(240, 51, 672, 28))
        self.cancelcustomernameadmin_4.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.cancelordernumadmin_4 = QLabel(self.shipordercontainer_5)
        self.cancelordernumadmin_4.setObjectName(u"cancelordernumadmin_4")
        self.cancelordernumadmin_4.setGeometry(QRect(240, 104, 672, 28))
        self.cancelordernumadmin_4.setStyleSheet(u"border: none;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.cancelproductnumadmin_4 = QLabel(self.shipordercontainer_5)
        self.cancelproductnumadmin_4.setObjectName(u"cancelproductnumadmin_4")
        self.cancelproductnumadmin_4.setGeometry(QRect(240, 157, 672, 28))
        self.cancelproductnumadmin_4.setStyleSheet(u"border: none;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.canceltotalpriceadmin_4 = QLabel(self.shipordercontainer_5)
        self.canceltotalpriceadmin_4.setObjectName(u"canceltotalpriceadmin_4")
        self.canceltotalpriceadmin_4.setGeometry(QRect(700, 157, 81, 28))
        self.canceltotalpriceadmin_4.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.totalpricecartnumlabel_8 = QLabel(self.shipordercontainer_5)
        self.totalpricecartnumlabel_8.setObjectName(u"totalpricecartnumlabel_8")
        self.totalpricecartnumlabel_8.setGeometry(QRect(850, 157, 49, 28))
        self.totalpricecartnumlabel_8.setStyleSheet(u"border: none;\n"
"color: #cd4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.canceladminbutton_4 = QPushButton(self.shipordercontainer_5)
        self.canceladminbutton_4.setObjectName(u"canceladminbutton_4")
        self.canceladminbutton_4.setGeometry(QRect(757, 210, 156, 42))
        self.canceladminbutton_4.setStyleSheet(u"color: #FFF;\n"
"background-color: #cd4662;\n"
"border: none;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border-radius: 5px;")
        self.stackedWidget_orderadmin.addWidget(self.canceladminpage)
        self.completeadminpage = QWidget()
        self.completeadminpage.setObjectName(u"completeadminpage")
        self.shipordercontainer_4 = QWidget(self.completeadminpage)
        self.shipordercontainer_4.setObjectName(u"shipordercontainer_4")
        self.shipordercontainer_4.setGeometry(QRect(41, 0, 912, 269))
        self.shipordercontainer_4.setStyleSheet(u"border-bottom: 1px solid #CD4662;\n"
"background: #FAF9F6;\n"
"")
        self.completeproductnameadmin_3 = QLabel(self.shipordercontainer_4)
        self.completeproductnameadmin_3.setObjectName(u"completeproductnameadmin_3")
        self.completeproductnameadmin_3.setGeometry(QRect(43, 0, 141, 41))
        self.completeproductnameadmin_3.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.completeadminpic_3 = QLabel(self.shipordercontainer_4)
        self.completeadminpic_3.setObjectName(u"completeadminpic_3")
        self.completeadminpic_3.setGeometry(QRect(43, 51, 134, 134))
        self.completeadminpic_3.setStyleSheet(u"border: none;\n"
"border-radius: 70px;\n"
"background: #cd4662;")
        self.completecustomernameadmin_3 = QLabel(self.shipordercontainer_4)
        self.completecustomernameadmin_3.setObjectName(u"completecustomernameadmin_3")
        self.completecustomernameadmin_3.setGeometry(QRect(240, 51, 672, 28))
        self.completecustomernameadmin_3.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.completeordernumadmin_3 = QLabel(self.shipordercontainer_4)
        self.completeordernumadmin_3.setObjectName(u"completeordernumadmin_3")
        self.completeordernumadmin_3.setGeometry(QRect(240, 104, 672, 28))
        self.completeordernumadmin_3.setStyleSheet(u"border: none;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.completeproductnumadmin_3 = QLabel(self.shipordercontainer_4)
        self.completeproductnumadmin_3.setObjectName(u"completeproductnumadmin_3")
        self.completeproductnumadmin_3.setGeometry(QRect(240, 157, 672, 28))
        self.completeproductnumadmin_3.setStyleSheet(u"border: none;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.completetotalpriceadmin_3 = QLabel(self.shipordercontainer_4)
        self.completetotalpriceadmin_3.setObjectName(u"completetotalpriceadmin_3")
        self.completetotalpriceadmin_3.setGeometry(QRect(700, 157, 81, 28))
        self.completetotalpriceadmin_3.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.totalpricecartnumlabel_7 = QLabel(self.shipordercontainer_4)
        self.totalpricecartnumlabel_7.setObjectName(u"totalpricecartnumlabel_7")
        self.totalpricecartnumlabel_7.setGeometry(QRect(850, 157, 49, 28))
        self.totalpricecartnumlabel_7.setStyleSheet(u"border: none;\n"
"color: #cd4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.completeadminbutton_3 = QPushButton(self.shipordercontainer_4)
        self.completeadminbutton_3.setObjectName(u"completeadminbutton_3")
        self.completeadminbutton_3.setGeometry(QRect(757, 210, 156, 42))
        self.completeadminbutton_3.setStyleSheet(u"color: #FFF;\n"
"background-color: #cd4662;\n"
"border: none;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border-radius: 5px;")
        self.stackedWidget_orderadmin.addWidget(self.completeadminpage)
        self.reviewsadminpage = QWidget()
        self.reviewsadminpage.setObjectName(u"reviewsadminpage")
        self.shipordercontainer_3 = QWidget(self.reviewsadminpage)
        self.shipordercontainer_3.setObjectName(u"shipordercontainer_3")
        self.shipordercontainer_3.setGeometry(QRect(41, 0, 912, 269))
        self.shipordercontainer_3.setStyleSheet(u"border-bottom: 1px solid #CD4662;\n"
"background: #FAF9F6;\n"
"")
        self.reviewproductnameadmin_2 = QLabel(self.shipordercontainer_3)
        self.reviewproductnameadmin_2.setObjectName(u"reviewproductnameadmin_2")
        self.reviewproductnameadmin_2.setGeometry(QRect(43, 0, 141, 41))
        self.reviewproductnameadmin_2.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.reviewadminpic_2 = QLabel(self.shipordercontainer_3)
        self.reviewadminpic_2.setObjectName(u"reviewadminpic_2")
        self.reviewadminpic_2.setGeometry(QRect(43, 51, 134, 134))
        self.reviewadminpic_2.setStyleSheet(u"border: none;\n"
"border-radius: 70px;\n"
"background: #cd4662;")
        self.reviewcustomernameadmin_2 = QLabel(self.shipordercontainer_3)
        self.reviewcustomernameadmin_2.setObjectName(u"reviewcustomernameadmin_2")
        self.reviewcustomernameadmin_2.setGeometry(QRect(240, 51, 672, 28))
        self.reviewcustomernameadmin_2.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.reviewordernumadmin_2 = QLabel(self.shipordercontainer_3)
        self.reviewordernumadmin_2.setObjectName(u"reviewordernumadmin_2")
        self.reviewordernumadmin_2.setGeometry(QRect(240, 104, 672, 28))
        self.reviewordernumadmin_2.setStyleSheet(u"border: none;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.reviewproductnumadmin_2 = QLabel(self.shipordercontainer_3)
        self.reviewproductnumadmin_2.setObjectName(u"reviewproductnumadmin_2")
        self.reviewproductnumadmin_2.setGeometry(QRect(240, 157, 672, 28))
        self.reviewproductnumadmin_2.setStyleSheet(u"border: none;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.reviewtotalpriceadmin_2 = QLabel(self.shipordercontainer_3)
        self.reviewtotalpriceadmin_2.setObjectName(u"reviewtotalpriceadmin_2")
        self.reviewtotalpriceadmin_2.setGeometry(QRect(700, 157, 81, 28))
        self.reviewtotalpriceadmin_2.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.totalpricecartnumlabel_6 = QLabel(self.shipordercontainer_3)
        self.totalpricecartnumlabel_6.setObjectName(u"totalpricecartnumlabel_6")
        self.totalpricecartnumlabel_6.setGeometry(QRect(850, 157, 49, 28))
        self.totalpricecartnumlabel_6.setStyleSheet(u"border: none;\n"
"color: #cd4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.reviewadminbutton_2 = QPushButton(self.shipordercontainer_3)
        self.reviewadminbutton_2.setObjectName(u"reviewadminbutton_2")
        self.reviewadminbutton_2.setGeometry(QRect(757, 210, 156, 42))
        self.reviewadminbutton_2.setStyleSheet(u"color: #FFF;\n"
"background-color: #cd4662;\n"
"border: none;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border-radius: 5px;")
        self.stackedWidget_orderadmin.addWidget(self.reviewsadminpage)
        self.stackedWidget_adminmain.addWidget(self.orderstatus_admin)
        self.productspage_admin = QWidget()
        self.productspage_admin.setObjectName(u"productspage_admin")
        self.stackedWidget_adminproducts = QStackedWidget(self.productspage_admin)
        self.stackedWidget_adminproducts.setObjectName(u"stackedWidget_adminproducts")
        self.stackedWidget_adminproducts.setGeometry(QRect(0, 0, 1031, 611))
        self.stackedWidget_adminproducts.setStyleSheet(u"background: #FAF9F6")
        self.alltypesproductspage_admin = QWidget()
        self.alltypesproductspage_admin.setObjectName(u"alltypesproductspage_admin")
        self.productcontainernav_admin = QWidget(self.alltypesproductspage_admin)
        self.productcontainernav_admin.setObjectName(u"productcontainernav_admin")
        self.productcontainernav_admin.setGeometry(QRect(0, 0, 1031, 139))
        self.productcontainernav_admin.setStyleSheet(u"background-color: #FAF9F6;")
        self.productlabel_admin = QLabel(self.productcontainernav_admin)
        self.productlabel_admin.setObjectName(u"productlabel_admin")
        self.productlabel_admin.setGeometry(QRect(50, 0, 180, 51))
        self.productlabel_admin.setStyleSheet(u"color: #545454;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.allproductbutton_admin = QPushButton(self.productcontainernav_admin)
        self.allproductbutton_admin.setObjectName(u"allproductbutton_admin")
        self.allproductbutton_admin.setGeometry(QRect(50, 90, 455, 50))
        self.allproductbutton_admin.setStyleSheet(u"QPushButton{\n"
"	color: #CD4662;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border: none;\n"
"border-bottom: 3px solid #CD4662;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #F4DBDB;\n"
"	color: #545454;\n"
"border: none;\n"
"}\n"
"\n"
"")
        self.producttypesbutton_admin = QPushButton(self.productcontainernav_admin)
        self.producttypesbutton_admin.setObjectName(u"producttypesbutton_admin")
        self.producttypesbutton_admin.setGeometry(QRect(510, 90, 455, 50))
        self.producttypesbutton_admin.setStyleSheet(u"QPushButton{\n"
"	color: #545454;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #F4DBDB;\n"
"	color: #545454;\n"
"}\n"
"\n"
"")
        self.stackedWidget_allandtype_admin = QStackedWidget(self.alltypesproductspage_admin)
        self.stackedWidget_allandtype_admin.setObjectName(u"stackedWidget_allandtype_admin")
        self.stackedWidget_allandtype_admin.setGeometry(QRect(0, 140, 1031, 471))
        self.adminallproductpage = QWidget()
        self.adminallproductpage.setObjectName(u"adminallproductpage")
        self.verticalLayout_24 = QVBoxLayout(self.adminallproductpage)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.scrollArea_allproduct_admin = QScrollArea(self.adminallproductpage)
        self.scrollArea_allproduct_admin.setObjectName(u"scrollArea_allproduct_admin")
        self.scrollArea_allproduct_admin.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_allproduct_admin.setWidgetResizable(True)
        self.scrollAreaWidgetContents_17 = QWidget()
        self.scrollAreaWidgetContents_17.setObjectName(u"scrollAreaWidgetContents_17")
        self.scrollAreaWidgetContents_17.setGeometry(QRect(0, 0, 998, 471))
        self.verticalLayout_25 = QVBoxLayout(self.scrollAreaWidgetContents_17)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_allproducts_admin = QFrame(self.scrollAreaWidgetContents_17)
        self.frame_allproducts_admin.setObjectName(u"frame_allproducts_admin")
        self.frame_allproducts_admin.setMinimumSize(QSize(0, 453))
        self.frame_allproducts_admin.setFrameShape(QFrame.StyledPanel)
        self.frame_allproducts_admin.setFrameShadow(QFrame.Raised)

        self.verticalLayout_25.addWidget(self.frame_allproducts_admin)

        self.scrollArea_allproduct_admin.setWidget(self.scrollAreaWidgetContents_17)

        self.verticalLayout_24.addWidget(self.scrollArea_allproduct_admin)

        self.stackedWidget_allandtype_admin.addWidget(self.adminallproductpage)
        self.adminproducttypespage = QWidget()
        self.adminproducttypespage.setObjectName(u"adminproducttypespage")
        self.verticalLayout_26 = QVBoxLayout(self.adminproducttypespage)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.scrollArea_producttype_3 = QScrollArea(self.adminproducttypespage)
        self.scrollArea_producttype_3.setObjectName(u"scrollArea_producttype_3")
        self.scrollArea_producttype_3.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_producttype_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_18 = QWidget()
        self.scrollAreaWidgetContents_18.setObjectName(u"scrollAreaWidgetContents_18")
        self.scrollAreaWidgetContents_18.setGeometry(QRect(0, 0, 67, 1518))
        self.verticalLayout_27 = QVBoxLayout(self.scrollAreaWidgetContents_18)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_producttype_3 = QFrame(self.scrollAreaWidgetContents_18)
        self.frame_producttype_3.setObjectName(u"frame_producttype_3")
        self.frame_producttype_3.setMinimumSize(QSize(0, 1500))
        self.frame_producttype_3.setFrameShape(QFrame.StyledPanel)
        self.frame_producttype_3.setFrameShadow(QFrame.Raised)
        self.topwearwidget_3 = QWidget(self.frame_producttype_3)
        self.topwearwidget_3.setObjectName(u"topwearwidget_3")
        self.topwearwidget_3.setGeometry(QRect(30, 52, 911, 99))
        self.topwearwidget_3.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #F4DBDB;\n"
"background: #FAF9F6;")
        self.topwearpic_3 = QLabel(self.topwearwidget_3)
        self.topwearpic_3.setObjectName(u"topwearpic_3")
        self.topwearpic_3.setGeometry(QRect(25, 20, 60, 60))
        self.topwearpic_3.setStyleSheet(u"image: url(:/pic/images/newres/profile.png);\n"
"border: none;")
        self.topwearlabel_3 = QLabel(self.topwearwidget_3)
        self.topwearlabel_3.setObjectName(u"topwearlabel_3")
        self.topwearlabel_3.setGeometry(QRect(120, 8, 263, 81))
        self.topwearlabel_3.setStyleSheet(u"color: #000;\n"
"border: none;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.topwearnum_3 = QLabel(self.topwearwidget_3)
        self.topwearnum_3.setObjectName(u"topwearnum_3")
        self.topwearnum_3.setGeometry(QRect(660, 8, 169, 81))
        self.topwearnum_3.setStyleSheet(u"color: #545454;\n"
"text-align: right;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.topwearnum_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.topwearbutton_3 = QPushButton(self.topwearwidget_3)
        self.topwearbutton_3.setObjectName(u"topwearbutton_3")
        self.topwearbutton_3.setGeometry(QRect(860, 40, 31, 21))
        self.topwearbutton_3.setStyleSheet(u"image: url(:/pic/images/newres/rightarrow_pink.png);\n"
"border: none;")
        self.bottomwidget_3 = QWidget(self.frame_producttype_3)
        self.bottomwidget_3.setObjectName(u"bottomwidget_3")
        self.bottomwidget_3.setGeometry(QRect(30, 176, 911, 99))
        self.bottomwidget_3.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #F4DBDB;\n"
"background: #FAF9F6;\n"
"")
        self.bottomwearpic_3 = QLabel(self.bottomwidget_3)
        self.bottomwearpic_3.setObjectName(u"bottomwearpic_3")
        self.bottomwearpic_3.setGeometry(QRect(25, 20, 60, 60))
        self.bottomwearpic_3.setStyleSheet(u"image: url(:/pic/images/newres/profile.png);\n"
"border: none;")
        self.bottomwearlabel_3 = QLabel(self.bottomwidget_3)
        self.bottomwearlabel_3.setObjectName(u"bottomwearlabel_3")
        self.bottomwearlabel_3.setGeometry(QRect(120, 8, 263, 81))
        self.bottomwearlabel_3.setStyleSheet(u"color: #000;\n"
"border: none;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.bottomwearnum_3 = QLabel(self.bottomwidget_3)
        self.bottomwearnum_3.setObjectName(u"bottomwearnum_3")
        self.bottomwearnum_3.setGeometry(QRect(660, 8, 169, 81))
        self.bottomwearnum_3.setStyleSheet(u"color: #545454;\n"
"text-align: right;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.bottomwearnum_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.bottmwearbutton_3 = QPushButton(self.bottomwidget_3)
        self.bottmwearbutton_3.setObjectName(u"bottmwearbutton_3")
        self.bottmwearbutton_3.setGeometry(QRect(860, 40, 31, 21))
        self.bottmwearbutton_3.setStyleSheet(u"image: url(:/pic/images/newres/rightarrow_pink.png);\n"
"border: none;")
        self.footwearwidget_3 = QWidget(self.frame_producttype_3)
        self.footwearwidget_3.setObjectName(u"footwearwidget_3")
        self.footwearwidget_3.setGeometry(QRect(30, 300, 911, 99))
        self.footwearwidget_3.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #F4DBDB;\n"
"background: #FAF9F6;\n"
"")
        self.footwearpic_3 = QLabel(self.footwearwidget_3)
        self.footwearpic_3.setObjectName(u"footwearpic_3")
        self.footwearpic_3.setGeometry(QRect(25, 20, 60, 60))
        self.footwearpic_3.setStyleSheet(u"image: url(:/pic/images/newres/profile.png);\n"
"border: none;")
        self.footwearlabel_3 = QLabel(self.footwearwidget_3)
        self.footwearlabel_3.setObjectName(u"footwearlabel_3")
        self.footwearlabel_3.setGeometry(QRect(120, 8, 263, 81))
        self.footwearlabel_3.setStyleSheet(u"color: #000;\n"
"border: none;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.footwearnum_3 = QLabel(self.footwearwidget_3)
        self.footwearnum_3.setObjectName(u"footwearnum_3")
        self.footwearnum_3.setGeometry(QRect(660, 8, 169, 81))
        self.footwearnum_3.setStyleSheet(u"color: #545454;\n"
"text-align: right;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.footwearnum_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.footwearbutton_3 = QPushButton(self.footwearwidget_3)
        self.footwearbutton_3.setObjectName(u"footwearbutton_3")
        self.footwearbutton_3.setGeometry(QRect(860, 40, 31, 21))
        self.footwearbutton_3.setStyleSheet(u"image: url(:/pic/images/newres/rightarrow_pink.png);\n"
"border: none;")

        self.verticalLayout_27.addWidget(self.frame_producttype_3)

        self.scrollArea_producttype_3.setWidget(self.scrollAreaWidgetContents_18)

        self.verticalLayout_26.addWidget(self.scrollArea_producttype_3)

        self.stackedWidget_allandtype_admin.addWidget(self.adminproducttypespage)
        self.stackedWidget_adminproducts.addWidget(self.alltypesproductspage_admin)
        self.addproductpage_admin = QWidget()
        self.addproductpage_admin.setObjectName(u"addproductpage_admin")
        self.scrollArea = QScrollArea(self.addproductpage_admin)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 1021, 601))
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 1006, 1400))
        self.scrollAreaWidgetContents_8.setMinimumSize(QSize(0, 1400))
        self.frame_addproduct = QFrame(self.scrollAreaWidgetContents_8)
        self.frame_addproduct.setObjectName(u"frame_addproduct")
        self.frame_addproduct.setGeometry(QRect(39, 11, 961, 1400))
        self.frame_addproduct.setMinimumSize(QSize(0, 1400))
        self.frame_addproduct.setFrameShape(QFrame.StyledPanel)
        self.frame_addproduct.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_addproduct)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.addproductlabel = QLabel(self.frame_addproduct)
        self.addproductlabel.setObjectName(u"addproductlabel")
        self.addproductlabel.setMinimumSize(QSize(890, 21))
        self.addproductlabel.setMaximumSize(QSize(16777215, 20))
        self.addproductlabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")

        self.verticalLayout_14.addWidget(self.addproductlabel)

        self.addimageproductcontainer = QWidget(self.frame_addproduct)
        self.addimageproductcontainer.setObjectName(u"addimageproductcontainer")
        self.addimageproductcontainer.setMinimumSize(QSize(0, 250))
        self.addimageproductcontainer.setMaximumSize(QSize(16777215, 250))
        self.addimageproductcontainer.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"	padding-top: 10px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	height: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-width: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.horizontalLayout_9 = QHBoxLayout(self.addimageproductcontainer)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.scrollArea_addimageproduct = QScrollArea(self.addimageproductcontainer)
        self.scrollArea_addimageproduct.setObjectName(u"scrollArea_addimageproduct")
        self.scrollArea_addimageproduct.setMinimumSize(QSize(0, 240))
        self.scrollArea_addimageproduct.setMaximumSize(QSize(16777215, 240))
        self.scrollArea_addimageproduct.setWidgetResizable(True)
        self.scrollAreaWidgetContents_22 = QWidget()
        self.scrollAreaWidgetContents_22.setObjectName(u"scrollAreaWidgetContents_22")
        self.scrollAreaWidgetContents_22.setGeometry(QRect(0, 0, 1218, 210))
        self.scrollAreaWidgetContents_22.setMinimumSize(QSize(0, 210))
        self.scrollAreaWidgetContents_22.setMaximumSize(QSize(16777215, 210))
        self.horizontalLayout_10 = QHBoxLayout(self.scrollAreaWidgetContents_22)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_addimageproduct = QFrame(self.scrollAreaWidgetContents_22)
        self.frame_addimageproduct.setObjectName(u"frame_addimageproduct")
        self.frame_addimageproduct.setMinimumSize(QSize(1200, 210))
        self.frame_addimageproduct.setMaximumSize(QSize(16777215, 210))
        self.frame_addimageproduct.setFrameShape(QFrame.StyledPanel)
        self.frame_addimageproduct.setFrameShadow(QFrame.Raised)
        self.addproductimagelabel = QLabel(self.frame_addimageproduct)
        self.addproductimagelabel.setObjectName(u"addproductimagelabel")
        self.addproductimagelabel.setGeometry(QRect(0, 0, 220, 31))
        self.addproductimagelabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.addimagebutton = QPushButton(self.frame_addimageproduct)
        self.addimagebutton.setObjectName(u"addimagebutton")
        self.addimagebutton.setGeometry(QRect(0, 45, 151, 151))
        self.addimagebutton.setStyleSheet(u"QPushButton {\n"
"	border: 3px dashed #D9D9D9;\n"
"	font-size: 46px;\n"
"	background: #FAF9F6;\n"
"	color: #D9D9D9;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: #CD4662;\n"
"	color: #CD4662;\n"
"	background-color: #EDEDED;\n"
"}")
        self.addimagebutton.setIconSize(QSize(151, 151))
        self.img_1 = QLabel(self.frame_addimageproduct)
        self.img_1.setObjectName(u"img_1")
        self.img_1.setGeometry(QRect(5, 50, 141, 141))
        self.img_1.setStyleSheet(u"image: url(:/pic/product_img/IMG_2025.JPG)")
        self.img_1.setAlignment(Qt.AlignCenter)
        self.delete_pic_button_1 = QPushButton(self.frame_addimageproduct)
        self.delete_pic_button_1.setObjectName(u"delete_pic_button_1")
        self.delete_pic_button_1.setEnabled(True)
        self.delete_pic_button_1.setGeometry(QRect(130, 30, 31, 32))
        self.delete_pic_button_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_pic_button_1.setAutoFillBackground(False)
        self.delete_pic_button_1.setStyleSheet(u"QPushButton {\n"
"	border-radius: 25px;\n"
"	border-color: rgb(217, 217, 217);\n"
"	border-width: 2px;\n"
"	background: #FAF9F6;\n"
"	color: #D9D9D9;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: #CD4662;\n"
"	color: rgb(116,23,17);\n"
"	background-color: rgb(237,106,94);\n"
"}")

        self.horizontalLayout_10.addWidget(self.frame_addimageproduct)

        self.scrollArea_addimageproduct.setWidget(self.scrollAreaWidgetContents_22)

        self.horizontalLayout_9.addWidget(self.scrollArea_addimageproduct)


        self.verticalLayout_14.addWidget(self.addimageproductcontainer)

        self.addproductnamelabel = QLabel(self.frame_addproduct)
        self.addproductnamelabel.setObjectName(u"addproductnamelabel")
        self.addproductnamelabel.setMinimumSize(QSize(0, 50))
        self.addproductnamelabel.setMaximumSize(QSize(16777215, 50))
        self.addproductnamelabel.setStyleSheet(u"color: #000;\n"
"padding-top: 20px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_14.addWidget(self.addproductnamelabel)

        self.addproductnametextbox = QLineEdit(self.frame_addproduct)
        self.addproductnametextbox.setObjectName(u"addproductnametextbox")
        self.addproductnametextbox.setMaximumSize(QSize(910, 16777215))
        self.addproductnametextbox.setStyleSheet(u"border-radius: 5px;\n"
"background: #EDEDED;\n"
"padding: 5px;\n"
"font-size: 16px;\n"
"")

        self.verticalLayout_14.addWidget(self.addproductnametextbox)

        self.addproductdescriptionlabel = QLabel(self.frame_addproduct)
        self.addproductdescriptionlabel.setObjectName(u"addproductdescriptionlabel")
        self.addproductdescriptionlabel.setMinimumSize(QSize(0, 50))
        self.addproductdescriptionlabel.setMaximumSize(QSize(16777215, 50))
        self.addproductdescriptionlabel.setStyleSheet(u"color: #000;\n"
"padding-top: 20px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_14.addWidget(self.addproductdescriptionlabel)

        self.addproductdescriptiontextbox = QPlainTextEdit(self.frame_addproduct)
        self.addproductdescriptiontextbox.setObjectName(u"addproductdescriptiontextbox")
        self.addproductdescriptiontextbox.setMaximumSize(QSize(910, 117))
        self.addproductdescriptiontextbox.setStyleSheet(u"border-radius: 5px;\n"
"background: #EDEDED;\n"
"padding: 5px;\n"
"font-size: 16px;\n"
"")

        self.verticalLayout_14.addWidget(self.addproductdescriptiontextbox)

        self.addproductpricelabel = QLabel(self.frame_addproduct)
        self.addproductpricelabel.setObjectName(u"addproductpricelabel")
        self.addproductpricelabel.setMinimumSize(QSize(0, 50))
        self.addproductpricelabel.setMaximumSize(QSize(16777215, 50))
        self.addproductpricelabel.setStyleSheet(u"color: #000;\n"
"padding-top: 20px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_14.addWidget(self.addproductpricelabel)

        self.addproductpricespinbox = QSpinBox(self.frame_addproduct)
        self.addproductpricespinbox.setObjectName(u"addproductpricespinbox")
        self.addproductpricespinbox.setMaximumSize(QSize(281, 16777215))
        self.addproductpricespinbox.setStyleSheet(u"QSpinBox {\n"
"	border-radius: 5px;\n"
"	background: #EDEDED;\n"
"	padding: 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QSpinBox::up-button {\n"
"	color: #F4DBDB;\n"
"}")
        self.addproductpricespinbox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.addproductpricespinbox.setMinimum(1)
        self.addproductpricespinbox.setMaximum(10000)

        self.verticalLayout_14.addWidget(self.addproductpricespinbox)

        self.addproductsizelabel = QLabel(self.frame_addproduct)
        self.addproductsizelabel.setObjectName(u"addproductsizelabel")
        self.addproductsizelabel.setMinimumSize(QSize(0, 50))
        self.addproductsizelabel.setMaximumSize(QSize(16777215, 50))
        self.addproductsizelabel.setStyleSheet(u"color: #000;\n"
"padding-top: 20px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_14.addWidget(self.addproductsizelabel)

        self.scrollArea_addsizes = QScrollArea(self.frame_addproduct)
        self.scrollArea_addsizes.setObjectName(u"scrollArea_addsizes")
        self.scrollArea_addsizes.setMinimumSize(QSize(941, 60))
        self.scrollArea_addsizes.setMaximumSize(QSize(941, 40))
        self.scrollArea_addsizes.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	height: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-width: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_addsizes.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 941, 60))
        self.scrollAreaWidgetContents_10.setMinimumSize(QSize(941, 0))
        self.scrollAreaWidgetContents_10.setMaximumSize(QSize(1000, 16777215))
        self.frame_sizes = QFrame(self.scrollAreaWidgetContents_10)
        self.frame_sizes.setObjectName(u"frame_sizes")
        self.frame_sizes.setGeometry(QRect(0, 0, 941, 58))
        self.frame_sizes.setMinimumSize(QSize(941, 40))
        self.frame_sizes.setMaximumSize(QSize(16777215, 16777215))
        self.frame_sizes.setFrameShape(QFrame.StyledPanel)
        self.frame_sizes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_sizes)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.addsizeproductbutton = QPushButton(self.frame_sizes)
        self.addsizeproductbutton.setObjectName(u"addsizeproductbutton")
        self.addsizeproductbutton.setMinimumSize(QSize(108, 38))
        self.addsizeproductbutton.setMaximumSize(QSize(108, 38))
        self.addsizeproductbutton.setStyleSheet(u"QPushButton {\n"
"	border-style: dashed;\n"
"	border-width: 2px;\n"
"	border-color: #D9D9D9;\n"
"	background: none;\n"
"	font-size: 16px;\n"
"	color: #D9D9D9;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: #CD4662;\n"
"	color: #CD4662;\n"
"	background-color: #EDEDED;\n"
"}")

        self.horizontalLayout_2.addWidget(self.addsizeproductbutton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.scrollArea_addsizes.setWidget(self.scrollAreaWidgetContents_10)

        self.verticalLayout_14.addWidget(self.scrollArea_addsizes)

        self.addproductoptionlabel = QLabel(self.frame_addproduct)
        self.addproductoptionlabel.setObjectName(u"addproductoptionlabel")
        self.addproductoptionlabel.setMinimumSize(QSize(0, 40))
        self.addproductoptionlabel.setMaximumSize(QSize(16777215, 40))
        self.addproductoptionlabel.setStyleSheet(u"color: #000;\n"
"padding-top:10px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_14.addWidget(self.addproductoptionlabel)

        self.scrollArea_addoptions = QScrollArea(self.frame_addproduct)
        self.scrollArea_addoptions.setObjectName(u"scrollArea_addoptions")
        self.scrollArea_addoptions.setMinimumSize(QSize(941, 60))
        self.scrollArea_addoptions.setMaximumSize(QSize(941, 40))
        self.scrollArea_addoptions.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	height: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-width: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_addoptions.setWidgetResizable(True)
        self.scrollAreaWidgetContents_12 = QWidget()
        self.scrollAreaWidgetContents_12.setObjectName(u"scrollAreaWidgetContents_12")
        self.scrollAreaWidgetContents_12.setGeometry(QRect(0, 0, 941, 60))
        self.scrollAreaWidgetContents_12.setMinimumSize(QSize(941, 0))
        self.scrollAreaWidgetContents_12.setMaximumSize(QSize(1000, 16777215))
        self.frame_options = QFrame(self.scrollAreaWidgetContents_12)
        self.frame_options.setObjectName(u"frame_options")
        self.frame_options.setGeometry(QRect(0, 0, 941, 58))
        self.frame_options.setMinimumSize(QSize(941, 40))
        self.frame_options.setMaximumSize(QSize(16777215, 16777215))
        self.frame_options.setFrameShape(QFrame.StyledPanel)
        self.frame_options.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_options)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.addoptionproductbutton = QPushButton(self.frame_options)
        self.addoptionproductbutton.setObjectName(u"addoptionproductbutton")
        self.addoptionproductbutton.setMinimumSize(QSize(108, 38))
        self.addoptionproductbutton.setMaximumSize(QSize(108, 38))
        self.addoptionproductbutton.setStyleSheet(u"QPushButton {\n"
"	border-style: dashed;\n"
"	border-width: 2px;\n"
"	border-color: #D9D9D9;\n"
"	background: none;\n"
"	font-size: 16px;\n"
"	color: #D9D9D9;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: #CD4662;\n"
"	color: #CD4662;\n"
"	background-color: #EDEDED;\n"
"}")

        self.horizontalLayout_3.addWidget(self.addoptionproductbutton)

        self.horizontalSpacer_2 = QSpacerItem(800, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.scrollArea_addoptions.setWidget(self.scrollAreaWidgetContents_12)

        self.verticalLayout_14.addWidget(self.scrollArea_addoptions)

        self.addproductstocklabel = QLabel(self.frame_addproduct)
        self.addproductstocklabel.setObjectName(u"addproductstocklabel")
        self.addproductstocklabel.setMinimumSize(QSize(0, 40))
        self.addproductstocklabel.setMaximumSize(QSize(16777215, 40))
        self.addproductstocklabel.setStyleSheet(u"color: #000;\n"
"padding-top:10px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_14.addWidget(self.addproductstocklabel)

        self.addproductstockspinbox = QSpinBox(self.frame_addproduct)
        self.addproductstockspinbox.setObjectName(u"addproductstockspinbox")
        self.addproductstockspinbox.setMinimumSize(QSize(281, 38))
        self.addproductstockspinbox.setMaximumSize(QSize(281, 38))
        self.addproductstockspinbox.setStyleSheet(u"QSpinBox {\n"
"	border-radius: 5px;\n"
"	background: #EDEDED;\n"
"	padding: 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QSpinBox::up-button {\n"
"	color: #F4DBDB;\n"
"}")
        self.addproductstockspinbox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.addproductstockspinbox.setMinimum(1)
        self.addproductstockspinbox.setMaximum(1000000)

        self.verticalLayout_14.addWidget(self.addproductstockspinbox)

        self.addproductscategorieslabel = QLabel(self.frame_addproduct)
        self.addproductscategorieslabel.setObjectName(u"addproductscategorieslabel")
        self.addproductscategorieslabel.setMinimumSize(QSize(0, 50))
        self.addproductscategorieslabel.setMaximumSize(QSize(16777215, 50))
        self.addproductscategorieslabel.setStyleSheet(u"color: #000;\n"
"padding-top: 20px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_14.addWidget(self.addproductscategorieslabel)

        self.categories_container = QFrame(self.frame_addproduct)
        self.categories_container.setObjectName(u"categories_container")
        self.categories_container.setMinimumSize(QSize(0, 200))
        self.categories_container.setStyleSheet(u"")
        self.categories_container.setFrameShape(QFrame.StyledPanel)
        self.categories_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.categories_container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_categories_gender = QFrame(self.categories_container)
        self.frame_categories_gender.setObjectName(u"frame_categories_gender")
        self.frame_categories_gender.setFrameShape(QFrame.StyledPanel)
        self.frame_categories_gender.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_categories_gender)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.checkBox_men = QCheckBox(self.frame_categories_gender)
        self.checkBox_men.setObjectName(u"checkBox_men")
        self.checkBox_men.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.verticalLayout_16.addWidget(self.checkBox_men)

        self.checkBox_women = QCheckBox(self.frame_categories_gender)
        self.checkBox_women.setObjectName(u"checkBox_women")
        self.checkBox_women.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.verticalLayout_16.addWidget(self.checkBox_women)

        self.checkBox_kids = QCheckBox(self.frame_categories_gender)
        self.checkBox_kids.setObjectName(u"checkBox_kids")
        self.checkBox_kids.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.verticalLayout_16.addWidget(self.checkBox_kids)


        self.horizontalLayout.addWidget(self.frame_categories_gender)

        self.frame_categories_wear = QFrame(self.categories_container)
        self.frame_categories_wear.setObjectName(u"frame_categories_wear")
        self.frame_categories_wear.setFrameShape(QFrame.StyledPanel)
        self.frame_categories_wear.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_categories_wear)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_top = QCheckBox(self.frame_categories_wear)
        self.checkBox_top.setObjectName(u"checkBox_top")
        self.checkBox_top.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.gridLayout_2.addWidget(self.checkBox_top, 0, 0, 1, 1)

        self.checkBox_dress = QCheckBox(self.frame_categories_wear)
        self.checkBox_dress.setObjectName(u"checkBox_dress")
        self.checkBox_dress.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.gridLayout_2.addWidget(self.checkBox_dress, 2, 0, 1, 1)

        self.checkBox_headwear = QCheckBox(self.frame_categories_wear)
        self.checkBox_headwear.setObjectName(u"checkBox_headwear")
        self.checkBox_headwear.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.gridLayout_2.addWidget(self.checkBox_headwear, 4, 0, 1, 1)

        self.checkBox_bottom = QCheckBox(self.frame_categories_wear)
        self.checkBox_bottom.setObjectName(u"checkBox_bottom")
        self.checkBox_bottom.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.gridLayout_2.addWidget(self.checkBox_bottom, 0, 1, 1, 1)

        self.checkBox_footwear = QCheckBox(self.frame_categories_wear)
        self.checkBox_footwear.setObjectName(u"checkBox_footwear")
        self.checkBox_footwear.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.gridLayout_2.addWidget(self.checkBox_footwear, 2, 1, 1, 1)

        self.checkBox_accessories = QCheckBox(self.frame_categories_wear)
        self.checkBox_accessories.setObjectName(u"checkBox_accessories")
        self.checkBox_accessories.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.gridLayout_2.addWidget(self.checkBox_accessories, 4, 1, 1, 1)


        self.horizontalLayout.addWidget(self.frame_categories_wear)


        self.verticalLayout_14.addWidget(self.categories_container)

        self.frame_addproduct_submit = QFrame(self.frame_addproduct)
        self.frame_addproduct_submit.setObjectName(u"frame_addproduct_submit")
        self.frame_addproduct_submit.setMinimumSize(QSize(0, 80))
        self.frame_addproduct_submit.setMaximumSize(QSize(16777215, 80))
        self.frame_addproduct_submit.setFrameShape(QFrame.StyledPanel)
        self.frame_addproduct_submit.setFrameShadow(QFrame.Raised)
        self.canceladdproductbutton = QPushButton(self.frame_addproduct_submit)
        self.canceladdproductbutton.setObjectName(u"canceladdproductbutton")
        self.canceladdproductbutton.setGeometry(QRect(502, 10, 157, 49))
        self.canceladdproductbutton.setStyleSheet(u"QPushButton {	\n"
"	border-radius: 5px;\n"
"	background: #AEC289;\n"
"	color: #FFF;\n"
"	text-align: center;\n"
"	font-family: Suwannaphum;\n"
"	font-size: 20px;\n"
"	font-style: normal;\n"
"	font-weight: 400;\n"
"	line-height: normal;\n"
"}\n"
"QPushButton:hover {\n"
"	background: #F4DBDB;\n"
"	color: #545454;\n"
"}")
        self.addproductbutton = QPushButton(self.frame_addproduct_submit)
        self.addproductbutton.setObjectName(u"addproductbutton")
        self.addproductbutton.setGeometry(QRect(710, 10, 204, 49))
        self.addproductbutton.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"	background: #CD4662;\n"
"	color: #FFF;\n"
"	text-align: center;\n"
"	font-family: Suwannaphum;\n"
"	font-size: 20px;\n"
"	font-style: normal;\n"
"	font-weight: 400;\n"
"	line-height: normal;\n"
"}\n"
"QPushButton:hover {\n"
"	background: #F4DBDB;\n"
"	color: #545454;\n"
"}")

        self.verticalLayout_14.addWidget(self.frame_addproduct_submit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_8)
        self.stackedWidget_adminproducts.addWidget(self.addproductpage_admin)
        self.editproductspage_admin = QWidget()
        self.editproductspage_admin.setObjectName(u"editproductspage_admin")
        self.scrollArea_editproduct = QScrollArea(self.editproductspage_admin)
        self.scrollArea_editproduct.setObjectName(u"scrollArea_editproduct")
        self.scrollArea_editproduct.setGeometry(QRect(0, 0, 1021, 601))
        self.scrollArea_editproduct.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_editproduct.setWidgetResizable(True)
        self.scrollAreaWidgetContents_21 = QWidget()
        self.scrollAreaWidgetContents_21.setObjectName(u"scrollAreaWidgetContents_21")
        self.scrollAreaWidgetContents_21.setGeometry(QRect(0, 0, 1006, 1400))
        self.scrollAreaWidgetContents_21.setMinimumSize(QSize(0, 1400))
        self.frame_editproduct = QFrame(self.scrollAreaWidgetContents_21)
        self.frame_editproduct.setObjectName(u"frame_editproduct")
        self.frame_editproduct.setGeometry(QRect(39, 11, 961, 1400))
        self.frame_editproduct.setMinimumSize(QSize(0, 1400))
        self.frame_editproduct.setFrameShape(QFrame.StyledPanel)
        self.frame_editproduct.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_editproduct)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.editproductlabel_3 = QLabel(self.frame_editproduct)
        self.editproductlabel_3.setObjectName(u"editproductlabel_3")
        self.editproductlabel_3.setMinimumSize(QSize(890, 21))
        self.editproductlabel_3.setMaximumSize(QSize(16777215, 20))
        self.editproductlabel_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")

        self.verticalLayout_19.addWidget(self.editproductlabel_3)

        self.editproductimagecontainer = QWidget(self.frame_editproduct)
        self.editproductimagecontainer.setObjectName(u"editproductimagecontainer")
        self.editproductimagecontainer.setMinimumSize(QSize(0, 250))
        self.editproductimagecontainer.setMaximumSize(QSize(16777215, 250))
        self.editproductimagecontainer.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"	padding-top: 10px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	height: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-width: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.horizontalLayout_13 = QHBoxLayout(self.editproductimagecontainer)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.scrollArea_addimageproduct_3 = QScrollArea(self.editproductimagecontainer)
        self.scrollArea_addimageproduct_3.setObjectName(u"scrollArea_addimageproduct_3")
        self.scrollArea_addimageproduct_3.setMinimumSize(QSize(0, 240))
        self.scrollArea_addimageproduct_3.setMaximumSize(QSize(16777215, 240))
        self.scrollArea_addimageproduct_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_24 = QWidget()
        self.scrollAreaWidgetContents_24.setObjectName(u"scrollAreaWidgetContents_24")
        self.scrollAreaWidgetContents_24.setGeometry(QRect(0, 0, 1218, 210))
        self.scrollAreaWidgetContents_24.setMinimumSize(QSize(0, 210))
        self.scrollAreaWidgetContents_24.setMaximumSize(QSize(16777215, 210))
        self.horizontalLayout_14 = QHBoxLayout(self.scrollAreaWidgetContents_24)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_addimageproduct_3 = QFrame(self.scrollAreaWidgetContents_24)
        self.frame_addimageproduct_3.setObjectName(u"frame_addimageproduct_3")
        self.frame_addimageproduct_3.setMinimumSize(QSize(1200, 210))
        self.frame_addimageproduct_3.setMaximumSize(QSize(16777215, 210))
        self.frame_addimageproduct_3.setFrameShape(QFrame.StyledPanel)
        self.frame_addimageproduct_3.setFrameShadow(QFrame.Raised)
        self.addproductimagelabel_3 = QLabel(self.frame_addimageproduct_3)
        self.addproductimagelabel_3.setObjectName(u"addproductimagelabel_3")
        self.addproductimagelabel_3.setGeometry(QRect(0, 0, 220, 31))
        self.addproductimagelabel_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.addimagebutton_3 = QPushButton(self.frame_addimageproduct_3)
        self.addimagebutton_3.setObjectName(u"addimagebutton_3")
        self.addimagebutton_3.setGeometry(QRect(0, 45, 151, 151))
        self.addimagebutton_3.setStyleSheet(u"QPushButton {\n"
"	border: 3px dashed #D9D9D9;\n"
"	font-size: 46px;\n"
"	background: #FAF9F6;\n"
"	color: #D9D9D9;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: #CD4662;\n"
"	color: #CD4662;\n"
"	background-color: #EDEDED;\n"
"}")
        self.addimagebutton_3.setIconSize(QSize(151, 151))
        self.img_3 = QLabel(self.frame_addimageproduct_3)
        self.img_3.setObjectName(u"img_3")
        self.img_3.setGeometry(QRect(5, 50, 141, 141))
        self.img_3.setStyleSheet(u"image: url(:/pic/product_img/IMG_2025.JPG)")
        self.img_3.setAlignment(Qt.AlignCenter)
        self.delete_pic_button_3 = QPushButton(self.frame_addimageproduct_3)
        self.delete_pic_button_3.setObjectName(u"delete_pic_button_3")
        self.delete_pic_button_3.setEnabled(True)
        self.delete_pic_button_3.setGeometry(QRect(130, 30, 31, 32))
        self.delete_pic_button_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_pic_button_3.setAutoFillBackground(False)
        self.delete_pic_button_3.setStyleSheet(u"QPushButton {\n"
"	border-radius: 25px;\n"
"	border-color: rgb(217, 217, 217);\n"
"	border-width: 2px;\n"
"	background: #FAF9F6;\n"
"	color: #D9D9D9;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: #CD4662;\n"
"	color: rgb(116,23,17);\n"
"	background-color: rgb(237,106,94);\n"
"}")

        self.horizontalLayout_14.addWidget(self.frame_addimageproduct_3)

        self.scrollArea_addimageproduct_3.setWidget(self.scrollAreaWidgetContents_24)

        self.horizontalLayout_13.addWidget(self.scrollArea_addimageproduct_3)


        self.verticalLayout_19.addWidget(self.editproductimagecontainer)

        self.editproductnamelabel_3 = QLabel(self.frame_editproduct)
        self.editproductnamelabel_3.setObjectName(u"editproductnamelabel_3")
        self.editproductnamelabel_3.setMinimumSize(QSize(0, 50))
        self.editproductnamelabel_3.setMaximumSize(QSize(16777215, 50))
        self.editproductnamelabel_3.setStyleSheet(u"color: #000;\n"
"padding-top: 20px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_19.addWidget(self.editproductnamelabel_3)

        self.editproductnametextbox = QLineEdit(self.frame_editproduct)
        self.editproductnametextbox.setObjectName(u"editproductnametextbox")
        self.editproductnametextbox.setMaximumSize(QSize(910, 16777215))
        self.editproductnametextbox.setStyleSheet(u"border-radius: 5px;\n"
"background: #EDEDED;\n"
"padding: 5px;\n"
"font-size: 16px;\n"
"")

        self.verticalLayout_19.addWidget(self.editproductnametextbox)

        self.editproductdescriptionlabel_3 = QLabel(self.frame_editproduct)
        self.editproductdescriptionlabel_3.setObjectName(u"editproductdescriptionlabel_3")
        self.editproductdescriptionlabel_3.setMinimumSize(QSize(0, 50))
        self.editproductdescriptionlabel_3.setMaximumSize(QSize(16777215, 50))
        self.editproductdescriptionlabel_3.setStyleSheet(u"color: #000;\n"
"padding-top: 20px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_19.addWidget(self.editproductdescriptionlabel_3)

        self.editproductdescriptiontextbox_3 = QPlainTextEdit(self.frame_editproduct)
        self.editproductdescriptiontextbox_3.setObjectName(u"editproductdescriptiontextbox_3")
        self.editproductdescriptiontextbox_3.setMaximumSize(QSize(910, 117))
        self.editproductdescriptiontextbox_3.setStyleSheet(u"border-radius: 5px;\n"
"background: #EDEDED;\n"
"padding: 5px;\n"
"font-size: 16px;\n"
"")

        self.verticalLayout_19.addWidget(self.editproductdescriptiontextbox_3)

        self.editproductpricelabel_3 = QLabel(self.frame_editproduct)
        self.editproductpricelabel_3.setObjectName(u"editproductpricelabel_3")
        self.editproductpricelabel_3.setMinimumSize(QSize(0, 50))
        self.editproductpricelabel_3.setMaximumSize(QSize(16777215, 50))
        self.editproductpricelabel_3.setStyleSheet(u"color: #000;\n"
"padding-top: 20px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_19.addWidget(self.editproductpricelabel_3)

        self.editproductpricespinbox = QSpinBox(self.frame_editproduct)
        self.editproductpricespinbox.setObjectName(u"editproductpricespinbox")
        self.editproductpricespinbox.setMaximumSize(QSize(281, 16777215))
        self.editproductpricespinbox.setStyleSheet(u"QSpinBox {\n"
"	border-radius: 5px;\n"
"	background: #EDEDED;\n"
"	padding: 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QSpinBox::up-button {\n"
"	color: #F4DBDB;\n"
"}")
        self.editproductpricespinbox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.editproductpricespinbox.setMinimum(1)
        self.editproductpricespinbox.setMaximum(10000)

        self.verticalLayout_19.addWidget(self.editproductpricespinbox)

        self.editproductsizelabel_3 = QLabel(self.frame_editproduct)
        self.editproductsizelabel_3.setObjectName(u"editproductsizelabel_3")
        self.editproductsizelabel_3.setMinimumSize(QSize(0, 50))
        self.editproductsizelabel_3.setMaximumSize(QSize(16777215, 50))
        self.editproductsizelabel_3.setStyleSheet(u"color: #000;\n"
"padding-top: 20px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_19.addWidget(self.editproductsizelabel_3)

        self.scrollArea_addsizes_3 = QScrollArea(self.frame_editproduct)
        self.scrollArea_addsizes_3.setObjectName(u"scrollArea_addsizes_3")
        self.scrollArea_addsizes_3.setMinimumSize(QSize(941, 60))
        self.scrollArea_addsizes_3.setMaximumSize(QSize(941, 40))
        self.scrollArea_addsizes_3.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	height: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-width: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_addsizes_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_25 = QWidget()
        self.scrollAreaWidgetContents_25.setObjectName(u"scrollAreaWidgetContents_25")
        self.scrollAreaWidgetContents_25.setGeometry(QRect(0, 0, 941, 60))
        self.scrollAreaWidgetContents_25.setMinimumSize(QSize(941, 0))
        self.scrollAreaWidgetContents_25.setMaximumSize(QSize(1000, 16777215))
        self.frame_sizes_3 = QFrame(self.scrollAreaWidgetContents_25)
        self.frame_sizes_3.setObjectName(u"frame_sizes_3")
        self.frame_sizes_3.setGeometry(QRect(0, 0, 941, 58))
        self.frame_sizes_3.setMinimumSize(QSize(941, 40))
        self.frame_sizes_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_sizes_3.setFrameShape(QFrame.StyledPanel)
        self.frame_sizes_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_sizes_3)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_15.setContentsMargins(9, -1, -1, -1)
        self.frame_size_each = QFrame(self.frame_sizes_3)
        self.frame_size_each.setObjectName(u"frame_size_each")
        self.frame_size_each.setMinimumSize(QSize(155, 38))
        self.frame_size_each.setMaximumSize(QSize(155, 38))
        self.frame_size_each.setStyleSheet(u"boder-radius: 5px;")
        self.frame_size_each.setFrameShape(QFrame.StyledPanel)
        self.frame_size_each.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_size_each = QHBoxLayout(self.frame_size_each)
        self.horizontalLayout_size_each.setSpacing(0)
        self.horizontalLayout_size_each.setObjectName(u"horizontalLayout_size_each")
        self.horizontalLayout_size_each.setContentsMargins(0, 0, 0, 0)
        self.size_1 = QLineEdit(self.frame_size_each)
        self.size_1.setObjectName(u"size_1")
        self.size_1.setMinimumSize(QSize(108, 38))
        self.size_1.setMaximumSize(QSize(108, 38))
        self.size_1.setStyleSheet(u"border-radius: 5px;\n"
"background: #EDEDED;\n"
"padding: 5px;\n"
"font-size: 16px;")

        self.horizontalLayout_size_each.addWidget(self.size_1)

        self.deletesizebutton = QPushButton(self.frame_size_each)
        self.deletesizebutton.setObjectName(u"deletesizebutton")
        self.deletesizebutton.setMinimumSize(QSize(55, 38))
        self.deletesizebutton.setMaximumSize(QSize(55, 38))
        self.deletesizebutton.setStyleSheet(u"background: #CD4662;\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"border: none;")
        icon7 = QIcon()
        icon7.addFile(u":/pic/images/newres/trashcan.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deletesizebutton.setIcon(icon7)
        self.deletesizebutton.setIconSize(QSize(30, 30))

        self.horizontalLayout_size_each.addWidget(self.deletesizebutton)

        self.deletesizebutton.raise_()
        self.size_1.raise_()

        self.horizontalLayout_15.addWidget(self.frame_size_each)

        self.addsizeproductbutton_3 = QPushButton(self.frame_sizes_3)
        self.addsizeproductbutton_3.setObjectName(u"addsizeproductbutton_3")
        self.addsizeproductbutton_3.setMinimumSize(QSize(108, 38))
        self.addsizeproductbutton_3.setMaximumSize(QSize(108, 38))
        self.addsizeproductbutton_3.setStyleSheet(u"QPushButton {\n"
"	border-style: dashed;\n"
"	border-width: 2px;\n"
"	border-color: #D9D9D9;\n"
"	background: none;\n"
"	font-size: 16px;\n"
"	color: #D9D9D9;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: #CD4662;\n"
"	color: #CD4662;\n"
"	background-color: #EDEDED;\n"
"}")

        self.horizontalLayout_15.addWidget(self.addsizeproductbutton_3)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_7)

        self.scrollArea_addsizes_3.setWidget(self.scrollAreaWidgetContents_25)

        self.verticalLayout_19.addWidget(self.scrollArea_addsizes_3)

        self.editproductoptionlabel = QLabel(self.frame_editproduct)
        self.editproductoptionlabel.setObjectName(u"editproductoptionlabel")
        self.editproductoptionlabel.setMinimumSize(QSize(0, 40))
        self.editproductoptionlabel.setMaximumSize(QSize(16777215, 40))
        self.editproductoptionlabel.setStyleSheet(u"color: #000;\n"
"padding-top:10px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_19.addWidget(self.editproductoptionlabel)

        self.scrollArea_addoptions_3 = QScrollArea(self.frame_editproduct)
        self.scrollArea_addoptions_3.setObjectName(u"scrollArea_addoptions_3")
        self.scrollArea_addoptions_3.setMinimumSize(QSize(941, 60))
        self.scrollArea_addoptions_3.setMaximumSize(QSize(941, 40))
        self.scrollArea_addoptions_3.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	height: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-width: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_addoptions_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_26 = QWidget()
        self.scrollAreaWidgetContents_26.setObjectName(u"scrollAreaWidgetContents_26")
        self.scrollAreaWidgetContents_26.setGeometry(QRect(0, 0, 941, 60))
        self.scrollAreaWidgetContents_26.setMinimumSize(QSize(941, 0))
        self.scrollAreaWidgetContents_26.setMaximumSize(QSize(1000, 16777215))
        self.frame_options_3 = QFrame(self.scrollAreaWidgetContents_26)
        self.frame_options_3.setObjectName(u"frame_options_3")
        self.frame_options_3.setGeometry(QRect(0, 0, 941, 58))
        self.frame_options_3.setMinimumSize(QSize(941, 40))
        self.frame_options_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_options_3.setFrameShape(QFrame.StyledPanel)
        self.frame_options_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_options_3)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.addoptionproductbutton_3 = QPushButton(self.frame_options_3)
        self.addoptionproductbutton_3.setObjectName(u"addoptionproductbutton_3")
        self.addoptionproductbutton_3.setMinimumSize(QSize(108, 38))
        self.addoptionproductbutton_3.setMaximumSize(QSize(108, 38))
        self.addoptionproductbutton_3.setStyleSheet(u"QPushButton {\n"
"	border-style: dashed;\n"
"	border-width: 2px;\n"
"	border-color: #D9D9D9;\n"
"	background: none;\n"
"	font-size: 16px;\n"
"	color: #D9D9D9;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: #CD4662;\n"
"	color: #CD4662;\n"
"	background-color: #EDEDED;\n"
"}")

        self.horizontalLayout_16.addWidget(self.addoptionproductbutton_3)

        self.horizontalSpacer_8 = QSpacerItem(800, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_8)

        self.scrollArea_addoptions_3.setWidget(self.scrollAreaWidgetContents_26)

        self.verticalLayout_19.addWidget(self.scrollArea_addoptions_3)

        self.editproductstocklabel_3 = QLabel(self.frame_editproduct)
        self.editproductstocklabel_3.setObjectName(u"editproductstocklabel_3")
        self.editproductstocklabel_3.setMinimumSize(QSize(0, 40))
        self.editproductstocklabel_3.setMaximumSize(QSize(16777215, 40))
        self.editproductstocklabel_3.setStyleSheet(u"color: #000;\n"
"padding-top:10px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_19.addWidget(self.editproductstocklabel_3)

        self.editproductstockspinbox_3 = QSpinBox(self.frame_editproduct)
        self.editproductstockspinbox_3.setObjectName(u"editproductstockspinbox_3")
        self.editproductstockspinbox_3.setMinimumSize(QSize(281, 38))
        self.editproductstockspinbox_3.setMaximumSize(QSize(281, 38))
        self.editproductstockspinbox_3.setStyleSheet(u"QSpinBox {\n"
"	border-radius: 5px;\n"
"	background: #EDEDED;\n"
"	padding: 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QSpinBox::up-button {\n"
"	color: #F4DBDB;\n"
"}")
        self.editproductstockspinbox_3.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.editproductstockspinbox_3.setMinimum(1)
        self.editproductstockspinbox_3.setMaximum(1000000)

        self.verticalLayout_19.addWidget(self.editproductstockspinbox_3)

        self.editproductcategorieslabel_3 = QLabel(self.frame_editproduct)
        self.editproductcategorieslabel_3.setObjectName(u"editproductcategorieslabel_3")
        self.editproductcategorieslabel_3.setMinimumSize(QSize(0, 50))
        self.editproductcategorieslabel_3.setMaximumSize(QSize(16777215, 50))
        self.editproductcategorieslabel_3.setStyleSheet(u"color: #000;\n"
"padding-top: 20px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_19.addWidget(self.editproductcategorieslabel_3)

        self.categories_container_3 = QFrame(self.frame_editproduct)
        self.categories_container_3.setObjectName(u"categories_container_3")
        self.categories_container_3.setMinimumSize(QSize(0, 200))
        self.categories_container_3.setStyleSheet(u"")
        self.categories_container_3.setFrameShape(QFrame.StyledPanel)
        self.categories_container_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.categories_container_3)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame_categories_gender_3 = QFrame(self.categories_container_3)
        self.frame_categories_gender_3.setObjectName(u"frame_categories_gender_3")
        self.frame_categories_gender_3.setFrameShape(QFrame.StyledPanel)
        self.frame_categories_gender_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_categories_gender_3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.checkBox_men_3 = QCheckBox(self.frame_categories_gender_3)
        self.checkBox_men_3.setObjectName(u"checkBox_men_3")
        self.checkBox_men_3.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.verticalLayout_20.addWidget(self.checkBox_men_3)

        self.checkBox_women_3 = QCheckBox(self.frame_categories_gender_3)
        self.checkBox_women_3.setObjectName(u"checkBox_women_3")
        self.checkBox_women_3.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.verticalLayout_20.addWidget(self.checkBox_women_3)

        self.checkBox_kids_3 = QCheckBox(self.frame_categories_gender_3)
        self.checkBox_kids_3.setObjectName(u"checkBox_kids_3")
        self.checkBox_kids_3.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.verticalLayout_20.addWidget(self.checkBox_kids_3)


        self.horizontalLayout_17.addWidget(self.frame_categories_gender_3)

        self.frame_categories_wear_3 = QFrame(self.categories_container_3)
        self.frame_categories_wear_3.setObjectName(u"frame_categories_wear_3")
        self.frame_categories_wear_3.setFrameShape(QFrame.StyledPanel)
        self.frame_categories_wear_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_categories_wear_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.checkBox_top_3 = QCheckBox(self.frame_categories_wear_3)
        self.checkBox_top_3.setObjectName(u"checkBox_top_3")
        self.checkBox_top_3.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_top_3, 0, 0, 1, 1)

        self.checkBox_dress_3 = QCheckBox(self.frame_categories_wear_3)
        self.checkBox_dress_3.setObjectName(u"checkBox_dress_3")
        self.checkBox_dress_3.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_dress_3, 2, 0, 1, 1)

        self.checkBox_headwear_3 = QCheckBox(self.frame_categories_wear_3)
        self.checkBox_headwear_3.setObjectName(u"checkBox_headwear_3")
        self.checkBox_headwear_3.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_headwear_3, 4, 0, 1, 1)

        self.checkBox_bottom_3 = QCheckBox(self.frame_categories_wear_3)
        self.checkBox_bottom_3.setObjectName(u"checkBox_bottom_3")
        self.checkBox_bottom_3.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_bottom_3, 0, 1, 1, 1)

        self.checkBox_footwear_3 = QCheckBox(self.frame_categories_wear_3)
        self.checkBox_footwear_3.setObjectName(u"checkBox_footwear_3")
        self.checkBox_footwear_3.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_footwear_3, 2, 1, 1, 1)

        self.checkBox_accessories_3 = QCheckBox(self.frame_categories_wear_3)
        self.checkBox_accessories_3.setObjectName(u"checkBox_accessories_3")
        self.checkBox_accessories_3.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_accessories_3, 4, 1, 1, 1)


        self.horizontalLayout_17.addWidget(self.frame_categories_wear_3)


        self.verticalLayout_19.addWidget(self.categories_container_3)

        self.frame_addproduct_submit_3 = QFrame(self.frame_editproduct)
        self.frame_addproduct_submit_3.setObjectName(u"frame_addproduct_submit_3")
        self.frame_addproduct_submit_3.setMinimumSize(QSize(0, 80))
        self.frame_addproduct_submit_3.setMaximumSize(QSize(16777215, 80))
        self.frame_addproduct_submit_3.setFrameShape(QFrame.StyledPanel)
        self.frame_addproduct_submit_3.setFrameShadow(QFrame.Raised)
        self.addproductbutton_4 = QPushButton(self.frame_addproduct_submit_3)
        self.addproductbutton_4.setObjectName(u"addproductbutton_4")
        self.addproductbutton_4.setGeometry(QRect(710, 10, 204, 49))
        self.addproductbutton_4.setStyleSheet(u"QPushButton {	\n"
"	border-radius: 5px;\n"
"	background: #AEC289;\n"
"	color: #FFF;\n"
"	text-align: center;\n"
"	font-family: Suwannaphum;\n"
"	font-size: 20px;\n"
"	font-style: normal;\n"
"	font-weight: 400;\n"
"	line-height: normal;\n"
"}\n"
"QPushButton:hover {\n"
"	background: #F4DBDB;\n"
"	color: #545454;\n"
"}")

        self.verticalLayout_19.addWidget(self.frame_addproduct_submit_3)

        self.scrollArea_editproduct.setWidget(self.scrollAreaWidgetContents_21)
        self.stackedWidget_adminproducts.addWidget(self.editproductspage_admin)
        self.showproductforadmin = QWidget()
        self.showproductforadmin.setObjectName(u"showproductforadmin")
        self.scrollArea_productviewpage_2 = QScrollArea(self.showproductforadmin)
        self.scrollArea_productviewpage_2.setObjectName(u"scrollArea_productviewpage_2")
        self.scrollArea_productviewpage_2.setGeometry(QRect(0, 0, 1013, 593))
        self.scrollArea_productviewpage_2.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_productviewpage_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_29 = QWidget()
        self.scrollAreaWidgetContents_29.setObjectName(u"scrollAreaWidgetContents_29")
        self.scrollAreaWidgetContents_29.setGeometry(QRect(0, 0, 998, 1318))
        self.verticalLayout_331 = QVBoxLayout(self.scrollAreaWidgetContents_29)
        self.verticalLayout_331.setObjectName(u"verticalLayout_331")
        self.frame_productviewpage_2 = QFrame(self.scrollAreaWidgetContents_29)
        self.frame_productviewpage_2.setObjectName(u"frame_productviewpage_2")
        self.frame_productviewpage_2.setMinimumSize(QSize(0, 1300))
        self.frame_productviewpage_2.setStyleSheet(u"background-color: #FAF9F6;")
        self.frame_productviewpage_2.setFrameShape(QFrame.StyledPanel)
        self.frame_productviewpage_2.setFrameShadow(QFrame.Raised)
        self.productcontainer_3 = QWidget(self.frame_productviewpage_2)
        self.productcontainer_3.setObjectName(u"productcontainer_3")
        self.productcontainer_3.setGeometry(QRect(46, 0, 910, 481))
        self.productcontainer_3.setStyleSheet(u"background-color: #FAF9F6;\n"
";\n"
"border-radius: 10px 10px 0px 0px;")
        self.mainpic_2 = QLabel(self.productcontainer_3)
        self.mainpic_2.setObjectName(u"mainpic_2")
        self.mainpic_2.setGeometry(QRect(47, 34, 352, 352))
        self.mainpic_2.setStyleSheet(u"\n"
"background-color: #D9D9D9;")
        self.mainpic_2.setAlignment(Qt.AlignCenter)
        self.productname_2 = QLabel(self.productcontainer_3)
        self.productname_2.setObjectName(u"productname_2")
        self.productname_2.setGeometry(QRect(534, 34, 281, 41))
        self.productname_2.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"background-color: red;\n"
"background-color: #FAF9F6;")
        self.deleteproductbutton = QPushButton(self.productcontainer_3)
        self.deleteproductbutton.setObjectName(u"deleteproductbutton")
        self.deleteproductbutton.setGeometry(QRect(726, 420, 141, 44))
        self.deleteproductbutton.setStyleSheet(u"border-radius: 5px;\n"
"background-color: #CD4662;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"")
        self.editproductbutton = QPushButton(self.productcontainer_3)
        self.editproductbutton.setObjectName(u"editproductbutton")
        self.editproductbutton.setGeometry(QRect(534, 420, 141, 44))
        self.editproductbutton.setStyleSheet(u"QPushButton{\n"
"	color: #FAF9F6;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 16px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                background-color: #AEC289;\n"
"                border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }\n"
"")
        self.star1_2 = QLabel(self.productcontainer_3)
        self.star1_2.setObjectName(u"star1_2")
        self.star1_2.setGeometry(QRect(534, 110, 21, 21))
        self.star1_2.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star2_2 = QLabel(self.productcontainer_3)
        self.star2_2.setObjectName(u"star2_2")
        self.star2_2.setGeometry(QRect(555, 110, 21, 21))
        self.star2_2.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star3_2 = QLabel(self.productcontainer_3)
        self.star3_2.setObjectName(u"star3_2")
        self.star3_2.setGeometry(QRect(576, 110, 21, 21))
        self.star3_2.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star4_2 = QLabel(self.productcontainer_3)
        self.star4_2.setObjectName(u"star4_2")
        self.star4_2.setGeometry(QRect(597, 110, 21, 21))
        self.star4_2.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star5_2 = QLabel(self.productcontainer_3)
        self.star5_2.setObjectName(u"star5_2")
        self.star5_2.setGeometry(QRect(618, 110, 21, 21))
        self.star5_2.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.numberofstar_2 = QLabel(self.productcontainer_3)
        self.numberofstar_2.setObjectName(u"numberofstar_2")
        self.numberofstar_2.setGeometry(QRect(645, 110, 21, 21))
        self.numberofstar_2.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.numberofsold_2 = QLabel(self.productcontainer_3)
        self.numberofsold_2.setObjectName(u"numberofsold_2")
        self.numberofsold_2.setGeometry(QRect(710, 110, 101, 21))
        self.numberofsold_2.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.currencypic_2 = QLabel(self.productcontainer_3)
        self.currencypic_2.setObjectName(u"currencypic_2")
        self.currencypic_2.setGeometry(QRect(534, 83, 21, 21))
        self.currencypic_2.setStyleSheet(u"image: url(:/pic/images/baht.png);\n"
"border: none;")
        self.productprice_2 = QLabel(self.productcontainer_3)
        self.productprice_2.setObjectName(u"productprice_2")
        self.productprice_2.setGeometry(QRect(555, 83, 261, 21))
        self.productprice_2.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.sizelabel_2 = QLabel(self.productcontainer_3)
        self.sizelabel_2.setObjectName(u"sizelabel_2")
        self.sizelabel_2.setGeometry(QRect(534, 155, 49, 21))
        self.sizelabel_2.setStyleSheet(u"color:#545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.sbutton_2 = QPushButton(self.productcontainer_3)
        self.sbutton_2.setObjectName(u"sbutton_2")
        self.sbutton_2.setGeometry(QRect(534, 190, 75, 24))
        self.sbutton_2.setStyleSheet(u"color:#545454;\n"
"font-family: Suwannaphum;\n"
"background: #D9D9D9;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.mbutton_2 = QPushButton(self.productcontainer_3)
        self.mbutton_2.setObjectName(u"mbutton_2")
        self.mbutton_2.setGeometry(QRect(620, 190, 75, 24))
        self.mbutton_2.setStyleSheet(u"color:#545454;\n"
"font-family: Suwannaphum;\n"
"background: #D9D9D9;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.lbutton_2 = QPushButton(self.productcontainer_3)
        self.lbutton_2.setObjectName(u"lbutton_2")
        self.lbutton_2.setGeometry(QRect(706, 190, 75, 24))
        self.lbutton_2.setStyleSheet(u"color:#545454;\n"
"font-family: Suwannaphum;\n"
"background: #D9D9D9;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.xlbutton_2 = QPushButton(self.productcontainer_3)
        self.xlbutton_2.setObjectName(u"xlbutton_2")
        self.xlbutton_2.setGeometry(QRect(792, 190, 75, 24))
        self.xlbutton_2.setStyleSheet(u"color:#545454;\n"
"font-family: Suwannaphum;\n"
"background: #D9D9D9;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.optionslabel_2 = QLabel(self.productcontainer_3)
        self.optionslabel_2.setObjectName(u"optionslabel_2")
        self.optionslabel_2.setGeometry(QRect(534, 240, 61, 21))
        self.optionslabel_2.setStyleSheet(u"color:#545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.mbutton_3 = QPushButton(self.productcontainer_3)
        self.mbutton_3.setObjectName(u"mbutton_3")
        self.mbutton_3.setGeometry(QRect(620, 280, 75, 24))
        self.mbutton_3.setStyleSheet(u"color:#545454;\n"
"font-family: Suwannaphum;\n"
"background: #D9D9D9;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.lbutton_3 = QPushButton(self.productcontainer_3)
        self.lbutton_3.setObjectName(u"lbutton_3")
        self.lbutton_3.setGeometry(QRect(706, 280, 75, 24))
        self.lbutton_3.setStyleSheet(u"color:#545454;\n"
"font-family: Suwannaphum;\n"
"background: #D9D9D9;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.sbutton_3 = QPushButton(self.productcontainer_3)
        self.sbutton_3.setObjectName(u"sbutton_3")
        self.sbutton_3.setGeometry(QRect(534, 280, 75, 24))
        self.sbutton_3.setStyleSheet(u"color:#545454;\n"
"font-family: Suwannaphum;\n"
"background: #D9D9D9;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.xlbutton_3 = QPushButton(self.productcontainer_3)
        self.xlbutton_3.setObjectName(u"xlbutton_3")
        self.xlbutton_3.setGeometry(QRect(792, 280, 75, 24))
        self.xlbutton_3.setStyleSheet(u"color:#545454;\n"
"font-family: Suwannaphum;\n"
"background: #D9D9D9;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.nextpicrightsidebutton = QPushButton(self.productcontainer_3)
        self.nextpicrightsidebutton.setObjectName(u"nextpicrightsidebutton")
        self.nextpicrightsidebutton.setGeometry(QRect(405, 200, 21, 24))
        self.nextpicrightsidebutton.setStyleSheet(u"image: url(:/pic/images/newres/rightarrow_pink.png);\n"
"border: none;")
        self.nextpicrightsidebutton_2 = QPushButton(self.productcontainer_3)
        self.nextpicrightsidebutton_2.setObjectName(u"nextpicrightsidebutton_2")
        self.nextpicrightsidebutton_2.setGeometry(QRect(20, 200, 21, 24))
        self.nextpicrightsidebutton_2.setStyleSheet(u"image: url(:/pic/realimages/backhomoe.png);\n"
"border: none;")
        self.productdescription_2 = QLabel(self.frame_productviewpage_2)
        self.productdescription_2.setObjectName(u"productdescription_2")
        self.productdescription_2.setGeometry(QRect(70, 550, 818, 274))
        self.productdescription_2.setMaximumSize(QSize(919, 16777215))
        self.productdescription_2.setStyleSheet(u"color: #545454;\n"
"background-color: #FAF9F6;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.productdescription_2.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.frame_productviewpage_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 500, 121, 31))
        self.label_4.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.widget_3 = QWidget(self.frame_productviewpage_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(100, 880, 818, 421))
        self.widget_3.setStyleSheet(u"border-top: 1px solid #CD4662;\n"
"border-bottom: 1px solid #CD4662;\n"
"background-color: #FAF9F6;")
        self.reviewerprofile_2 = QLabel(self.widget_3)
        self.reviewerprofile_2.setObjectName(u"reviewerprofile_2")
        self.reviewerprofile_2.setGeometry(QRect(0, 20, 45, 45))
        self.reviewerprofile_2.setStyleSheet(u"image: url(:/pic/images/newres/profile.png);\n"
"border: none;\n"
"border-radius: 50%;\n"
"background-color: #D9D9D9;")
        self.reviewername_2 = QLabel(self.widget_3)
        self.reviewername_2.setObjectName(u"reviewername_2")
        self.reviewername_2.setGeometry(QRect(71, 20, 390, 39))
        self.reviewername_2.setStyleSheet(u"color: #000;\n"
"border: none;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.star11_2 = QLabel(self.widget_3)
        self.star11_2.setObjectName(u"star11_2")
        self.star11_2.setGeometry(QRect(71, 59, 21, 21))
        self.star11_2.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star12_2 = QLabel(self.widget_3)
        self.star12_2.setObjectName(u"star12_2")
        self.star12_2.setGeometry(QRect(98, 59, 21, 21))
        self.star12_2.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star13_2 = QLabel(self.widget_3)
        self.star13_2.setObjectName(u"star13_2")
        self.star13_2.setGeometry(QRect(126, 59, 21, 21))
        self.star13_2.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star14_2 = QLabel(self.widget_3)
        self.star14_2.setObjectName(u"star14_2")
        self.star14_2.setGeometry(QRect(154, 59, 21, 21))
        self.star14_2.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star15_2 = QLabel(self.widget_3)
        self.star15_2.setObjectName(u"star15_2")
        self.star15_2.setGeometry(QRect(182, 59, 21, 21))
        self.star15_2.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.productchoose_2 = QLabel(self.widget_3)
        self.productchoose_2.setObjectName(u"productchoose_2")
        self.productchoose_2.setGeometry(QRect(71, 100, 390, 39))
        self.productchoose_2.setStyleSheet(u"border: none;\n"
"color: #BFBFBF;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.productchoosereview_3 = QLabel(self.widget_3)
        self.productchoosereview_3.setObjectName(u"productchoosereview_3")
        self.productchoosereview_3.setGeometry(QRect(71, 140, 390, 39))
        self.productchoosereview_3.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.reviewpic1_2 = QPushButton(self.widget_3)
        self.reviewpic1_2.setObjectName(u"reviewpic1_2")
        self.reviewpic1_2.setGeometry(QRect(71, 199, 151, 151))
        self.reviewpic1_2.setStyleSheet(u"background-color: #D9D9D9;\n"
"border: none;")
        self.reviewpic2_2 = QPushButton(self.widget_3)
        self.reviewpic2_2.setObjectName(u"reviewpic2_2")
        self.reviewpic2_2.setGeometry(QRect(261, 199, 151, 151))
        self.reviewpic2_2.setStyleSheet(u"background-color: #D9D9D9;\n"
"border: none;")
        self.productchoosereview_4 = QLabel(self.widget_3)
        self.productchoosereview_4.setObjectName(u"productchoosereview_4")
        self.productchoosereview_4.setGeometry(QRect(71, 385, 390, 21))
        self.productchoosereview_4.setStyleSheet(u"color: #BFBFBF;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.reviewlabel_2 = QLabel(self.frame_productviewpage_2)
        self.reviewlabel_2.setObjectName(u"reviewlabel_2")
        self.reviewlabel_2.setGeometry(QRect(100, 840, 111, 16))
        self.reviewlabel_2.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.viewallbutton_2 = QPushButton(self.frame_productviewpage_2)
        self.viewallbutton_2.setObjectName(u"viewallbutton_2")
        self.viewallbutton_2.setGeometry(QRect(820, 840, 81, 24))
        self.viewallbutton_2.setStyleSheet(u"color: #CD4662;\n"
"border: none;\n"
"text-align: right;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_331.addWidget(self.frame_productviewpage_2)

        self.scrollArea_productviewpage_2.setWidget(self.scrollAreaWidgetContents_29)
        self.stackedWidget_adminproducts.addWidget(self.showproductforadmin)
        self.stackedWidget_adminmain.addWidget(self.productspage_admin)
        self.productviewpage_admin = QWidget()
        self.productviewpage_admin.setObjectName(u"productviewpage_admin")
        self.scrollArea_productviewpage_3 = QScrollArea(self.productviewpage_admin)
        self.scrollArea_productviewpage_3.setObjectName(u"scrollArea_productviewpage_3")
        self.scrollArea_productviewpage_3.setGeometry(QRect(0, 0, 1013, 593))
        self.scrollArea_productviewpage_3.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_productviewpage_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_31 = QWidget()
        self.scrollAreaWidgetContents_31.setObjectName(u"scrollAreaWidgetContents_31")
        self.scrollAreaWidgetContents_31.setGeometry(QRect(0, 0, 998, 1100))
        self.scrollAreaWidgetContents_31.setMinimumSize(QSize(0, 1100))
        self.verticalLayout_34 = QVBoxLayout(self.scrollAreaWidgetContents_31)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_productviewpage_3 = QFrame(self.scrollAreaWidgetContents_31)
        self.frame_productviewpage_3.setObjectName(u"frame_productviewpage_3")
        self.frame_productviewpage_3.setMinimumSize(QSize(0, 1100))
        self.frame_productviewpage_3.setStyleSheet(u"background-color: #FAF9F6;")
        self.frame_productviewpage_3.setFrameShape(QFrame.StyledPanel)
        self.frame_productviewpage_3.setFrameShadow(QFrame.Raised)
        self.productcontainer_admin_2 = QWidget(self.frame_productviewpage_3)
        self.productcontainer_admin_2.setObjectName(u"productcontainer_admin_2")
        self.productcontainer_admin_2.setGeometry(QRect(46, 0, 910, 491))
        self.productcontainer_admin_2.setStyleSheet(u"background-color: #FAF9F6;\n"
"border-radius: 10px 10px 0px 0px;")
        self.mainpic_admin = QLabel(self.productcontainer_admin_2)
        self.mainpic_admin.setObjectName(u"mainpic_admin")
        self.mainpic_admin.setGeometry(QRect(47, 34, 352, 352))
        self.mainpic_admin.setStyleSheet(u"\n"
"background-color: #D9D9D9;")
        self.mainpic_admin.setAlignment(Qt.AlignCenter)
        self.productname_admin = QLabel(self.productcontainer_admin_2)
        self.productname_admin.setObjectName(u"productname_admin")
        self.productname_admin.setGeometry(QRect(534, 24, 281, 41))
        self.productname_admin.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"background-color: red;\n"
"background-color: #FAF9F6;")
        self.deleteproductbutton_admin = QPushButton(self.productcontainer_admin_2)
        self.deleteproductbutton_admin.setObjectName(u"deleteproductbutton_admin")
        self.deleteproductbutton_admin.setGeometry(QRect(726, 420, 160, 38))
        self.deleteproductbutton_admin.setMinimumSize(QSize(160, 38))
        self.deleteproductbutton_admin.setMaximumSize(QSize(160, 38))
        self.deleteproductbutton_admin.setStyleSheet(u"border-radius: 19px;\n"
"background-color: #CD4662;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"")
        self.editproductbutton_admin = QPushButton(self.productcontainer_admin_2)
        self.editproductbutton_admin.setObjectName(u"editproductbutton_admin")
        self.editproductbutton_admin.setGeometry(QRect(534, 420, 160, 38))
        self.editproductbutton_admin.setMinimumSize(QSize(160, 38))
        self.editproductbutton_admin.setMaximumSize(QSize(160, 38))
        self.editproductbutton_admin.setStyleSheet(u"border-radius: 19px;\n"
"border: none;\n"
"background: #AEC289;\n"
"color: white;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.star1_admin = QLabel(self.productcontainer_admin_2)
        self.star1_admin.setObjectName(u"star1_admin")
        self.star1_admin.setGeometry(QRect(534, 110, 21, 21))
        self.star1_admin.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star2_admin = QLabel(self.productcontainer_admin_2)
        self.star2_admin.setObjectName(u"star2_admin")
        self.star2_admin.setGeometry(QRect(555, 110, 21, 21))
        self.star2_admin.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star3_admin = QLabel(self.productcontainer_admin_2)
        self.star3_admin.setObjectName(u"star3_admin")
        self.star3_admin.setGeometry(QRect(576, 110, 21, 21))
        self.star3_admin.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star4_admin = QLabel(self.productcontainer_admin_2)
        self.star4_admin.setObjectName(u"star4_admin")
        self.star4_admin.setGeometry(QRect(597, 110, 21, 21))
        self.star4_admin.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star5_admin = QLabel(self.productcontainer_admin_2)
        self.star5_admin.setObjectName(u"star5_admin")
        self.star5_admin.setGeometry(QRect(618, 110, 21, 21))
        self.star5_admin.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.numberofstar_admin = QLabel(self.productcontainer_admin_2)
        self.numberofstar_admin.setObjectName(u"numberofstar_admin")
        self.numberofstar_admin.setGeometry(QRect(645, 110, 21, 21))
        self.numberofstar_admin.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.numberofsold_admin = QLabel(self.productcontainer_admin_2)
        self.numberofsold_admin.setObjectName(u"numberofsold_admin")
        self.numberofsold_admin.setGeometry(QRect(710, 110, 101, 21))
        self.numberofsold_admin.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.currencypic_admin = QLabel(self.productcontainer_admin_2)
        self.currencypic_admin.setObjectName(u"currencypic_admin")
        self.currencypic_admin.setGeometry(QRect(534, 73, 21, 21))
        self.currencypic_admin.setStyleSheet(u"image: url(:/pic/images/baht.png);\n"
"border: none;")
        self.productprice_admin = QLabel(self.productcontainer_admin_2)
        self.productprice_admin.setObjectName(u"productprice_admin")
        self.productprice_admin.setGeometry(QRect(555, 73, 261, 21))
        self.productprice_admin.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.frame_sizeoption_productviewpage_admin = QFrame(self.productcontainer_admin_2)
        self.frame_sizeoption_productviewpage_admin.setObjectName(u"frame_sizeoption_productviewpage_admin")
        self.frame_sizeoption_productviewpage_admin.setGeometry(QRect(534, 160, 372, 231))
        self.frame_sizeoption_productviewpage_admin.setMinimumSize(QSize(372, 231))
        self.frame_sizeoption_productviewpage_admin.setMaximumSize(QSize(372, 16777215))
        self.frame_sizeoption_productviewpage_admin.setFrameShape(QFrame.StyledPanel)
        self.frame_sizeoption_productviewpage_admin.setFrameShadow(QFrame.Raised)
        self.verticalLayout_sizeoption_productviewpage_2 = QVBoxLayout(self.frame_sizeoption_productviewpage_admin)
        self.verticalLayout_sizeoption_productviewpage_2.setSpacing(0)
        self.verticalLayout_sizeoption_productviewpage_2.setObjectName(u"verticalLayout_sizeoption_productviewpage_2")
        self.verticalLayout_sizeoption_productviewpage_2.setContentsMargins(0, 0, 0, 0)
        self.sizelabel_admin = QLabel(self.frame_sizeoption_productviewpage_admin)
        self.sizelabel_admin.setObjectName(u"sizelabel_admin")
        self.sizelabel_admin.setMinimumSize(QSize(49, 21))
        self.sizelabel_admin.setMaximumSize(QSize(49, 21))
        self.sizelabel_admin.setStyleSheet(u"color:#545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_sizeoption_productviewpage_2.addWidget(self.sizelabel_admin)

        self.frame_size_productviewpage_admin = QFrame(self.frame_sizeoption_productviewpage_admin)
        self.frame_size_productviewpage_admin.setObjectName(u"frame_size_productviewpage_admin")
        self.frame_size_productviewpage_admin.setMinimumSize(QSize(381, 80))
        self.frame_size_productviewpage_admin.setMaximumSize(QSize(381, 80))
        self.frame_size_productviewpage_admin.setFrameShape(QFrame.StyledPanel)
        self.frame_size_productviewpage_admin.setFrameShadow(QFrame.Raised)
        self.gridLayout_size_productviewpage_2 = QGridLayout(self.frame_size_productviewpage_admin)
        self.gridLayout_size_productviewpage_2.setObjectName(u"gridLayout_size_productviewpage_2")
        self.gridLayout_size_productviewpage_2.setHorizontalSpacing(25)
        self.gridLayout_size_productviewpage_2.setVerticalSpacing(10)
        self.gridLayout_size_productviewpage_2.setContentsMargins(0, -1, 0, -1)

        self.verticalLayout_sizeoption_productviewpage_2.addWidget(self.frame_size_productviewpage_admin)

        self.optionslabel_admin = QLabel(self.frame_sizeoption_productviewpage_admin)
        self.optionslabel_admin.setObjectName(u"optionslabel_admin")
        self.optionslabel_admin.setMinimumSize(QSize(61, 21))
        self.optionslabel_admin.setMaximumSize(QSize(61, 21))
        self.optionslabel_admin.setStyleSheet(u"color:#545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_sizeoption_productviewpage_2.addWidget(self.optionslabel_admin)

        self.frame_option_productviewpage_admin = QFrame(self.frame_sizeoption_productviewpage_admin)
        self.frame_option_productviewpage_admin.setObjectName(u"frame_option_productviewpage_admin")
        self.frame_option_productviewpage_admin.setMinimumSize(QSize(381, 80))
        self.frame_option_productviewpage_admin.setMaximumSize(QSize(381, 80))
        self.frame_option_productviewpage_admin.setFrameShape(QFrame.StyledPanel)
        self.frame_option_productviewpage_admin.setFrameShadow(QFrame.Raised)
        self.gridLayout_option_productviewpage_2 = QGridLayout(self.frame_option_productviewpage_admin)
        self.gridLayout_option_productviewpage_2.setObjectName(u"gridLayout_option_productviewpage_2")
        self.gridLayout_option_productviewpage_2.setHorizontalSpacing(25)
        self.gridLayout_option_productviewpage_2.setVerticalSpacing(10)
        self.gridLayout_option_productviewpage_2.setContentsMargins(0, -1, 0, -1)

        self.verticalLayout_sizeoption_productviewpage_2.addWidget(self.frame_option_productviewpage_admin)

        self.prevpicbutton_admin = QPushButton(self.productcontainer_admin_2)
        self.prevpicbutton_admin.setObjectName(u"prevpicbutton_admin")
        self.prevpicbutton_admin.setGeometry(QRect(0, 190, 21, 39))
        self.prevpicbutton_admin.setIcon(icon4)
        self.prevpicbutton_admin.setIconSize(QSize(21, 39))
        self.nextpicbutton_admin = QPushButton(self.productcontainer_admin_2)
        self.nextpicbutton_admin.setObjectName(u"nextpicbutton_admin")
        self.nextpicbutton_admin.setGeometry(QRect(420, 190, 21, 39))
        self.nextpicbutton_admin.setIcon(icon5)
        self.nextpicbutton_admin.setIconSize(QSize(21, 39))
        self.descriptionlabel_productviewpage_admin = QLabel(self.frame_productviewpage_3)
        self.descriptionlabel_productviewpage_admin.setObjectName(u"descriptionlabel_productviewpage_admin")
        self.descriptionlabel_productviewpage_admin.setGeometry(QRect(50, 510, 171, 31))
        self.descriptionlabel_productviewpage_admin.setStyleSheet(u"font-size: 24px;\n"
"font-weight: 400;")
        self.frame_description_productviewpage_admin = QFrame(self.frame_productviewpage_3)
        self.frame_description_productviewpage_admin.setObjectName(u"frame_description_productviewpage_admin")
        self.frame_description_productviewpage_admin.setGeometry(QRect(50, 560, 901, 481))
        self.frame_description_productviewpage_admin.setFrameShape(QFrame.StyledPanel)
        self.frame_description_productviewpage_admin.setFrameShadow(QFrame.Raised)
        self.descriptioninfolabel_productviewpage_admin = QLabel(self.frame_description_productviewpage_admin)
        self.descriptioninfolabel_productviewpage_admin.setObjectName(u"descriptioninfolabel_productviewpage_admin")
        self.descriptioninfolabel_productviewpage_admin.setGeometry(QRect(0, 10, 901, 471))
        self.descriptioninfolabel_productviewpage_admin.setStyleSheet(u"font-size: 14px;\n"
"border-bottom: 2px solid #CD4662;")
        self.descriptioninfolabel_productviewpage_admin.setTextFormat(Qt.AutoText)
        self.descriptioninfolabel_productviewpage_admin.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.descriptioninfolabel_productviewpage_admin.setWordWrap(True)

        self.verticalLayout_34.addWidget(self.frame_productviewpage_3)

        self.scrollArea_productviewpage_3.setWidget(self.scrollAreaWidgetContents_31)
        self.stackedWidget_adminmain.addWidget(self.productviewpage_admin)
        self.nouse_2 = QWidget()
        self.nouse_2.setObjectName(u"nouse_2")
        self.nouse_2.setMinimumSize(QSize(0, 0))
        self.scrollArea_2 = QScrollArea(self.nouse_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(0, 0, 1021, 1500))
        self.scrollArea_2.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_13 = QWidget()
        self.scrollAreaWidgetContents_13.setObjectName(u"scrollAreaWidgetContents_13")
        self.scrollAreaWidgetContents_13.setGeometry(QRect(0, 0, 1021, 1500))
        self.scrollAreaWidgetContents_13.setMinimumSize(QSize(0, 0))
        self.frame_addproduct_2 = QFrame(self.scrollAreaWidgetContents_13)
        self.frame_addproduct_2.setObjectName(u"frame_addproduct_2")
        self.frame_addproduct_2.setGeometry(QRect(39, 11, 961, 1400))
        self.frame_addproduct_2.setMinimumSize(QSize(0, 1400))
        self.frame_addproduct_2.setFrameShape(QFrame.StyledPanel)
        self.frame_addproduct_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_addproduct_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.addproductlabel_2 = QLabel(self.frame_addproduct_2)
        self.addproductlabel_2.setObjectName(u"addproductlabel_2")
        self.addproductlabel_2.setMinimumSize(QSize(890, 21))
        self.addproductlabel_2.setMaximumSize(QSize(16777215, 20))
        self.addproductlabel_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")

        self.verticalLayout_17.addWidget(self.addproductlabel_2)

        self.addimageproductcontainer_2 = QWidget(self.frame_addproduct_2)
        self.addimageproductcontainer_2.setObjectName(u"addimageproductcontainer_2")
        self.addimageproductcontainer_2.setMinimumSize(QSize(0, 250))
        self.addimageproductcontainer_2.setMaximumSize(QSize(16777215, 250))
        self.addimageproductcontainer_2.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"	padding-top: 10px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	height: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-width: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.horizontalLayout_11 = QHBoxLayout(self.addimageproductcontainer_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.scrollArea_addimageproduct_2 = QScrollArea(self.addimageproductcontainer_2)
        self.scrollArea_addimageproduct_2.setObjectName(u"scrollArea_addimageproduct_2")
        self.scrollArea_addimageproduct_2.setMinimumSize(QSize(0, 240))
        self.scrollArea_addimageproduct_2.setMaximumSize(QSize(16777215, 240))
        self.scrollArea_addimageproduct_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_23 = QWidget()
        self.scrollAreaWidgetContents_23.setObjectName(u"scrollAreaWidgetContents_23")
        self.scrollAreaWidgetContents_23.setGeometry(QRect(0, 0, 1218, 210))
        self.scrollAreaWidgetContents_23.setMinimumSize(QSize(0, 210))
        self.scrollAreaWidgetContents_23.setMaximumSize(QSize(16777215, 210))
        self.horizontalLayout_12 = QHBoxLayout(self.scrollAreaWidgetContents_23)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_addimageproduct_2 = QFrame(self.scrollAreaWidgetContents_23)
        self.frame_addimageproduct_2.setObjectName(u"frame_addimageproduct_2")
        self.frame_addimageproduct_2.setMinimumSize(QSize(1200, 210))
        self.frame_addimageproduct_2.setMaximumSize(QSize(16777215, 210))
        self.frame_addimageproduct_2.setFrameShape(QFrame.StyledPanel)
        self.frame_addimageproduct_2.setFrameShadow(QFrame.Raised)
        self.addproductimagelabel_2 = QLabel(self.frame_addimageproduct_2)
        self.addproductimagelabel_2.setObjectName(u"addproductimagelabel_2")
        self.addproductimagelabel_2.setGeometry(QRect(0, 0, 220, 31))
        self.addproductimagelabel_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.addimagebutton_2 = QPushButton(self.frame_addimageproduct_2)
        self.addimagebutton_2.setObjectName(u"addimagebutton_2")
        self.addimagebutton_2.setGeometry(QRect(0, 45, 151, 151))
        self.addimagebutton_2.setStyleSheet(u"QPushButton {\n"
"	border: 3px dashed #D9D9D9;\n"
"	font-size: 46px;\n"
"	background: #FAF9F6;\n"
"	color: #D9D9D9;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: #CD4662;\n"
"	color: #CD4662;\n"
"	background-color: #EDEDED;\n"
"}")
        self.addimagebutton_2.setIconSize(QSize(151, 151))
        self.img_2 = QLabel(self.frame_addimageproduct_2)
        self.img_2.setObjectName(u"img_2")
        self.img_2.setGeometry(QRect(5, 50, 141, 141))
        self.img_2.setStyleSheet(u"image: url(:/pic/product_img/IMG_2025.JPG)")
        self.img_2.setAlignment(Qt.AlignCenter)
        self.delete_pic_button_2 = QPushButton(self.frame_addimageproduct_2)
        self.delete_pic_button_2.setObjectName(u"delete_pic_button_2")
        self.delete_pic_button_2.setEnabled(True)
        self.delete_pic_button_2.setGeometry(QRect(130, 30, 31, 32))
        self.delete_pic_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_pic_button_2.setAutoFillBackground(False)
        self.delete_pic_button_2.setStyleSheet(u"QPushButton {\n"
"	border-radius: 25px;\n"
"	border-color: rgb(217, 217, 217);\n"
"	border-width: 2px;\n"
"	background: #FAF9F6;\n"
"	color: #D9D9D9;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: #CD4662;\n"
"	color: rgb(116,23,17);\n"
"	background-color: rgb(237,106,94);\n"
"}")

        self.horizontalLayout_12.addWidget(self.frame_addimageproduct_2)

        self.scrollArea_addimageproduct_2.setWidget(self.scrollAreaWidgetContents_23)

        self.horizontalLayout_11.addWidget(self.scrollArea_addimageproduct_2)


        self.verticalLayout_17.addWidget(self.addimageproductcontainer_2)

        self.addproductnamelabel_2 = QLabel(self.frame_addproduct_2)
        self.addproductnamelabel_2.setObjectName(u"addproductnamelabel_2")
        self.addproductnamelabel_2.setMinimumSize(QSize(0, 50))
        self.addproductnamelabel_2.setMaximumSize(QSize(16777215, 50))
        self.addproductnamelabel_2.setStyleSheet(u"color: #000;\n"
"padding-top: 20px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_17.addWidget(self.addproductnamelabel_2)

        self.addproductnametextbox_2 = QLineEdit(self.frame_addproduct_2)
        self.addproductnametextbox_2.setObjectName(u"addproductnametextbox_2")
        self.addproductnametextbox_2.setMaximumSize(QSize(910, 16777215))
        self.addproductnametextbox_2.setStyleSheet(u"border-radius: 5px;\n"
"background: #EDEDED;\n"
"padding: 5px;\n"
"font-size: 16px;\n"
"")

        self.verticalLayout_17.addWidget(self.addproductnametextbox_2)

        self.addproductdescriptionlabel_2 = QLabel(self.frame_addproduct_2)
        self.addproductdescriptionlabel_2.setObjectName(u"addproductdescriptionlabel_2")
        self.addproductdescriptionlabel_2.setMinimumSize(QSize(0, 50))
        self.addproductdescriptionlabel_2.setMaximumSize(QSize(16777215, 50))
        self.addproductdescriptionlabel_2.setStyleSheet(u"color: #000;\n"
"padding-top: 20px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_17.addWidget(self.addproductdescriptionlabel_2)

        self.addproductdescriptiontextbox_2 = QPlainTextEdit(self.frame_addproduct_2)
        self.addproductdescriptiontextbox_2.setObjectName(u"addproductdescriptiontextbox_2")
        self.addproductdescriptiontextbox_2.setMaximumSize(QSize(910, 117))
        self.addproductdescriptiontextbox_2.setStyleSheet(u"border-radius: 5px;\n"
"background: #EDEDED;\n"
"padding: 5px;\n"
"font-size: 16px;\n"
"")

        self.verticalLayout_17.addWidget(self.addproductdescriptiontextbox_2)

        self.addproductpricelabel_2 = QLabel(self.frame_addproduct_2)
        self.addproductpricelabel_2.setObjectName(u"addproductpricelabel_2")
        self.addproductpricelabel_2.setMinimumSize(QSize(0, 50))
        self.addproductpricelabel_2.setMaximumSize(QSize(16777215, 50))
        self.addproductpricelabel_2.setStyleSheet(u"color: #000;\n"
"padding-top: 20px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_17.addWidget(self.addproductpricelabel_2)

        self.addproductpricespinbox_2 = QSpinBox(self.frame_addproduct_2)
        self.addproductpricespinbox_2.setObjectName(u"addproductpricespinbox_2")
        self.addproductpricespinbox_2.setMaximumSize(QSize(281, 16777215))
        self.addproductpricespinbox_2.setStyleSheet(u"QSpinBox {\n"
"	border-radius: 5px;\n"
"	background: #EDEDED;\n"
"	padding: 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QSpinBox::up-button {\n"
"	color: #F4DBDB;\n"
"}")
        self.addproductpricespinbox_2.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.addproductpricespinbox_2.setMinimum(1)
        self.addproductpricespinbox_2.setMaximum(10000)

        self.verticalLayout_17.addWidget(self.addproductpricespinbox_2)

        self.addproductsizelabel_2 = QLabel(self.frame_addproduct_2)
        self.addproductsizelabel_2.setObjectName(u"addproductsizelabel_2")
        self.addproductsizelabel_2.setMinimumSize(QSize(0, 50))
        self.addproductsizelabel_2.setMaximumSize(QSize(16777215, 50))
        self.addproductsizelabel_2.setStyleSheet(u"color: #000;\n"
"padding-top: 20px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_17.addWidget(self.addproductsizelabel_2)

        self.scrollArea_addsizes_2 = QScrollArea(self.frame_addproduct_2)
        self.scrollArea_addsizes_2.setObjectName(u"scrollArea_addsizes_2")
        self.scrollArea_addsizes_2.setMinimumSize(QSize(941, 60))
        self.scrollArea_addsizes_2.setMaximumSize(QSize(941, 40))
        self.scrollArea_addsizes_2.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	height: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-width: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_addsizes_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_14 = QWidget()
        self.scrollAreaWidgetContents_14.setObjectName(u"scrollAreaWidgetContents_14")
        self.scrollAreaWidgetContents_14.setGeometry(QRect(0, 0, 941, 60))
        self.scrollAreaWidgetContents_14.setMinimumSize(QSize(941, 0))
        self.scrollAreaWidgetContents_14.setMaximumSize(QSize(1000, 16777215))
        self.frame_sizes_2 = QFrame(self.scrollAreaWidgetContents_14)
        self.frame_sizes_2.setObjectName(u"frame_sizes_2")
        self.frame_sizes_2.setGeometry(QRect(0, 0, 941, 58))
        self.frame_sizes_2.setMinimumSize(QSize(941, 40))
        self.frame_sizes_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_sizes_2.setFrameShape(QFrame.StyledPanel)
        self.frame_sizes_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_sizes_2)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(9, -1, -1, -1)
        self.addsizeproductbutton_2 = QPushButton(self.frame_sizes_2)
        self.addsizeproductbutton_2.setObjectName(u"addsizeproductbutton_2")
        self.addsizeproductbutton_2.setMinimumSize(QSize(108, 38))
        self.addsizeproductbutton_2.setMaximumSize(QSize(108, 38))
        self.addsizeproductbutton_2.setStyleSheet(u"QPushButton {\n"
"	border-style: dashed;\n"
"	border-width: 2px;\n"
"	border-color: #D9D9D9;\n"
"	background: none;\n"
"	font-size: 16px;\n"
"	color: #D9D9D9;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: #CD4662;\n"
"	color: #CD4662;\n"
"	background-color: #EDEDED;\n"
"}")

        self.horizontalLayout_6.addWidget(self.addsizeproductbutton_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.scrollArea_addsizes_2.setWidget(self.scrollAreaWidgetContents_14)

        self.verticalLayout_17.addWidget(self.scrollArea_addsizes_2)

        self.addproductoptionlabel_2 = QLabel(self.frame_addproduct_2)
        self.addproductoptionlabel_2.setObjectName(u"addproductoptionlabel_2")
        self.addproductoptionlabel_2.setMinimumSize(QSize(0, 40))
        self.addproductoptionlabel_2.setMaximumSize(QSize(16777215, 40))
        self.addproductoptionlabel_2.setStyleSheet(u"color: #000;\n"
"padding-top:10px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_17.addWidget(self.addproductoptionlabel_2)

        self.scrollArea_addoptions_2 = QScrollArea(self.frame_addproduct_2)
        self.scrollArea_addoptions_2.setObjectName(u"scrollArea_addoptions_2")
        self.scrollArea_addoptions_2.setMinimumSize(QSize(941, 60))
        self.scrollArea_addoptions_2.setMaximumSize(QSize(941, 40))
        self.scrollArea_addoptions_2.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	height: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-width: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_addoptions_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_15 = QWidget()
        self.scrollAreaWidgetContents_15.setObjectName(u"scrollAreaWidgetContents_15")
        self.scrollAreaWidgetContents_15.setGeometry(QRect(0, 0, 941, 60))
        self.scrollAreaWidgetContents_15.setMinimumSize(QSize(941, 0))
        self.scrollAreaWidgetContents_15.setMaximumSize(QSize(1000, 16777215))
        self.frame_options_2 = QFrame(self.scrollAreaWidgetContents_15)
        self.frame_options_2.setObjectName(u"frame_options_2")
        self.frame_options_2.setGeometry(QRect(0, 0, 941, 58))
        self.frame_options_2.setMinimumSize(QSize(941, 40))
        self.frame_options_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_options_2.setFrameShape(QFrame.StyledPanel)
        self.frame_options_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_options_2)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.addoptionproductbutton_2 = QPushButton(self.frame_options_2)
        self.addoptionproductbutton_2.setObjectName(u"addoptionproductbutton_2")
        self.addoptionproductbutton_2.setMinimumSize(QSize(108, 38))
        self.addoptionproductbutton_2.setMaximumSize(QSize(108, 38))
        self.addoptionproductbutton_2.setStyleSheet(u"QPushButton {\n"
"	border-style: dashed;\n"
"	border-width: 2px;\n"
"	border-color: #D9D9D9;\n"
"	background: none;\n"
"	font-size: 16px;\n"
"	color: #D9D9D9;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: #CD4662;\n"
"	color: #CD4662;\n"
"	background-color: #EDEDED;\n"
"}")

        self.horizontalLayout_7.addWidget(self.addoptionproductbutton_2)

        self.horizontalSpacer_6 = QSpacerItem(800, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.scrollArea_addoptions_2.setWidget(self.scrollAreaWidgetContents_15)

        self.verticalLayout_17.addWidget(self.scrollArea_addoptions_2)

        self.addproductstocklabel_2 = QLabel(self.frame_addproduct_2)
        self.addproductstocklabel_2.setObjectName(u"addproductstocklabel_2")
        self.addproductstocklabel_2.setMinimumSize(QSize(0, 40))
        self.addproductstocklabel_2.setMaximumSize(QSize(16777215, 40))
        self.addproductstocklabel_2.setStyleSheet(u"color: #000;\n"
"padding-top:10px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_17.addWidget(self.addproductstocklabel_2)

        self.addproductstockspinbox_2 = QSpinBox(self.frame_addproduct_2)
        self.addproductstockspinbox_2.setObjectName(u"addproductstockspinbox_2")
        self.addproductstockspinbox_2.setMinimumSize(QSize(281, 38))
        self.addproductstockspinbox_2.setMaximumSize(QSize(281, 38))
        self.addproductstockspinbox_2.setStyleSheet(u"QSpinBox {\n"
"	border-radius: 5px;\n"
"	background: #EDEDED;\n"
"	padding: 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QSpinBox::up-button {\n"
"	color: #F4DBDB;\n"
"}")
        self.addproductstockspinbox_2.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.addproductstockspinbox_2.setMinimum(1)
        self.addproductstockspinbox_2.setMaximum(1000000)

        self.verticalLayout_17.addWidget(self.addproductstockspinbox_2)

        self.addproductscategorieslabel_2 = QLabel(self.frame_addproduct_2)
        self.addproductscategorieslabel_2.setObjectName(u"addproductscategorieslabel_2")
        self.addproductscategorieslabel_2.setMinimumSize(QSize(0, 50))
        self.addproductscategorieslabel_2.setMaximumSize(QSize(16777215, 50))
        self.addproductscategorieslabel_2.setStyleSheet(u"color: #000;\n"
"padding-top: 20px;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_17.addWidget(self.addproductscategorieslabel_2)

        self.categories_container_2 = QFrame(self.frame_addproduct_2)
        self.categories_container_2.setObjectName(u"categories_container_2")
        self.categories_container_2.setMinimumSize(QSize(0, 200))
        self.categories_container_2.setStyleSheet(u"")
        self.categories_container_2.setFrameShape(QFrame.StyledPanel)
        self.categories_container_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.categories_container_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_categories_gender_2 = QFrame(self.categories_container_2)
        self.frame_categories_gender_2.setObjectName(u"frame_categories_gender_2")
        self.frame_categories_gender_2.setFrameShape(QFrame.StyledPanel)
        self.frame_categories_gender_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_categories_gender_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.checkBox_men_2 = QCheckBox(self.frame_categories_gender_2)
        self.checkBox_men_2.setObjectName(u"checkBox_men_2")
        self.checkBox_men_2.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.verticalLayout_18.addWidget(self.checkBox_men_2)

        self.checkBox_women_2 = QCheckBox(self.frame_categories_gender_2)
        self.checkBox_women_2.setObjectName(u"checkBox_women_2")
        self.checkBox_women_2.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.verticalLayout_18.addWidget(self.checkBox_women_2)

        self.checkBox_kids_2 = QCheckBox(self.frame_categories_gender_2)
        self.checkBox_kids_2.setObjectName(u"checkBox_kids_2")
        self.checkBox_kids_2.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.verticalLayout_18.addWidget(self.checkBox_kids_2)


        self.horizontalLayout_8.addWidget(self.frame_categories_gender_2)

        self.frame_categories_wear_2 = QFrame(self.categories_container_2)
        self.frame_categories_wear_2.setObjectName(u"frame_categories_wear_2")
        self.frame_categories_wear_2.setFrameShape(QFrame.StyledPanel)
        self.frame_categories_wear_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_categories_wear_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_top_2 = QCheckBox(self.frame_categories_wear_2)
        self.checkBox_top_2.setObjectName(u"checkBox_top_2")
        self.checkBox_top_2.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.gridLayout_3.addWidget(self.checkBox_top_2, 0, 0, 1, 1)

        self.checkBox_dress_2 = QCheckBox(self.frame_categories_wear_2)
        self.checkBox_dress_2.setObjectName(u"checkBox_dress_2")
        self.checkBox_dress_2.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.gridLayout_3.addWidget(self.checkBox_dress_2, 2, 0, 1, 1)

        self.checkBox_headwear_2 = QCheckBox(self.frame_categories_wear_2)
        self.checkBox_headwear_2.setObjectName(u"checkBox_headwear_2")
        self.checkBox_headwear_2.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.gridLayout_3.addWidget(self.checkBox_headwear_2, 4, 0, 1, 1)

        self.checkBox_bottom_2 = QCheckBox(self.frame_categories_wear_2)
        self.checkBox_bottom_2.setObjectName(u"checkBox_bottom_2")
        self.checkBox_bottom_2.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.gridLayout_3.addWidget(self.checkBox_bottom_2, 0, 1, 1, 1)

        self.checkBox_footwear_2 = QCheckBox(self.frame_categories_wear_2)
        self.checkBox_footwear_2.setObjectName(u"checkBox_footwear_2")
        self.checkBox_footwear_2.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.gridLayout_3.addWidget(self.checkBox_footwear_2, 2, 1, 1, 1)

        self.checkBox_accessories_2 = QCheckBox(self.frame_categories_wear_2)
        self.checkBox_accessories_2.setObjectName(u"checkBox_accessories_2")
        self.checkBox_accessories_2.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")

        self.gridLayout_3.addWidget(self.checkBox_accessories_2, 4, 1, 1, 1)


        self.horizontalLayout_8.addWidget(self.frame_categories_wear_2)


        self.verticalLayout_17.addWidget(self.categories_container_2)

        self.frame_addproduct_submit_2 = QFrame(self.frame_addproduct_2)
        self.frame_addproduct_submit_2.setObjectName(u"frame_addproduct_submit_2")
        self.frame_addproduct_submit_2.setMinimumSize(QSize(0, 80))
        self.frame_addproduct_submit_2.setMaximumSize(QSize(16777215, 80))
        self.frame_addproduct_submit_2.setFrameShape(QFrame.StyledPanel)
        self.frame_addproduct_submit_2.setFrameShadow(QFrame.Raised)
        self.canceladdproductbutton_3 = QPushButton(self.frame_addproduct_submit_2)
        self.canceladdproductbutton_3.setObjectName(u"canceladdproductbutton_3")
        self.canceladdproductbutton_3.setGeometry(QRect(502, 10, 157, 49))
        self.canceladdproductbutton_3.setStyleSheet(u"QPushButton {	\n"
"	border-radius: 5px;\n"
"	background: #AEC289;\n"
"	color: #FFF;\n"
"	text-align: center;\n"
"	font-family: Suwannaphum;\n"
"	font-size: 20px;\n"
"	font-style: normal;\n"
"	font-weight: 400;\n"
"	line-height: normal;\n"
"}\n"
"QPushButton:hover {\n"
"	background: #F4DBDB;\n"
"	color: #545454;\n"
"}")
        self.addproductbutton_3 = QPushButton(self.frame_addproduct_submit_2)
        self.addproductbutton_3.setObjectName(u"addproductbutton_3")
        self.addproductbutton_3.setGeometry(QRect(710, 10, 204, 49))
        self.addproductbutton_3.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"	background: #CD4662;\n"
"	color: #FFF;\n"
"	text-align: center;\n"
"	font-family: Suwannaphum;\n"
"	font-size: 20px;\n"
"	font-style: normal;\n"
"	font-weight: 400;\n"
"	line-height: normal;\n"
"}\n"
"QPushButton:hover {\n"
"	background: #F4DBDB;\n"
"	color: #545454;\n"
"}")

        self.verticalLayout_17.addWidget(self.frame_addproduct_submit_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_13)
        self.stackedWidget_adminmain.addWidget(self.nouse_2)
        self.stackedWidget_adminwidget.addWidget(self.adminmain)

        self.gridLayout_adminwidget.addWidget(self.stackedWidget_adminwidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.adminwidget)
        self.userprofile = QWidget()
        self.userprofile.setObjectName(u"userprofile")
        self.verticalLayout = QVBoxLayout(self.userprofile)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea_userprofile = QScrollArea(self.userprofile)
        self.scrollArea_userprofile.setObjectName(u"scrollArea_userprofile")
        self.scrollArea_userprofile.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.scrollArea_userprofile.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 67, 1018))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_userprofile = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_userprofile.setObjectName(u"frame_userprofile")
        self.frame_userprofile.setMinimumSize(QSize(0, 1000))
        self.frame_userprofile.setFrameShape(QFrame.StyledPanel)
        self.frame_userprofile.setFrameShadow(QFrame.Raised)
        self.profilecontainer = QWidget(self.frame_userprofile)
        self.profilecontainer.setObjectName(u"profilecontainer")
        self.profilecontainer.setGeometry(QRect(42, 42, 1151, 180))
        self.profilecontainer.setStyleSheet(u"border-bottom: 3px solid #CD4662;\n"
"background: #FAF9F6;")
        self.profilepic = QLabel(self.profilecontainer)
        self.profilepic.setObjectName(u"profilepic")
        self.profilepic.setGeometry(QRect(30, 0, 140, 140))
        self.profilepic.setStyleSheet(u"border: none;\n"
"border-radius: 70px;\n"
"background: #cd4662;")
        self.usernamelabel = QLabel(self.profilecontainer)
        self.usernamelabel.setObjectName(u"usernamelabel")
        self.usernamelabel.setGeometry(QRect(250, 0, 151, 41))
        self.usernamelabel.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.favloriteabel = QLabel(self.profilecontainer)
        self.favloriteabel.setObjectName(u"favloriteabel")
        self.favloriteabel.setGeometry(QRect(250, 45, 151, 41))
        self.favloriteabel.setStyleSheet(u"border: none;\n"
"color: #AEC289;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.backbutton = QPushButton(self.frame_userprofile)
        self.backbutton.setObjectName(u"backbutton")
        self.backbutton.setGeometry(QRect(0, 10, 20, 31))
        self.backbutton.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/backhomoe.png);")
        self.myordercontainer = QWidget(self.frame_userprofile)
        self.myordercontainer.setObjectName(u"myordercontainer")
        self.myordercontainer.setGeometry(QRect(40, 350, 1151, 157))
        self.myordercontainer.setStyleSheet(u"border-bottom: 3px solid #CD4662;\n"
"background: #FAF9F6;\n"
"")
        self.myorderlabel = QLabel(self.myordercontainer)
        self.myorderlabel.setObjectName(u"myorderlabel")
        self.myorderlabel.setGeometry(QRect(0, 0, 100, 25))
        self.myorderlabel.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.tobeshipbutton = QPushButton(self.myordercontainer)
        self.tobeshipbutton.setObjectName(u"tobeshipbutton")
        self.tobeshipbutton.setGeometry(QRect(250, 40, 90, 90))
        self.tobeshipbutton.setStyleSheet(u"image: url(:/pic/images/newres/tobeshipped.png);\n"
"border: none;")
        self.tobereceivebutton = QPushButton(self.myordercontainer)
        self.tobereceivebutton.setObjectName(u"tobereceivebutton")
        self.tobereceivebutton.setGeometry(QRect(550, 40, 90, 90))
        self.tobereceivebutton.setStyleSheet(u"image: url(:/pic/images/newres/toberecieved.png);\n"
"border: none;")
        self.completebutton = QPushButton(self.myordercontainer)
        self.completebutton.setObjectName(u"completebutton")
        self.completebutton.setGeometry(QRect(850, 40, 90, 90))
        self.completebutton.setStyleSheet(u"image: url(:/pic/images/newres/completed.png);\n"
"border: none;")
        self.favcontainer = QWidget(self.frame_userprofile)
        self.favcontainer.setObjectName(u"favcontainer")
        self.favcontainer.setGeometry(QRect(42, 534, 1151, 440))
        self.favcontainer.setStyleSheet(u"border-bottom: 3px solid #CD4662;\n"
"background: #FAF9F6;")
        self.product_13 = QWidget(self.favcontainer)
        self.product_13.setObjectName(u"product_13")
        self.product_13.setGeometry(QRect(45, 70, 251, 320))
        self.product_13.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;\n"
"border:none;")
        self.picproduct1_15 = QPushButton(self.product_13)
        self.picproduct1_15.setObjectName(u"picproduct1_15")
        self.picproduct1_15.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_15.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.favlabel = QLabel(self.favcontainer)
        self.favlabel.setObjectName(u"favlabel")
        self.favlabel.setGeometry(QRect(0, 0, 100, 25))
        self.favlabel.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.product_14 = QWidget(self.favcontainer)
        self.product_14.setObjectName(u"product_14")
        self.product_14.setGeometry(QRect(450, 70, 251, 320))
        self.product_14.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;\n"
"border:none;")
        self.picproduct1_18 = QPushButton(self.product_14)
        self.picproduct1_18.setObjectName(u"picproduct1_18")
        self.picproduct1_18.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_18.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_15 = QWidget(self.favcontainer)
        self.product_15.setObjectName(u"product_15")
        self.product_15.setGeometry(QRect(855, 70, 251, 320))
        self.product_15.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;\n"
"border:none;")
        self.picproduct1_19 = QPushButton(self.product_15)
        self.picproduct1_19.setObjectName(u"picproduct1_19")
        self.picproduct1_19.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_19.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.viewallfavbutton = QPushButton(self.favcontainer)
        self.viewallfavbutton.setObjectName(u"viewallfavbutton")
        self.viewallfavbutton.setGeometry(QRect(1020, 0, 121, 24))
        self.viewallfavbutton.setStyleSheet(u"color:  #CD4662;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 12px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.openshopbutton = QPushButton(self.frame_userprofile)
        self.openshopbutton.setObjectName(u"openshopbutton")
        self.openshopbutton.setGeometry(QRect(42, 252, 1151, 65))
        self.openshopbutton.setStyleSheet(u"border-radius: 10px;\n"
"background: #F4DBDB;\n"
"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.openshoppic = QLabel(self.frame_userprofile)
        self.openshoppic.setObjectName(u"openshoppic")
        self.openshoppic.setGeometry(QRect(520, 252, 49, 65))
        self.openshoppic.setStyleSheet(u"image: url(:/pic/images/newres/openyourshop.png);\n"
"border: none;\n"
"background: none;")

        self.verticalLayout_2.addWidget(self.frame_userprofile)

        self.scrollArea_userprofile.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout.addWidget(self.scrollArea_userprofile)

        self.stackedWidget.addWidget(self.userprofile)
        self.reviewpage = QWidget()
        self.reviewpage.setObjectName(u"reviewpage")
        self.settingscontainer_2 = QWidget(self.reviewpage)
        self.settingscontainer_2.setObjectName(u"settingscontainer_2")
        self.settingscontainer_2.setGeometry(QRect(60, 60, 1160, 630))
        self.settingscontainer_2.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.verticalLayout_21 = QVBoxLayout(self.settingscontainer_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.scrollArea_settings_2 = QScrollArea(self.settingscontainer_2)
        self.scrollArea_settings_2.setObjectName(u"scrollArea_settings_2")
        self.scrollArea_settings_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_27 = QWidget()
        self.scrollAreaWidgetContents_27.setObjectName(u"scrollAreaWidgetContents_27")
        self.scrollAreaWidgetContents_27.setGeometry(QRect(0, 0, 1127, 1318))
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents_27)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_settings_2 = QFrame(self.scrollAreaWidgetContents_27)
        self.frame_settings_2.setObjectName(u"frame_settings_2")
        self.frame_settings_2.setMinimumSize(QSize(0, 1300))
        self.frame_settings_2.setFrameShape(QFrame.StyledPanel)
        self.frame_settings_2.setFrameShadow(QFrame.Raised)
        self.accsettingslabel_2 = QLabel(self.frame_settings_2)
        self.accsettingslabel_2.setObjectName(u"accsettingslabel_2")
        self.accsettingslabel_2.setGeometry(QRect(417, 10, 290, 61))
        self.accsettingslabel_2.setStyleSheet(u"color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 32px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.accsettingslabel_2.setAlignment(Qt.AlignCenter)
        self.myacclabel_2 = QLabel(self.frame_settings_2)
        self.myacclabel_2.setObjectName(u"myacclabel_2")
        self.myacclabel_2.setGeometry(QRect(48, 70, 181, 61))
        self.myacclabel_2.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.settingslabel_2 = QLabel(self.frame_settings_2)
        self.settingslabel_2.setObjectName(u"settingslabel_2")
        self.settingslabel_2.setGeometry(QRect(48, 140, 131, 61))
        self.settingslabel_2.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.helplabel_2 = QLabel(self.frame_settings_2)
        self.helplabel_2.setObjectName(u"helplabel_2")
        self.helplabel_2.setGeometry(QRect(48, 210, 131, 61))
        self.helplabel_2.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.logoutsettingsbutton_2 = QPushButton(self.frame_settings_2)
        self.logoutsettingsbutton_2.setObjectName(u"logoutsettingsbutton_2")
        self.logoutsettingsbutton_2.setGeometry(QRect(810, 1220, 251, 61))
        self.logoutsettingsbutton_2.setStyleSheet(u"QPushButton {\n"
"                background-color: #cd4662;\n"
"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border-radius: 10px;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }\n"
"\n"
"")
        self.addimageproductcontainer_4 = QWidget(self.frame_settings_2)
        self.addimageproductcontainer_4.setObjectName(u"addimageproductcontainer_4")
        self.addimageproductcontainer_4.setGeometry(QRect(30, 280, 951, 250))
        self.addimageproductcontainer_4.setMinimumSize(QSize(0, 250))
        self.addimageproductcontainer_4.setMaximumSize(QSize(16777215, 250))
        self.addimageproductcontainer_4.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"	padding-top: 10px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	height: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-width: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.horizontalLayout_18 = QHBoxLayout(self.addimageproductcontainer_4)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.scrollArea_addimageproduct_4 = QScrollArea(self.addimageproductcontainer_4)
        self.scrollArea_addimageproduct_4.setObjectName(u"scrollArea_addimageproduct_4")
        self.scrollArea_addimageproduct_4.setMinimumSize(QSize(0, 240))
        self.scrollArea_addimageproduct_4.setMaximumSize(QSize(16777215, 240))
        self.scrollArea_addimageproduct_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_28 = QWidget()
        self.scrollAreaWidgetContents_28.setObjectName(u"scrollAreaWidgetContents_28")
        self.scrollAreaWidgetContents_28.setGeometry(QRect(0, 0, 1218, 210))
        self.scrollAreaWidgetContents_28.setMinimumSize(QSize(0, 210))
        self.scrollAreaWidgetContents_28.setMaximumSize(QSize(16777215, 210))
        self.horizontalLayout_19 = QHBoxLayout(self.scrollAreaWidgetContents_28)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_addimageproduct_4 = QFrame(self.scrollAreaWidgetContents_28)
        self.frame_addimageproduct_4.setObjectName(u"frame_addimageproduct_4")
        self.frame_addimageproduct_4.setMinimumSize(QSize(1200, 210))
        self.frame_addimageproduct_4.setMaximumSize(QSize(16777215, 210))
        self.frame_addimageproduct_4.setFrameShape(QFrame.StyledPanel)
        self.frame_addimageproduct_4.setFrameShadow(QFrame.Raised)
        self.addproductimagelabel_4 = QLabel(self.frame_addimageproduct_4)
        self.addproductimagelabel_4.setObjectName(u"addproductimagelabel_4")
        self.addproductimagelabel_4.setGeometry(QRect(0, 0, 220, 31))
        self.addproductimagelabel_4.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.addimagebutton_4 = QPushButton(self.frame_addimageproduct_4)
        self.addimagebutton_4.setObjectName(u"addimagebutton_4")
        self.addimagebutton_4.setGeometry(QRect(0, 45, 151, 151))
        self.addimagebutton_4.setStyleSheet(u"QPushButton {\n"
"	border: 3px dashed #D9D9D9;\n"
"	font-size: 46px;\n"
"	background: #FAF9F6;\n"
"	color: #D9D9D9;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: #CD4662;\n"
"	color: #CD4662;\n"
"	background-color: #EDEDED;\n"
"}")
        self.addimagebutton_4.setIconSize(QSize(151, 151))
        self.img_4 = QLabel(self.frame_addimageproduct_4)
        self.img_4.setObjectName(u"img_4")
        self.img_4.setGeometry(QRect(5, 50, 141, 141))
        self.img_4.setStyleSheet(u"image: url(:/pic/product_img/IMG_2025.JPG)")
        self.img_4.setAlignment(Qt.AlignCenter)
        self.delete_pic_button_4 = QPushButton(self.frame_addimageproduct_4)
        self.delete_pic_button_4.setObjectName(u"delete_pic_button_4")
        self.delete_pic_button_4.setEnabled(True)
        self.delete_pic_button_4.setGeometry(QRect(130, 30, 31, 32))
        self.delete_pic_button_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_pic_button_4.setAutoFillBackground(False)
        self.delete_pic_button_4.setStyleSheet(u"QPushButton {\n"
"	border-radius: 25px;\n"
"	border-color: rgb(217, 217, 217);\n"
"	border-width: 2px;\n"
"	background: #FAF9F6;\n"
"	color: #D9D9D9;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: #CD4662;\n"
"	color: rgb(116,23,17);\n"
"	background-color: rgb(237,106,94);\n"
"}")

        self.horizontalLayout_19.addWidget(self.frame_addimageproduct_4)

        self.scrollArea_addimageproduct_4.setWidget(self.scrollAreaWidgetContents_28)

        self.horizontalLayout_18.addWidget(self.scrollArea_addimageproduct_4)

        self.myacclabel_3 = QLabel(self.frame_settings_2)
        self.myacclabel_3.setObjectName(u"myacclabel_3")
        self.myacclabel_3.setGeometry(QRect(48, 570, 201, 61))
        self.myacclabel_3.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.myacclabel_5 = QLabel(self.frame_settings_2)
        self.myacclabel_5.setObjectName(u"myacclabel_5")
        self.myacclabel_5.setGeometry(QRect(48, 640, 181, 61))
        self.myacclabel_5.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.myacclabel_6 = QLabel(self.frame_settings_2)
        self.myacclabel_6.setObjectName(u"myacclabel_6")
        self.myacclabel_6.setGeometry(QRect(48, 710, 181, 61))
        self.myacclabel_6.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.curpasstextbox_2 = QLineEdit(self.frame_settings_2)
        self.curpasstextbox_2.setObjectName(u"curpasstextbox_2")
        self.curpasstextbox_2.setGeometry(QRect(300, 80, 681, 41))
        self.curpasstextbox_2.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.curpasstextbox_4 = QLineEdit(self.frame_settings_2)
        self.curpasstextbox_4.setObjectName(u"curpasstextbox_4")
        self.curpasstextbox_4.setGeometry(QRect(300, 150, 681, 41))
        self.curpasstextbox_4.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.curpasstextbox_5 = QLineEdit(self.frame_settings_2)
        self.curpasstextbox_5.setObjectName(u"curpasstextbox_5")
        self.curpasstextbox_5.setGeometry(QRect(300, 220, 681, 41))
        self.curpasstextbox_5.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.curpasstextbox_6 = QLineEdit(self.frame_settings_2)
        self.curpasstextbox_6.setObjectName(u"curpasstextbox_6")
        self.curpasstextbox_6.setGeometry(QRect(300, 580, 681, 41))
        self.curpasstextbox_6.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.curpasstextbox_7 = QLineEdit(self.frame_settings_2)
        self.curpasstextbox_7.setObjectName(u"curpasstextbox_7")
        self.curpasstextbox_7.setGeometry(QRect(300, 650, 681, 41))
        self.curpasstextbox_7.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.curpasstextbox_8 = QLineEdit(self.frame_settings_2)
        self.curpasstextbox_8.setObjectName(u"curpasstextbox_8")
        self.curpasstextbox_8.setGeometry(QRect(300, 720, 681, 461))
        self.curpasstextbox_8.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.curpasstextbox_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_22.addWidget(self.frame_settings_2)

        self.scrollArea_settings_2.setWidget(self.scrollAreaWidgetContents_27)

        self.verticalLayout_21.addWidget(self.scrollArea_settings_2)

        self.backbutton_settings_2 = QPushButton(self.reviewpage)
        self.backbutton_settings_2.setObjectName(u"backbutton_settings_2")
        self.backbutton_settings_2.setGeometry(QRect(20, 30, 20, 31))
        self.backbutton_settings_2.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/backhomoe.png);")
        self.stackedWidget.addWidget(self.reviewpage)
        self.editprofile = QWidget()
        self.editprofile.setObjectName(u"editprofile")
        self.editprofile.setStyleSheet(u"background: #FAF9F6;")
        self.editprofilecontainer = QWidget(self.editprofile)
        self.editprofilecontainer.setObjectName(u"editprofilecontainer")
        self.editprofilecontainer.setGeometry(QRect(60, 60, 1160, 630))
        self.editprofilecontainer.setStyleSheet(u"background: #FAF9F6;")
        self.textboxeditcontainer = QWidget(self.editprofilecontainer)
        self.textboxeditcontainer.setObjectName(u"textboxeditcontainer")
        self.textboxeditcontainer.setGeometry(QRect(300, 0, 830, 600))
        self.textboxeditcontainer.setStyleSheet(u"border-radius: 20px;\n"
"background: #F4DBDB;")
        self.editlabel = QLabel(self.textboxeditcontainer)
        self.editlabel.setObjectName(u"editlabel")
        self.editlabel.setGeometry(QRect(43, 34, 171, 51))
        self.editlabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.userabel = QLabel(self.textboxeditcontainer)
        self.userabel.setObjectName(u"userabel")
        self.userabel.setGeometry(QRect(43, 100, 121, 31))
        self.userabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.fisrtlabel = QLabel(self.textboxeditcontainer)
        self.fisrtlabel.setObjectName(u"fisrtlabel")
        self.fisrtlabel.setGeometry(QRect(43, 200, 121, 31))
        self.fisrtlabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.lastlabel = QLabel(self.textboxeditcontainer)
        self.lastlabel.setObjectName(u"lastlabel")
        self.lastlabel.setGeometry(QRect(450, 200, 121, 31))
        self.lastlabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.genlabel = QLabel(self.textboxeditcontainer)
        self.genlabel.setObjectName(u"genlabel")
        self.genlabel.setGeometry(QRect(43, 300, 121, 31))
        self.genlabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.birthlabel = QLabel(self.textboxeditcontainer)
        self.birthlabel.setObjectName(u"birthlabel")
        self.birthlabel.setGeometry(QRect(450, 300, 121, 31))
        self.birthlabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.pholabel = QLabel(self.textboxeditcontainer)
        self.pholabel.setObjectName(u"pholabel")
        self.pholabel.setGeometry(QRect(43, 400, 121, 31))
        self.pholabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.emaillabel_2 = QLabel(self.textboxeditcontainer)
        self.emaillabel_2.setObjectName(u"emaillabel_2")
        self.emaillabel_2.setGeometry(QRect(450, 400, 121, 31))
        self.emaillabel_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.userbox = QLineEdit(self.textboxeditcontainer)
        self.userbox.setObjectName(u"userbox")
        self.userbox.setGeometry(QRect(43, 150, 341, 31))
        self.userbox.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.firstnamebox = QLineEdit(self.textboxeditcontainer)
        self.firstnamebox.setObjectName(u"firstnamebox")
        self.firstnamebox.setGeometry(QRect(43, 250, 341, 31))
        self.firstnamebox.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.genderbox = QLineEdit(self.textboxeditcontainer)
        self.genderbox.setObjectName(u"genderbox")
        self.genderbox.setGeometry(QRect(43, 350, 341, 31))
        self.genderbox.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.phonebox = QLineEdit(self.textboxeditcontainer)
        self.phonebox.setObjectName(u"phonebox")
        self.phonebox.setGeometry(QRect(43, 450, 341, 31))
        self.phonebox.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.lastnamebox = QLineEdit(self.textboxeditcontainer)
        self.lastnamebox.setObjectName(u"lastnamebox")
        self.lastnamebox.setGeometry(QRect(450, 250, 341, 31))
        self.lastnamebox.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.emailbox = QLineEdit(self.textboxeditcontainer)
        self.emailbox.setObjectName(u"emailbox")
        self.emailbox.setGeometry(QRect(450, 450, 341, 31))
        self.emailbox.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.savechangebutton_2 = QPushButton(self.textboxeditcontainer)
        self.savechangebutton_2.setObjectName(u"savechangebutton_2")
        self.savechangebutton_2.setGeometry(QRect(590, 530, 201, 41))
        self.savechangebutton_2.setStyleSheet(u"color: #FFF;\n"
"background: #AEC289;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border-radius: 10px;")
        self.deleteaccbutton = QPushButton(self.textboxeditcontainer)
        self.deleteaccbutton.setObjectName(u"deleteaccbutton")
        self.deleteaccbutton.setGeometry(QRect(350, 530, 201, 41))
        self.deleteaccbutton.setStyleSheet(u"color: #FFF;\n"
"background: #cd4662;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border-radius: 10px;")
        self.birthdaydateEdit = QDateEdit(self.textboxeditcontainer)
        self.birthdaydateEdit.setObjectName(u"birthdaydateEdit")
        self.birthdaydateEdit.setGeometry(QRect(450, 350, 341, 31))
        self.birthdaydateEdit.setStyleSheet(u"QDateTimeEdit {\n"
"	background-color: #F4F2EF; \n"
"	font-size: 16px;\n"
"	border: 2px solid #CD4662; \n"
"	padding: 5px;\n"
"	border-radius: 5px; \n"
"}\n"
"QDateTimeEdit::down-button, QDateTimeEdit::up-button {\n"
"	width: 20px; \n"
"	height: 13px;\n"
"	background-color: #F4F2EF; \n"
"	border: 2px solid #CD4662; \n"
"	font-size: 16px;\n"
"}\n"
"QDateTimeEdit::down-button {\n"
"	subcontrol-origin: border;\n"
"	subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QDateTimeEdit::up-button {\n"
"	subcontrol-origin: border;\n"
"	subcontrol-position: top right;\n"
"}\n"
"    \n"
"QDateTimeEdit::down-button:pressed, QDateTimeEdit::up-button:pressed {\n"
"	background-color: #CD4662;\n"
"}\n"
"    \n"
"QDateTimeEdit::down-arrow, QDateTimeEdit::up-arrow {\n"
"	image: url(arrow.png); \n"
"}")
        self.birthdaydateEdit.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.editprofilepic = QLabel(self.editprofilecontainer)
        self.editprofilepic.setObjectName(u"editprofilepic")
        self.editprofilepic.setGeometry(QRect(40, 0, 160, 160))
        self.editprofilepic.setStyleSheet(u"border: none;\n"
"border-radius: 80px;\n"
"background: #cd4662;")
        self.editnameprofile = QLabel(self.editprofilecontainer)
        self.editnameprofile.setObjectName(u"editnameprofile")
        self.editnameprofile.setGeometry(QRect(40, 190, 165, 41))
        self.editnameprofile.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.editnameprofile.setAlignment(Qt.AlignCenter)
        self.backbutton_2 = QPushButton(self.editprofile)
        self.backbutton_2.setObjectName(u"backbutton_2")
        self.backbutton_2.setGeometry(QRect(20, 30, 20, 31))
        self.backbutton_2.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/backhomoe.png);")
        self.stackedWidget.addWidget(self.editprofile)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.stackedWidget_settings = QStackedWidget(self.settings)
        self.stackedWidget_settings.setObjectName(u"stackedWidget_settings")
        self.stackedWidget_settings.setGeometry(QRect(0, 0, 1280, 720))
        self.stackedWidget_settings.setStyleSheet(u"background-color: #FAF9F6;")
        self.settingsmainpage = QWidget()
        self.settingsmainpage.setObjectName(u"settingsmainpage")
        self.settingscontainer = QWidget(self.settingsmainpage)
        self.settingscontainer.setObjectName(u"settingscontainer")
        self.settingscontainer.setGeometry(QRect(60, 60, 1160, 630))
        self.settingscontainer.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.settingscontainer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scrollArea_settings = QScrollArea(self.settingscontainer)
        self.scrollArea_settings.setObjectName(u"scrollArea_settings")
        self.scrollArea_settings.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 1127, 868))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_settings = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_settings.setObjectName(u"frame_settings")
        self.frame_settings.setMinimumSize(QSize(0, 850))
        self.frame_settings.setFrameShape(QFrame.StyledPanel)
        self.frame_settings.setFrameShadow(QFrame.Raised)
        self.accsettingslabel = QLabel(self.frame_settings)
        self.accsettingslabel.setObjectName(u"accsettingslabel")
        self.accsettingslabel.setGeometry(QRect(417, 10, 290, 61))
        self.accsettingslabel.setStyleSheet(u"color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 32px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.accsettingslabel.setAlignment(Qt.AlignCenter)
        self.myacclabel = QLabel(self.frame_settings)
        self.myacclabel.setObjectName(u"myacclabel")
        self.myacclabel.setGeometry(QRect(30, 70, 131, 61))
        self.myacclabel.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.accountbutton = QPushButton(self.frame_settings)
        self.accountbutton.setObjectName(u"accountbutton")
        self.accountbutton.setGeometry(QRect(30, 140, 1051, 61))
        self.accountbutton.setStyleSheet(u"QPushButton {\n"
"                background-color: #D9D9D9;\n"
"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }")
        self.settingslabel = QLabel(self.frame_settings)
        self.settingslabel.setObjectName(u"settingslabel")
        self.settingslabel.setGeometry(QRect(30, 310, 131, 61))
        self.settingslabel.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.changepassbutton = QPushButton(self.frame_settings)
        self.changepassbutton.setObjectName(u"changepassbutton")
        self.changepassbutton.setGeometry(QRect(30, 470, 1051, 61))
        self.changepassbutton.setStyleSheet(u"QPushButton {\n"
"                background-color: #D9D9D9;\n"
"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }")
        self.editprobutton = QPushButton(self.frame_settings)
        self.editprobutton.setObjectName(u"editprobutton")
        self.editprobutton.setGeometry(QRect(30, 380, 1051, 61))
        self.editprobutton.setStyleSheet(u"QPushButton {\n"
"                background-color: #D9D9D9;\n"
"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }")
        self.helplabel = QLabel(self.frame_settings)
        self.helplabel.setObjectName(u"helplabel")
        self.helplabel.setGeometry(QRect(30, 540, 131, 61))
        self.helplabel.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.rulebutton = QPushButton(self.frame_settings)
        self.rulebutton.setObjectName(u"rulebutton")
        self.rulebutton.setGeometry(QRect(30, 610, 1051, 61))
        self.rulebutton.setStyleSheet(u"QPushButton {\n"
"                background-color: #D9D9D9;\n"
"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }")
        self.logoutsettingsbutton = QPushButton(self.frame_settings)
        self.logoutsettingsbutton.setObjectName(u"logoutsettingsbutton")
        self.logoutsettingsbutton.setGeometry(QRect(30, 740, 1051, 61))
        self.logoutsettingsbutton.setStyleSheet(u"QPushButton {\n"
"                background-color: #cd4662;\n"
"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }")
        self.addressbutton = QPushButton(self.frame_settings)
        self.addressbutton.setObjectName(u"addressbutton")
        self.addressbutton.setGeometry(QRect(30, 230, 1051, 61))
        self.addressbutton.setStyleSheet(u"QPushButton {\n"
"                background-color: #D9D9D9;\n"
"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }")

        self.verticalLayout_7.addWidget(self.frame_settings)

        self.scrollArea_settings.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_6.addWidget(self.scrollArea_settings)

        self.backbutton_settings = QPushButton(self.settingsmainpage)
        self.backbutton_settings.setObjectName(u"backbutton_settings")
        self.backbutton_settings.setGeometry(QRect(20, 30, 20, 31))
        self.backbutton_settings.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/backhomoe.png);")
        self.stackedWidget_settings.addWidget(self.settingsmainpage)
        self.addresssettingspage = QWidget()
        self.addresssettingspage.setObjectName(u"addresssettingspage")
        self.editprofilecontainer_4 = QWidget(self.addresssettingspage)
        self.editprofilecontainer_4.setObjectName(u"editprofilecontainer_4")
        self.editprofilecontainer_4.setGeometry(QRect(60, 60, 1160, 321))
        self.editprofilecontainer_4.setStyleSheet(u"background: #FAF9F6;")
        self.textboxeditcontainer_12 = QWidget(self.editprofilecontainer_4)
        self.textboxeditcontainer_12.setObjectName(u"textboxeditcontainer_12")
        self.textboxeditcontainer_12.setGeometry(QRect(29, 0, 1101, 321))
        self.textboxeditcontainer_12.setStyleSheet(u"border-radius: 20px;\n"
"background: #F4DBDB;")
        self.addressdisplaylabel_3 = QLabel(self.textboxeditcontainer_12)
        self.addressdisplaylabel_3.setObjectName(u"addressdisplaylabel_3")
        self.addressdisplaylabel_3.setGeometry(QRect(470, 10, 160, 51))
        self.addressdisplaylabel_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.addressdisplaylabel_3.setAlignment(Qt.AlignCenter)
        self.fisrtnameaddress_3 = QLabel(self.textboxeditcontainer_12)
        self.fisrtnameaddress_3.setObjectName(u"fisrtnameaddress_3")
        self.fisrtnameaddress_3.setGeometry(QRect(30, 60, 121, 31))
        self.fisrtnameaddress_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.lastnameaddress_3 = QLabel(self.textboxeditcontainer_12)
        self.lastnameaddress_3.setObjectName(u"lastnameaddress_3")
        self.lastnameaddress_3.setGeometry(QRect(340, 60, 101, 31))
        self.lastnameaddress_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.addressaddress_3 = QLabel(self.textboxeditcontainer_12)
        self.addressaddress_3.setObjectName(u"addressaddress_3")
        self.addressaddress_3.setGeometry(QRect(30, 100, 161, 31))
        self.addressaddress_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.phoneaddress_3 = QLabel(self.textboxeditcontainer_12)
        self.phoneaddress_3.setObjectName(u"phoneaddress_3")
        self.phoneaddress_3.setGeometry(QRect(590, 60, 61, 31))
        self.phoneaddress_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.firstnameaddressdisplay_3 = QLabel(self.textboxeditcontainer_12)
        self.firstnameaddressdisplay_3.setObjectName(u"firstnameaddressdisplay_3")
        self.firstnameaddressdisplay_3.setGeometry(QRect(180, 60, 121, 31))
        self.firstnameaddressdisplay_3.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.firstnameaddressdisplay_3.setAlignment(Qt.AlignCenter)
        self.phoneaddressdisplay_3 = QLabel(self.textboxeditcontainer_12)
        self.phoneaddressdisplay_3.setObjectName(u"phoneaddressdisplay_3")
        self.phoneaddressdisplay_3.setGeometry(QRect(700, 60, 201, 31))
        self.phoneaddressdisplay_3.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.phoneaddressdisplay_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lastnameaddressdisplay_3 = QLabel(self.textboxeditcontainer_12)
        self.lastnameaddressdisplay_3.setObjectName(u"lastnameaddressdisplay_3")
        self.lastnameaddressdisplay_3.setGeometry(QRect(450, 60, 101, 31))
        self.lastnameaddressdisplay_3.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.lastnameaddressdisplay_3.setAlignment(Qt.AlignCenter)
        self.addressaddressdisplay_3 = QLabel(self.textboxeditcontainer_12)
        self.addressaddressdisplay_3.setObjectName(u"addressaddressdisplay_3")
        self.addressaddressdisplay_3.setGeometry(QRect(180, 100, 871, 141))
        self.addressaddressdisplay_3.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.addressaddressdisplay_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.editaddressbutton = QPushButton(self.textboxeditcontainer_12)
        self.editaddressbutton.setObjectName(u"editaddressbutton")
        self.editaddressbutton.setGeometry(QRect(860, 260, 201, 41))
        self.editaddressbutton.setStyleSheet(u"color: #FFF;\n"
"background: #AEC289;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border-radius: 10px;")
        self.backtomainsettingbutton_5 = QPushButton(self.addresssettingspage)
        self.backtomainsettingbutton_5.setObjectName(u"backtomainsettingbutton_5")
        self.backtomainsettingbutton_5.setGeometry(QRect(20, 30, 20, 31))
        self.backtomainsettingbutton_5.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/backhomoe.png);")
        self.stackedWidget_settings.addWidget(self.addresssettingspage)
        self.editaddresssettingspage = QWidget()
        self.editaddresssettingspage.setObjectName(u"editaddresssettingspage")
        self.editprofilecontainer_5 = QWidget(self.editaddresssettingspage)
        self.editprofilecontainer_5.setObjectName(u"editprofilecontainer_5")
        self.editprofilecontainer_5.setGeometry(QRect(60, 60, 1160, 571))
        self.editprofilecontainer_5.setStyleSheet(u"background: #FAF9F6;")
        self.textboxeditcontainer_6 = QWidget(self.editprofilecontainer_5)
        self.textboxeditcontainer_6.setObjectName(u"textboxeditcontainer_6")
        self.textboxeditcontainer_6.setGeometry(QRect(29, 0, 1101, 571))
        self.textboxeditcontainer_6.setStyleSheet(u"border-radius: 20px;\n"
"background: #F4DBDB;")
        self.editaddrlabel = QLabel(self.textboxeditcontainer_6)
        self.editaddrlabel.setObjectName(u"editaddrlabel")
        self.editaddrlabel.setGeometry(QRect(449, 10, 191, 51))
        self.editaddrlabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.editaddrlabel.setAlignment(Qt.AlignCenter)
        self.firstnameeditaddr = QLabel(self.textboxeditcontainer_6)
        self.firstnameeditaddr.setObjectName(u"firstnameeditaddr")
        self.firstnameeditaddr.setGeometry(QRect(30, 80, 121, 31))
        self.firstnameeditaddr.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.lastnameeditaddr = QLabel(self.textboxeditcontainer_6)
        self.lastnameeditaddr.setObjectName(u"lastnameeditaddr")
        self.lastnameeditaddr.setGeometry(QRect(600, 80, 121, 31))
        self.lastnameeditaddr.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.addresseditaddr = QLabel(self.textboxeditcontainer_6)
        self.addresseditaddr.setObjectName(u"addresseditaddr")
        self.addresseditaddr.setGeometry(QRect(30, 180, 161, 31))
        self.addresseditaddr.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.phoneeditaddr = QLabel(self.textboxeditcontainer_6)
        self.phoneeditaddr.setObjectName(u"phoneeditaddr")
        self.phoneeditaddr.setGeometry(QRect(30, 130, 121, 31))
        self.phoneeditaddr.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.savechangeeditaddrbutton = QPushButton(self.textboxeditcontainer_6)
        self.savechangeeditaddrbutton.setObjectName(u"savechangeeditaddrbutton")
        self.savechangeeditaddrbutton.setGeometry(QRect(880, 510, 201, 41))
        self.savechangeeditaddrbutton.setStyleSheet(u"color: #FFF;\n"
"background: #AEC289;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border-radius: 10px;")
        self.firstnameeditaddrbox = QLineEdit(self.textboxeditcontainer_6)
        self.firstnameeditaddrbox.setObjectName(u"firstnameeditaddrbox")
        self.firstnameeditaddrbox.setGeometry(QRect(220, 80, 341, 31))
        self.firstnameeditaddrbox.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.lastnameeditaddrbox = QLineEdit(self.textboxeditcontainer_6)
        self.lastnameeditaddrbox.setObjectName(u"lastnameeditaddrbox")
        self.lastnameeditaddrbox.setGeometry(QRect(740, 80, 341, 31))
        self.lastnameeditaddrbox.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.lastnameeditaddrbox.setReadOnly(False)
        self.phoneeditaddrbox = QLineEdit(self.textboxeditcontainer_6)
        self.phoneeditaddrbox.setObjectName(u"phoneeditaddrbox")
        self.phoneeditaddrbox.setGeometry(QRect(220, 130, 341, 31))
        self.phoneeditaddrbox.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.addresseditaddrbox = QLineEdit(self.textboxeditcontainer_6)
        self.addresseditaddrbox.setObjectName(u"addresseditaddrbox")
        self.addresseditaddrbox.setGeometry(QRect(220, 180, 861, 311))
        self.addresseditaddrbox.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.addresseditaddrbox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.cleardataeditaddrbutton = QPushButton(self.textboxeditcontainer_6)
        self.cleardataeditaddrbutton.setObjectName(u"cleardataeditaddrbutton")
        self.cleardataeditaddrbutton.setGeometry(QRect(650, 510, 201, 41))
        self.cleardataeditaddrbutton.setStyleSheet(u"color: #FFF;\n"
"background: #cd4662;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border-radius: 10px;")
        self.backtoeditarresssettingbutton = QPushButton(self.editaddresssettingspage)
        self.backtoeditarresssettingbutton.setObjectName(u"backtoeditarresssettingbutton")
        self.backtoeditarresssettingbutton.setGeometry(QRect(20, 30, 20, 31))
        self.backtoeditarresssettingbutton.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/backhomoe.png);")
        self.stackedWidget_settings.addWidget(self.editaddresssettingspage)
        self.changepasswordpage = QWidget()
        self.changepasswordpage.setObjectName(u"changepasswordpage")
        self.backtomainsettingbutton_2 = QPushButton(self.changepasswordpage)
        self.backtomainsettingbutton_2.setObjectName(u"backtomainsettingbutton_2")
        self.backtomainsettingbutton_2.setGeometry(QRect(20, 30, 20, 31))
        self.backtomainsettingbutton_2.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/backhomoe.png);")
        self.changepasswordcontainer = QWidget(self.changepasswordpage)
        self.changepasswordcontainer.setObjectName(u"changepasswordcontainer")
        self.changepasswordcontainer.setGeometry(QRect(60, 60, 1160, 630))
        self.changepasswordcontainer.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}\n"
"")
        self.verticalLayout_10 = QVBoxLayout(self.changepasswordcontainer)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.scrollArea_changepassword = QScrollArea(self.changepasswordcontainer)
        self.scrollArea_changepassword.setObjectName(u"scrollArea_changepassword")
        self.scrollArea_changepassword.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 1127, 1518))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_changepassword = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_changepassword.setObjectName(u"frame_changepassword")
        self.frame_changepassword.setMinimumSize(QSize(0, 1500))
        self.frame_changepassword.setFrameShape(QFrame.StyledPanel)
        self.frame_changepassword.setFrameShadow(QFrame.Raised)
        self.changepasswordlabel = QLabel(self.frame_changepassword)
        self.changepasswordlabel.setObjectName(u"changepasswordlabel")
        self.changepasswordlabel.setGeometry(QRect(417, 10, 290, 61))
        self.changepasswordlabel.setStyleSheet(u"color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 32px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.changepasswordlabel.setAlignment(Qt.AlignCenter)
        self.currentpasslabel = QLabel(self.frame_changepassword)
        self.currentpasslabel.setObjectName(u"currentpasslabel")
        self.currentpasslabel.setGeometry(QRect(40, 100, 221, 51))
        self.currentpasslabel.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.savechangebutton_4 = QPushButton(self.frame_changepassword)
        self.savechangebutton_4.setObjectName(u"savechangebutton_4")
        self.savechangebutton_4.setGeometry(QRect(860, 510, 201, 41))
        self.savechangebutton_4.setStyleSheet(u"color: #FFF;\n"
"background: #AEC289;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border-radius: 10px;")
        self.newpasslabel = QLabel(self.frame_changepassword)
        self.newpasslabel.setObjectName(u"newpasslabel")
        self.newpasslabel.setGeometry(QRect(40, 270, 221, 51))
        self.newpasslabel.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.curpasstextbox = QLineEdit(self.frame_changepassword)
        self.curpasstextbox.setObjectName(u"curpasstextbox")
        self.curpasstextbox.setGeometry(QRect(40, 180, 481, 41))
        self.curpasstextbox.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.newpasstextbox = QLineEdit(self.frame_changepassword)
        self.newpasstextbox.setObjectName(u"newpasstextbox")
        self.newpasstextbox.setGeometry(QRect(40, 350, 481, 41))
        self.newpasstextbox.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")

        self.verticalLayout_13.addWidget(self.frame_changepassword)

        self.scrollArea_changepassword.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_10.addWidget(self.scrollArea_changepassword)

        self.stackedWidget_settings.addWidget(self.changepasswordpage)
        self.accountpage = QWidget()
        self.accountpage.setObjectName(u"accountpage")
        self.backtomainsettingbutton_4 = QPushButton(self.accountpage)
        self.backtomainsettingbutton_4.setObjectName(u"backtomainsettingbutton_4")
        self.backtomainsettingbutton_4.setGeometry(QRect(20, 30, 20, 31))
        self.backtomainsettingbutton_4.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/backhomoe.png);")
        self.editprofilecontainer_3 = QWidget(self.accountpage)
        self.editprofilecontainer_3.setObjectName(u"editprofilecontainer_3")
        self.editprofilecontainer_3.setGeometry(QRect(60, 60, 1160, 441))
        self.editprofilecontainer_3.setStyleSheet(u"background: #FAF9F6;")
        self.textboxeditcontainer_4 = QWidget(self.editprofilecontainer_3)
        self.textboxeditcontainer_4.setObjectName(u"textboxeditcontainer_4")
        self.textboxeditcontainer_4.setGeometry(QRect(29, 0, 1101, 441))
        self.textboxeditcontainer_4.setStyleSheet(u"border-radius: 20px;\n"
"background: #F4DBDB;")
        self.profilelabel = QLabel(self.textboxeditcontainer_4)
        self.profilelabel.setObjectName(u"profilelabel")
        self.profilelabel.setGeometry(QRect(470, 10, 160, 51))
        self.profilelabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.profilelabel.setAlignment(Qt.AlignCenter)
        self.usernameprofile = QLabel(self.textboxeditcontainer_4)
        self.usernameprofile.setObjectName(u"usernameprofile")
        self.usernameprofile.setGeometry(QRect(60, 270, 121, 31))
        self.usernameprofile.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.fisrtnameprofile = QLabel(self.textboxeditcontainer_4)
        self.fisrtnameprofile.setObjectName(u"fisrtnameprofile")
        self.fisrtnameprofile.setGeometry(QRect(400, 270, 121, 31))
        self.fisrtnameprofile.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.lastnameprofile = QLabel(self.textboxeditcontainer_4)
        self.lastnameprofile.setObjectName(u"lastnameprofile")
        self.lastnameprofile.setGeometry(QRect(770, 270, 121, 31))
        self.lastnameprofile.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.genderprofile = QLabel(self.textboxeditcontainer_4)
        self.genderprofile.setObjectName(u"genderprofile")
        self.genderprofile.setGeometry(QRect(400, 330, 111, 31))
        self.genderprofile.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.birthprofile = QLabel(self.textboxeditcontainer_4)
        self.birthprofile.setObjectName(u"birthprofile")
        self.birthprofile.setGeometry(QRect(60, 330, 101, 31))
        self.birthprofile.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.phoneprofile = QLabel(self.textboxeditcontainer_4)
        self.phoneprofile.setObjectName(u"phoneprofile")
        self.phoneprofile.setGeometry(QRect(770, 330, 71, 31))
        self.phoneprofile.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.emailprofile = QLabel(self.textboxeditcontainer_4)
        self.emailprofile.setObjectName(u"emailprofile")
        self.emailprofile.setGeometry(QRect(60, 390, 61, 31))
        self.emailprofile.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.pictureprofile = QLabel(self.textboxeditcontainer_4)
        self.pictureprofile.setObjectName(u"pictureprofile")
        self.pictureprofile.setGeometry(QRect(470, 70, 160, 160))
        self.pictureprofile.setStyleSheet(u"border: none;\n"
"border-radius: 80px;\n"
"background: #cd4662;")
        self.username = QLabel(self.textboxeditcontainer_4)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(180, 270, 121, 31))
        self.username.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.username.setAlignment(Qt.AlignCenter)
        self.firstname = QLabel(self.textboxeditcontainer_4)
        self.firstname.setObjectName(u"firstname")
        self.firstname.setGeometry(QRect(520, 270, 165, 31))
        self.firstname.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.firstname.setAlignment(Qt.AlignCenter)
        self.gender = QLabel(self.textboxeditcontainer_4)
        self.gender.setObjectName(u"gender")
        self.gender.setGeometry(QRect(514, 330, 151, 31))
        self.gender.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.gender.setAlignment(Qt.AlignCenter)
        self.phone = QLabel(self.textboxeditcontainer_4)
        self.phone.setObjectName(u"phone")
        self.phone.setGeometry(QRect(870, 330, 165, 31))
        self.phone.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.phone.setAlignment(Qt.AlignCenter)
        self.lastname = QLabel(self.textboxeditcontainer_4)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setGeometry(QRect(890, 270, 165, 31))
        self.lastname.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.lastname.setAlignment(Qt.AlignCenter)
        self.birthday = QLabel(self.textboxeditcontainer_4)
        self.birthday.setObjectName(u"birthday")
        self.birthday.setGeometry(QRect(164, 330, 151, 31))
        self.birthday.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.birthday.setAlignment(Qt.AlignCenter)
        self.email = QLabel(self.textboxeditcontainer_4)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(140, 390, 281, 31))
        self.email.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.email.setAlignment(Qt.AlignCenter)
        self.stackedWidget_settings.addWidget(self.accountpage)
        self.editprofilesettingspage = QWidget()
        self.editprofilesettingspage.setObjectName(u"editprofilesettingspage")
        self.editprofilecontainer_2 = QWidget(self.editprofilesettingspage)
        self.editprofilecontainer_2.setObjectName(u"editprofilecontainer_2")
        self.editprofilecontainer_2.setGeometry(QRect(60, 60, 1160, 630))
        self.editprofilecontainer_2.setStyleSheet(u"background: #FAF9F6;")
        self.textboxeditcontainer_3 = QWidget(self.editprofilecontainer_2)
        self.textboxeditcontainer_3.setObjectName(u"textboxeditcontainer_3")
        self.textboxeditcontainer_3.setGeometry(QRect(300, 0, 830, 600))
        self.textboxeditcontainer_3.setStyleSheet(u"border-radius: 20px;\n"
"background: #F4DBDB;")
        self.editlabel_2 = QLabel(self.textboxeditcontainer_3)
        self.editlabel_2.setObjectName(u"editlabel_2")
        self.editlabel_2.setGeometry(QRect(43, 34, 171, 51))
        self.editlabel_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.userabel_2 = QLabel(self.textboxeditcontainer_3)
        self.userabel_2.setObjectName(u"userabel_2")
        self.userabel_2.setGeometry(QRect(43, 100, 121, 31))
        self.userabel_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.fisrtlabel_2 = QLabel(self.textboxeditcontainer_3)
        self.fisrtlabel_2.setObjectName(u"fisrtlabel_2")
        self.fisrtlabel_2.setGeometry(QRect(43, 200, 121, 31))
        self.fisrtlabel_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.lastlabel_2 = QLabel(self.textboxeditcontainer_3)
        self.lastlabel_2.setObjectName(u"lastlabel_2")
        self.lastlabel_2.setGeometry(QRect(450, 200, 121, 31))
        self.lastlabel_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.genlabel_2 = QLabel(self.textboxeditcontainer_3)
        self.genlabel_2.setObjectName(u"genlabel_2")
        self.genlabel_2.setGeometry(QRect(43, 300, 121, 31))
        self.genlabel_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.birthlabel_2 = QLabel(self.textboxeditcontainer_3)
        self.birthlabel_2.setObjectName(u"birthlabel_2")
        self.birthlabel_2.setGeometry(QRect(450, 300, 121, 31))
        self.birthlabel_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.pholabel_2 = QLabel(self.textboxeditcontainer_3)
        self.pholabel_2.setObjectName(u"pholabel_2")
        self.pholabel_2.setGeometry(QRect(43, 400, 121, 31))
        self.pholabel_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.emaillabel_3 = QLabel(self.textboxeditcontainer_3)
        self.emaillabel_3.setObjectName(u"emaillabel_3")
        self.emaillabel_3.setGeometry(QRect(450, 400, 121, 31))
        self.emaillabel_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.userbox_2 = QLineEdit(self.textboxeditcontainer_3)
        self.userbox_2.setObjectName(u"userbox_2")
        self.userbox_2.setGeometry(QRect(43, 150, 341, 31))
        self.userbox_2.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.firstnamebox_2 = QLineEdit(self.textboxeditcontainer_3)
        self.firstnamebox_2.setObjectName(u"firstnamebox_2")
        self.firstnamebox_2.setGeometry(QRect(43, 250, 341, 31))
        self.firstnamebox_2.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.genderbox_2 = QLineEdit(self.textboxeditcontainer_3)
        self.genderbox_2.setObjectName(u"genderbox_2")
        self.genderbox_2.setGeometry(QRect(43, 350, 341, 31))
        self.genderbox_2.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.phonebox_2 = QLineEdit(self.textboxeditcontainer_3)
        self.phonebox_2.setObjectName(u"phonebox_2")
        self.phonebox_2.setGeometry(QRect(43, 450, 341, 31))
        self.phonebox_2.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.lastnamebox_2 = QLineEdit(self.textboxeditcontainer_3)
        self.lastnamebox_2.setObjectName(u"lastnamebox_2")
        self.lastnamebox_2.setGeometry(QRect(450, 250, 341, 31))
        self.lastnamebox_2.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.emailbox_2 = QLineEdit(self.textboxeditcontainer_3)
        self.emailbox_2.setObjectName(u"emailbox_2")
        self.emailbox_2.setGeometry(QRect(450, 450, 341, 31))
        self.emailbox_2.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding: 0 5px;")
        self.savechangebutton_3 = QPushButton(self.textboxeditcontainer_3)
        self.savechangebutton_3.setObjectName(u"savechangebutton_3")
        self.savechangebutton_3.setGeometry(QRect(590, 530, 201, 41))
        self.savechangebutton_3.setStyleSheet(u"color: #FFF;\n"
"background: #AEC289;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border-radius: 10px;")
        self.deleteaccbutton_2 = QPushButton(self.textboxeditcontainer_3)
        self.deleteaccbutton_2.setObjectName(u"deleteaccbutton_2")
        self.deleteaccbutton_2.setGeometry(QRect(350, 530, 201, 41))
        self.deleteaccbutton_2.setStyleSheet(u"color: #FFF;\n"
"background: #cd4662;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border-radius: 10px;")
        self.birthdaydateEdit_2 = QDateEdit(self.textboxeditcontainer_3)
        self.birthdaydateEdit_2.setObjectName(u"birthdaydateEdit_2")
        self.birthdaydateEdit_2.setGeometry(QRect(450, 350, 341, 31))
        self.birthdaydateEdit_2.setStyleSheet(u"QDateTimeEdit {\n"
"	background-color: #F4F2EF; \n"
"	font-size: 16px;\n"
"	border: 2px solid #CD4662; \n"
"	padding: 5px;\n"
"	border-radius: 5px; \n"
"}\n"
"QDateTimeEdit::down-button, QDateTimeEdit::up-button {\n"
"	width: 20px; \n"
"	height: 13px;\n"
"	background-color: #F4F2EF; \n"
"	border: 2px solid #CD4662; \n"
"	font-size: 16px;\n"
"}\n"
"QDateTimeEdit::down-button {\n"
"	subcontrol-origin: border;\n"
"	subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QDateTimeEdit::up-button {\n"
"	subcontrol-origin: border;\n"
"	subcontrol-position: top right;\n"
"}\n"
"    \n"
"QDateTimeEdit::down-button:pressed, QDateTimeEdit::up-button:pressed {\n"
"	background-color: #CD4662;\n"
"}\n"
"    \n"
"QDateTimeEdit::down-arrow, QDateTimeEdit::up-arrow {\n"
"	image: url(arrow.png); \n"
"}")
        self.birthdaydateEdit_2.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.editprofilepic_2 = QLabel(self.editprofilecontainer_2)
        self.editprofilepic_2.setObjectName(u"editprofilepic_2")
        self.editprofilepic_2.setGeometry(QRect(40, 0, 160, 160))
        self.editprofilepic_2.setStyleSheet(u"border: none;\n"
"border-radius: 80px;\n"
"background: #cd4662;")
        self.editnameprofile_2 = QLabel(self.editprofilecontainer_2)
        self.editnameprofile_2.setObjectName(u"editnameprofile_2")
        self.editnameprofile_2.setGeometry(QRect(40, 190, 165, 41))
        self.editnameprofile_2.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.editnameprofile_2.setAlignment(Qt.AlignCenter)
        self.backtomainsettingbutton_3 = QPushButton(self.editprofilesettingspage)
        self.backtomainsettingbutton_3.setObjectName(u"backtomainsettingbutton_3")
        self.backtomainsettingbutton_3.setGeometry(QRect(20, 30, 20, 31))
        self.backtomainsettingbutton_3.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/backhomoe.png);")
        self.stackedWidget_settings.addWidget(self.editprofilesettingspage)
        self.rulepage = QWidget()
        self.rulepage.setObjectName(u"rulepage")
        self.backtomainsettingbutton = QPushButton(self.rulepage)
        self.backtomainsettingbutton.setObjectName(u"backtomainsettingbutton")
        self.backtomainsettingbutton.setGeometry(QRect(20, 30, 20, 31))
        self.backtomainsettingbutton.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/backhomoe.png);")
        self.ruleofusecontainer = QWidget(self.rulepage)
        self.ruleofusecontainer.setObjectName(u"ruleofusecontainer")
        self.ruleofusecontainer.setGeometry(QRect(60, 60, 1160, 630))
        self.ruleofusecontainer.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: #FAF9F6;\n"
"	width: 15px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #E1E3E7;\n"
"	border-radius: 7px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #F4DBDB;\n"
"}\n"
"")
        self.verticalLayout_8 = QVBoxLayout(self.ruleofusecontainer)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scrollArea_ruleofuse = QScrollArea(self.ruleofusecontainer)
        self.scrollArea_ruleofuse.setObjectName(u"scrollArea_ruleofuse")
        self.scrollArea_ruleofuse.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 1127, 1518))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_ruleofuse = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_ruleofuse.setObjectName(u"frame_ruleofuse")
        self.frame_ruleofuse.setMinimumSize(QSize(0, 1500))
        self.frame_ruleofuse.setFrameShape(QFrame.StyledPanel)
        self.frame_ruleofuse.setFrameShadow(QFrame.Raised)
        self.ruleofuselabel = QLabel(self.frame_ruleofuse)
        self.ruleofuselabel.setObjectName(u"ruleofuselabel")
        self.ruleofuselabel.setGeometry(QRect(417, 10, 290, 61))
        self.ruleofuselabel.setStyleSheet(u"color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 32px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.ruleofuselabel.setAlignment(Qt.AlignCenter)
        self.ruleofusecontentlabel = QLabel(self.frame_ruleofuse)
        self.ruleofusecontentlabel.setObjectName(u"ruleofusecontentlabel")
        self.ruleofusecontentlabel.setGeometry(QRect(40, 100, 1040, 531))
        self.ruleofusecontentlabel.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_9.addWidget(self.frame_ruleofuse)

        self.scrollArea_ruleofuse.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_8.addWidget(self.scrollArea_ruleofuse)

        self.stackedWidget_settings.addWidget(self.rulepage)
        self.stackedWidget.addWidget(self.settings)
        self.canceladdproductbutton_2 = QPushButton(Main)
        self.canceladdproductbutton_2.setObjectName(u"canceladdproductbutton_2")
        self.canceladdproductbutton_2.setGeometry(QRect(998, 761, 157, 49))
        self.canceladdproductbutton_2.setStyleSheet(u"QPushButton {	\n"
"	border-radius: 5px;\n"
"	background: #AEC289;\n"
"	color: #FFF;\n"
"	text-align: center;\n"
"	font-family: Suwannaphum;\n"
"	font-size: 20px;\n"
"	font-style: normal;\n"
"	font-weight: 400;\n"
"	line-height: normal;\n"
"}\n"
"QPushButton:hover {\n"
"	background: #F4DBDB;\n"
"	color: #545454;\n"
"}")
        self.addproductbutton_2 = QPushButton(Main)
        self.addproductbutton_2.setObjectName(u"addproductbutton_2")
        self.addproductbutton_2.setGeometry(QRect(1206, 761, 204, 49))
        self.addproductbutton_2.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"	background: #CD4662;\n"
"	color: #FFF;\n"
"	text-align: center;\n"
"	font-family: Suwannaphum;\n"
"	font-size: 20px;\n"
"	font-style: normal;\n"
"	font-weight: 400;\n"
"	line-height: normal;\n"
"}\n"
"QPushButton:hover {\n"
"	background: #F4DBDB;\n"
"	color: #545454;\n"
"}")

        self.retranslateUi(Main)

        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_main.setCurrentIndex(1)
        self.stackedWidget_myorders.setCurrentIndex(0)
        self.stackedWidget_adminmain.setCurrentIndex(0)
        self.stackedWidget_orderadmin.setCurrentIndex(0)
        self.stackedWidget_adminproducts.setCurrentIndex(1)
        self.stackedWidget_allandtype_admin.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Form", None))
        self.backbutton_settingsadmin.setText("")
        self.accsettingslabel_4.setText(QCoreApplication.translate("Main", u"Account Settings", None))
        self.myacclabel_4.setText(QCoreApplication.translate("Main", u"My Account", None))
        self.settingslabel_4.setText(QCoreApplication.translate("Main", u"Settings", None))
        self.helplabel_4.setText(QCoreApplication.translate("Main", u"Help", None))
        self.ruleadminbutton.setText(QCoreApplication.translate("Main", u"Rules of use", None))
        self.logoutsettingsadminbutton.setText(QCoreApplication.translate("Main", u"Log out", None))
        self.shopaccountbutton.setText(QCoreApplication.translate("Main", u"Shop Account", None))
        self.exitshopbutton.setText(QCoreApplication.translate("Main", u"Exit Shop", None))
        self.editshopbutton.setText(QCoreApplication.translate("Main", u"Edit Shop", None))
        self.shopnamelabel_3.setText(QCoreApplication.translate("Main", u"Shop's name", None))
        self.fisrtnamelabel_admin_3.setText(QCoreApplication.translate("Main", u"First name", None))
        self.lastnamelabel_admin_3.setText(QCoreApplication.translate("Main", u"Last name", None))
        self.addresslabel_admin_3.setText(QCoreApplication.translate("Main", u"Address", None))
        self.phonelabel_admin_3.setText(QCoreApplication.translate("Main", u"Phone", None))
        self.emaillabel_admin_3.setText(QCoreApplication.translate("Main", u"Email", None))
        self.shopdescriptionlabel_3.setText(QCoreApplication.translate("Main", u"Description", None))
        self.shoplogolabel_3.setText(QCoreApplication.translate("Main", u"Shop Profile", None))
        self.editshoppic_3.setText("")
        self.shopdescriptionlabel_4.setText(QCoreApplication.translate("Main", u"Description", None))
        self.phonelabel_admin_4.setText(QCoreApplication.translate("Main", u"Phone", None))
        self.emaillabel_admin_4.setText(QCoreApplication.translate("Main", u"Email", None))
        self.fisrtnamelabel_admin_4.setText(QCoreApplication.translate("Main", u"First name", None))
        self.lastnamelabel_admin_4.setText(QCoreApplication.translate("Main", u"Last name", None))
        self.shopnamelabel_4.setText(QCoreApplication.translate("Main", u"Shop's name", None))
        self.addresslabel_admin_4.setText(QCoreApplication.translate("Main", u"Address", None))
        self.backbutton_settingsadmin_7.setText("")
        self.backbutton_settingsadmin_6.setText("")
        self.shopregisterationlabel_2.setText(QCoreApplication.translate("Main", u"Edit Shop Profile", None))
        self.shopnamelabel_2.setText(QCoreApplication.translate("Main", u"Shop's name", None))
        self.fisrtnamelabel_admin_2.setText(QCoreApplication.translate("Main", u"First name", None))
        self.lastnamelabel_admin_2.setText(QCoreApplication.translate("Main", u"Last name", None))
        self.addresslabel_admin_2.setText(QCoreApplication.translate("Main", u"Address", None))
        self.phonelabel_admin_2.setText(QCoreApplication.translate("Main", u"Phone", None))
        self.emaillabel_admin_2.setText(QCoreApplication.translate("Main", u"Email", None))
        self.shopnamebox_2.setText("")
        self.shopnamebox_2.setPlaceholderText(QCoreApplication.translate("Main", u"Shop's name", None))
        self.firstnamebox_admin_2.setText("")
        self.firstnamebox_admin_2.setPlaceholderText(QCoreApplication.translate("Main", u"First name", None))
        self.phonebox_admin_2.setText("")
        self.phonebox_admin_2.setPlaceholderText(QCoreApplication.translate("Main", u"Phone", None))
        self.lastnamebox_admin_2.setText("")
        self.lastnamebox_admin_2.setPlaceholderText(QCoreApplication.translate("Main", u"Last name", None))
        self.emailbox_admin_2.setText("")
        self.emailbox_admin_2.setPlaceholderText(QCoreApplication.translate("Main", u"Email", None))
        self.adminregisterbutton_2.setText(QCoreApplication.translate("Main", u"Save Changes", None))
        self.descriptionbox_admin_2.setText("")
        self.descriptionbox_admin_2.setPlaceholderText(QCoreApplication.translate("Main", u"Description", None))
        self.shopdescriptionlabel_2.setText(QCoreApplication.translate("Main", u"Description", None))
        self.addressbox_admin_2.setText("")
        self.addressbox_admin_2.setPlaceholderText(QCoreApplication.translate("Main", u"Address", None))
        self.deleteaccbutton_5.setText(QCoreApplication.translate("Main", u"Delete account", None))
        self.editshoppic_2.setText("")
        self.shoplogolabel_2.setText(QCoreApplication.translate("Main", u"Shop's Logo", None))
        self.ruleofuselabel_3.setText(QCoreApplication.translate("Main", u"Rule of use", None))
        self.ruleofusecontentlabel_3.setText(QCoreApplication.translate("Main", u"1. Eligibility: Users must be at least 18 years old or have the consent of a parent or legal guardian to use the app.\n"
"\n"
"Account Creation: Users must create an account to access certain features of the app, such as placing orders, tracking shipments, and saving payment methods.\n"
"\n"
"Accuracy of Information: Users are responsible for providing accurate and up-to-date information when creating an account, placing orders, and updating their profile.\n"
"\n"
"Security: Users are responsible for maintaining the security of their account credentials (username, password, etc.) and must not share this information with others.\n"
"\n"
"Prohibited Activities: Users must not engage in any illegal, fraudulent, or unauthorized activities while using the app. This includes but is not limited to hacking, phishing, and unauthorized access to other users' accounts.\n"
"\n"
"Intellectual Property: Users must respect the intellectual property rights of others, including copyrights, trademarks, and patents. Any use of c"
                        "opyrighted material must be done with proper authorization.\n"
"\n"
"Product Listings: Sellers must provide accurate and truthful information about their products, including descriptions, images, and pricing. Any misleading or deceptive practices are prohibited.\n"
"\n"
"Payment: Users must provide valid payment information when making purchases through the app. All transactions are subject to the app's payment policies and may be processed securely through a trusted payment gateway.\n"
"\n"
"Shipping and Delivery: Users should provide accurate shipping addresses to ensure timely delivery of their orders. The app will provide estimated delivery times, but delays may occur due to unforeseen circumstances such as weather or logistical issues.\n"
"\n"
"Returns and Refunds: Users may be eligible for returns and refunds according to the app's return policy. Any returned items must be in their original condition and packaging.\n"
"\n"
"User Conduct: Users must conduct themselves in a respectful and courteous manner "
                        "when interacting with other users, sellers, and customer support representatives. Any harassment, bullying, or abusive behavior will not be tolerated.\n"
"\n"
"Feedback and Reviews: Users are encouraged to provide honest feedback and reviews about their shopping experience and the products they purchase. However, any reviews containing offensive language, personal attacks, or false information will be removed.\n"
"\n"
"Privacy: The app will collect and process personal information according to its privacy policy. Users should review the privacy policy to understand how their data is collected, used, and protected.\n"
"\n"
"Updates and Modifications: The app reserves the right to update or modify these rules of use at any time. Users will be notified of any changes, and continued use of the app constitutes acceptance of the revised rules.\n"
"\n"
"Termination of Account: The app reserves the right to suspend or terminate user accounts that violate these rules of use or engage in prohibited activities. Users wil"
                        "l be notified of any account suspensions or terminations and may appeal the decision if necessary.", None))
        self.backbutton_settingsadmin_2.setText("")
        self.backbutton_settingsadmin_4.setText("")
        self.changepasswordlabel_3.setText(QCoreApplication.translate("Main", u"Change Password", None))
        self.currentpasslabel_3.setText(QCoreApplication.translate("Main", u"Current Password", None))
        self.savechangebutton_8.setText(QCoreApplication.translate("Main", u"Save changes", None))
        self.newpasslabel_3.setText(QCoreApplication.translate("Main", u"New Password", None))
        self.curpasstextbox_3.setPlaceholderText(QCoreApplication.translate("Main", u"Current Password", None))
        self.newpasstextbox_3.setPlaceholderText(QCoreApplication.translate("Main", u"New Password", None))
        self.backbutton_settingsadmin_5.setText("")
        self.profilelabel_3.setText(QCoreApplication.translate("Main", u"Profile", None))
        self.usernameprofile_3.setText(QCoreApplication.translate("Main", u"Username", None))
        self.fisrtnameprofile_3.setText(QCoreApplication.translate("Main", u"First name", None))
        self.lastnameprofile_3.setText(QCoreApplication.translate("Main", u"Last name", None))
        self.genderprofile_3.setText(QCoreApplication.translate("Main", u"Gender", None))
        self.birthprofile_3.setText(QCoreApplication.translate("Main", u"Birthday", None))
        self.phoneprofile_3.setText(QCoreApplication.translate("Main", u"Phone", None))
        self.emailprofile_3.setText(QCoreApplication.translate("Main", u"Email", None))
        self.pictureprofile_3.setText("")
        self.username_3.setText(QCoreApplication.translate("Main", u"User1", None))
        self.firstname_3.setText(QCoreApplication.translate("Main", u"Firsth name", None))
        self.gender_3.setText(QCoreApplication.translate("Main", u"Gender", None))
        self.phone_3.setText(QCoreApplication.translate("Main", u"Phone", None))
        self.lastname_3.setText(QCoreApplication.translate("Main", u"last name", None))
        self.birthday_3.setText(QCoreApplication.translate("Main", u"User1", None))
        self.email_3.setText(QCoreApplication.translate("Main", u"User1", None))
        self.backbutton_settingsadmin_3.setText("")
        self.editlabel_4.setText(QCoreApplication.translate("Main", u"Edit Profile", None))
        self.userabel_4.setText(QCoreApplication.translate("Main", u"Username", None))
        self.fisrtlabel_4.setText(QCoreApplication.translate("Main", u"First name", None))
        self.lastlabel_4.setText(QCoreApplication.translate("Main", u"Last name", None))
        self.genlabel_4.setText(QCoreApplication.translate("Main", u"Gender", None))
        self.birthlabel_4.setText(QCoreApplication.translate("Main", u"Birthday", None))
        self.pholabel_4.setText(QCoreApplication.translate("Main", u"Phone", None))
        self.emaillabel_5.setText(QCoreApplication.translate("Main", u"Email", None))
        self.userbox_4.setText("")
        self.userbox_4.setPlaceholderText(QCoreApplication.translate("Main", u"Username", None))
        self.firstnamebox_4.setText("")
        self.firstnamebox_4.setPlaceholderText(QCoreApplication.translate("Main", u"First name", None))
        self.genderbox_4.setText("")
        self.genderbox_4.setPlaceholderText(QCoreApplication.translate("Main", u"Gender", None))
        self.phonebox_4.setText("")
        self.phonebox_4.setPlaceholderText(QCoreApplication.translate("Main", u"Phone", None))
        self.lastnamebox_4.setText("")
        self.lastnamebox_4.setPlaceholderText(QCoreApplication.translate("Main", u"Last name", None))
        self.emailbox_4.setText("")
        self.emailbox_4.setPlaceholderText(QCoreApplication.translate("Main", u"Email", None))
        self.savechangebutton_7.setText(QCoreApplication.translate("Main", u"Save changes", None))
        self.deleteaccbutton_4.setText(QCoreApplication.translate("Main", u"Delete account", None))
        self.editprofilepic_4.setText("")
        self.editnameprofile_4.setText(QCoreApplication.translate("Main", u"User1", None))
        self.Logolabel.setText(QCoreApplication.translate("Main", u"ChopShop", None))
        self.homebutton.setText(QCoreApplication.translate("Main", u"Home", None))
        self.favbutton.setText(QCoreApplication.translate("Main", u"Favorites", None))
        self.orderbutton.setText(QCoreApplication.translate("Main", u"My Orders", None))
        self.messbutton.setText(QCoreApplication.translate("Main", u"Messages", None))
        self.settingbutton.setText("")
        self.searchbox.setPlaceholderText(QCoreApplication.translate("Main", u"Search..", None))
        self.loginsignoutbutton.setText(QCoreApplication.translate("Main", u"Log In", None))
        self.cartbutton.setText("")
        self.profilebutton.setText("")
        self.profilepic_admin_2.setText("")
        self.shopnamelabel_admin_2.setText(QCoreApplication.translate("Main", u"Username", None))
        self.numreviews_2.setText(QCoreApplication.translate("Main", u"4/5", None))
        self.numreviewlabel_2.setText(QCoreApplication.translate("Main", u"Reviews", None))
        self.numproducts_2.setText(QCoreApplication.translate("Main", u"1000", None))
        self.numproductslebel_2.setText(QCoreApplication.translate("Main", u"Products", None))
        self.numsolds_2.setText(QCoreApplication.translate("Main", u"30000", None))
        self.numyearregisteredlabel_2.setText(QCoreApplication.translate("Main", u"Years Registered", None))
        self.numsoldslabel_2.setText(QCoreApplication.translate("Main", u"Sold", None))
        self.numyearregistered_2.setText(QCoreApplication.translate("Main", u"2", None))
        self.productslabel_admin_4.setText(QCoreApplication.translate("Main", u"Products", None))
        self.viewallproductbutton_admin_2.setText(QCoreApplication.translate("Main", u"View all Products    >", None))
        self.stylelabbutton.setText(QCoreApplication.translate("Main", u"Style Lab", None))
        self.newarrivalbutton.setText(QCoreApplication.translate("Main", u"New Arrival", None))
        self.onsalesbutton.setText(QCoreApplication.translate("Main", u"On Sales", None))
        self.buyagainbutton.setText(QCoreApplication.translate("Main", u"Buy Again", None))
        self.bestsellingbutton.setText(QCoreApplication.translate("Main", u"Best Selling", None))
        self.suggestlabel.setText(QCoreApplication.translate("Main", u"Suggestions", None))
        self.cartlabel.setText(QCoreApplication.translate("Main", u"Cart", None))
        self.purchaseallcartbutton.setText(QCoreApplication.translate("Main", u"Purchase all", None))
        self.picproduct1_12.setText("")
        self.picproduct1_6.setText("")
        self.picproduct1_7.setText("")
        self.picproduct1_8.setText("")
        self.picproduct1_13.setText("")
        self.picproduct1_14.setText("")
        self.suggestlabel_2.setText(QCoreApplication.translate("Main", u"Favorites", None))
        self.myorderslabel.setText(QCoreApplication.translate("Main", u"My Orders", None))
        self.tobeshippedbutton.setText(QCoreApplication.translate("Main", u"To be shipped", None))
        self.toberecievedbutton.setText(QCoreApplication.translate("Main", u"To be recieved", None))
        self.completedbutton.setText(QCoreApplication.translate("Main", u"Completed", None))
        self.shopnameforcart_3.setText(QCoreApplication.translate("Main", u"Shop's name", None))
        self.cartorderpic_3.setText("")
        self.productcartname_3.setText(QCoreApplication.translate("Main", u"Product's name", None))
        self.productcartdescrip_3.setText(QCoreApplication.translate("Main", u"Description", None))
        self.productnum_3.setText(QCoreApplication.translate("Main", u"1 piece", None))
        self.totalpricecartlabel_3.setText(QCoreApplication.translate("Main", u"Total Price:", None))
        self.totalpricecartnumlabel_3.setText(QCoreApplication.translate("Main", u"B 400", None))
        self.checkstatusreceivebutton.setText(QCoreApplication.translate("Main", u"Check Status", None))
        self.shopnameforcart_4.setText(QCoreApplication.translate("Main", u"Shop's name", None))
        self.cartorderpic_4.setText("")
        self.productcartname_4.setText(QCoreApplication.translate("Main", u"Product's name", None))
        self.productcartdescrip_4.setText(QCoreApplication.translate("Main", u"Description", None))
        self.productnum_4.setText(QCoreApplication.translate("Main", u"1 piece", None))
        self.totalpricecartlabel_4.setText(QCoreApplication.translate("Main", u"Total Price:", None))
        self.totalpricecartnumlabel_4.setText(QCoreApplication.translate("Main", u"B 500", None))
        self.buyagaincompletebutton.setText(QCoreApplication.translate("Main", u"Buy again", None))
        self.mainpic.setText(QCoreApplication.translate("Main", u"Mainpic", None))
        self.productname.setText(QCoreApplication.translate("Main", u"Name of the product", None))
        self.buynowbutton.setText(QCoreApplication.translate("Main", u"Buy Now", None))
        self.addtocartbutton.setText(QCoreApplication.translate("Main", u"Add to Cart", None))
        self.shopprofile.setText("")
        self.shopname.setText(QCoreApplication.translate("Main", u"Seller's Account", None))
        self.shopfollower.setText(QCoreApplication.translate("Main", u"10,000 followers", None))
        self.star1.setText("")
        self.star2.setText("")
        self.star3.setText("")
        self.star4.setText("")
        self.star5.setText("")
        self.numberofstar.setText(QCoreApplication.translate("Main", u"0", None))
        self.numberofsold.setText(QCoreApplication.translate("Main", u"0 Sold", None))
        self.currencypic.setText("")
        self.productprice.setText(QCoreApplication.translate("Main", u"100", None))
        self.review_3.setText(QCoreApplication.translate("Main", u"Reviews", None))
        self.numyearregis_3.setText(QCoreApplication.translate("Main", u"2", None))
        self.numreview_3.setText(QCoreApplication.translate("Main", u"4/5", None))
        self.yearregis_3.setText(QCoreApplication.translate("Main", u"Register Date", None))
        self.numproduct_3.setText(QCoreApplication.translate("Main", u"1000", None))
        self.numsold_3.setText(QCoreApplication.translate("Main", u"30000", None))
        self.sold_3.setText(QCoreApplication.translate("Main", u"Sold", None))
        self.product_35.setText(QCoreApplication.translate("Main", u"Products", None))
        self.sizelabel.setText(QCoreApplication.translate("Main", u"Size", None))
        self.optionslabel.setText(QCoreApplication.translate("Main", u"Options", None))
        self.prevpicbutton.setText("")
        self.nextpicbutton.setText("")
        self.pushButton.setText("")
        self.descriptionlabel_productviewpage.setText(QCoreApplication.translate("Main", u"Description", None))
        self.descriptioninfolabel_productviewpage.setText(QCoreApplication.translate("Main", u"Details jkdesdjskfn vdnfksdjiwqjlksdcf difjedjfiejsd cdsfnfjns fceifnslk dcvksij fo ;alm eifjeds cvsdedf ieklmfc dsvi djsosfm efodsjkmc vdesjkf oemkf d vojdofmke cfdoodnfm ecjdpsfjkel vokdinfjejs fncs", None))
        self.backtocartbutton.setText("")
        self.addressdisplaylabel_2.setText(QCoreApplication.translate("Main", u"Address", None))
        self.fisrtnameaddress_2.setText(QCoreApplication.translate("Main", u"First name", None))
        self.lastnameaddress_2.setText(QCoreApplication.translate("Main", u"Last name", None))
        self.homenumaddress_2.setText(QCoreApplication.translate("Main", u"Address", None))
        self.phoneaddress_2.setText(QCoreApplication.translate("Main", u"Phone", None))
        self.firstnameaddressdisplay_2.setText(QCoreApplication.translate("Main", u"Firsth name", None))
        self.phoneaddressdisplay_2.setText(QCoreApplication.translate("Main", u"Phone", None))
        self.lastnameaddressdisplay_2.setText(QCoreApplication.translate("Main", u"last name", None))
        self.homenumaddressdisplay_2.setText(QCoreApplication.translate("Main", u"Address", None))
        self.orderlabel.setText(QCoreApplication.translate("Main", u"Order", None))
        self.choosemethodlabel.setText(QCoreApplication.translate("Main", u"Choose Payment Method", None))
        self.promptpaybutton.setText(QCoreApplication.translate("Main", u"Promptpay", None))
        self.cashdeliverybutton.setText(QCoreApplication.translate("Main", u"Cash on delivery", None))
        self.purchasebutton.setText(QCoreApplication.translate("Main", u"Purchase", None))
        self.totalpricelabel.setText(QCoreApplication.translate("Main", u"Total Price:", None))
        self.totalprice.setText(QCoreApplication.translate("Main", u"10000", None))
        self.pickupstorebutton.setText(QCoreApplication.translate("Main", u"Pick up at the store", None))
        self.orderlabel_9.setText("")
        self.orderlabel_10.setText(QCoreApplication.translate("Main", u"Thanks for purchasing!", None))
        self.backtohomebutton.setText(QCoreApplication.translate("Main", u"Back to home", None))
        self.backtochoosingtypebutton.setText("")
        self.orderlabel_6.setText(QCoreApplication.translate("Main", u"Total Price:", None))
        self.orderlabel_7.setText(QCoreApplication.translate("Main", u"10000", None))
        self.orderlabel_8.setText(QCoreApplication.translate("Main", u"QR Code Picture", None))
        self.purchasebutton_2.setText(QCoreApplication.translate("Main", u"Submit", None))
        self.orderlabel_11.setText(QCoreApplication.translate("Main", u"Instruction", None))
        self.orderlabel_12.setText(QCoreApplication.translate("Main", u"1. Open your mobile banking application", None))
        self.orderlabel_13.setText(QCoreApplication.translate("Main", u"2. Scan the Qr Code above and pay", None))
        self.orderlabel_14.setText(QCoreApplication.translate("Main", u"3. Press the submit button", None))
        self.backbutton_adminregister.setText("")
        self.shopregisterationlabel.setText(QCoreApplication.translate("Main", u"Shop Registeration", None))
        self.shopnamelabel.setText(QCoreApplication.translate("Main", u"Shop's name", None))
        self.fisrtnamelabel_admin.setText(QCoreApplication.translate("Main", u"First name", None))
        self.lastnamelabel_admin.setText(QCoreApplication.translate("Main", u"Last name", None))
        self.addresslabel_admin.setText(QCoreApplication.translate("Main", u"Address", None))
        self.phonelabel_admin.setText(QCoreApplication.translate("Main", u"Phone", None))
        self.emaillabel_admin.setText(QCoreApplication.translate("Main", u"Email", None))
        self.shopnamebox.setText("")
        self.shopnamebox.setPlaceholderText(QCoreApplication.translate("Main", u"Shop's name", None))
        self.firstnamebox_admin.setText("")
        self.firstnamebox_admin.setPlaceholderText(QCoreApplication.translate("Main", u"First name", None))
        self.phonebox_admin.setText("")
        self.phonebox_admin.setPlaceholderText(QCoreApplication.translate("Main", u"Phone", None))
        self.lastnamebox_admin.setText("")
        self.lastnamebox_admin.setPlaceholderText(QCoreApplication.translate("Main", u"Last name", None))
        self.emailbox_admin.setText("")
        self.emailbox_admin.setPlaceholderText(QCoreApplication.translate("Main", u"Email", None))
        self.adminregisterbutton.setText(QCoreApplication.translate("Main", u"Register", None))
        self.descriptionbox_admin.setText("")
        self.descriptionbox_admin.setPlaceholderText(QCoreApplication.translate("Main", u"Description", None))
        self.shopdescriptionlabel.setText(QCoreApplication.translate("Main", u"Description", None))
        self.addressbox_admin.setText("")
        self.addressbox_admin.setPlaceholderText(QCoreApplication.translate("Main", u"Address", None))
        self.editshoppic.setText("")
        self.shoplogolabel.setText(QCoreApplication.translate("Main", u"Shop's Logo", None))
        self.loginsignoutbutton_admin.setText(QCoreApplication.translate("Main", u"Log In", None))
        self.profilebutton_admin.setText("")
        self.Logolabel_admin.setText(QCoreApplication.translate("Main", u"ChopShop", None))
        self.homebutton_admin.setText(QCoreApplication.translate("Main", u"Home", None))
        self.orderstatusbutton_admin.setText(QCoreApplication.translate("Main", u"Order Status", None))
        self.productsbutton_admin.setText(QCoreApplication.translate("Main", u"Products", None))
        self.messbutton_admin.setText(QCoreApplication.translate("Main", u"Messages", None))
        self.settingbutton_admin.setText("")
        self.profilepic_admin.setText("")
        self.shopnamelabel_admin.setText(QCoreApplication.translate("Main", u"Username", None))
        self.numreviews.setText(QCoreApplication.translate("Main", u"4/5", None))
        self.numreviewlabel.setText(QCoreApplication.translate("Main", u"Reviews", None))
        self.numproducts.setText(QCoreApplication.translate("Main", u"1000", None))
        self.numproductslebel.setText(QCoreApplication.translate("Main", u"Products", None))
        self.numsolds.setText(QCoreApplication.translate("Main", u"30000", None))
        self.numyearregisteredlabel.setText(QCoreApplication.translate("Main", u"Years Registered", None))
        self.numsoldslabel.setText(QCoreApplication.translate("Main", u"Sold", None))
        self.numyearregistered.setText(QCoreApplication.translate("Main", u"2", None))
        self.tobeshippedbutton_admin.setText("")
        self.toberevievedbutton_admin.setText("")
        self.completedbutton_admin.setText("")
        self.reviewsbutton_admin.setText("")
        self.allorderstatusbutton_admin.setText(QCoreApplication.translate("Main", u"View all order status    >", None))
        self.productslabel_admin_2.setText(QCoreApplication.translate("Main", u"Oder Status", None))
        self.vieworderstatusbutton_admin.setText(QCoreApplication.translate("Main", u"View Order status    >", None))
        self.productslabel_admin.setText(QCoreApplication.translate("Main", u"Products", None))
        self.viewallproductbutton_admin.setText(QCoreApplication.translate("Main", u"View all Products    >", None))
        self.addproduct_admin.setText(QCoreApplication.translate("Main", u"     Add Product", None))
        self.myorderslabel_2.setText(QCoreApplication.translate("Main", u"My Orders", None))
        self.toshipadminbutton.setText(QCoreApplication.translate("Main", u"To be shipped", None))
        self.canceladminvutton.setText(QCoreApplication.translate("Main", u"Canceled", None))
        self.completedadminbutton.setText(QCoreApplication.translate("Main", u"Completed", None))
        self.reviewsadminvutton.setText(QCoreApplication.translate("Main", u"Reviews", None))
        self.tobeshipproductnameadmin.setText(QCoreApplication.translate("Main", u"Product name", None))
        self.tobeshipadminpic.setText("")
        self.tobeshipcustomernameadmin.setText(QCoreApplication.translate("Main", u"Customer's name", None))
        self.tobeshipordernumadmin.setText(QCoreApplication.translate("Main", u"Order number", None))
        self.tobeshipproductnumadmin.setText(QCoreApplication.translate("Main", u"1 piece", None))
        self.tobeshiptotalpriceadmin.setText(QCoreApplication.translate("Main", u"Total Price:", None))
        self.totalpricecartnumlabel_5.setText(QCoreApplication.translate("Main", u"B 500", None))
        self.shippedadminbutton.setText(QCoreApplication.translate("Main", u"Shipped", None))
        self.cancelproductnameadmin_4.setText(QCoreApplication.translate("Main", u"Product name", None))
        self.canceladminpic_4.setText("")
        self.cancelcustomernameadmin_4.setText(QCoreApplication.translate("Main", u"Customer's name", None))
        self.cancelordernumadmin_4.setText(QCoreApplication.translate("Main", u"Order number", None))
        self.cancelproductnumadmin_4.setText(QCoreApplication.translate("Main", u"1 piece", None))
        self.canceltotalpriceadmin_4.setText(QCoreApplication.translate("Main", u"Total Price:", None))
        self.totalpricecartnumlabel_8.setText(QCoreApplication.translate("Main", u"B 500", None))
        self.canceladminbutton_4.setText(QCoreApplication.translate("Main", u"Canceled", None))
        self.completeproductnameadmin_3.setText(QCoreApplication.translate("Main", u"Product name", None))
        self.completeadminpic_3.setText("")
        self.completecustomernameadmin_3.setText(QCoreApplication.translate("Main", u"Customer's name", None))
        self.completeordernumadmin_3.setText(QCoreApplication.translate("Main", u"Order number", None))
        self.completeproductnumadmin_3.setText(QCoreApplication.translate("Main", u"1 piece", None))
        self.completetotalpriceadmin_3.setText(QCoreApplication.translate("Main", u"Total Price:", None))
        self.totalpricecartnumlabel_7.setText(QCoreApplication.translate("Main", u"B 500", None))
        self.completeadminbutton_3.setText(QCoreApplication.translate("Main", u"Completed", None))
        self.reviewproductnameadmin_2.setText(QCoreApplication.translate("Main", u"Product name", None))
        self.reviewadminpic_2.setText("")
        self.reviewcustomernameadmin_2.setText(QCoreApplication.translate("Main", u"Customer's name", None))
        self.reviewordernumadmin_2.setText(QCoreApplication.translate("Main", u"Order number", None))
        self.reviewproductnumadmin_2.setText(QCoreApplication.translate("Main", u"1 piece", None))
        self.reviewtotalpriceadmin_2.setText(QCoreApplication.translate("Main", u"Total Price:", None))
        self.totalpricecartnumlabel_6.setText(QCoreApplication.translate("Main", u"B 500", None))
        self.reviewadminbutton_2.setText(QCoreApplication.translate("Main", u"Reviewed", None))
        self.productlabel_admin.setText(QCoreApplication.translate("Main", u"Products", None))
        self.allproductbutton_admin.setText(QCoreApplication.translate("Main", u"All Products", None))
        self.producttypesbutton_admin.setText(QCoreApplication.translate("Main", u"Product Types", None))
        self.topwearpic_3.setText("")
        self.topwearlabel_3.setText(QCoreApplication.translate("Main", u"Tops", None))
        self.topwearnum_3.setText(QCoreApplication.translate("Main", u"20", None))
        self.topwearbutton_3.setText("")
        self.bottomwearpic_3.setText("")
        self.bottomwearlabel_3.setText(QCoreApplication.translate("Main", u"Bottoms", None))
        self.bottomwearnum_3.setText(QCoreApplication.translate("Main", u"30", None))
        self.bottmwearbutton_3.setText("")
        self.footwearpic_3.setText("")
        self.footwearlabel_3.setText(QCoreApplication.translate("Main", u"Foot Wears", None))
        self.footwearnum_3.setText(QCoreApplication.translate("Main", u"40", None))
        self.footwearbutton_3.setText("")
        self.addproductlabel.setText(QCoreApplication.translate("Main", u"Add Product", None))
        self.addproductimagelabel.setText(QCoreApplication.translate("Main", u"Product's Images", None))
        self.addimagebutton.setText(QCoreApplication.translate("Main", u"+", None))
        self.img_1.setText("")
        self.delete_pic_button_1.setText(QCoreApplication.translate("Main", u"X", None))
        self.addproductnamelabel.setText(QCoreApplication.translate("Main", u"Product's Name", None))
        self.addproductdescriptionlabel.setText(QCoreApplication.translate("Main", u"Description", None))
        self.addproductpricelabel.setText(QCoreApplication.translate("Main", u"Price", None))
        self.addproductsizelabel.setText(QCoreApplication.translate("Main", u"Sizes", None))
        self.addsizeproductbutton.setText(QCoreApplication.translate("Main", u"+", None))
        self.addproductoptionlabel.setText(QCoreApplication.translate("Main", u"Options", None))
        self.addoptionproductbutton.setText(QCoreApplication.translate("Main", u"+", None))
        self.addproductstocklabel.setText(QCoreApplication.translate("Main", u"Stock", None))
        self.addproductscategorieslabel.setText(QCoreApplication.translate("Main", u"Categories", None))
        self.checkBox_men.setText(QCoreApplication.translate("Main", u"Men", None))
        self.checkBox_women.setText(QCoreApplication.translate("Main", u"Women", None))
        self.checkBox_kids.setText(QCoreApplication.translate("Main", u"Kids", None))
        self.checkBox_top.setText(QCoreApplication.translate("Main", u"Top", None))
        self.checkBox_dress.setText(QCoreApplication.translate("Main", u"Dress", None))
        self.checkBox_headwear.setText(QCoreApplication.translate("Main", u"Headwear", None))
        self.checkBox_bottom.setText(QCoreApplication.translate("Main", u"Bottom", None))
        self.checkBox_footwear.setText(QCoreApplication.translate("Main", u"Footwear", None))
        self.checkBox_accessories.setText(QCoreApplication.translate("Main", u"Accesories", None))
        self.canceladdproductbutton.setText(QCoreApplication.translate("Main", u"Cancel", None))
        self.addproductbutton.setText(QCoreApplication.translate("Main", u"Add Product", None))
        self.editproductlabel_3.setText(QCoreApplication.translate("Main", u"Edit Product", None))
        self.addproductimagelabel_3.setText(QCoreApplication.translate("Main", u"Product's Images", None))
        self.addimagebutton_3.setText(QCoreApplication.translate("Main", u"+", None))
        self.img_3.setText("")
        self.delete_pic_button_3.setText(QCoreApplication.translate("Main", u"X", None))
        self.editproductnamelabel_3.setText(QCoreApplication.translate("Main", u"Product's Name", None))
        self.editproductdescriptionlabel_3.setText(QCoreApplication.translate("Main", u"Description", None))
        self.editproductpricelabel_3.setText(QCoreApplication.translate("Main", u"Price", None))
        self.editproductsizelabel_3.setText(QCoreApplication.translate("Main", u"Sizes", None))
        self.deletesizebutton.setText("")
        self.addsizeproductbutton_3.setText(QCoreApplication.translate("Main", u"+", None))
        self.editproductoptionlabel.setText(QCoreApplication.translate("Main", u"Options", None))
        self.addoptionproductbutton_3.setText(QCoreApplication.translate("Main", u"+", None))
        self.editproductstocklabel_3.setText(QCoreApplication.translate("Main", u"Stock", None))
        self.editproductcategorieslabel_3.setText(QCoreApplication.translate("Main", u"Categories", None))
        self.checkBox_men_3.setText(QCoreApplication.translate("Main", u"Men", None))
        self.checkBox_women_3.setText(QCoreApplication.translate("Main", u"Women", None))
        self.checkBox_kids_3.setText(QCoreApplication.translate("Main", u"Kids", None))
        self.checkBox_top_3.setText(QCoreApplication.translate("Main", u"Top", None))
        self.checkBox_dress_3.setText(QCoreApplication.translate("Main", u"Dress", None))
        self.checkBox_headwear_3.setText(QCoreApplication.translate("Main", u"Headwear", None))
        self.checkBox_bottom_3.setText(QCoreApplication.translate("Main", u"Bottom", None))
        self.checkBox_footwear_3.setText(QCoreApplication.translate("Main", u"Footwear", None))
        self.checkBox_accessories_3.setText(QCoreApplication.translate("Main", u"Accesories", None))
        self.addproductbutton_4.setText(QCoreApplication.translate("Main", u"Save Changes", None))
        self.mainpic_2.setText(QCoreApplication.translate("Main", u"Mainpic", None))
        self.productname_2.setText(QCoreApplication.translate("Main", u"Name of the product", None))
        self.deleteproductbutton.setText(QCoreApplication.translate("Main", u"Delete Product", None))
        self.editproductbutton.setText(QCoreApplication.translate("Main", u"Edit Product", None))
        self.star1_2.setText("")
        self.star2_2.setText("")
        self.star3_2.setText("")
        self.star4_2.setText("")
        self.star5_2.setText("")
        self.numberofstar_2.setText(QCoreApplication.translate("Main", u"1", None))
        self.numberofsold_2.setText(QCoreApplication.translate("Main", u"480 Sold", None))
        self.currencypic_2.setText("")
        self.productprice_2.setText(QCoreApplication.translate("Main", u"100", None))
        self.sizelabel_2.setText(QCoreApplication.translate("Main", u"Size", None))
        self.sbutton_2.setText(QCoreApplication.translate("Main", u"S", None))
        self.mbutton_2.setText(QCoreApplication.translate("Main", u"m", None))
        self.lbutton_2.setText(QCoreApplication.translate("Main", u"l", None))
        self.xlbutton_2.setText(QCoreApplication.translate("Main", u"xl", None))
        self.optionslabel_2.setText(QCoreApplication.translate("Main", u"Options", None))
        self.mbutton_3.setText(QCoreApplication.translate("Main", u"blue", None))
        self.lbutton_3.setText(QCoreApplication.translate("Main", u"yellow", None))
        self.sbutton_3.setText(QCoreApplication.translate("Main", u"red", None))
        self.xlbutton_3.setText(QCoreApplication.translate("Main", u"pink", None))
        self.nextpicrightsidebutton.setText("")
        self.nextpicrightsidebutton_2.setText("")
        self.productdescription_2.setText(QCoreApplication.translate("Main", u"Description", None))
        self.label_4.setText(QCoreApplication.translate("Main", u"Description", None))
        self.reviewerprofile_2.setText("")
        self.reviewername_2.setText(QCoreApplication.translate("Main", u"User1", None))
        self.star11_2.setText("")
        self.star12_2.setText("")
        self.star13_2.setText("")
        self.star14_2.setText("")
        self.star15_2.setText("")
        self.productchoose_2.setText(QCoreApplication.translate("Main", u"Product Choice: Brown S", None))
        self.productchoosereview_3.setText(QCoreApplication.translate("Main", u"Good", None))
        self.reviewpic1_2.setText(QCoreApplication.translate("Main", u"reviewpic 1", None))
        self.reviewpic2_2.setText(QCoreApplication.translate("Main", u"reviewpic 2", None))
        self.productchoosereview_4.setText(QCoreApplication.translate("Main", u"06-02-2024", None))
        self.reviewlabel_2.setText(QCoreApplication.translate("Main", u"Reviews", None))
        self.viewallbutton_2.setText(QCoreApplication.translate("Main", u"View all", None))
        self.mainpic_admin.setText(QCoreApplication.translate("Main", u"Mainpic", None))
        self.productname_admin.setText(QCoreApplication.translate("Main", u"Name of the product", None))
        self.deleteproductbutton_admin.setText(QCoreApplication.translate("Main", u"Delete Product", None))
        self.editproductbutton_admin.setText(QCoreApplication.translate("Main", u"Edit Product", None))
        self.star1_admin.setText("")
        self.star2_admin.setText("")
        self.star3_admin.setText("")
        self.star4_admin.setText("")
        self.star5_admin.setText("")
        self.numberofstar_admin.setText(QCoreApplication.translate("Main", u"0", None))
        self.numberofsold_admin.setText(QCoreApplication.translate("Main", u"0 Sold", None))
        self.currencypic_admin.setText("")
        self.productprice_admin.setText(QCoreApplication.translate("Main", u"100", None))
        self.sizelabel_admin.setText(QCoreApplication.translate("Main", u"Size", None))
        self.optionslabel_admin.setText(QCoreApplication.translate("Main", u"Options", None))
        self.prevpicbutton_admin.setText("")
        self.nextpicbutton_admin.setText("")
        self.descriptionlabel_productviewpage_admin.setText(QCoreApplication.translate("Main", u"Description", None))
        self.descriptioninfolabel_productviewpage_admin.setText(QCoreApplication.translate("Main", u"Details jkdesdjskfn vdnfksdjiwqjlksdcf difjedjfiejsd cdsfnfjns fceifnslk dcvksij fo ;alm eifjeds cvsdedf ieklmfc dsvi djsosfm efodsjkmc vdesjkf oemkf d vojdofmke cfdoodnfm ecjdpsfjkel vokdinfjejs fncs", None))
        self.addproductlabel_2.setText(QCoreApplication.translate("Main", u"Add Product", None))
        self.addproductimagelabel_2.setText(QCoreApplication.translate("Main", u"Product's Images", None))
        self.addimagebutton_2.setText(QCoreApplication.translate("Main", u"+", None))
        self.img_2.setText("")
        self.delete_pic_button_2.setText(QCoreApplication.translate("Main", u"X", None))
        self.addproductnamelabel_2.setText(QCoreApplication.translate("Main", u"Product's Name", None))
        self.addproductdescriptionlabel_2.setText(QCoreApplication.translate("Main", u"Description", None))
        self.addproductpricelabel_2.setText(QCoreApplication.translate("Main", u"Price", None))
        self.addproductsizelabel_2.setText(QCoreApplication.translate("Main", u"Sizes", None))
        self.addsizeproductbutton_2.setText(QCoreApplication.translate("Main", u"+", None))
        self.addproductoptionlabel_2.setText(QCoreApplication.translate("Main", u"Options", None))
        self.addoptionproductbutton_2.setText(QCoreApplication.translate("Main", u"+", None))
        self.addproductstocklabel_2.setText(QCoreApplication.translate("Main", u"Stock", None))
        self.addproductscategorieslabel_2.setText(QCoreApplication.translate("Main", u"Categories", None))
        self.checkBox_men_2.setText(QCoreApplication.translate("Main", u"Men", None))
        self.checkBox_women_2.setText(QCoreApplication.translate("Main", u"Women", None))
        self.checkBox_kids_2.setText(QCoreApplication.translate("Main", u"Kids", None))
        self.checkBox_top_2.setText(QCoreApplication.translate("Main", u"Top", None))
        self.checkBox_dress_2.setText(QCoreApplication.translate("Main", u"Dress", None))
        self.checkBox_headwear_2.setText(QCoreApplication.translate("Main", u"Headwear", None))
        self.checkBox_bottom_2.setText(QCoreApplication.translate("Main", u"Bottom", None))
        self.checkBox_footwear_2.setText(QCoreApplication.translate("Main", u"Footwear", None))
        self.checkBox_accessories_2.setText(QCoreApplication.translate("Main", u"Accesories", None))
        self.canceladdproductbutton_3.setText(QCoreApplication.translate("Main", u"Cancel", None))
        self.addproductbutton_3.setText(QCoreApplication.translate("Main", u"Add Product", None))
        self.profilepic.setText("")
        self.usernamelabel.setText(QCoreApplication.translate("Main", u"Username", None))
        self.favloriteabel.setText(QCoreApplication.translate("Main", u"3 Favorites", None))
        self.backbutton.setText("")
        self.myorderlabel.setText(QCoreApplication.translate("Main", u"My Orders", None))
        self.tobeshipbutton.setText("")
        self.tobereceivebutton.setText("")
        self.completebutton.setText("")
        self.picproduct1_15.setText("")
        self.favlabel.setText(QCoreApplication.translate("Main", u"Favorites", None))
        self.picproduct1_18.setText("")
        self.picproduct1_19.setText("")
        self.viewallfavbutton.setText(QCoreApplication.translate("Main", u"View all Favorites    >", None))
        self.openshopbutton.setText(QCoreApplication.translate("Main", u"           Open Your Shop", None))
        self.openshoppic.setText("")
        self.accsettingslabel_2.setText(QCoreApplication.translate("Main", u"Review", None))
        self.myacclabel_2.setText(QCoreApplication.translate("Main", u"Product's Name", None))
        self.settingslabel_2.setText(QCoreApplication.translate("Main", u"Size", None))
        self.helplabel_2.setText(QCoreApplication.translate("Main", u"Color", None))
        self.logoutsettingsbutton_2.setText(QCoreApplication.translate("Main", u"Submit", None))
        self.addproductimagelabel_4.setText(QCoreApplication.translate("Main", u"Product's Images", None))
        self.addimagebutton_4.setText(QCoreApplication.translate("Main", u"+", None))
        self.img_4.setText("")
        self.delete_pic_button_4.setText(QCoreApplication.translate("Main", u"X", None))
        self.myacclabel_3.setText(QCoreApplication.translate("Main", u"Customer's Name", None))
        self.myacclabel_5.setText(QCoreApplication.translate("Main", u"Quality", None))
        self.myacclabel_6.setText(QCoreApplication.translate("Main", u"Review Detail", None))
        self.curpasstextbox_2.setPlaceholderText("")
        self.curpasstextbox_4.setPlaceholderText("")
        self.curpasstextbox_5.setPlaceholderText("")
        self.curpasstextbox_6.setPlaceholderText("")
        self.curpasstextbox_7.setPlaceholderText("")
        self.curpasstextbox_8.setText("")
        self.curpasstextbox_8.setPlaceholderText("")
        self.backbutton_settings_2.setText("")
        self.editlabel.setText(QCoreApplication.translate("Main", u"Edit Profile", None))
        self.userabel.setText(QCoreApplication.translate("Main", u"Username", None))
        self.fisrtlabel.setText(QCoreApplication.translate("Main", u"First name", None))
        self.lastlabel.setText(QCoreApplication.translate("Main", u"Last name", None))
        self.genlabel.setText(QCoreApplication.translate("Main", u"Gender", None))
        self.birthlabel.setText(QCoreApplication.translate("Main", u"Birthday", None))
        self.pholabel.setText(QCoreApplication.translate("Main", u"Phone", None))
        self.emaillabel_2.setText(QCoreApplication.translate("Main", u"Email", None))
        self.userbox.setText("")
        self.userbox.setPlaceholderText(QCoreApplication.translate("Main", u"Username", None))
        self.firstnamebox.setText("")
        self.firstnamebox.setPlaceholderText(QCoreApplication.translate("Main", u"First name", None))
        self.genderbox.setText("")
        self.genderbox.setPlaceholderText(QCoreApplication.translate("Main", u"Gender", None))
        self.phonebox.setText("")
        self.phonebox.setPlaceholderText(QCoreApplication.translate("Main", u"Phone", None))
        self.lastnamebox.setText("")
        self.lastnamebox.setPlaceholderText(QCoreApplication.translate("Main", u"Last name", None))
        self.emailbox.setText("")
        self.emailbox.setPlaceholderText(QCoreApplication.translate("Main", u"Email", None))
        self.savechangebutton_2.setText(QCoreApplication.translate("Main", u"Save changes", None))
        self.deleteaccbutton.setText(QCoreApplication.translate("Main", u"Delete account", None))
        self.editprofilepic.setText("")
        self.editnameprofile.setText(QCoreApplication.translate("Main", u"User1", None))
        self.backbutton_2.setText("")
        self.accsettingslabel.setText(QCoreApplication.translate("Main", u"Account Settings", None))
        self.myacclabel.setText(QCoreApplication.translate("Main", u"My Account", None))
        self.accountbutton.setText(QCoreApplication.translate("Main", u"Account", None))
        self.settingslabel.setText(QCoreApplication.translate("Main", u"Settings", None))
        self.changepassbutton.setText(QCoreApplication.translate("Main", u"Change Password", None))
        self.editprobutton.setText(QCoreApplication.translate("Main", u"Edit Profile", None))
        self.helplabel.setText(QCoreApplication.translate("Main", u"Help", None))
        self.rulebutton.setText(QCoreApplication.translate("Main", u"Rules of use", None))
        self.logoutsettingsbutton.setText(QCoreApplication.translate("Main", u"Log out", None))
        self.addressbutton.setText(QCoreApplication.translate("Main", u"Address", None))
        self.backbutton_settings.setText("")
        self.addressdisplaylabel_3.setText(QCoreApplication.translate("Main", u"Address", None))
        self.fisrtnameaddress_3.setText(QCoreApplication.translate("Main", u"First name", None))
        self.lastnameaddress_3.setText(QCoreApplication.translate("Main", u"Last name", None))
        self.addressaddress_3.setText(QCoreApplication.translate("Main", u"Address", None))
        self.phoneaddress_3.setText(QCoreApplication.translate("Main", u"Phone", None))
        self.firstnameaddressdisplay_3.setText(QCoreApplication.translate("Main", u"Firsth name", None))
        self.phoneaddressdisplay_3.setText(QCoreApplication.translate("Main", u"Phone", None))
        self.lastnameaddressdisplay_3.setText(QCoreApplication.translate("Main", u"last name", None))
        self.addressaddressdisplay_3.setText(QCoreApplication.translate("Main", u"Address", None))
        self.editaddressbutton.setText(QCoreApplication.translate("Main", u"Edit", None))
        self.backtomainsettingbutton_5.setText("")
        self.editaddrlabel.setText(QCoreApplication.translate("Main", u"Edit Address", None))
        self.firstnameeditaddr.setText(QCoreApplication.translate("Main", u"First name", None))
        self.lastnameeditaddr.setText(QCoreApplication.translate("Main", u"Last name", None))
        self.addresseditaddr.setText(QCoreApplication.translate("Main", u"Address", None))
        self.phoneeditaddr.setText(QCoreApplication.translate("Main", u"Phone", None))
        self.savechangeeditaddrbutton.setText(QCoreApplication.translate("Main", u"Save Changes", None))
        self.firstnameeditaddrbox.setText("")
        self.firstnameeditaddrbox.setPlaceholderText(QCoreApplication.translate("Main", u"Firstname", None))
        self.lastnameeditaddrbox.setText("")
        self.lastnameeditaddrbox.setPlaceholderText(QCoreApplication.translate("Main", u"Lastname", None))
        self.phoneeditaddrbox.setText("")
        self.phoneeditaddrbox.setPlaceholderText(QCoreApplication.translate("Main", u"Phone", None))
        self.addresseditaddrbox.setText("")
        self.addresseditaddrbox.setPlaceholderText(QCoreApplication.translate("Main", u"Address", None))
        self.cleardataeditaddrbutton.setText(QCoreApplication.translate("Main", u"Clear Data", None))
        self.backtoeditarresssettingbutton.setText("")
        self.backtomainsettingbutton_2.setText("")
        self.changepasswordlabel.setText(QCoreApplication.translate("Main", u"Change Password", None))
        self.currentpasslabel.setText(QCoreApplication.translate("Main", u"Current Password", None))
        self.savechangebutton_4.setText(QCoreApplication.translate("Main", u"Save changes", None))
        self.newpasslabel.setText(QCoreApplication.translate("Main", u"New Password", None))
        self.curpasstextbox.setPlaceholderText(QCoreApplication.translate("Main", u"Current Password", None))
        self.newpasstextbox.setPlaceholderText(QCoreApplication.translate("Main", u"New Password", None))
        self.backtomainsettingbutton_4.setText("")
        self.profilelabel.setText(QCoreApplication.translate("Main", u"Profile", None))
        self.usernameprofile.setText(QCoreApplication.translate("Main", u"Username", None))
        self.fisrtnameprofile.setText(QCoreApplication.translate("Main", u"First name", None))
        self.lastnameprofile.setText(QCoreApplication.translate("Main", u"Last name", None))
        self.genderprofile.setText(QCoreApplication.translate("Main", u"Gender", None))
        self.birthprofile.setText(QCoreApplication.translate("Main", u"Birthday", None))
        self.phoneprofile.setText(QCoreApplication.translate("Main", u"Phone", None))
        self.emailprofile.setText(QCoreApplication.translate("Main", u"Email", None))
        self.pictureprofile.setText("")
        self.username.setText(QCoreApplication.translate("Main", u"User1", None))
        self.firstname.setText(QCoreApplication.translate("Main", u"First name", None))
        self.gender.setText(QCoreApplication.translate("Main", u"Gender", None))
        self.phone.setText(QCoreApplication.translate("Main", u"Phone", None))
        self.lastname.setText(QCoreApplication.translate("Main", u"last name", None))
        self.birthday.setText(QCoreApplication.translate("Main", u"bday", None))
        self.email.setText(QCoreApplication.translate("Main", u"email", None))
        self.editlabel_2.setText(QCoreApplication.translate("Main", u"Edit Profile", None))
        self.userabel_2.setText(QCoreApplication.translate("Main", u"Username", None))
        self.fisrtlabel_2.setText(QCoreApplication.translate("Main", u"First name", None))
        self.lastlabel_2.setText(QCoreApplication.translate("Main", u"Last name", None))
        self.genlabel_2.setText(QCoreApplication.translate("Main", u"Gender", None))
        self.birthlabel_2.setText(QCoreApplication.translate("Main", u"Birthday", None))
        self.pholabel_2.setText(QCoreApplication.translate("Main", u"Phone", None))
        self.emaillabel_3.setText(QCoreApplication.translate("Main", u"Email", None))
        self.userbox_2.setText("")
        self.userbox_2.setPlaceholderText(QCoreApplication.translate("Main", u"Username", None))
        self.firstnamebox_2.setText("")
        self.firstnamebox_2.setPlaceholderText(QCoreApplication.translate("Main", u"First name", None))
        self.genderbox_2.setText("")
        self.genderbox_2.setPlaceholderText(QCoreApplication.translate("Main", u"Gender", None))
        self.phonebox_2.setText("")
        self.phonebox_2.setPlaceholderText(QCoreApplication.translate("Main", u"Phone", None))
        self.lastnamebox_2.setText("")
        self.lastnamebox_2.setPlaceholderText(QCoreApplication.translate("Main", u"Last name", None))
        self.emailbox_2.setText("")
        self.emailbox_2.setPlaceholderText(QCoreApplication.translate("Main", u"Email", None))
        self.savechangebutton_3.setText(QCoreApplication.translate("Main", u"Save changes", None))
        self.deleteaccbutton_2.setText(QCoreApplication.translate("Main", u"Delete account", None))
        self.editprofilepic_2.setText("")
        self.editnameprofile_2.setText(QCoreApplication.translate("Main", u"User1", None))
        self.backtomainsettingbutton_3.setText("")
        self.backtomainsettingbutton.setText("")
        self.ruleofuselabel.setText(QCoreApplication.translate("Main", u"Rule of use", None))
        self.ruleofusecontentlabel.setText(QCoreApplication.translate("Main", u"1. Eligibility: Users must be at least 18 years old or have the consent of a parent or legal guardian to use the app.\n"
"\n"
"Account Creation: Users must create an account to access certain features of the app, such as placing orders, tracking shipments, and saving payment methods.\n"
"\n"
"Accuracy of Information: Users are responsible for providing accurate and up-to-date information when creating an account, placing orders, and updating their profile.\n"
"\n"
"Security: Users are responsible for maintaining the security of their account credentials (username, password, etc.) and must not share this information with others.\n"
"\n"
"Prohibited Activities: Users must not engage in any illegal, fraudulent, or unauthorized activities while using the app. This includes but is not limited to hacking, phishing, and unauthorized access to other users' accounts.\n"
"\n"
"Intellectual Property: Users must respect the intellectual property rights of others, including copyrights, trademarks, and patents. Any use of c"
                        "opyrighted material must be done with proper authorization.\n"
"\n"
"Product Listings: Sellers must provide accurate and truthful information about their products, including descriptions, images, and pricing. Any misleading or deceptive practices are prohibited.\n"
"\n"
"Payment: Users must provide valid payment information when making purchases through the app. All transactions are subject to the app's payment policies and may be processed securely through a trusted payment gateway.\n"
"\n"
"Shipping and Delivery: Users should provide accurate shipping addresses to ensure timely delivery of their orders. The app will provide estimated delivery times, but delays may occur due to unforeseen circumstances such as weather or logistical issues.\n"
"\n"
"Returns and Refunds: Users may be eligible for returns and refunds according to the app's return policy. Any returned items must be in their original condition and packaging.\n"
"\n"
"User Conduct: Users must conduct themselves in a respectful and courteous manner "
                        "when interacting with other users, sellers, and customer support representatives. Any harassment, bullying, or abusive behavior will not be tolerated.\n"
"\n"
"Feedback and Reviews: Users are encouraged to provide honest feedback and reviews about their shopping experience and the products they purchase. However, any reviews containing offensive language, personal attacks, or false information will be removed.\n"
"\n"
"Privacy: The app will collect and process personal information according to its privacy policy. Users should review the privacy policy to understand how their data is collected, used, and protected.\n"
"\n"
"Updates and Modifications: The app reserves the right to update or modify these rules of use at any time. Users will be notified of any changes, and continued use of the app constitutes acceptance of the revised rules.\n"
"\n"
"Termination of Account: The app reserves the right to suspend or terminate user accounts that violate these rules of use or engage in prohibited activities. Users wil"
                        "l be notified of any account suspensions or terminations and may appeal the decision if necessary.", None))
        self.canceladdproductbutton_2.setText(QCoreApplication.translate("Main", u"Cancel", None))
        self.addproductbutton_2.setText(QCoreApplication.translate("Main", u"Add Product", None))
    # retranslateUi

