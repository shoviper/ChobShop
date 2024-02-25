# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'product.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)
import app.assets.sourceimg.all

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.menu = QWidget(self.centralwidget)
        self.menu.setObjectName(u"menu")
        self.menu.setEnabled(False)
        self.menu.setGeometry(QRect(0, 0, 373, 1080))
        self.menu.setStyleSheet(u"background-color: #FAF9F6;\n"
"box-shadow: 2px 0px 40px 2px rgba(0,0,0,0.25);")
        self.label = QLabel(self.menu)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(45, 68, 285, 77))
        self.label.setStyleSheet(u"font-family: Supermercado;\n"
"                font-size: 64px;\n"
"                font-weight: 400;\n"
"                line-height: 77px;\n"
"                letter-spacing: 0em;\n"
"                text-align: center;\n"
"                color: #000000;")
        self.homebutton = QPushButton(self.menu)
        self.homebutton.setObjectName(u"homebutton")
        self.homebutton.setGeometry(QRect(54, 211, 265, 94))
        self.homebutton.setStyleSheet(u"color: #000;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 24px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                background-color: #E1E3E7;\n"
"                border-radius: 10px;\n"
"")
        self.favbutton = QPushButton(self.menu)
        self.favbutton.setObjectName(u"favbutton")
        self.favbutton.setGeometry(QRect(54, 371, 265, 94))
        self.favbutton.setStyleSheet(u"color: #000;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 24px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                background-color: #E1E3E7;\n"
"                border-radius: 10px;\n"
"")
        self.orderbutton = QPushButton(self.menu)
        self.orderbutton.setObjectName(u"orderbutton")
        self.orderbutton.setGeometry(QRect(54, 531, 265, 94))
        self.orderbutton.setStyleSheet(u"color: #000;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 24px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                background-color: #E1E3E7;\n"
"                border-radius: 10px;")
        self.messbutton = QPushButton(self.menu)
        self.messbutton.setObjectName(u"messbutton")
        self.messbutton.setGeometry(QRect(54, 691, 265, 94))
        self.messbutton.setStyleSheet(u"color: #000;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 24px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                background-color: #E1E3E7;\n"
"                border-radius: 10px;")
        self.settingsbutton = QPushButton(self.menu)
        self.settingsbutton.setObjectName(u"settingsbutton")
        self.settingsbutton.setGeometry(QRect(119, 930, 68, 48))
        self.settingsbutton.setStyleSheet(u"image: url(:/pic/images/settings.png);\n"
"border: none;")
        self.exitbutton = QPushButton(self.menu)
        self.exitbutton.setObjectName(u"exitbutton")
        self.exitbutton.setGeometry(QRect(187, 930, 68, 48))
        self.exitbutton.setStyleSheet(u"image: url(:/pic/images/exit.png);\n"
"border: none;")
        self.searchcontainer = QWidget(self.centralwidget)
        self.searchcontainer.setObjectName(u"searchcontainer")
        self.searchcontainer.setGeometry(QRect(373, 0, 1547, 161))
        self.searchcontainer.setStyleSheet(u"background-color: #FAF9F6;")
        self.searchbox = QLineEdit(self.searchcontainer)
        self.searchbox.setObjectName(u"searchbox")
        self.searchbox.setGeometry(QRect(76, 78, 1076, 57))
        self.searchbox.setStyleSheet(u"border-radius: 27%;\n"
"                background-color: #EDEDED;\n"
"                color: #CD4662;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 24px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;")
        self.profilebutton = QPushButton(self.searchcontainer)
        self.profilebutton.setObjectName(u"profilebutton")
        self.profilebutton.setGeometry(QRect(1292, 78, 68, 48))
        self.profilebutton.setStyleSheet(u"image: url(:/pic/images/profile.png);\n"
"border: none;")
        self.cartbutton = QPushButton(self.searchcontainer)
        self.cartbutton.setObjectName(u"cartbutton")
        self.cartbutton.setGeometry(QRect(1186, 78, 68, 48))
        self.cartbutton.setAutoFillBackground(False)
        self.cartbutton.setStyleSheet(u"image: url(:/pic/images/cart.png);\n"
"border: none;")
        self.cartbutton.setAutoDefault(False)
        self.signinsignoutbutton = QPushButton(self.searchcontainer)
        self.signinsignoutbutton.setObjectName(u"signinsignoutbutton")
        self.signinsignoutbutton.setGeometry(QRect(1384, 78, 113, 58))
        self.signinsignoutbutton.setStyleSheet(u"color: #000;\n"
"                text-align: right;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 32px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                border: none;\n"
"                margin-bottom: 15px;")
        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setGeometry(QRect(373, 161, 1547, 919))
        self.main.setStyleSheet(u"background-color: #FAF9F6;")
        self.verticalLayout = QVBoxLayout(self.main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.main)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: #FAF9F6;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1510, 2518))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 2500))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.piccontainer = QWidget(self.frame)
        self.piccontainer.setObjectName(u"piccontainer")
        self.piccontainer.setGeometry(QRect(62, 9, 1431, 812))
        self.piccontainer.setStyleSheet(u"background-color: blue;\n"
"border-radius: 10px 10px 0px 0px;")
        self.picpress1 = QPushButton(self.piccontainer)
        self.picpress1.setObjectName(u"picpress1")
        self.picpress1.setGeometry(QRect(47, 598, 141, 142))
        self.picpress1.setStyleSheet(u"border: 1px solid #000;\n"
"background-color: #D9D9D9;")
        self.picpress2 = QPushButton(self.piccontainer)
        self.picpress2.setObjectName(u"picpress2")
        self.picpress2.setGeometry(QRect(188, 598, 141, 142))
        self.picpress2.setStyleSheet(u"border: 1px solid #000;\n"
"background-color: #D9D9D9;")
        self.picpress3 = QPushButton(self.piccontainer)
        self.picpress3.setObjectName(u"picpress3")
        self.picpress3.setGeometry(QRect(329, 598, 141, 142))
        self.picpress3.setStyleSheet(u"border: 1px solid #000;\n"
"background-color: #D9D9D9;")
        self.picpress4 = QPushButton(self.piccontainer)
        self.picpress4.setObjectName(u"picpress4")
        self.picpress4.setGeometry(QRect(470, 598, 141, 142))
        self.picpress4.setStyleSheet(u"border: 1px solid #000;\n"
"background-color: #D9D9D9;")
        self.mainpic = QLabel(self.piccontainer)
        self.mainpic.setObjectName(u"mainpic")
        self.mainpic.setGeometry(QRect(47, 34, 564, 564))
        self.mainpic.setStyleSheet(u"border-radius: 10px 10px 0px 0px;\n"
"border: 1px solid #000;\n"
"background-color: #D9D9D9;")
        self.productname = QLabel(self.piccontainer)
        self.productname.setObjectName(u"productname")
        self.productname.setGeometry(QRect(797, 34, 579, 72))
        self.productname.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 40px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"background-color: red;")
        self.productdetail = QLabel(self.piccontainer)
        self.productdetail.setObjectName(u"productdetail")
        self.productdetail.setGeometry(QRect(794, 292, 577, 274))
        self.productdetail.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid #000;\n"
