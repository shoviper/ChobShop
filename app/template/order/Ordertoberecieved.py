# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ordertoberecieved.ui'
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
        self.ordernavcontainer = QWidget(self.centralwidget)
        self.ordernavcontainer.setObjectName(u"ordernavcontainer")
        self.ordernavcontainer.setGeometry(QRect(373, 161, 1547, 190))
        self.ordernavcontainer.setStyleSheet(u"background-color: #FAF9F6;")
        self.reviewlabel = QLabel(self.ordernavcontainer)
        self.reviewlabel.setObjectName(u"reviewlabel")
        self.reviewlabel.setGeometry(QRect(76, 23, 207, 72))
        self.reviewlabel.setStyleSheet(u"color: #545454;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 40px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.tobeshipbutton = QPushButton(self.ordernavcontainer)
        self.tobeshipbutton.setObjectName(u"tobeshipbutton")
        self.tobeshipbutton.setGeometry(QRect(73, 119, 476, 71))
        self.tobeshipbutton.setStyleSheet(u"color: #545454;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border: none;")
        self.toberecievebutton = QPushButton(self.ordernavcontainer)
        self.toberecievebutton.setObjectName(u"toberecievebutton")
        self.toberecievebutton.setGeometry(QRect(552, 119, 476, 71))
        self.toberecievebutton.setStyleSheet(u"\n"
"\n"
"color: #CD4662;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border: none;")
        self.completebutton = QPushButton(self.ordernavcontainer)
        self.completebutton.setObjectName(u"completebutton")
        self.completebutton.setGeometry(QRect(1029, 119, 476, 71))
        self.completebutton.setStyleSheet(u"color: #545454;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border: none;")
        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setGeometry(QRect(373, 351, 1547, 729))
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1512, 3018))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 3000))
        self.frame.setStyleSheet(u"background-color: #FAF9F6;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.shopcontainer = QWidget(self.frame)
        self.shopcontainer.setObjectName(u"shopcontainer")
        self.shopcontainer.setGeometry(QRect(58, -7, 1427, 523))
        self.shopcontainer.setStyleSheet(u"background-color: yellow;")
        self.shopname = QLabel(self.shopcontainer)
        self.shopname.setObjectName(u"shopname")
        self.shopname.setGeometry(QRect(68, 46, 390, 59))
        self.shopname.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 26px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.shoppic = QPushButton(self.shopcontainer)
        self.shoppic.setObjectName(u"shoppic")
        self.shoppic.setGeometry(QRect(68, 123, 333, 333))
        self.shoppic.setStyleSheet(u"background: #D9D9D9;")
        self.productname = QLabel(self.shopcontainer)
        self.productname.setObjectName(u"productname")
        self.productname.setGeometry(QRect(476, 123, 951, 78))
        self.productname.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 26px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.productdesciption = QLabel(self.shopcontainer)
        self.productdesciption.setObjectName(u"productdesciption")
        self.productdesciption.setGeometry(QRect(476, 199, 951, 78))
        self.productdesciption.setStyleSheet(u"color: #545454;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 26px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.productquantity = QLabel(self.shopcontainer)
        self.productquantity.setObjectName(u"productquantity")
        self.productquantity.setGeometry(QRect(476, 277, 951, 78))
        self.productquantity.setStyleSheet(u"color: #545454;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 26px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.totalpricecontainer = QWidget(self.shopcontainer)
        self.totalpricecontainer.setObjectName(u"totalpricecontainer")
        self.totalpricecontainer.setGeometry(QRect(1069, 277, 358, 78))
        self.totalpricecontainer.setStyleSheet(u"background-color: white;")
        self.totalpricelabel = QLabel(self.totalpricecontainer)
        self.totalpricelabel.setObjectName(u"totalpricelabel")
        self.totalpricelabel.setGeometry(QRect(30, 30, 49, 16))
        self.bahtpic = QLabel(self.totalpricecontainer)
        self.bahtpic.setObjectName(u"bahtpic")
        self.bahtpic.setGeometry(QRect(160, 30, 49, 16))
        self.bahtpic.setStyleSheet(u"image: url(:/pic/images/baht.png);\n"
"border: none;")
        self.checkstatusbutton = QPushButton(self.shopcontainer)
        self.checkstatusbutton.setObjectName(u"checkstatusbutton")
        self.checkstatusbutton.setGeometry(QRect(1181, 378, 248, 78))
        self.checkstatusbutton.setStyleSheet(u"color: #FFF;\n"
"border-radius: 10px;\n"
"background-color: #CD4662;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.shopcontainer_2 = QWidget(self.frame)
        self.shopcontainer_2.setObjectName(u"shopcontainer_2")
        self.shopcontainer_2.setGeometry(QRect(58, 516, 1427, 523))
        self.shopcontainer_2.setStyleSheet(u"background-color: yellow;")
        self.shopname_2 = QLabel(self.shopcontainer_2)
        self.shopname_2.setObjectName(u"shopname_2")
        self.shopname_2.setGeometry(QRect(68, 46, 390, 59))
        self.shopname_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 26px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.shoppic_2 = QPushButton(self.shopcontainer_2)
        self.shoppic_2.setObjectName(u"shoppic_2")
        self.shoppic_2.setGeometry(QRect(68, 123, 333, 333))
        self.shoppic_2.setStyleSheet(u"background: #D9D9D9;")
        self.productname_2 = QLabel(self.shopcontainer_2)
        self.productname_2.setObjectName(u"productname_2")
        self.productname_2.setGeometry(QRect(476, 123, 951, 78))
        self.productname_2.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 26px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.productdesciption_2 = QLabel(self.shopcontainer_2)
        self.productdesciption_2.setObjectName(u"productdesciption_2")
        self.productdesciption_2.setGeometry(QRect(476, 199, 951, 78))
        self.productdesciption_2.setStyleSheet(u"color: #545454;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 26px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.productquantity_2 = QLabel(self.shopcontainer_2)
        self.productquantity_2.setObjectName(u"productquantity_2")
        self.productquantity_2.setGeometry(QRect(476, 277, 951, 78))
        self.productquantity_2.setStyleSheet(u"color: #545454;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 26px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.totalpricecontainer_2 = QWidget(self.shopcontainer_2)
        self.totalpricecontainer_2.setObjectName(u"totalpricecontainer_2")
        self.totalpricecontainer_2.setGeometry(QRect(1069, 277, 358, 78))
        self.totalpricecontainer_2.setStyleSheet(u"background-color: white;")
        self.totalpricelabel_2 = QLabel(self.totalpricecontainer_2)
        self.totalpricelabel_2.setObjectName(u"totalpricelabel_2")
        self.totalpricelabel_2.setGeometry(QRect(30, 30, 49, 16))
        self.bahtpic_2 = QLabel(self.totalpricecontainer_2)
        self.bahtpic_2.setObjectName(u"bahtpic_2")
        self.bahtpic_2.setGeometry(QRect(160, 30, 49, 16))
        self.bahtpic_2.setStyleSheet(u"image: url(:/pic/images/baht.png);\n"
"border: none;")
        self.checkstatusbutton_2 = QPushButton(self.shopcontainer_2)
        self.checkstatusbutton_2.setObjectName(u"checkstatusbutton_2")
        self.checkstatusbutton_2.setGeometry(QRect(1181, 378, 248, 78))
        self.checkstatusbutton_2.setStyleSheet(u"color: #FFF;\n"
"border-radius: 10px;\n"
"background-color: #CD4662;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.shopcontainer_3 = QWidget(self.frame)
        self.shopcontainer_3.setObjectName(u"shopcontainer_3")
        self.shopcontainer_3.setGeometry(QRect(58, 1039, 1427, 523))
        self.shopcontainer_3.setStyleSheet(u"background-color: yellow;")
        self.shopname_3 = QLabel(self.shopcontainer_3)
        self.shopname_3.setObjectName(u"shopname_3")
        self.shopname_3.setGeometry(QRect(68, 46, 390, 59))
        self.shopname_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 26px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.shoppic_3 = QPushButton(self.shopcontainer_3)
        self.shoppic_3.setObjectName(u"shoppic_3")
        self.shoppic_3.setGeometry(QRect(68, 123, 333, 333))
        self.shoppic_3.setStyleSheet(u"background: #D9D9D9;")
        self.productname_3 = QLabel(self.shopcontainer_3)
        self.productname_3.setObjectName(u"productname_3")
        self.productname_3.setGeometry(QRect(476, 123, 951, 78))
        self.productname_3.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 26px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.productdesciption_3 = QLabel(self.shopcontainer_3)
        self.productdesciption_3.setObjectName(u"productdesciption_3")
        self.productdesciption_3.setGeometry(QRect(476, 199, 951, 78))
        self.productdesciption_3.setStyleSheet(u"color: #545454;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 26px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.productquantity_3 = QLabel(self.shopcontainer_3)
        self.productquantity_3.setObjectName(u"productquantity_3")
        self.productquantity_3.setGeometry(QRect(476, 277, 951, 78))
        self.productquantity_3.setStyleSheet(u"color: #545454;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 26px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.totalpricecontainer_3 = QWidget(self.shopcontainer_3)
        self.totalpricecontainer_3.setObjectName(u"totalpricecontainer_3")
        self.totalpricecontainer_3.setGeometry(QRect(1069, 277, 358, 78))
        self.totalpricecontainer_3.setStyleSheet(u"background-color: white;")
        self.totalpricelabel_3 = QLabel(self.totalpricecontainer_3)
        self.totalpricelabel_3.setObjectName(u"totalpricelabel_3")
        self.totalpricelabel_3.setGeometry(QRect(30, 30, 49, 16))
        self.bahtpic_3 = QLabel(self.totalpricecontainer_3)
        self.bahtpic_3.setObjectName(u"bahtpic_3")
        self.bahtpic_3.setGeometry(QRect(160, 30, 49, 16))
        self.bahtpic_3.setStyleSheet(u"image: url(:/pic/images/baht.png);\n"
"border: none;")
        self.checkstatusbutton_3 = QPushButton(self.shopcontainer_3)
        self.checkstatusbutton_3.setObjectName(u"checkstatusbutton_3")
        self.checkstatusbutton_3.setGeometry(QRect(1181, 378, 248, 78))
        self.checkstatusbutton_3.setStyleSheet(u"color: #FFF;\n"
"border-radius: 10px;\n"
"background-color: #CD4662;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.shopcontainer_4 = QWidget(self.frame)
        self.shopcontainer_4.setObjectName(u"shopcontainer_4")
        self.shopcontainer_4.setGeometry(QRect(58, 1562, 1427, 523))
        self.shopcontainer_4.setStyleSheet(u"background-color: yellow;")
        self.shopname_4 = QLabel(self.shopcontainer_4)
        self.shopname_4.setObjectName(u"shopname_4")
        self.shopname_4.setGeometry(QRect(68, 46, 390, 59))
        self.shopname_4.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 26px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.shoppic_4 = QPushButton(self.shopcontainer_4)
        self.shoppic_4.setObjectName(u"shoppic_4")
        self.shoppic_4.setGeometry(QRect(68, 123, 333, 333))
        self.shoppic_4.setStyleSheet(u"background: #D9D9D9;")
        self.productname_4 = QLabel(self.shopcontainer_4)
        self.productname_4.setObjectName(u"productname_4")
        self.productname_4.setGeometry(QRect(476, 123, 951, 78))
        self.productname_4.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 26px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.productdesciption_4 = QLabel(self.shopcontainer_4)
        self.productdesciption_4.setObjectName(u"productdesciption_4")
        self.productdesciption_4.setGeometry(QRect(476, 199, 951, 78))
        self.productdesciption_4.setStyleSheet(u"color: #545454;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 26px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.productquantity_4 = QLabel(self.shopcontainer_4)
        self.productquantity_4.setObjectName(u"productquantity_4")
        self.productquantity_4.setGeometry(QRect(476, 277, 951, 78))
        self.productquantity_4.setStyleSheet(u"color: #545454;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 26px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.totalpricecontainer_4 = QWidget(self.shopcontainer_4)
        self.totalpricecontainer_4.setObjectName(u"totalpricecontainer_4")
        self.totalpricecontainer_4.setGeometry(QRect(1069, 277, 358, 78))
        self.totalpricecontainer_4.setStyleSheet(u"background-color: white;")
        self.totalpricelabel_4 = QLabel(self.totalpricecontainer_4)
        self.totalpricelabel_4.setObjectName(u"totalpricelabel_4")
        self.totalpricelabel_4.setGeometry(QRect(30, 30, 49, 16))
        self.bahtpic_4 = QLabel(self.totalpricecontainer_4)
        self.bahtpic_4.setObjectName(u"bahtpic_4")
        self.bahtpic_4.setGeometry(QRect(160, 30, 49, 16))
        self.bahtpic_4.setStyleSheet(u"image: url(:/pic/images/baht.png);\n"
"border: none;")
        self.checkstatusbutton_4 = QPushButton(self.shopcontainer_4)
        self.checkstatusbutton_4.setObjectName(u"checkstatusbutton_4")
        self.checkstatusbutton_4.setGeometry(QRect(1181, 378, 248, 78))
        self.checkstatusbutton_4.setStyleSheet(u"color: #FFF;\n"
"border-radius: 10px;\n"
"background-color: #CD4662;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")

        self.verticalLayout_2.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

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
        self.reviewlabel.setText(QCoreApplication.translate("MainWindow", u"Reviews", None))
        self.tobeshipbutton.setText(QCoreApplication.translate("MainWindow", u"To be shipped", None))
        self.toberecievebutton.setText(QCoreApplication.translate("MainWindow", u"To be recieved", None))
        self.completebutton.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.shopname.setText(QCoreApplication.translate("MainWindow", u"Shop's name", None))
        self.shoppic.setText("")
        self.productname.setText(QCoreApplication.translate("MainWindow", u"Product's name", None))
        self.productdesciption.setText(QCoreApplication.translate("MainWindow", u"Desciption", None))
        self.productquantity.setText(QCoreApplication.translate("MainWindow", u"1 piece", None))
        self.totalpricelabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.bahtpic.setText("")
        self.checkstatusbutton.setText(QCoreApplication.translate("MainWindow", u"Check Status", None))
        self.shopname_2.setText(QCoreApplication.translate("MainWindow", u"Shop's name", None))
        self.shoppic_2.setText("")
        self.productname_2.setText(QCoreApplication.translate("MainWindow", u"Product's name", None))
        self.productdesciption_2.setText(QCoreApplication.translate("MainWindow", u"Desciption", None))
        self.productquantity_2.setText(QCoreApplication.translate("MainWindow", u"1 piece", None))
        self.totalpricelabel_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.bahtpic_2.setText("")
        self.checkstatusbutton_2.setText(QCoreApplication.translate("MainWindow", u"Check Status", None))
        self.shopname_3.setText(QCoreApplication.translate("MainWindow", u"Shop's name", None))
        self.shoppic_3.setText("")
        self.productname_3.setText(QCoreApplication.translate("MainWindow", u"Product's name", None))
        self.productdesciption_3.setText(QCoreApplication.translate("MainWindow", u"Desciption", None))
        self.productquantity_3.setText(QCoreApplication.translate("MainWindow", u"1 piece", None))
        self.totalpricelabel_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.bahtpic_3.setText("")
        self.checkstatusbutton_3.setText(QCoreApplication.translate("MainWindow", u"Check Status", None))
        self.shopname_4.setText(QCoreApplication.translate("MainWindow", u"Shop's name", None))
        self.shoppic_4.setText("")
        self.productname_4.setText(QCoreApplication.translate("MainWindow", u"Product's name", None))
        self.productdesciption_4.setText(QCoreApplication.translate("MainWindow", u"Desciption", None))
        self.productquantity_4.setText(QCoreApplication.translate("MainWindow", u"1 piece", None))
        self.totalpricelabel_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.bahtpic_4.setText("")
        self.checkstatusbutton_4.setText(QCoreApplication.translate("MainWindow", u"Check Status", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ChopShop", None))
        self.homebutton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.favbutton.setText(QCoreApplication.translate("MainWindow", u"Favorites", None))
        self.orderbutton.setText(QCoreApplication.translate("MainWindow", u"My Orders", None))
        self.messbutton.setText(QCoreApplication.translate("MainWindow", u"Messages", None))
        self.settingsbutton.setText("")
        self.exitbutton.setText("")
    # retranslateUi

