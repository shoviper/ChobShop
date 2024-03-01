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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
import app.assets.realsourceimg.real

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(1280, 720)
        Main.setStyleSheet(u"background-color: #FAF9F6;")
        self.stackedWidget = QStackedWidget(Main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-1, -1, 1280, 720))
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
        self.settingbutton.setGeometry(QRect(70, 630, 30, 30))
        self.settingbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingbutton.setStyleSheet(u"image: url(:/pic/realimages/settingpic.png);\n"
"border: none;")
        self.settingbutton.setIconSize(QSize(30, 30))
        self.exitbutton = QPushButton(self.navbar)
        self.exitbutton.setObjectName(u"exitbutton")
        self.exitbutton.setGeometry(QRect(140, 630, 27, 27))
        self.exitbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitbutton.setStyleSheet(u"image: url(:/pic/realimages/exitpic.png);\n"
"border: none;")
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1006, 1000))
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
        self.newarrivalpic = QLabel(self.frame_homepage)
        self.newarrivalpic.setObjectName(u"newarrivalpic")
        self.newarrivalpic.setGeometry(QRect(75, 300, 20, 20))
        self.newarrivalpic.setStyleSheet(u"border: none;\n"
"background: none;\n"
"image: url(:/pic/images/newres/newarrival.png);")
        self.onsalepic = QLabel(self.frame_homepage)
        self.onsalepic.setObjectName(u"onsalepic")
        self.onsalepic.setGeometry(QRect(325, 300, 20, 20))
        self.onsalepic.setStyleSheet(u"border: none;\n"
"background: none;\n"
"image: url(:/pic/images/newres/onsales.png);")
        self.buyafainpic = QLabel(self.frame_homepage)
        self.buyafainpic.setObjectName(u"buyafainpic")
        self.buyafainpic.setGeometry(QRect(570, 300, 20, 20))
        self.buyafainpic.setStyleSheet(u"border: none;\n"
"background: none;\n"
"image: url(:/pic/images/newres/buyagain.png);")
        self.bestsellpic = QLabel(self.frame_homepage)
        self.bestsellpic.setObjectName(u"bestsellpic")
        self.bestsellpic.setGeometry(QRect(805, 300, 20, 20))
        self.bestsellpic.setStyleSheet(u"border: none;\n"
"background: none;\n"
"image: url(:/pic/images/newres/bestselling.png);")
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
        self.scrollAreaWidgetContents_tobeshipped.setGeometry(QRect(0, 0, 1016, 500))
        self.scrollAreaWidgetContents_tobeshipped.setMinimumSize(QSize(0, 500))
        self.frame_tobeshipped = QFrame(self.scrollAreaWidgetContents_tobeshipped)
        self.frame_tobeshipped.setObjectName(u"frame_tobeshipped")
        self.frame_tobeshipped.setGeometry(QRect(0, 0, 1031, 471))
        self.frame_tobeshipped.setFrameShape(QFrame.StyledPanel)
        self.frame_tobeshipped.setFrameShadow(QFrame.Raised)
        self.tobeshippedlabel = QLabel(self.frame_tobeshipped)
        self.tobeshippedlabel.setObjectName(u"tobeshippedlabel")
        self.tobeshippedlabel.setGeometry(QRect(470, 180, 211, 111))
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
        self.toberecievedlabel = QLabel(self.frame_toberecieved)
        self.toberecievedlabel.setObjectName(u"toberecievedlabel")
        self.toberecievedlabel.setGeometry(QRect(470, 180, 211, 111))
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
        self.completedlabel = QLabel(self.frame_completed)
        self.completedlabel.setObjectName(u"completedlabel")
        self.completedlabel.setGeometry(QRect(470, 180, 211, 111))
        self.scrollArea_completed.setWidget(self.scrollAreaWidgetContents_completed)
        self.stackedWidget_myorders.addWidget(self.completedpage)
        self.stackedWidget_main.addWidget(self.myorderspage)
        self.stackedWidget.addWidget(self.main)
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
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1247, 1018))
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
        self.editprofilebutton = QPushButton(self.profilecontainer)
        self.editprofilebutton.setObjectName(u"editprofilebutton")
        self.editprofilebutton.setGeometry(QRect(250, 90, 131, 41))
        self.editprofilebutton.setStyleSheet(u"border: none;\n"
"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"text-align: left;")
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
        self.pushButton = QPushButton(self.favcontainer)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1020, 0, 121, 24))
        self.pushButton.setStyleSheet(u"color:  #CD4662;\n"
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

        self.retranslateUi(Main)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_main.setCurrentIndex(0)


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
        self.newarrivalpic.setText("")
        self.onsalepic.setText("")
        self.buyafainpic.setText("")
        self.bestsellpic.setText("")
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
        self.tobeshippedlabel.setText(QCoreApplication.translate("Main", u"to be shipped", None))
        self.toberecievedlabel.setText(QCoreApplication.translate("Main", u"to be recieved", None))
        self.completedlabel.setText(QCoreApplication.translate("Main", u"completed", None))
        self.profilepic.setText("")
        self.usernamelabel.setText(QCoreApplication.translate("Main", u"Username", None))
        self.favloriteabel.setText(QCoreApplication.translate("Main", u"3 Favorites", None))
        self.editprofilebutton.setText(QCoreApplication.translate("Main", u"Edit Profile", None))
        self.backbutton.setText("")
        self.myorderlabel.setText(QCoreApplication.translate("Main", u"My Orders", None))
        self.tobeshipbutton.setText("")
        self.tobereceivebutton.setText("")
        self.completebutton.setText("")
        self.picproduct1_15.setText("")
        self.favlabel.setText(QCoreApplication.translate("Main", u"Favorites", None))
        self.picproduct1_18.setText("")
        self.picproduct1_19.setText("")
        self.pushButton.setText(QCoreApplication.translate("Main", u"View all Favorites    >", None))
        self.openshopbutton.setText(QCoreApplication.translate("Main", u"           Open Your Shop", None))
        self.openshoppic.setText("")
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
    # retranslateUi

