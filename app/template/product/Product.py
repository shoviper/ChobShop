# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Product.ui'
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
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 373, 1080))
        self.widget.setStyleSheet(u"background-color: #FAF9F6;")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(45, 68, 285, 77))
        self.label.setStyleSheet(u"font-family: Supermercado;\n"
"                font-size: 64px;\n"
"                font-weight: 400;\n"
"                line-height: 77px;\n"
"                letter-spacing: 0em;\n"
"                text-align: center;\n"
"                color: #000000;")
        self.homebutton = QPushButton(self.widget)
        self.homebutton.setObjectName(u"homebutton")
        self.homebutton.setGeometry(QRect(54, 211, 265, 94))
        self.homebutton.setStyleSheet(u"QPushButton{\n"
"	color: #000;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 24px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                background-color: #E1E3E7;\n"
"                border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: #AEC289;\n"
"                color: #FAF9F6;\n"
"            }\n"
"")
        self.favbutton = QPushButton(self.widget)
        self.favbutton.setObjectName(u"favbutton")
        self.favbutton.setGeometry(QRect(54, 371, 265, 94))
        self.favbutton.setStyleSheet(u"QPushButton{\n"
"	color: #000;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 24px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                background-color: #E1E3E7;\n"
"                border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: #AEC289;\n"
"                color: #FAF9F6;\n"
"            }\n"
"")
        self.orderbutton = QPushButton(self.widget)
        self.orderbutton.setObjectName(u"orderbutton")
        self.orderbutton.setGeometry(QRect(54, 531, 265, 94))
        self.orderbutton.setStyleSheet(u"QPushButton{\n"
"	color: #000;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 24px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                background-color: #E1E3E7;\n"
"                border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: #AEC289;\n"
"                color: #FAF9F6;\n"
"            }\n"
"")
        self.messbutton = QPushButton(self.widget)
        self.messbutton.setObjectName(u"messbutton")
        self.messbutton.setGeometry(QRect(54, 691, 265, 94))
        self.messbutton.setStyleSheet(u"QPushButton{\n"
"	color: #000;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 24px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                background-color: #E1E3E7;\n"
"                border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: #AEC289;\n"
"                color: #FAF9F6;\n"
"            }\n"
"")
        self.settingsbutton = QPushButton(self.widget)
        self.settingsbutton.setObjectName(u"settingsbutton")
        self.settingsbutton.setGeometry(QRect(119, 930, 68, 48))
        self.settingsbutton.setStyleSheet(u"image: url(:/pic/images/settings.png);\n"
"border: none;")
        self.exitbutton = QPushButton(self.widget)
        self.exitbutton.setObjectName(u"exitbutton")
        self.exitbutton.setGeometry(QRect(187, 930, 68, 48))
        self.exitbutton.setStyleSheet(u"image: url(:/pic/images/exit.png);\n"
"border: none;")
        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setGeometry(QRect(373, 161, 1547, 919))
        self.main.setStyleSheet(u"background-color: #FAF9F6;")
        self.verticalLayout = QVBoxLayout(self.main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.main)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1512, 2518))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 2500))
        self.frame.setStyleSheet(u"background-color: #FAF9F6;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.productcontainer = QWidget(self.frame)
        self.productcontainer.setObjectName(u"productcontainer")
        self.productcontainer.setGeometry(QRect(62, 9, 1431, 812))
        self.productcontainer.setStyleSheet(u"background-color: #FAF9F6;\n"
"border-radius: 10px 10px 0px 0px;")
        self.picpress1 = QPushButton(self.productcontainer)
        self.picpress1.setObjectName(u"picpress1")
        self.picpress1.setGeometry(QRect(47, 598, 141, 142))
        self.picpress1.setStyleSheet(u"border: 1px solid #000;\n"
"background-color: #D9D9D9;")
        self.picpress2 = QPushButton(self.productcontainer)
        self.picpress2.setObjectName(u"picpress2")
        self.picpress2.setGeometry(QRect(188, 598, 141, 142))
        self.picpress2.setStyleSheet(u"border: 1px solid #000;\n"
"background-color: #D9D9D9;")
        self.picpress3 = QPushButton(self.productcontainer)
        self.picpress3.setObjectName(u"picpress3")
        self.picpress3.setGeometry(QRect(329, 598, 141, 142))
        self.picpress3.setStyleSheet(u"border: 1px solid #000;\n"
"background-color: #D9D9D9;")
        self.picpress4 = QPushButton(self.productcontainer)
        self.picpress4.setObjectName(u"picpress4")
        self.picpress4.setGeometry(QRect(470, 598, 141, 142))
        self.picpress4.setStyleSheet(u"border: 1px solid #000;\n"
"background-color: #D9D9D9;")
        self.mainpic = QLabel(self.productcontainer)
        self.mainpic.setObjectName(u"mainpic")
        self.mainpic.setGeometry(QRect(47, 34, 564, 564))
        self.mainpic.setStyleSheet(u"border-radius: 10px 10px 0px 0px;\n"
"border: 1px solid #000;\n"
"background-color: #D9D9D9;")
        self.productname = QLabel(self.productcontainer)
        self.productname.setObjectName(u"productname")
        self.productname.setGeometry(QRect(797, 34, 579, 72))
        self.productname.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 40px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"background-color: red;\n"
"background-color: #FAF9F6;")
        self.productdetail = QLabel(self.productcontainer)
        self.productdetail.setObjectName(u"productdetail")
        self.productdetail.setGeometry(QRect(794, 292, 577, 274))
        self.productdetail.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid #000;\n"