"background-color: yellow;")
        self.buynowbutton = QPushButton(self.piccontainer)
        self.buynowbutton.setObjectName(u"buynowbutton")
        self.buynowbutton.setGeometry(QRect(794, 223, 251, 44))
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
        self.addtocartbutton = QPushButton(self.piccontainer)
        self.addtocartbutton.setObjectName(u"addtocartbutton")
        self.addtocartbutton.setGeometry(QRect(1120, 223, 251, 44))
        self.addtocartbutton.setStyleSheet(u"border-radius: 50px;\n"
"background-color: #CD4662;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")

        self.verticalLayout_2.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ChobShop", None))
        self.homebutton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.favbutton.setText(QCoreApplication.translate("MainWindow", u"Favorites", None))
        self.orderbutton.setText(QCoreApplication.translate("MainWindow", u"My Orders", None))
        self.messbutton.setText(QCoreApplication.translate("MainWindow", u"Messages", None))
        self.settingsbutton.setText("")
        self.exitbutton.setText("")
        self.searchbox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search..", None))
        self.profilebutton.setText("")
        self.cartbutton.setText("")
        self.signinsignoutbutton.setText(QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.picpress1.setText(QCoreApplication.translate("MainWindow", u"Pic1", None))
        self.picpress2.setText(QCoreApplication.translate("MainWindow", u"Pic2", None))
        self.picpress3.setText(QCoreApplication.translate("MainWindow", u"Pic3", None))
        self.picpress4.setText(QCoreApplication.translate("MainWindow", u"Pic4", None))
        self.mainpic.setText(QCoreApplication.translate("MainWindow", u"Mainpic", None))
        self.productname.setText(QCoreApplication.translate("MainWindow", u"Name of the product", None))
        self.productdetail.setText(QCoreApplication.translate("MainWindow", u"Detail", None))
        self.buynowbutton.setText(QCoreApplication.translate("MainWindow", u"Buy Now", None))
        self.addtocartbutton.setText(QCoreApplication.translate("MainWindow", u"Add to Cart", None))
    # retranslateUi

