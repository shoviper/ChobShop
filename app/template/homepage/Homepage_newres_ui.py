# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Homepage_newres.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(1280, 720)
        Main.setStyleSheet(u"background-color: #FAF9F6;")
        self.stackedWidget = QStackedWidget(Main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-1, -1, 1281, 721))
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
        self.Logolabel.setStyleSheet(u"font-family: Supermercado;\n"
"                font-size: 36px;\n"
"                font-weight: 700;\n"
"                line-height: normalpx;\n"
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
"                font-weight: 500;\n"
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
"                font-weight: 500;\n"
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
"                font-weight: 500;\n"
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
"                font-weight: 500;\n"
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
        self.settingbutton.setGeometry(QRect(70, 630, 41, 41))
        self.settingbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingbutton.setStyleSheet(u"border: none;")
        icon = QIcon()
        icon.addFile(u"../../assets/images/newres/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingbutton.setIcon(icon)
        self.settingbutton.setIconSize(QSize(30, 30))
        self.exitbutton = QPushButton(self.navbar)
        self.exitbutton.setObjectName(u"exitbutton")
        self.exitbutton.setGeometry(QRect(140, 630, 41, 41))
        self.exitbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitbutton.setStyleSheet(u"image: url(://assets/newres/exitbutton.png);\n"
"border: none;")
        icon1 = QIcon()
        icon1.addFile(u"../../assets/images/newres/exitbutton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitbutton.setIcon(icon1)
        self.exitbutton.setIconSize(QSize(27, 27))
        self.exitbutton.setFlat(False)

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
        self.cartbutton.setStyleSheet(u"border: none;")
        icon2 = QIcon()
        icon2.addFile(u"../../assets/images/newres/cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cartbutton.setIcon(icon2)
        self.cartbutton.setIconSize(QSize(34, 31))
        self.profilebutton = QPushButton(self.searchcontainer)
        self.profilebutton.setObjectName(u"profilebutton")
        self.profilebutton.setGeometry(QRect(840, 50, 31, 31))
        self.profilebutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.profilebutton.setStyleSheet(u"border: none;")
        icon3 = QIcon()
        icon3.addFile(u"../../assets/images/newres/profile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profilebutton.setIcon(icon3)
        self.profilebutton.setIconSize(QSize(31, 31))
        self.stackedWidget_main = QStackedWidget(self.main)
        self.stackedWidget_main.setObjectName(u"stackedWidget_main")
        self.stackedWidget_main.setGeometry(QRect(250, 110, 1031, 611))
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -380, 1006, 1000))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 1000))
        self.frame_homepage = QFrame(self.scrollAreaWidgetContents)
        self.frame_homepage.setObjectName(u"frame_homepage")
        self.frame_homepage.setGeometry(QRect(0, 0, 1031, 1000))
        self.frame_homepage.setMinimumSize(QSize(0, 1000))
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
        icon4 = QIcon()
        icon4.addFile(u"../../assets/images/newres/newarrival.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newarrivalbutton.setIcon(icon4)
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
        icon5 = QIcon()
        icon5.addFile(u"../../assets/images/newres/onsales.png", QSize(), QIcon.Normal, QIcon.Off)
        self.onsalesbutton.setIcon(icon5)
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
        icon6 = QIcon()
        icon6.addFile(u"../../assets/images/newres/buyagain.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buyagainbutton.setIcon(icon6)
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
        icon7 = QIcon()
        icon7.addFile(u"../../assets/images/newres/bestselling.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bestsellingbutton.setIcon(icon7)
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
        self.product_1 = QWidget(self.frame_homepage)
        self.product_1.setObjectName(u"product_1")
        self.product_1.setGeometry(QRect(60, 500, 251, 320))
        self.product_1.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1_3 = QPushButton(self.product_1)
        self.picproduct1_3.setObjectName(u"picproduct1_3")
        self.picproduct1_3.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_3.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_2 = QWidget(self.frame_homepage)
        self.product_2.setObjectName(u"product_2")
        self.product_2.setGeometry(QRect(720, 500, 251, 320))
        self.product_2.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1_4 = QPushButton(self.product_2)
        self.picproduct1_4.setObjectName(u"picproduct1_4")
        self.picproduct1_4.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_4.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_3 = QWidget(self.frame_homepage)
        self.product_3.setObjectName(u"product_3")
        self.product_3.setGeometry(QRect(390, 500, 251, 320))
        self.product_3.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1_5 = QPushButton(self.product_3)
        self.picproduct1_5.setObjectName(u"picproduct1_5")
        self.picproduct1_5.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_5.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_6 = QWidget(self.frame_homepage)
        self.product_6.setObjectName(u"product_6")
        self.product_6.setGeometry(QRect(720, 900, 251, 320))
        self.product_6.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1_11 = QPushButton(self.product_6)
        self.picproduct1_11.setObjectName(u"picproduct1_11")
        self.picproduct1_11.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_11.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_5 = QWidget(self.frame_homepage)
        self.product_5.setObjectName(u"product_5")
        self.product_5.setGeometry(QRect(60, 900, 251, 320))
        self.product_5.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1_10 = QPushButton(self.product_5)
        self.picproduct1_10.setObjectName(u"picproduct1_10")
        self.picproduct1_10.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_10.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_4 = QWidget(self.frame_homepage)
        self.product_4.setObjectName(u"product_4")
        self.product_4.setGeometry(QRect(390, 900, 251, 320))
        self.product_4.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1_9 = QPushButton(self.product_4)
        self.picproduct1_9.setObjectName(u"picproduct1_9")
        self.picproduct1_9.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_9.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.scrollArea_homepage.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget_main.addWidget(self.homepage)
        self.favpage = QWidget()
        self.favpage.setObjectName(u"favpage")
        self.favpage.setStyleSheet(u"favpage")
        self.scrollArea = QScrollArea(self.favpage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(-1, -1, 1021, 611))
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
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1006, 1000))
        self.scrollAreaWidgetContents_2.setMinimumSize(QSize(0, 1000))
        self.frame = QFrame(self.scrollAreaWidgetContents_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 1031, 611))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.product_7 = QWidget(self.frame)
        self.product_7.setObjectName(u"product_7")
        self.product_7.setGeometry(QRect(720, 520, 251, 320))
        self.product_7.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1_12 = QPushButton(self.product_7)
        self.picproduct1_12.setObjectName(u"picproduct1_12")
        self.picproduct1_12.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_12.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_8 = QWidget(self.frame)
        self.product_8.setObjectName(u"product_8")
        self.product_8.setGeometry(QRect(60, 120, 251, 320))
        self.product_8.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1_6 = QPushButton(self.product_8)
        self.picproduct1_6.setObjectName(u"picproduct1_6")
        self.picproduct1_6.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_6.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_9 = QWidget(self.frame)
        self.product_9.setObjectName(u"product_9")
        self.product_9.setGeometry(QRect(720, 120, 251, 320))
        self.product_9.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1_7 = QPushButton(self.product_9)
        self.picproduct1_7.setObjectName(u"picproduct1_7")
        self.picproduct1_7.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_7.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_10 = QWidget(self.frame)
        self.product_10.setObjectName(u"product_10")
        self.product_10.setGeometry(QRect(390, 120, 251, 320))
        self.product_10.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1_8 = QPushButton(self.product_10)
        self.picproduct1_8.setObjectName(u"picproduct1_8")
        self.picproduct1_8.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_8.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_11 = QWidget(self.frame)
        self.product_11.setObjectName(u"product_11")
        self.product_11.setGeometry(QRect(390, 520, 251, 320))
        self.product_11.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1_13 = QPushButton(self.product_11)
        self.picproduct1_13.setObjectName(u"picproduct1_13")
        self.picproduct1_13.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_13.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_12 = QWidget(self.frame)
        self.product_12.setObjectName(u"product_12")
        self.product_12.setGeometry(QRect(60, 520, 251, 320))
        self.product_12.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1_14 = QPushButton(self.product_12)
        self.picproduct1_14.setObjectName(u"picproduct1_14")
        self.picproduct1_14.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_14.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.suggestlabel_2 = QLabel(self.frame)
        self.suggestlabel_2.setObjectName(u"suggestlabel_2")
        self.suggestlabel_2.setGeometry(QRect(60, 10, 201, 41))
        self.suggestlabel_2.setStyleSheet(u"color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 32px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget_main.addWidget(self.favpage)
        self.stackedWidget.addWidget(self.main)
        self.userprofile = QWidget()
        self.userprofile.setObjectName(u"userprofile")
        self.stackedWidget.addWidget(self.userprofile)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Form", None))
        self.Logolabel.setText(QCoreApplication.translate("Main", u"ChopShop", None))
        self.homebutton.setText(QCoreApplication.translate("Main", u"Home", None))
        self.favbutton.setText(QCoreApplication.translate("Main", u"Favorites", None))
        self.orderbutton.setText(QCoreApplication.translate("Main", u"My Orders", None))
        self.messbutton.setText(QCoreApplication.translate("Main", u"Messages", None))
        self.settingbutton.setText("")
        self.exitbutton.setText("")
        self.searchbox.setPlaceholderText(QCoreApplication.translate("Main", u"Search..", None))
        self.loginsignoutbutton.setText(QCoreApplication.translate("Main", u"Log In", None))
        self.cartbutton.setText("")
        self.profilebutton.setText("")
        self.stylelabbutton.setText(QCoreApplication.translate("Main", u"Style Lab", None))
        self.newarrivalbutton.setText(QCoreApplication.translate("Main", u"New Arrival", None))
        self.onsalesbutton.setText(QCoreApplication.translate("Main", u"On Sales", None))
        self.buyagainbutton.setText(QCoreApplication.translate("Main", u"Buy Again", None))
        self.bestsellingbutton.setText(QCoreApplication.translate("Main", u"Best Selling", None))
        self.suggestlabel.setText(QCoreApplication.translate("Main", u"Suggestions", None))
        self.picproduct1_3.setText("")
        self.picproduct1_4.setText("")
        self.picproduct1_5.setText("")
        self.picproduct1_11.setText("")
        self.picproduct1_10.setText("")
        self.picproduct1_9.setText("")
        self.picproduct1_12.setText("")
        self.picproduct1_6.setText("")
        self.picproduct1_7.setText("")
        self.picproduct1_8.setText("")
        self.picproduct1_13.setText("")
        self.picproduct1_14.setText("")
        self.suggestlabel_2.setText(QCoreApplication.translate("Main", u"Favorites", None))
    # retranslateUi