"background-color: #FAF9F6;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.buynowbutton = QPushButton(self.productcontainer)
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
        self.addtocartbutton = QPushButton(self.productcontainer)
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
        self.shopprofile = QLabel(self.productcontainer)
        self.shopprofile.setObjectName(u"shopprofile")
        self.shopprofile.setGeometry(QRect(798, 599, 141, 141))
        self.shopprofile.setStyleSheet(u"image: url(:/pic/images/profile.png);\n"
"background-color: #D9D9D9;\n"
"border-radius: 50%;")
        self.shopname = QLabel(self.productcontainer)
        self.shopname.setObjectName(u"shopname")
        self.shopname.setGeometry(QRect(989, 602, 390, 39))
        self.shopname.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.shopfollower = QLabel(self.productcontainer)
        self.shopfollower.setObjectName(u"shopfollower")
        self.shopfollower.setGeometry(QRect(989, 644, 277, 39))
        self.shopfollower.setStyleSheet(u"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.viewshopbutton = QPushButton(self.productcontainer)
        self.viewshopbutton.setObjectName(u"viewshopbutton")
        self.viewshopbutton.setGeometry(QRect(989, 694, 277, 46))
        self.viewshopbutton.setStyleSheet(u"color: #FFF;\n"
"background-color: #AEC289;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.star1 = QLabel(self.productcontainer)
        self.star1.setObjectName(u"star1")
        self.star1.setGeometry(QRect(797, 161, 36, 36))
        self.star1.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star2 = QLabel(self.productcontainer)
        self.star2.setObjectName(u"star2")
        self.star2.setGeometry(QRect(833, 161, 36, 36))
        self.star2.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star3 = QLabel(self.productcontainer)
        self.star3.setObjectName(u"star3")
        self.star3.setGeometry(QRect(869, 161, 36, 36))
        self.star3.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star4 = QLabel(self.productcontainer)
        self.star4.setObjectName(u"star4")
        self.star4.setGeometry(QRect(905, 161, 36, 36))
        self.star4.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star5 = QLabel(self.productcontainer)
        self.star5.setObjectName(u"star5")
        self.star5.setGeometry(QRect(941, 161, 36, 36))
        self.star5.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.numberofstar = QLabel(self.productcontainer)
        self.numberofstar.setObjectName(u"numberofstar")
        self.numberofstar.setGeometry(QRect(986, 161, 37, 40))
        self.numberofstar.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.numberofsold = QLabel(self.productcontainer)
        self.numberofsold.setObjectName(u"numberofsold")
        self.numberofsold.setGeometry(QRect(1096, 161, 137, 40))
        self.numberofsold.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.currencypic = QLabel(self.productcontainer)
        self.currencypic.setObjectName(u"currencypic")
        self.currencypic.setGeometry(QRect(797, 115, 24, 38))
        self.currencypic.setStyleSheet(u"image: url(:/pic/images/baht.png);\n"
"border: none;")
        self.productprice = QLabel(self.productcontainer)
        self.productprice.setObjectName(u"productprice")
        self.productprice.setGeometry(QRect(833, 114, 343, 40))
        self.productprice.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 36px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(90, 930, 1322, 533))
        self.widget_2.setStyleSheet(u"border-top: 1px solid #CD4662;\n"
"border-bottom: 1px solid #CD4662;\n"
"background-color: #FAF9F6;")
        self.reviewerprofile = QLabel(self.widget_2)
        self.reviewerprofile.setObjectName(u"reviewerprofile")
        self.reviewerprofile.setGeometry(QRect(0, 20, 45, 45))
        self.reviewerprofile.setStyleSheet(u"image: url(:/pic/images/profile.png);\n"
"border: none;\n"
"border-radius: 50%;\n"
"background-color: #D9D9D9;")
        self.reviewername = QLabel(self.widget_2)
        self.reviewername.setObjectName(u"reviewername")
        self.reviewername.setGeometry(QRect(71, 20, 390, 39))
        self.reviewername.setStyleSheet(u"color: #000;\n"
"border: none;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.star11 = QLabel(self.widget_2)
        self.star11.setObjectName(u"star11")
        self.star11.setGeometry(QRect(71, 59, 27, 27))
        self.star11.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star12 = QLabel(self.widget_2)
        self.star12.setObjectName(u"star12")
        self.star12.setGeometry(QRect(98, 59, 27, 27))
        self.star12.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star13 = QLabel(self.widget_2)
        self.star13.setObjectName(u"star13")
        self.star13.setGeometry(QRect(126, 59, 27, 27))
        self.star13.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star14 = QLabel(self.widget_2)
        self.star14.setObjectName(u"star14")
        self.star14.setGeometry(QRect(154, 59, 27, 27))
        self.star14.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.star15 = QLabel(self.widget_2)
        self.star15.setObjectName(u"star15")
        self.star15.setGeometry(QRect(182, 59, 27, 27))
        self.star15.setStyleSheet(u"image: url(:/pic/images/star.png);\n"
"border: none;")
        self.productchoose = QLabel(self.widget_2)
        self.productchoose.setObjectName(u"productchoose")
        self.productchoose.setGeometry(QRect(71, 126, 390, 39))
        self.productchoose.setStyleSheet(u"border: none;\n"
"color: #BFBFBF;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.productchoosereview = QLabel(self.widget_2)
        self.productchoosereview.setObjectName(u"productchoosereview")
        self.productchoosereview.setGeometry(QRect(71, 165, 390, 39))
        self.productchoosereview.setStyleSheet(u"border: none;\n"
"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.reviewpic1 = QPushButton(self.widget_2)
        self.reviewpic1.setObjectName(u"reviewpic1")
        self.reviewpic1.setGeometry(QRect(71, 229, 215, 217))
        self.reviewpic1.setStyleSheet(u"background-color: #D9D9D9;\n"
"border: none;")
        self.reviewpic2 = QPushButton(self.widget_2)
        self.reviewpic2.setObjectName(u"reviewpic2")
        self.reviewpic2.setGeometry(QRect(361, 229, 215, 217))
        self.reviewpic2.setStyleSheet(u"background-color: #D9D9D9;\n"
"border: none;")
        self.productchoosereview_2 = QLabel(self.widget_2)
        self.productchoosereview_2.setObjectName(u"productchoosereview_2")
        self.productchoosereview_2.setGeometry(QRect(71, 471, 390, 51))
        self.productchoosereview_2.setStyleSheet(u"color: #BFBFBF;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.reviewlabel = QLabel(self.frame)
        self.reviewlabel.setObjectName(u"reviewlabel")
        self.reviewlabel.setGeometry(QRect(70, 816, 343, 40))
        self.reviewlabel.setStyleSheet(u"color: #000;\n"
"font-family: Suwannaphum;\n"
"font-size: 36px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.viewallbutton = QPushButton(self.frame)
        self.viewallbutton.setObjectName(u"viewallbutton")
        self.viewallbutton.setGeometry(QRect(1086, 816, 343, 40))
        self.viewallbutton.setStyleSheet(u"color: #CD4662;\n"
"text-align: right;\n"
"font-family: Suwannaphum;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")

        self.verticalLayout_2.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.searchbox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search..", None))
        self.profilebutton.setText("")
        self.cartbutton.setText("")
        self.signinsignoutbutton.setText(QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ChopShop", None))
        self.homebutton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.favbutton.setText(QCoreApplication.translate("MainWindow", u"Favorites", None))
        self.orderbutton.setText(QCoreApplication.translate("MainWindow", u"My Orders", None))
        self.messbutton.setText(QCoreApplication.translate("MainWindow", u"Messages", None))
        self.settingsbutton.setText("")
        self.exitbutton.setText("")
        self.picpress1.setText(QCoreApplication.translate("MainWindow", u"Pic1", None))
        self.picpress2.setText(QCoreApplication.translate("MainWindow", u"Pic2", None))
        self.picpress3.setText(QCoreApplication.translate("MainWindow", u"Pic3", None))
        self.picpress4.setText(QCoreApplication.translate("MainWindow", u"Pic4", None))
        self.mainpic.setText(QCoreApplication.translate("MainWindow", u"Mainpic", None))
        self.productname.setText(QCoreApplication.translate("MainWindow", u"Name of the product", None))
        self.productdetail.setText(QCoreApplication.translate("MainWindow", u"Detail", None))
        self.buynowbutton.setText(QCoreApplication.translate("MainWindow", u"Buy Now", None))
        self.addtocartbutton.setText(QCoreApplication.translate("MainWindow", u"Add to Cart", None))
        self.shopprofile.setText("")
        self.shopname.setText(QCoreApplication.translate("MainWindow", u"Seller's Account", None))
        self.shopfollower.setText(QCoreApplication.translate("MainWindow", u"followers", None))
        self.viewshopbutton.setText(QCoreApplication.translate("MainWindow", u"View Shop", None))
        self.star1.setText("")
        self.star2.setText("")
        self.star3.setText("")
        self.star4.setText("")
        self.star5.setText("")
        self.numberofstar.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.numberofsold.setText(QCoreApplication.translate("MainWindow", u"480 Sold", None))
        self.currencypic.setText("")
        self.productprice.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.reviewerprofile.setText("")
        self.reviewername.setText(QCoreApplication.translate("MainWindow", u"User1", None))
        self.star11.setText("")
        self.star12.setText("")
        self.star13.setText("")
        self.star14.setText("")
        self.star15.setText("")
        self.productchoose.setText(QCoreApplication.translate("MainWindow", u"Product Choice: Brown S", None))
        self.productchoosereview.setText(QCoreApplication.translate("MainWindow", u"Good", None))
        self.reviewpic1.setText(QCoreApplication.translate("MainWindow", u"reviewpic 1", None))
        self.reviewpic2.setText(QCoreApplication.translate("MainWindow", u"reviewpic 2", None))
        self.productchoosereview_2.setText(QCoreApplication.translate("MainWindow", u"06-02-2024", None))
        self.reviewlabel.setText(QCoreApplication.translate("MainWindow", u"Reviews", None))
        self.viewallbutton.setText(QCoreApplication.translate("MainWindow", u"View all", None))
    # retranslateUi

