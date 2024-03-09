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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)
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
        self.cartpage = QWidget()
        self.cartpage.setObjectName(u"cartpage")
        self.verticalLayout_3 = QVBoxLayout(self.cartpage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea_cart = QScrollArea(self.cartpage)
        self.scrollArea_cart.setObjectName(u"scrollArea_cart")
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
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 998, 2018))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_cartpage = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_cartpage.setObjectName(u"frame_cartpage")
        self.frame_cartpage.setMinimumSize(QSize(0, 2000))
        self.frame_cartpage.setFrameShape(QFrame.StyledPanel)
        self.frame_cartpage.setFrameShadow(QFrame.Raised)
        self.cartshopcontainer = QWidget(self.frame_cartpage)
        self.cartshopcontainer.setObjectName(u"cartshopcontainer")
        self.cartshopcontainer.setGeometry(QRect(41, 0, 912, 269))
        self.cartshopcontainer.setStyleSheet(u"border-bottom: 1px solid #CD4662;\n"
"background: #FAF9F6;\n"
"")
        self.shopnameforcart = QLabel(self.cartshopcontainer)
        self.shopnameforcart.setObjectName(u"shopnameforcart")
        self.shopnameforcart.setGeometry(QRect(43, 0, 131, 41))
        self.shopnameforcart.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.cartorderpic = QLabel(self.cartshopcontainer)
        self.cartorderpic.setObjectName(u"cartorderpic")
        self.cartorderpic.setGeometry(QRect(43, 51, 134, 134))
        self.cartorderpic.setStyleSheet(u"border: none;\n"
"border-radius: 70px;\n"
"background: #cd4662;")
        self.productcartname = QLabel(self.cartshopcontainer)
        self.productcartname.setObjectName(u"productcartname")
        self.productcartname.setGeometry(QRect(240, 51, 672, 28))
        self.productcartname.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.productcartdescrip = QLabel(self.cartshopcontainer)
        self.productcartdescrip.setObjectName(u"productcartdescrip")
        self.productcartdescrip.setGeometry(QRect(240, 104, 672, 28))
        self.productcartdescrip.setStyleSheet(u"border: none;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.productnum = QLabel(self.cartshopcontainer)
        self.productnum.setObjectName(u"productnum")
        self.productnum.setGeometry(QRect(240, 157, 672, 28))
        self.productnum.setStyleSheet(u"border: none;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.totalpricecartlabel = QLabel(self.cartshopcontainer)
        self.totalpricecartlabel.setObjectName(u"totalpricecartlabel")
        self.totalpricecartlabel.setGeometry(QRect(700, 157, 81, 28))
        self.totalpricecartlabel.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.totalpricecartnumlabel = QLabel(self.cartshopcontainer)
        self.totalpricecartnumlabel.setObjectName(u"totalpricecartnumlabel")
        self.totalpricecartnumlabel.setGeometry(QRect(850, 157, 49, 28))
        self.totalpricecartnumlabel.setStyleSheet(u"border: none;\n"
"color: #cd4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.checkstatuscartbutton = QPushButton(self.cartshopcontainer)
        self.checkstatuscartbutton.setObjectName(u"checkstatuscartbutton")
        self.checkstatuscartbutton.setGeometry(QRect(757, 210, 156, 42))
        self.checkstatuscartbutton.setStyleSheet(u"color: #FFF;\n"
"background-color: #cd4662;\n"
"border: none;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border-radius: 5px;")

        self.verticalLayout_4.addWidget(self.frame_cartpage)

        self.scrollArea_cart.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_3.addWidget(self.scrollArea_cart)

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
"                font-size: 24px;\n"
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
        self.myorderslabel.setGeometry(QRect(60, 10, 180, 31))
        self.myorderslabel.setStyleSheet(u"color: #545454;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
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
        self.shipordercontainer = QWidget(self.frame_tobeshipped)
        self.shipordercontainer.setObjectName(u"shipordercontainer")
        self.shipordercontainer.setGeometry(QRect(60, 40, 912, 269))
        self.shipordercontainer.setStyleSheet(u"border-bottom: 1px solid #CD4662;\n"
"background: #FAF9F6;\n"
"")
        self.shopnameforcart_2 = QLabel(self.shipordercontainer)
        self.shopnameforcart_2.setObjectName(u"shopnameforcart_2")
        self.shopnameforcart_2.setGeometry(QRect(43, 0, 131, 41))
        self.shopnameforcart_2.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.cartorderpic_2 = QLabel(self.shipordercontainer)
        self.cartorderpic_2.setObjectName(u"cartorderpic_2")
        self.cartorderpic_2.setGeometry(QRect(43, 51, 134, 134))
        self.cartorderpic_2.setStyleSheet(u"border: none;\n"
"border-radius: 70px;\n"
"background: #cd4662;")
        self.productcartname_2 = QLabel(self.shipordercontainer)
        self.productcartname_2.setObjectName(u"productcartname_2")
        self.productcartname_2.setGeometry(QRect(240, 51, 672, 28))
        self.productcartname_2.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.productcartdescrip_2 = QLabel(self.shipordercontainer)
        self.productcartdescrip_2.setObjectName(u"productcartdescrip_2")
        self.productcartdescrip_2.setGeometry(QRect(240, 104, 672, 28))
        self.productcartdescrip_2.setStyleSheet(u"border: none;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.productnum_2 = QLabel(self.shipordercontainer)
        self.productnum_2.setObjectName(u"productnum_2")
        self.productnum_2.setGeometry(QRect(240, 157, 672, 28))
        self.productnum_2.setStyleSheet(u"border: none;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.totalpricecartlabel_2 = QLabel(self.shipordercontainer)
        self.totalpricecartlabel_2.setObjectName(u"totalpricecartlabel_2")
        self.totalpricecartlabel_2.setGeometry(QRect(700, 157, 81, 28))
        self.totalpricecartlabel_2.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.totalpricecartnumlabel_2 = QLabel(self.shipordercontainer)
        self.totalpricecartnumlabel_2.setObjectName(u"totalpricecartnumlabel_2")
        self.totalpricecartnumlabel_2.setGeometry(QRect(850, 157, 49, 28))
        self.totalpricecartnumlabel_2.setStyleSheet(u"border: none;\n"
"color: #cd4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.checkstatusshipbutton = QPushButton(self.shipordercontainer)
        self.checkstatusshipbutton.setObjectName(u"checkstatusshipbutton")
        self.checkstatusshipbutton.setGeometry(QRect(757, 210, 156, 42))
        self.checkstatusshipbutton.setStyleSheet(u"color: #FFF;\n"
"background-color: #cd4662;\n"
"border: none;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border-radius: 5px;")
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
        self.givereviewcompletebutton = QPushButton(self.completeordercontainer)
        self.givereviewcompletebutton.setObjectName(u"givereviewcompletebutton")
        self.givereviewcompletebutton.setGeometry(QRect(560, 210, 156, 42))
        self.givereviewcompletebutton.setStyleSheet(u"color: #FFF;\n"
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
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 67, 1218))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_productviewpage = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_productviewpage.setObjectName(u"frame_productviewpage")
        self.frame_productviewpage.setMinimumSize(QSize(0, 1200))
        self.frame_productviewpage.setFrameShape(QFrame.StyledPanel)
        self.frame_productviewpage.setFrameShadow(QFrame.Raised)
        self.productcontainer_2 = QWidget(self.frame_productviewpage)
        self.productcontainer_2.setObjectName(u"productcontainer_2")
        self.productcontainer_2.setGeometry(QRect(46, 0, 910, 812))
        self.productcontainer_2.setStyleSheet(u"background-color: yellow\n"
";\n"
"border-radius: 10px 10px 0px 0px;")
        self.picpress1 = QPushButton(self.productcontainer_2)
        self.picpress1.setObjectName(u"picpress1")
        self.picpress1.setGeometry(QRect(47, 386, 88, 88))
        self.picpress1.setStyleSheet(u"border: 1px solid #000;\n"
"background-color: #D9D9D9;")
        self.picpress2 = QPushButton(self.productcontainer_2)
        self.picpress2.setObjectName(u"picpress2")
        self.picpress2.setGeometry(QRect(135, 386, 88, 88))
        self.picpress2.setStyleSheet(u"border: 1px solid #000;\n"
"background-color: #D9D9D9;")
        self.picpress3 = QPushButton(self.productcontainer_2)
        self.picpress3.setObjectName(u"picpress3")
        self.picpress3.setGeometry(QRect(223, 386, 88, 88))
        self.picpress3.setStyleSheet(u"border: 1px solid #000;\n"
"background-color: #D9D9D9;")
        self.picpress4 = QPushButton(self.productcontainer_2)
        self.picpress4.setObjectName(u"picpress4")
        self.picpress4.setGeometry(QRect(311, 386, 88, 88))
        self.picpress4.setStyleSheet(u"border: 1px solid #000;\n"
"background-color: #D9D9D9;")
        self.mainpic = QLabel(self.productcontainer_2)
        self.mainpic.setObjectName(u"mainpic")
        self.mainpic.setGeometry(QRect(47, 34, 352, 352))
        self.mainpic.setStyleSheet(u"border-radius: 10px 10px 0px 0px;\n"
"border: 1px solid #000;\n"
"background-color: #D9D9D9;")
        self.productname = QLabel(self.productcontainer_2)
        self.productname.setObjectName(u"productname")
        self.productname.setGeometry(QRect(584, 34, 281, 41))
        self.productname.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"background-color: red;\n"
"background-color: #FAF9F6;")
        self.productdetail = QLabel(self.productcontainer_2)
        self.productdetail.setObjectName(u"productdetail")
        self.productdetail.setGeometry(QRect(500, 300, 321, 274))
        self.productdetail.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid #000;\n"
"background-color: #FAF9F6;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.buynowbutton = QPushButton(self.productcontainer_2)
        self.buynowbutton.setObjectName(u"buynowbutton")
        self.buynowbutton.setGeometry(QRect(480, 230, 171, 44))
        self.buynowbutton.setStyleSheet(u"border-radius: 50px;\n"
"background-color: #CD4662;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"")
        self.addtocartbutton = QPushButton(self.productcontainer_2)
        self.addtocartbutton.setObjectName(u"addtocartbutton")
        self.addtocartbutton.setGeometry(QRect(690, 230, 161, 44))
        self.addtocartbutton.setStyleSheet(u"border-radius: 50px;\n"
"background-color: #CD4662;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.shopprofile = QLabel(self.productcontainer_2)
        self.shopprofile.setObjectName(u"shopprofile")
        self.shopprofile.setGeometry(QRect(490, 590, 141, 141))
        self.shopprofile.setStyleSheet(u"image: url(:/pic/images/profile.png);\n"
"background-color: #D9D9D9;\n"
"border-radius: 50%;")
        self.shopname = QLabel(self.productcontainer_2)
        self.shopname.setObjectName(u"shopname")
        self.shopname.setGeometry(QRect(650, 590, 201, 39))
        self.shopname.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.shopfollower = QLabel(self.productcontainer_2)
        self.shopfollower.setObjectName(u"shopfollower")
        self.shopfollower.setGeometry(QRect(650, 640, 277, 39))
        self.shopfollower.setStyleSheet(u"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.viewshopbutton = QPushButton(self.productcontainer_2)
        self.viewshopbutton.setObjectName(u"viewshopbutton")
        self.viewshopbutton.setGeometry(QRect(650, 710, 277, 46))
        self.viewshopbutton.setStyleSheet(u"color: #FFF;\n"
"background-color: #AEC289;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.star1 = QLabel(self.productcontainer_2)
        self.star1.setObjectName(u"star1")
        self.star1.setGeometry(QRect(660, 161, 36, 36))
        self.star1.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star2 = QLabel(self.productcontainer_2)
        self.star2.setObjectName(u"star2")
        self.star2.setGeometry(QRect(694, 161, 36, 36))
        self.star2.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star3 = QLabel(self.productcontainer_2)
        self.star3.setObjectName(u"star3")
        self.star3.setGeometry(QRect(728, 161, 36, 36))
        self.star3.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star4 = QLabel(self.productcontainer_2)
        self.star4.setObjectName(u"star4")
        self.star4.setGeometry(QRect(762, 161, 36, 36))
        self.star4.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star5 = QLabel(self.productcontainer_2)
        self.star5.setObjectName(u"star5")
        self.star5.setGeometry(QRect(796, 161, 36, 36))
        self.star5.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.numberofstar = QLabel(self.productcontainer_2)
        self.numberofstar.setObjectName(u"numberofstar")
        self.numberofstar.setGeometry(QRect(500, 161, 37, 40))
        self.numberofstar.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.numberofsold = QLabel(self.productcontainer_2)
        self.numberofsold.setObjectName(u"numberofsold")
        self.numberofsold.setGeometry(QRect(550, 161, 101, 40))
        self.numberofsold.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.currencypic = QLabel(self.productcontainer_2)
        self.currencypic.setObjectName(u"currencypic")
        self.currencypic.setGeometry(QRect(797, 115, 24, 38))
        self.currencypic.setStyleSheet(u"image: url(:/pic/images/baht.png);\n"
"border: none;")
        self.productprice = QLabel(self.productcontainer_2)
        self.productprice.setObjectName(u"productprice")
        self.productprice.setGeometry(QRect(584, 83, 281, 21))
        self.productprice.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_12.addWidget(self.frame_productviewpage)

        self.scrollArea_productviewpage.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_11.addWidget(self.scrollArea_productviewpage)

        self.stackedWidget_main.addWidget(self.productviewpage)
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
        self.searchcontainer_3 = QWidget(self.adminmain)
        self.searchcontainer_3.setObjectName(u"searchcontainer_3")
        self.searchcontainer_3.setGeometry(QRect(250, 0, 1031, 109))
        self.searchcontainer_3.setStyleSheet(u"background-color: #FAF9F6;")
        self.searchbox_3 = QLineEdit(self.searchcontainer_3)
        self.searchbox_3.setObjectName(u"searchbox_3")
        self.searchbox_3.setGeometry(QRect(50, 50, 746, 31))
        self.searchbox_3.setStyleSheet(u"				border-radius: 15px;\n"
"                background-color: #EDEDED;\n"
"                color: #CD4662;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 16px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"				padding-left: 20px;\n"
"")
        self.loginsignoutbutton_3 = QPushButton(self.searchcontainer_3)
        self.loginsignoutbutton_3.setObjectName(u"loginsignoutbutton_3")
        self.loginsignoutbutton_3.setGeometry(QRect(900, 50, 71, 31))
        self.loginsignoutbutton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginsignoutbutton_3.setStyleSheet(u"color: #000;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 20px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                border: none;\n"
"				text-align: center;")
        self.profilebutton_3 = QPushButton(self.searchcontainer_3)
        self.profilebutton_3.setObjectName(u"profilebutton_3")
        self.profilebutton_3.setGeometry(QRect(840, 50, 31, 31))
        self.profilebutton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.profilebutton_3.setStyleSheet(u"image: url(:/pic/realimages/profilepic.png);\n"
"border: none;")
        self.profilebutton_3.setIconSize(QSize(31, 31))
        self.navbar_3 = QWidget(self.adminmain)
        self.navbar_3.setObjectName(u"navbar_3")
        self.navbar_3.setGeometry(QRect(0, 0, 249, 719))
        self.navbar_3.setCursor(QCursor(Qt.ArrowCursor))
        self.navbar_3.setStyleSheet(u"background-color: #FAF9F6;")
        self.Logolabel_3 = QLabel(self.navbar_3)
        self.Logolabel_3.setObjectName(u"Logolabel_3")
        self.Logolabel_3.setGeometry(QRect(30, 40, 191, 51))
        self.Logolabel_3.setStyleSheet(u"font-family: Supermercado;\n"
"                font-size: 36px;\n"
"                font-weight: 700;\n"
"                line-height: normalpx;\n"
"                text-align: center;\n"
"                color: #000000;")
        self.homebutton_3 = QPushButton(self.navbar_3)
        self.homebutton_3.setObjectName(u"homebutton_3")
        self.homebutton_3.setGeometry(QRect(40, 130, 171, 67))
        self.homebutton_3.setStyleSheet(u"QPushButton{\n"
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
        self.homebutton_3.setCheckable(True)
        self.homebutton_3.setAutoExclusive(True)
        self.orderstatusbutton_3 = QPushButton(self.navbar_3)
        self.orderstatusbutton_3.setObjectName(u"orderstatusbutton_3")
        self.orderstatusbutton_3.setGeometry(QRect(40, 240, 171, 67))
        self.orderstatusbutton_3.setStyleSheet(u"QPushButton{\n"
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
        self.orderstatusbutton_3.setCheckable(True)
        self.orderstatusbutton_3.setAutoExclusive(True)
        self.orderproductbutton_2 = QPushButton(self.navbar_3)
        self.orderproductbutton_2.setObjectName(u"orderproductbutton_2")
        self.orderproductbutton_2.setGeometry(QRect(40, 350, 171, 67))
        self.orderproductbutton_2.setStyleSheet(u"QPushButton{\n"
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
        self.orderproductbutton_2.setCheckable(True)
        self.orderproductbutton_2.setAutoExclusive(True)
        self.messbutton_3 = QPushButton(self.navbar_3)
        self.messbutton_3.setObjectName(u"messbutton_3")
        self.messbutton_3.setGeometry(QRect(40, 460, 171, 67))
        self.messbutton_3.setStyleSheet(u"QPushButton{\n"
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
        self.messbutton_3.setCheckable(True)
        self.messbutton_3.setAutoExclusive(True)
        self.settingbutton_3 = QPushButton(self.navbar_3)
        self.settingbutton_3.setObjectName(u"settingbutton_3")
        self.settingbutton_3.setGeometry(QRect(70, 630, 30, 30))
        self.settingbutton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingbutton_3.setStyleSheet(u"image: url(:/pic/realimages/settingpic.png);\n"
"border: none;")
        self.settingbutton_3.setIconSize(QSize(30, 30))
        self.exitbutton_3 = QPushButton(self.navbar_3)
        self.exitbutton_3.setObjectName(u"exitbutton_3")
        self.exitbutton_3.setGeometry(QRect(140, 630, 27, 27))
        self.exitbutton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitbutton_3.setStyleSheet(u"image: url(:/pic/realimages/exitpic.png);\n"
"border: none;")
        self.exitbutton_3.setIconSize(QSize(27, 27))
        self.exitbutton_3.setFlat(False)
        self.stackedWidget_adminmain = QStackedWidget(self.adminmain)
        self.stackedWidget_adminmain.setObjectName(u"stackedWidget_adminmain")
        self.stackedWidget_adminmain.setGeometry(QRect(250, 110, 1031, 611))
        self.adminhomepage_2 = QWidget()
        self.adminhomepage_2.setObjectName(u"adminhomepage_2")
        self.scrollArea_adminhomepage_2 = QScrollArea(self.adminhomepage_2)
        self.scrollArea_adminhomepage_2.setObjectName(u"scrollArea_adminhomepage_2")
        self.scrollArea_adminhomepage_2.setGeometry(QRect(0, 0, 1021, 611))
        self.scrollArea_adminhomepage_2.setStyleSheet(u"QScrollArea {\n"
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
        self.scrollArea_adminhomepage_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 1006, 1338))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_11)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_adminhomepage_2 = QFrame(self.scrollAreaWidgetContents_11)
        self.frame_adminhomepage_2.setObjectName(u"frame_adminhomepage_2")
        self.frame_adminhomepage_2.setMinimumSize(QSize(0, 1320))
        self.frame_adminhomepage_2.setFrameShape(QFrame.StyledPanel)
        self.frame_adminhomepage_2.setFrameShadow(QFrame.Raised)
        self.adminhomepagecontainer_2 = QWidget(self.frame_adminhomepage_2)
        self.adminhomepagecontainer_2.setObjectName(u"adminhomepagecontainer_2")
        self.adminhomepagecontainer_2.setGeometry(QRect(40, 24, 913, 221))
        self.adminhomepagecontainer_2.setStyleSheet(u"border-radius: 10px;\n"
"background: #F4F2EF;")
        self.profilepic_3 = QLabel(self.adminhomepagecontainer_2)
        self.profilepic_3.setObjectName(u"profilepic_3")
        self.profilepic_3.setGeometry(QRect(47, 50, 130, 130))
        self.profilepic_3.setStyleSheet(u"border: none;\n"
"border-radius: 65px;\n"
"background: #cd4662;")
        self.usernamelabel_3 = QLabel(self.adminhomepagecontainer_2)
        self.usernamelabel_3.setObjectName(u"usernamelabel_3")
        self.usernamelabel_3.setGeometry(QRect(213, 93, 171, 41))
        self.usernamelabel_3.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.numreview_2 = QLabel(self.adminhomepagecontainer_2)
        self.numreview_2.setObjectName(u"numreview_2")
        self.numreview_2.setGeometry(QRect(480, 50, 49, 16))
        self.numreview_2.setStyleSheet(u"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numreview_2.setAlignment(Qt.AlignCenter)
        self.review_2 = QLabel(self.adminhomepagecontainer_2)
        self.review_2.setObjectName(u"review_2")
        self.review_2.setGeometry(QRect(560, 50, 61, 16))
        self.review_2.setStyleSheet(u"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numproduct_2 = QLabel(self.adminhomepagecontainer_2)
        self.numproduct_2.setObjectName(u"numproduct_2")
        self.numproduct_2.setGeometry(QRect(480, 140, 49, 16))
        self.numproduct_2.setStyleSheet(u"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numproduct_2.setAlignment(Qt.AlignCenter)
        self.product_22 = QLabel(self.adminhomepagecontainer_2)
        self.product_22.setObjectName(u"product_22")
        self.product_22.setGeometry(QRect(560, 140, 61, 16))
        self.product_22.setStyleSheet(u"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numsold_2 = QLabel(self.adminhomepagecontainer_2)
        self.numsold_2.setObjectName(u"numsold_2")
        self.numsold_2.setGeometry(QRect(680, 50, 49, 16))
        self.numsold_2.setStyleSheet(u"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numsold_2.setAlignment(Qt.AlignCenter)
        self.yearregis_2 = QLabel(self.adminhomepagecontainer_2)
        self.yearregis_2.setObjectName(u"yearregis_2")
        self.yearregis_2.setGeometry(QRect(760, 140, 121, 16))
        self.yearregis_2.setStyleSheet(u"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.yearregis_2.setAlignment(Qt.AlignCenter)
        self.sold_2 = QLabel(self.adminhomepagecontainer_2)
        self.sold_2.setObjectName(u"sold_2")
        self.sold_2.setGeometry(QRect(750, 50, 49, 16))
        self.sold_2.setStyleSheet(u"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.sold_2.setAlignment(Qt.AlignCenter)
        self.numyearregis_2 = QLabel(self.adminhomepagecontainer_2)
        self.numyearregis_2.setObjectName(u"numyearregis_2")
        self.numyearregis_2.setGeometry(QRect(680, 140, 49, 16))
        self.numyearregis_2.setStyleSheet(u"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.numyearregis_2.setAlignment(Qt.AlignCenter)
        self.orderstatuscontainer_2 = QWidget(self.frame_adminhomepage_2)
        self.orderstatuscontainer_2.setObjectName(u"orderstatuscontainer_2")
        self.orderstatuscontainer_2.setGeometry(QRect(40, 280, 913, 157))
        self.orderstatuscontainer_2.setStyleSheet(u"border-bottom: 3px solid #CD4662;\n"
"background: #FAF9F6;\n"
"")
        self.orderstatuslabel_2 = QLabel(self.orderstatuscontainer_2)
        self.orderstatuslabel_2.setObjectName(u"orderstatuslabel_2")
        self.orderstatuslabel_2.setGeometry(QRect(0, 0, 161, 25))
        self.orderstatuslabel_2.setStyleSheet(u"color: #000;\n"
"border: none;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.admintobeshipbutton_2 = QPushButton(self.orderstatuscontainer_2)
        self.admintobeshipbutton_2.setObjectName(u"admintobeshipbutton_2")
        self.admintobeshipbutton_2.setGeometry(QRect(100, 40, 90, 90))
        self.admintobeshipbutton_2.setStyleSheet(u"image: url(:/pic/images/newres/tobeshipped.png);\n"
"border: none;")
        self.admincancelbutton_2 = QPushButton(self.orderstatuscontainer_2)
        self.admincancelbutton_2.setObjectName(u"admincancelbutton_2")
        self.admincancelbutton_2.setGeometry(QRect(300, 40, 90, 90))
        self.admincancelbutton_2.setStyleSheet(u"image: url(:/pic/images/newres/toberecieved.png);\n"
"border: none;")
        self.admincompletebutton_2 = QPushButton(self.orderstatuscontainer_2)
        self.admincompletebutton_2.setObjectName(u"admincompletebutton_2")
        self.admincompletebutton_2.setGeometry(QRect(500, 40, 90, 90))
        self.admincompletebutton_2.setStyleSheet(u"image: url(:/pic/images/newres/completed.png);\n"
"border: none;")
        self.adminreviewbutton_2 = QPushButton(self.orderstatuscontainer_2)
        self.adminreviewbutton_2.setObjectName(u"adminreviewbutton_2")
        self.adminreviewbutton_2.setGeometry(QRect(700, 40, 90, 90))
        self.adminreviewbutton_2.setStyleSheet(u"image: url(:/pic/images/newres/completed.png);\n"
"border: none;")
        self.orderstatusbutton_4 = QPushButton(self.orderstatuscontainer_2)
        self.orderstatusbutton_4.setObjectName(u"orderstatusbutton_4")
        self.orderstatusbutton_4.setGeometry(QRect(730, 0, 181, 24))
        self.orderstatusbutton_4.setStyleSheet(u"color:  #CD4662;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.productcontainer_3 = QWidget(self.frame_adminhomepage_2)
        self.productcontainer_3.setObjectName(u"productcontainer_3")
        self.productcontainer_3.setGeometry(QRect(40, 470, 913, 800))
        self.productcontainer_3.setStyleSheet(u"border-bottom: 3px solid #CD4662;\n"
"background: #FAF9F6;")
        self.product_23 = QWidget(self.productcontainer_3)
        self.product_23.setObjectName(u"product_23")
        self.product_23.setGeometry(QRect(30, 70, 251, 320))
        self.product_23.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;\n"
"border:none;")
        self.picproduct1_24 = QPushButton(self.product_23)
        self.picproduct1_24.setObjectName(u"picproduct1_24")
        self.picproduct1_24.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_24.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.favlabel_3 = QLabel(self.productcontainer_3)
        self.favlabel_3.setObjectName(u"favlabel_3")
        self.favlabel_3.setGeometry(QRect(0, 0, 111, 25))
        self.favlabel_3.setStyleSheet(u"color: #000;\n"
"border: none;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.product_24 = QWidget(self.productcontainer_3)
        self.product_24.setObjectName(u"product_24")
        self.product_24.setGeometry(QRect(333, 70, 251, 320))
        self.product_24.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;\n"
"border:none;")
        self.picproduct1_25 = QPushButton(self.product_24)
        self.picproduct1_25.setObjectName(u"picproduct1_25")
        self.picproduct1_25.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_25.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_25 = QWidget(self.productcontainer_3)
        self.product_25.setObjectName(u"product_25")
        self.product_25.setGeometry(QRect(637, 70, 251, 320))
        self.product_25.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;\n"
"border:none;")
        self.picproduct1_26 = QPushButton(self.product_25)
        self.picproduct1_26.setObjectName(u"picproduct1_26")
        self.picproduct1_26.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_26.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_27 = QWidget(self.productcontainer_3)
        self.product_27.setObjectName(u"product_27")
        self.product_27.setGeometry(QRect(637, 440, 251, 320))
        self.product_27.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;\n"
"border:none;")
        self.picproduct1_27 = QPushButton(self.product_27)
        self.picproduct1_27.setObjectName(u"picproduct1_27")
        self.picproduct1_27.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_27.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_28 = QWidget(self.productcontainer_3)
        self.product_28.setObjectName(u"product_28")
        self.product_28.setGeometry(QRect(333, 440, 251, 320))
        self.product_28.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;\n"
"border:none;")
        self.picproduct1_28 = QPushButton(self.product_28)
        self.picproduct1_28.setObjectName(u"picproduct1_28")
        self.picproduct1_28.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_28.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_34 = QWidget(self.productcontainer_3)
        self.product_34.setObjectName(u"product_34")
        self.product_34.setGeometry(QRect(30, 440, 251, 320))
        self.product_34.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;\n"
"border:none;")
        self.picproduct1_29 = QPushButton(self.product_34)
        self.picproduct1_29.setObjectName(u"picproduct1_29")
        self.picproduct1_29.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_29.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.viewallproductbutton_2 = QPushButton(self.productcontainer_3)
        self.viewallproductbutton_2.setObjectName(u"viewallproductbutton_2")
        self.viewallproductbutton_2.setGeometry(QRect(750, 0, 161, 24))
        self.viewallproductbutton_2.setStyleSheet(u"color:  #CD4662;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")

        self.verticalLayout_15.addWidget(self.frame_adminhomepage_2)

        self.scrollArea_adminhomepage_2.setWidget(self.scrollAreaWidgetContents_11)
        self.stackedWidget_adminmain.addWidget(self.adminhomepage_2)
        self.adminproductspage = QWidget()
        self.adminproductspage.setObjectName(u"adminproductspage")
        self.stackedWidget_adminproducts = QStackedWidget(self.adminproductspage)
        self.stackedWidget_adminproducts.setObjectName(u"stackedWidget_adminproducts")
        self.stackedWidget_adminproducts.setGeometry(QRect(0, 0, 1031, 611))
        self.stackedWidget_adminproducts.setStyleSheet(u"background: #FAF9F6")
        self.adminproductspage_alltypes = QWidget()
        self.adminproductspage_alltypes.setObjectName(u"adminproductspage_alltypes")
        self.adminproductcontainernav = QWidget(self.adminproductspage_alltypes)
        self.adminproductcontainernav.setObjectName(u"adminproductcontainernav")
        self.adminproductcontainernav.setGeometry(QRect(0, 0, 1031, 139))
        self.adminproductcontainernav.setStyleSheet(u"background-color: #FAF9F6;")
        self.productlabel_3 = QLabel(self.adminproductcontainernav)
        self.productlabel_3.setObjectName(u"productlabel_3")
        self.productlabel_3.setGeometry(QRect(50, 0, 180, 51))
        self.productlabel_3.setStyleSheet(u"color: #545454;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.allproductbutton_3 = QPushButton(self.adminproductcontainernav)
        self.allproductbutton_3.setObjectName(u"allproductbutton_3")
        self.allproductbutton_3.setGeometry(QRect(50, 90, 455, 50))
        self.allproductbutton_3.setStyleSheet(u"QPushButton{\n"
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
        self.producttypesbutton_3 = QPushButton(self.adminproductcontainernav)
        self.producttypesbutton_3.setObjectName(u"producttypesbutton_3")
        self.producttypesbutton_3.setGeometry(QRect(510, 90, 455, 50))
        self.producttypesbutton_3.setStyleSheet(u"QPushButton{\n"
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
        self.stackedWidget_allandtype = QStackedWidget(self.adminproductspage_alltypes)
        self.stackedWidget_allandtype.setObjectName(u"stackedWidget_allandtype")
        self.stackedWidget_allandtype.setGeometry(QRect(0, 140, 1031, 471))
        self.adminallproductpage = QWidget()
        self.adminallproductpage.setObjectName(u"adminallproductpage")
        self.verticalLayout_24 = QVBoxLayout(self.adminallproductpage)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.scrollArea_allproduct_3 = QScrollArea(self.adminallproductpage)
        self.scrollArea_allproduct_3.setObjectName(u"scrollArea_allproduct_3")
        self.scrollArea_allproduct_3.setStyleSheet(u"QScrollArea {\n"
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
        self.scrollArea_allproduct_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_17 = QWidget()
        self.scrollAreaWidgetContents_17.setObjectName(u"scrollAreaWidgetContents_17")
        self.scrollAreaWidgetContents_17.setGeometry(QRect(0, 0, 998, 1518))
        self.verticalLayout_25 = QVBoxLayout(self.scrollAreaWidgetContents_17)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_allproduct_3 = QFrame(self.scrollAreaWidgetContents_17)
        self.frame_allproduct_3.setObjectName(u"frame_allproduct_3")
        self.frame_allproduct_3.setMinimumSize(QSize(0, 1500))
        self.frame_allproduct_3.setFrameShape(QFrame.StyledPanel)
        self.frame_allproduct_3.setFrameShadow(QFrame.Raised)
        self.product_48 = QWidget(self.frame_allproduct_3)
        self.product_48.setObjectName(u"product_48")
        self.product_48.setGeometry(QRect(26, 43, 251, 320))
        self.product_48.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;\n"
"border:none;")
        self.picproduct1_48 = QPushButton(self.product_48)
        self.picproduct1_48.setObjectName(u"picproduct1_48")
        self.picproduct1_48.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_48.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_49 = QWidget(self.frame_allproduct_3)
        self.product_49.setObjectName(u"product_49")
        self.product_49.setGeometry(QRect(695, 400, 251, 320))
        self.product_49.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;\n"
"border:none;")
        self.picproduct1_49 = QPushButton(self.product_49)
        self.picproduct1_49.setObjectName(u"picproduct1_49")
        self.picproduct1_49.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_49.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_50 = QWidget(self.frame_allproduct_3)
        self.product_50.setObjectName(u"product_50")
        self.product_50.setGeometry(QRect(360, 43, 251, 320))
        self.product_50.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;\n"
"border:none;")
        self.picproduct1_50 = QPushButton(self.product_50)
        self.picproduct1_50.setObjectName(u"picproduct1_50")
        self.picproduct1_50.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_50.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_51 = QWidget(self.frame_allproduct_3)
        self.product_51.setObjectName(u"product_51")
        self.product_51.setGeometry(QRect(695, 43, 251, 320))
        self.product_51.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;\n"
"border:none;")
        self.picproduct1_51 = QPushButton(self.product_51)
        self.picproduct1_51.setObjectName(u"picproduct1_51")
        self.picproduct1_51.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_51.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_52 = QWidget(self.frame_allproduct_3)
        self.product_52.setObjectName(u"product_52")
        self.product_52.setGeometry(QRect(360, 400, 251, 320))
        self.product_52.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;\n"
"border:none;")
        self.picproduct1_52 = QPushButton(self.product_52)
        self.picproduct1_52.setObjectName(u"picproduct1_52")
        self.picproduct1_52.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_52.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.product_53 = QWidget(self.frame_allproduct_3)
        self.product_53.setObjectName(u"product_53")
        self.product_53.setGeometry(QRect(26, 400, 251, 320))
        self.product_53.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;\n"
"border:none;")
        self.picproduct1_53 = QPushButton(self.product_53)
        self.picproduct1_53.setObjectName(u"picproduct1_53")
        self.picproduct1_53.setGeometry(QRect(30, 30, 191, 188))
        self.picproduct1_53.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 0px;")
        self.gotoaddproductpagebutton_3 = QPushButton(self.frame_allproduct_3)
        self.gotoaddproductpagebutton_3.setObjectName(u"gotoaddproductpagebutton_3")
        self.gotoaddproductpagebutton_3.setGeometry(QRect(840, 310, 100, 100))
        self.gotoaddproductpagebutton_3.setStyleSheet(u"background: #CD4662;\n"
"border: none;\n"
"border-radius: 50px;\n"
"font-size: 60px;\n"
"color: white;")

        self.verticalLayout_25.addWidget(self.frame_allproduct_3)

        self.scrollArea_allproduct_3.setWidget(self.scrollAreaWidgetContents_17)

        self.verticalLayout_24.addWidget(self.scrollArea_allproduct_3)

        self.stackedWidget_allandtype.addWidget(self.adminallproductpage)
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
        self.scrollAreaWidgetContents_18.setGeometry(QRect(0, 0, 998, 1518))
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

        self.stackedWidget_allandtype.addWidget(self.adminproducttypespage)
        self.stackedWidget_adminproducts.addWidget(self.adminproductspage_alltypes)
        self.adminaddproductpage = QWidget()
        self.adminaddproductpage.setObjectName(u"adminaddproductpage")
        self.verticalLayout_28 = QVBoxLayout(self.adminaddproductpage)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.scrollArea_addproduct_3 = QScrollArea(self.adminaddproductpage)
        self.scrollArea_addproduct_3.setObjectName(u"scrollArea_addproduct_3")
        self.scrollArea_addproduct_3.setStyleSheet(u"QScrollArea {\n"
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
        self.scrollArea_addproduct_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_19 = QWidget()
        self.scrollAreaWidgetContents_19.setObjectName(u"scrollAreaWidgetContents_19")
        self.scrollAreaWidgetContents_19.setGeometry(QRect(0, 0, 998, 1218))
        self.verticalLayout_29 = QVBoxLayout(self.scrollAreaWidgetContents_19)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_addproduct_3 = QFrame(self.scrollAreaWidgetContents_19)
        self.frame_addproduct_3.setObjectName(u"frame_addproduct_3")
        self.frame_addproduct_3.setMinimumSize(QSize(0, 1200))
        self.frame_addproduct_3.setStyleSheet(u"background: #FAF9F6")
        self.frame_addproduct_3.setFrameShape(QFrame.StyledPanel)
        self.frame_addproduct_3.setFrameShadow(QFrame.Raised)
        self.addproductlabel_3 = QLabel(self.frame_addproduct_3)
        self.addproductlabel_3.setObjectName(u"addproductlabel_3")
        self.addproductlabel_3.setGeometry(QRect(40, 0, 201, 21))
        self.addproductlabel_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.addimageproductcontainer_3 = QWidget(self.frame_addproduct_3)
        self.addimageproductcontainer_3.setObjectName(u"addimageproductcontainer_3")
        self.addimageproductcontainer_3.setGeometry(QRect(24, 75, 910, 251))
        self.addimageproductcontainer_3.setStyleSheet(u"QScrollArea {\n"
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
        self.horizontalLayout_5 = QHBoxLayout(self.addimageproductcontainer_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.scrollArea_addimageproduct_3 = QScrollArea(self.addimageproductcontainer_3)
        self.scrollArea_addimageproduct_3.setObjectName(u"scrollArea_addimageproduct_3")
        self.scrollArea_addimageproduct_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_20 = QWidget()
        self.scrollAreaWidgetContents_20.setObjectName(u"scrollAreaWidgetContents_20")
        self.scrollAreaWidgetContents_20.setGeometry(QRect(0, 0, 1218, 218))
        self.horizontalLayout_6 = QHBoxLayout(self.scrollAreaWidgetContents_20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_addimageproduct_3 = QFrame(self.scrollAreaWidgetContents_20)
        self.frame_addimageproduct_3.setObjectName(u"frame_addimageproduct_3")
        self.frame_addimageproduct_3.setMinimumSize(QSize(1200, 0))
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
        self.addimagebutton_13 = QPushButton(self.frame_addimageproduct_3)
        self.addimagebutton_13.setObjectName(u"addimagebutton_13")
        self.addimagebutton_13.setGeometry(QRect(0, 45, 151, 151))
        self.addimagebutton_13.setStyleSheet(u"border: 3px dashed #D9D9D9;\n"
"font-size: 46px;\n"
"background: #FAF9F6;\n"
"color: #D9D9D9;")
        self.addimagebutton_14 = QPushButton(self.frame_addimageproduct_3)
        self.addimagebutton_14.setObjectName(u"addimagebutton_14")
        self.addimagebutton_14.setGeometry(QRect(201, 45, 151, 151))
        self.addimagebutton_14.setStyleSheet(u"border: 3px dashed #D9D9D9;\n"
"font-size: 46px;\n"
"background: #FAF9F6;\n"
"color: #D9D9D9;")
        self.addimagebutton_15 = QPushButton(self.frame_addimageproduct_3)
        self.addimagebutton_15.setObjectName(u"addimagebutton_15")
        self.addimagebutton_15.setGeometry(QRect(402, 45, 151, 151))
        self.addimagebutton_15.setStyleSheet(u"border: 3px dashed #D9D9D9;\n"
"font-size: 46px;\n"
"background: #FAF9F6;\n"
"color: #D9D9D9;")
        self.addimagebutton_16 = QPushButton(self.frame_addimageproduct_3)
        self.addimagebutton_16.setObjectName(u"addimagebutton_16")
        self.addimagebutton_16.setGeometry(QRect(603, 45, 151, 151))
        self.addimagebutton_16.setStyleSheet(u"border: 3px dashed #D9D9D9;\n"
"font-size: 46px;\n"
"background: #FAF9F6;\n"
"color: #D9D9D9;")
        self.addimagebutton_17 = QPushButton(self.frame_addimageproduct_3)
        self.addimagebutton_17.setObjectName(u"addimagebutton_17")
        self.addimagebutton_17.setGeometry(QRect(804, 45, 151, 151))
        self.addimagebutton_17.setStyleSheet(u"border: 3px dashed #D9D9D9;\n"
"font-size: 46px;\n"
"background: #FAF9F6;\n"
"color: #D9D9D9;")
        self.addimagebutton_18 = QPushButton(self.frame_addimageproduct_3)
        self.addimagebutton_18.setObjectName(u"addimagebutton_18")
        self.addimagebutton_18.setGeometry(QRect(1005, 45, 151, 151))
        self.addimagebutton_18.setStyleSheet(u"border: 3px dashed #D9D9D9;\n"
"font-size: 46px;\n"
"background: #FAF9F6;\n"
"color: #D9D9D9;")

        self.horizontalLayout_6.addWidget(self.frame_addimageproduct_3)

        self.scrollArea_addimageproduct_3.setWidget(self.scrollAreaWidgetContents_20)

        self.horizontalLayout_5.addWidget(self.scrollArea_addimageproduct_3)

        self.addproductnamelabel_3 = QLabel(self.frame_addproduct_3)
        self.addproductnamelabel_3.setObjectName(u"addproductnamelabel_3")
        self.addproductnamelabel_3.setGeometry(QRect(42, 347, 220, 21))
        self.addproductnamelabel_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.addproductdescriptionlabel_3 = QLabel(self.frame_addproduct_3)
        self.addproductdescriptionlabel_3.setObjectName(u"addproductdescriptionlabel_3")
        self.addproductdescriptionlabel_3.setGeometry(QRect(42, 443, 220, 31))
        self.addproductdescriptionlabel_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.addproductpricelabel_3 = QLabel(self.frame_addproduct_3)
        self.addproductpricelabel_3.setObjectName(u"addproductpricelabel_3")
        self.addproductpricelabel_3.setGeometry(QRect(42, 623, 220, 21))
        self.addproductpricelabel_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.addproductsizelabel_3 = QLabel(self.frame_addproduct_3)
        self.addproductsizelabel_3.setObjectName(u"addproductsizelabel_3")
        self.addproductsizelabel_3.setGeometry(QRect(42, 719, 220, 21))
        self.addproductsizelabel_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.addproductoptionlabel_3 = QLabel(self.frame_addproduct_3)
        self.addproductoptionlabel_3.setObjectName(u"addproductoptionlabel_3")
        self.addproductoptionlabel_3.setGeometry(QRect(42, 815, 220, 31))
        self.addproductoptionlabel_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.addproductstocklabel_3 = QLabel(self.frame_addproduct_3)
        self.addproductstocklabel_3.setObjectName(u"addproductstocklabel_3")
        self.addproductstocklabel_3.setGeometry(QRect(42, 921, 220, 21))
        self.addproductstocklabel_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.addproductnametextbox_3 = QLineEdit(self.frame_addproduct_3)
        self.addproductnametextbox_3.setObjectName(u"addproductnametextbox_3")
        self.addproductnametextbox_3.setGeometry(QRect(42, 382, 910, 33))
        self.addproductnametextbox_3.setStyleSheet(u"border-radius: 5px;\n"
"background: #F7F2EB;\n"
"")
        self.addproductdescriptiontextbox_3 = QLineEdit(self.frame_addproduct_3)
        self.addproductdescriptiontextbox_3.setObjectName(u"addproductdescriptiontextbox_3")
        self.addproductdescriptiontextbox_3.setGeometry(QRect(42, 488, 910, 107))
        self.addproductdescriptiontextbox_3.setStyleSheet(u"border-radius: 5px;\n"
"background: #F7F2EB;\n"
"")
        self.addproductpricetextbox_3 = QLineEdit(self.frame_addproduct_3)
        self.addproductpricetextbox_3.setObjectName(u"addproductpricetextbox_3")
        self.addproductpricetextbox_3.setGeometry(QRect(42, 658, 910, 33))
        self.addproductpricetextbox_3.setStyleSheet(u"border-radius: 5px;\n"
"background: #F7F2EB;\n"
"")
        self.addproductstocktextbox_3 = QLineEdit(self.frame_addproduct_3)
        self.addproductstocktextbox_3.setObjectName(u"addproductstocktextbox_3")
        self.addproductstocktextbox_3.setGeometry(QRect(42, 956, 910, 33))
        self.addproductstocktextbox_3.setStyleSheet(u"border-radius: 5px;\n"
"background: #F7F2EB;\n"
"")
        self.addsizeproductbutton_3 = QPushButton(self.frame_addproduct_3)
        self.addsizeproductbutton_3.setObjectName(u"addsizeproductbutton_3")
        self.addsizeproductbutton_3.setGeometry(QRect(42, 754, 108, 33))
        self.addsizeproductbutton_3.setStyleSheet(u"border-radius: 5px;\n"
"background: #F7F2EB;")
        self.addoptionsproductbutton_3 = QPushButton(self.frame_addproduct_3)
        self.addoptionsproductbutton_3.setObjectName(u"addoptionsproductbutton_3")
        self.addoptionsproductbutton_3.setGeometry(QRect(42, 860, 108, 33))
        self.addoptionsproductbutton_3.setStyleSheet(u"border-radius: 5px;\n"
"background: #F7F2EB;")
        self.canceladdproductbutton_3 = QPushButton(self.frame_addproduct_3)
        self.canceladdproductbutton_3.setObjectName(u"canceladdproductbutton_3")
        self.canceladdproductbutton_3.setGeometry(QRect(498, 1017, 157, 49))
        self.canceladdproductbutton_3.setStyleSheet(u"border-radius: 5px;\n"
"background: #AEC289;\n"
"color: #FFF;\n"
"\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.addproductbutton_3 = QPushButton(self.frame_addproduct_3)
        self.addproductbutton_3.setObjectName(u"addproductbutton_3")
        self.addproductbutton_3.setGeometry(QRect(706, 1017, 204, 49))
        self.addproductbutton_3.setStyleSheet(u"border-radius: 5px;\n"
"background: #CD4662;\n"
"color: #FFF;\n"
"\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_29.addWidget(self.frame_addproduct_3)

        self.scrollArea_addproduct_3.setWidget(self.scrollAreaWidgetContents_19)

        self.verticalLayout_28.addWidget(self.scrollArea_addproduct_3)

        self.stackedWidget_adminproducts.addWidget(self.adminaddproductpage)
        self.stackedWidget_adminmain.addWidget(self.adminproductspage)
        self.stackedWidget_adminwidget.addWidget(self.adminmain)

        self.gridLayout_adminwidget.addWidget(self.stackedWidget_adminwidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.adminwidget)
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
        self.stackedWidget_myorders.setCurrentIndex(0)
        self.stackedWidget_adminproducts.setCurrentIndex(0)
        self.stackedWidget_allandtype.setCurrentIndex(0)


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
        self.shopnameforcart.setText(QCoreApplication.translate("Main", u"Shop's name", None))
        self.cartorderpic.setText("")
        self.productcartname.setText(QCoreApplication.translate("Main", u"Product's name", None))
        self.productcartdescrip.setText(QCoreApplication.translate("Main", u"Description", None))
        self.productnum.setText(QCoreApplication.translate("Main", u"1 piece", None))
        self.totalpricecartlabel.setText(QCoreApplication.translate("Main", u"Total Price:", None))
        self.totalpricecartnumlabel.setText(QCoreApplication.translate("Main", u"B 500", None))
        self.checkstatuscartbutton.setText(QCoreApplication.translate("Main", u"Check Status", None))
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
        self.shopnameforcart_2.setText(QCoreApplication.translate("Main", u"Shop's name", None))
        self.cartorderpic_2.setText("")
        self.productcartname_2.setText(QCoreApplication.translate("Main", u"Product's name", None))
        self.productcartdescrip_2.setText(QCoreApplication.translate("Main", u"Description", None))
        self.productnum_2.setText(QCoreApplication.translate("Main", u"1 piece", None))
        self.totalpricecartlabel_2.setText(QCoreApplication.translate("Main", u"Total Price:", None))
        self.totalpricecartnumlabel_2.setText(QCoreApplication.translate("Main", u"B 500", None))
        self.checkstatusshipbutton.setText(QCoreApplication.translate("Main", u"Check Status", None))
        self.shopnameforcart_3.setText(QCoreApplication.translate("Main", u"Shop's name", None))
        self.cartorderpic_3.setText("")
        self.productcartname_3.setText(QCoreApplication.translate("Main", u"Product's name", None))
        self.productcartdescrip_3.setText(QCoreApplication.translate("Main", u"Description", None))
        self.productnum_3.setText(QCoreApplication.translate("Main", u"1 piece", None))
        self.totalpricecartlabel_3.setText(QCoreApplication.translate("Main", u"Total Price:", None))
        self.totalpricecartnumlabel_3.setText(QCoreApplication.translate("Main", u"B 500", None))
        self.checkstatusreceivebutton.setText(QCoreApplication.translate("Main", u"Check Status", None))
        self.shopnameforcart_4.setText(QCoreApplication.translate("Main", u"Shop's name", None))
        self.cartorderpic_4.setText("")
        self.productcartname_4.setText(QCoreApplication.translate("Main", u"Product's name", None))
        self.productcartdescrip_4.setText(QCoreApplication.translate("Main", u"Description", None))
        self.productnum_4.setText(QCoreApplication.translate("Main", u"1 piece", None))
        self.totalpricecartlabel_4.setText(QCoreApplication.translate("Main", u"Total Price:", None))
        self.totalpricecartnumlabel_4.setText(QCoreApplication.translate("Main", u"B 500", None))
        self.buyagaincompletebutton.setText(QCoreApplication.translate("Main", u"Buy again", None))
        self.givereviewcompletebutton.setText(QCoreApplication.translate("Main", u"Give Review", None))
        self.picpress1.setText(QCoreApplication.translate("Main", u"Pic1", None))
        self.picpress2.setText(QCoreApplication.translate("Main", u"Pic2", None))
        self.picpress3.setText(QCoreApplication.translate("Main", u"Pic3", None))
        self.picpress4.setText(QCoreApplication.translate("Main", u"Pic4", None))
        self.mainpic.setText(QCoreApplication.translate("Main", u"Mainpic", None))
        self.productname.setText(QCoreApplication.translate("Main", u"Name of the product", None))
        self.productdetail.setText(QCoreApplication.translate("Main", u"Detail", None))
        self.buynowbutton.setText(QCoreApplication.translate("Main", u"Buy Now", None))
        self.addtocartbutton.setText(QCoreApplication.translate("Main", u"Add to Cart", None))
        self.shopprofile.setText("")
        self.shopname.setText(QCoreApplication.translate("Main", u"Seller's Account", None))
        self.shopfollower.setText(QCoreApplication.translate("Main", u"followers", None))
        self.viewshopbutton.setText(QCoreApplication.translate("Main", u"View Shop", None))
        self.star1.setText("")
        self.star2.setText("")
        self.star3.setText("")
        self.star4.setText("")
        self.star5.setText("")
        self.numberofstar.setText(QCoreApplication.translate("Main", u"1", None))
        self.numberofsold.setText(QCoreApplication.translate("Main", u"480 Sold", None))
        self.currencypic.setText("")
        self.productprice.setText(QCoreApplication.translate("Main", u"100", None))
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
        self.viewallfavbutton.setText(QCoreApplication.translate("Main", u"View all Favorites    >", None))
        self.openshopbutton.setText(QCoreApplication.translate("Main", u"           Open Your Shop", None))
        self.openshoppic.setText("")
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
        self.searchbox_3.setPlaceholderText(QCoreApplication.translate("Main", u"Search..", None))
        self.loginsignoutbutton_3.setText(QCoreApplication.translate("Main", u"Log In", None))
        self.profilebutton_3.setText("")
        self.Logolabel_3.setText(QCoreApplication.translate("Main", u"ChopShop", None))
        self.homebutton_3.setText(QCoreApplication.translate("Main", u"Home", None))
        self.orderstatusbutton_3.setText(QCoreApplication.translate("Main", u"Order Status", None))
        self.orderproductbutton_2.setText(QCoreApplication.translate("Main", u"Products", None))
        self.messbutton_3.setText(QCoreApplication.translate("Main", u"Messages", None))
        self.settingbutton_3.setText("")
        self.exitbutton_3.setText("")
        self.profilepic_3.setText("")
        self.usernamelabel_3.setText(QCoreApplication.translate("Main", u"Username", None))
        self.numreview_2.setText(QCoreApplication.translate("Main", u"4/5", None))
        self.review_2.setText(QCoreApplication.translate("Main", u"Reviews", None))
        self.numproduct_2.setText(QCoreApplication.translate("Main", u"1000", None))
        self.product_22.setText(QCoreApplication.translate("Main", u"Products", None))
        self.numsold_2.setText(QCoreApplication.translate("Main", u"30000", None))
        self.yearregis_2.setText(QCoreApplication.translate("Main", u"Years Registered", None))
        self.sold_2.setText(QCoreApplication.translate("Main", u"Sold", None))
        self.numyearregis_2.setText(QCoreApplication.translate("Main", u"2", None))
        self.orderstatuslabel_2.setText(QCoreApplication.translate("Main", u"Order Status", None))
        self.admintobeshipbutton_2.setText("")
        self.admincancelbutton_2.setText("")
        self.admincompletebutton_2.setText("")
        self.adminreviewbutton_2.setText("")
        self.orderstatusbutton_4.setText(QCoreApplication.translate("Main", u"View all order status    >", None))
        self.picproduct1_24.setText("")
        self.favlabel_3.setText(QCoreApplication.translate("Main", u"Products", None))
        self.picproduct1_25.setText("")
        self.picproduct1_26.setText("")
        self.picproduct1_27.setText("")
        self.picproduct1_28.setText("")
        self.picproduct1_29.setText("")
        self.viewallproductbutton_2.setText(QCoreApplication.translate("Main", u"View all Products    >", None))
        self.productlabel_3.setText(QCoreApplication.translate("Main", u"Products", None))
        self.allproductbutton_3.setText(QCoreApplication.translate("Main", u"All Products", None))
        self.producttypesbutton_3.setText(QCoreApplication.translate("Main", u"Product Types", None))
        self.picproduct1_48.setText("")
        self.picproduct1_49.setText("")
        self.picproduct1_50.setText("")
        self.picproduct1_51.setText("")
        self.picproduct1_52.setText("")
        self.picproduct1_53.setText("")
        self.gotoaddproductpagebutton_3.setText(QCoreApplication.translate("Main", u"+", None))
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
        self.addproductlabel_3.setText(QCoreApplication.translate("Main", u"Add Product", None))
        self.addproductimagelabel_3.setText(QCoreApplication.translate("Main", u"Product's Images", None))
        self.addimagebutton_13.setText(QCoreApplication.translate("Main", u"+", None))
        self.addimagebutton_14.setText(QCoreApplication.translate("Main", u"+", None))
        self.addimagebutton_15.setText(QCoreApplication.translate("Main", u"+", None))
        self.addimagebutton_16.setText(QCoreApplication.translate("Main", u"+", None))
        self.addimagebutton_17.setText(QCoreApplication.translate("Main", u"+", None))
        self.addimagebutton_18.setText(QCoreApplication.translate("Main", u"+", None))
        self.addproductnamelabel_3.setText(QCoreApplication.translate("Main", u"Product's Name", None))
        self.addproductdescriptionlabel_3.setText(QCoreApplication.translate("Main", u"Description", None))
        self.addproductpricelabel_3.setText(QCoreApplication.translate("Main", u"Price", None))
        self.addproductsizelabel_3.setText(QCoreApplication.translate("Main", u"Size", None))
        self.addproductoptionlabel_3.setText(QCoreApplication.translate("Main", u"Options", None))
        self.addproductstocklabel_3.setText(QCoreApplication.translate("Main", u"Stock", None))
        self.addsizeproductbutton_3.setText(QCoreApplication.translate("Main", u"+", None))
        self.addoptionsproductbutton_3.setText(QCoreApplication.translate("Main", u"+", None))
        self.canceladdproductbutton_3.setText(QCoreApplication.translate("Main", u"Cancel", None))
        self.addproductbutton_3.setText(QCoreApplication.translate("Main", u"Add Product", None))
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

