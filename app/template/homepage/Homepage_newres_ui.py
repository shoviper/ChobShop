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
    QStackedWidget, QVBoxLayout, QWidget)

import app.assets.realsourceimg.real

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(1280, 720)
        Main.setStyleSheet(u"background-color: #FAF9F6;")
        self.stackedWidget = QStackedWidget(Main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-1, -1, 1281, 721))
        self.orderpage = QWidget()
        self.orderpage.setObjectName(u"orderpage")
        self.gridLayoutWidget_2 = QWidget(self.orderpage)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 251, 721))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.navbar_2 = QWidget(self.gridLayoutWidget_2)
        self.navbar_2.setObjectName(u"navbar_2")
        self.navbar_2.setCursor(QCursor(Qt.ArrowCursor))
        self.navbar_2.setStyleSheet(u"background-color: #FAF9F6;")
        self.Logolabel_4 = QLabel(self.navbar_2)
        self.Logolabel_4.setObjectName(u"Logolabel_4")
        self.Logolabel_4.setGeometry(QRect(30, 40, 191, 51))
        self.Logolabel_4.setStyleSheet(u"font-family: Supermercado;\n"
"                font-size: 36px;\n"
"                font-weight: 700;\n"
"                line-height: normalpx;\n"
"                text-align: center;\n"
"                color: #000000;")
        self.homebutton_4 = QPushButton(self.navbar_2)
        self.homebutton_4.setObjectName(u"homebutton_4")
        self.homebutton_4.setGeometry(QRect(40, 130, 171, 67))
        self.homebutton_4.setStyleSheet(u"QPushButton{\n"
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
        self.homebutton_4.setCheckable(True)
        self.homebutton_4.setAutoExclusive(True)
        self.favbutton_4 = QPushButton(self.navbar_2)
        self.favbutton_4.setObjectName(u"favbutton_4")
        self.favbutton_4.setGeometry(QRect(40, 240, 171, 67))
        self.favbutton_4.setStyleSheet(u"QPushButton{\n"
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
        self.favbutton_4.setCheckable(True)
        self.favbutton_4.setAutoExclusive(True)
        self.orderbutton_4 = QPushButton(self.navbar_2)
        self.orderbutton_4.setObjectName(u"orderbutton_4")
        self.orderbutton_4.setGeometry(QRect(40, 350, 171, 67))
        self.orderbutton_4.setStyleSheet(u"QPushButton{\n"
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
        self.orderbutton_4.setCheckable(True)
        self.orderbutton_4.setAutoExclusive(True)
        self.messbutton_4 = QPushButton(self.navbar_2)
        self.messbutton_4.setObjectName(u"messbutton_4")
        self.messbutton_4.setGeometry(QRect(40, 460, 171, 67))
        self.messbutton_4.setStyleSheet(u"QPushButton{\n"
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
        self.messbutton_4.setCheckable(True)
        self.messbutton_4.setAutoExclusive(True)
        self.settingbutton_4 = QPushButton(self.navbar_2)
        self.settingbutton_4.setObjectName(u"settingbutton_4")
        self.settingbutton_4.setGeometry(QRect(70, 630, 41, 41))
        self.settingbutton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingbutton_4.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/settingpic.png);")
        self.settingbutton_4.setIconSize(QSize(30, 30))
        self.exitbutton_4 = QPushButton(self.navbar_2)
        self.exitbutton_4.setObjectName(u"exitbutton_4")
        self.exitbutton_4.setGeometry(QRect(140, 630, 41, 41))
        self.exitbutton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitbutton_4.setStyleSheet(u"image: url(:/pic/realimages/exitpic.png);\n"
"border: none;")
        self.exitbutton_4.setIconSize(QSize(27, 27))
        self.exitbutton_4.setFlat(False)

        self.gridLayout_2.addWidget(self.navbar_2, 0, 0, 1, 1)

        self.searchcontainer_2 = QWidget(self.orderpage)
        self.searchcontainer_2.setObjectName(u"searchcontainer_2")
        self.searchcontainer_2.setGeometry(QRect(250, 0, 1031, 109))
        self.searchcontainer_2.setStyleSheet(u"background-color: #FAF9F6;")
        self.searchbox_2 = QLineEdit(self.searchcontainer_2)
        self.searchbox_2.setObjectName(u"searchbox_2")
        self.searchbox_2.setGeometry(QRect(60, 50, 684, 31))
        self.searchbox_2.setStyleSheet(u"				border-radius: 15px;\n"
"                background-color: #EDEDED;\n"
"                color: #CD4662;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 16px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"				padding-left: 20px;\n"
"")
        self.loginsignoutbutton_2 = QPushButton(self.searchcontainer_2)
        self.loginsignoutbutton_2.setObjectName(u"loginsignoutbutton_2")
        self.loginsignoutbutton_2.setGeometry(QRect(900, 50, 71, 31))
        self.loginsignoutbutton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginsignoutbutton_2.setStyleSheet(u"color: #000;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 20px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                border: none;\n"
"				text-align: center;")
        self.cartbutton_2 = QPushButton(self.searchcontainer_2)
        self.cartbutton_2.setObjectName(u"cartbutton_2")
        self.cartbutton_2.setGeometry(QRect(770, 50, 34, 31))
        self.cartbutton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.cartbutton_2.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/cartpic.png);")
        self.cartbutton_2.setIconSize(QSize(34, 31))
        self.profilebutton_2 = QPushButton(self.searchcontainer_2)
        self.profilebutton_2.setObjectName(u"profilebutton_2")
        self.profilebutton_2.setGeometry(QRect(840, 50, 31, 31))
        self.profilebutton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.profilebutton_2.setStyleSheet(u"border: none;\n"
"image: url(:/pic/realimages/profilepic.png);")
        self.profilebutton_2.setIconSize(QSize(31, 31))
        self.ordernavcontainer = QWidget(self.orderpage)
        self.ordernavcontainer.setObjectName(u"ordernavcontainer")
        self.ordernavcontainer.setGeometry(QRect(250, 109, 1031, 139))
        self.ordernavcontainer.setStyleSheet(u"background-color: #FAF9F6;")
        self.reviewlabel = QLabel(self.ordernavcontainer)
        self.reviewlabel.setObjectName(u"reviewlabel")
        self.reviewlabel.setGeometry(QRect(60, 15, 150, 51))
        self.reviewlabel.setStyleSheet(u"color: #545454;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.tobeshipbutton = QPushButton(self.ordernavcontainer)
        self.tobeshipbutton.setObjectName(u"tobeshipbutton")
        self.tobeshipbutton.setGeometry(QRect(60, 85, 320, 50))
        self.tobeshipbutton.setStyleSheet(u"QPushButton{\n"
"	color: #545454;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 22px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #CD4662;\n"
"}\n"
"\n"
"")
        self.toberecievebutton = QPushButton(self.ordernavcontainer)
        self.toberecievebutton.setObjectName(u"toberecievebutton")
        self.toberecievebutton.setGeometry(QRect(382, 85, 320, 50))
        self.toberecievebutton.setStyleSheet(u"QPushButton{\n"
"	color: #545454;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 22px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #CD4662;\n"
"}\n"
"\n"
"")
        self.completebutton = QPushButton(self.ordernavcontainer)
        self.completebutton.setObjectName(u"completebutton")
        self.completebutton.setGeometry(QRect(704, 85, 320, 50))
        self.completebutton.setStyleSheet(u"QPushButton{\n"
"	color: #545454;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 22px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #CD4662;\n"
"}\n"
"\n"
"")
        self.stackedWidget_order = QStackedWidget(self.orderpage)
        self.stackedWidget_order.setObjectName(u"stackedWidget_order")
        self.stackedWidget_order.setGeometry(QRect(250, 248, 1031, 472))
        self.stackedWidget_order.setStyleSheet(u"background-color: #FAF9F6;")
        self.tobeshippage = QWidget()
        self.tobeshippage.setObjectName(u"tobeshippage")
        self.verticalLayout = QVBoxLayout(self.tobeshippage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea_ship = QScrollArea(self.tobeshippage)
        self.scrollArea_ship.setObjectName(u"scrollArea_ship")
        self.scrollArea_ship.setStyleSheet(u"QScrollArea {\n"
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
        self.scrollArea_ship.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 998, 1018))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_ship = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_ship.setObjectName(u"frame_ship")
        self.frame_ship.setMinimumSize(QSize(0, 1000))
        self.frame_ship.setStyleSheet(u"background-color: #FAF9F6;")
        self.frame_ship.setFrameShape(QFrame.StyledPanel)
        self.frame_ship.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_3 = QWidget(self.frame_ship)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(40, 0, 931, 321))
        self.gridLayoutordership1 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayoutordership1.setObjectName(u"gridLayoutordership1")
        self.gridLayoutordership1.setContentsMargins(0, 0, 0, 0)
        self.ordership1 = QWidget(self.gridLayoutWidget_3)
        self.ordership1.setObjectName(u"ordership1")
        self.label_3 = QLabel(self.ordership1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 80, 441, 121))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayoutordership1.addWidget(self.ordership1, 0, 0, 1, 1)

        self.gridLayoutWidget_4 = QWidget(self.frame_ship)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(40, 320, 931, 321))
        self.gridLayoutordership2 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayoutordership2.setObjectName(u"gridLayoutordership2")
        self.gridLayoutordership2.setContentsMargins(0, 0, 0, 0)
        self.ordership2 = QWidget(self.gridLayoutWidget_4)
        self.ordership2.setObjectName(u"ordership2")

        self.gridLayoutordership2.addWidget(self.ordership2, 0, 0, 1, 1)

        self.gridLayoutWidget_5 = QWidget(self.frame_ship)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(40, 640, 931, 321))
        self.gridLayoutordership3 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayoutordership3.setObjectName(u"gridLayoutordership3")
        self.gridLayoutordership3.setContentsMargins(0, 0, 0, 0)
        self.ordership3 = QWidget(self.gridLayoutWidget_5)
        self.ordership3.setObjectName(u"ordership3")

        self.gridLayoutordership3.addWidget(self.ordership3, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_ship)

        self.scrollArea_ship.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout.addWidget(self.scrollArea_ship)

        self.stackedWidget_order.addWidget(self.tobeshippage)
        self.tobereceivepage = QWidget()
        self.tobereceivepage.setObjectName(u"tobereceivepage")
        self.verticalLayout_3 = QVBoxLayout(self.tobereceivepage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea_receive = QScrollArea(self.tobereceivepage)
        self.scrollArea_receive.setObjectName(u"scrollArea_receive")
        self.scrollArea_receive.setStyleSheet(u"QScrollArea {\n"
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
        self.scrollArea_receive.setWidgetResizable(True)
        self.scrollAreaWidgetContents_receive = QWidget()
        self.scrollAreaWidgetContents_receive.setObjectName(u"scrollAreaWidgetContents_receive")
        self.scrollAreaWidgetContents_receive.setGeometry(QRect(0, 0, 998, 1018))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_receive)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_receive = QFrame(self.scrollAreaWidgetContents_receive)
        self.frame_receive.setObjectName(u"frame_receive")
        self.frame_receive.setMinimumSize(QSize(0, 1000))
        self.frame_receive.setFrameShape(QFrame.StyledPanel)
        self.frame_receive.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_6 = QWidget(self.frame_receive)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(40, 0, 931, 321))
        self.gridLayoutorderreceive1 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayoutorderreceive1.setObjectName(u"gridLayoutorderreceive1")
        self.gridLayoutorderreceive1.setContentsMargins(0, 0, 0, 0)
        self.orderreceive1 = QWidget(self.gridLayoutWidget_6)
        self.orderreceive1.setObjectName(u"orderreceive1")
        self.label = QLabel(self.orderreceive1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 100, 441, 121))
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayoutorderreceive1.addWidget(self.orderreceive1, 0, 0, 1, 1)

        self.gridLayoutWidget_8 = QWidget(self.frame_receive)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(40, 320, 931, 321))
        self.gridLayoutorderreceive2 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayoutorderreceive2.setObjectName(u"gridLayoutorderreceive2")
        self.gridLayoutorderreceive2.setContentsMargins(0, 0, 0, 0)
        self.orderreceive2 = QWidget(self.gridLayoutWidget_8)
        self.orderreceive2.setObjectName(u"orderreceive2")

        self.gridLayoutorderreceive2.addWidget(self.orderreceive2, 0, 0, 1, 1)

        self.gridLayoutWidget_9 = QWidget(self.frame_receive)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(40, 640, 931, 321))
        self.gridLayoutorderreceive3 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayoutorderreceive3.setObjectName(u"gridLayoutorderreceive3")
        self.gridLayoutorderreceive3.setContentsMargins(0, 0, 0, 0)
        self.orderreceive3 = QWidget(self.gridLayoutWidget_9)
        self.orderreceive3.setObjectName(u"orderreceive3")

        self.gridLayoutorderreceive3.addWidget(self.orderreceive3, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_receive)

        self.scrollArea_receive.setWidget(self.scrollAreaWidgetContents_receive)

        self.verticalLayout_3.addWidget(self.scrollArea_receive)

        self.stackedWidget_order.addWidget(self.tobereceivepage)
        self.completepage = QWidget()
        self.completepage.setObjectName(u"completepage")
        self.verticalLayout_5 = QVBoxLayout(self.completepage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea_complete = QScrollArea(self.completepage)
        self.scrollArea_complete.setObjectName(u"scrollArea_complete")
        self.scrollArea_complete.setStyleSheet(u"QScrollArea {\n"
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
        self.scrollArea_complete.setWidgetResizable(True)
        self.scrollAreaWidgetContents_complete = QWidget()
        self.scrollAreaWidgetContents_complete.setObjectName(u"scrollAreaWidgetContents_complete")
        self.scrollAreaWidgetContents_complete.setGeometry(QRect(0, 0, 998, 1018))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_complete)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_complete = QFrame(self.scrollAreaWidgetContents_complete)
        self.frame_complete.setObjectName(u"frame_complete")
        self.frame_complete.setMinimumSize(QSize(0, 1000))
        self.frame_complete.setFrameShape(QFrame.StyledPanel)
        self.frame_complete.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_7 = QWidget(self.frame_complete)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(40, 0, 931, 321))
        self.gridLayoutordercomplete1 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayoutordercomplete1.setObjectName(u"gridLayoutordercomplete1")
        self.gridLayoutordercomplete1.setContentsMargins(0, 0, 0, 0)
        self.ordercomplete1 = QWidget(self.gridLayoutWidget_7)
        self.ordercomplete1.setObjectName(u"ordercomplete1")
        self.label_2 = QLabel(self.ordercomplete1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 80, 441, 121))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayoutordercomplete1.addWidget(self.ordercomplete1, 0, 0, 1, 1)

        self.gridLayoutWidget_10 = QWidget(self.frame_complete)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(40, 320, 931, 321))
        self.gridLayoutordercomplete2 = QGridLayout(self.gridLayoutWidget_10)
        self.gridLayoutordercomplete2.setObjectName(u"gridLayoutordercomplete2")
        self.gridLayoutordercomplete2.setContentsMargins(0, 0, 0, 0)
        self.ordercomplete2 = QWidget(self.gridLayoutWidget_10)
        self.ordercomplete2.setObjectName(u"ordercomplete2")

        self.gridLayoutordercomplete2.addWidget(self.ordercomplete2, 0, 0, 1, 1)

        self.gridLayoutWidget_11 = QWidget(self.frame_complete)
        self.gridLayoutWidget_11.setObjectName(u"gridLayoutWidget_11")
        self.gridLayoutWidget_11.setGeometry(QRect(40, 640, 931, 321))
        self.gridLayoutordercomplete3 = QGridLayout(self.gridLayoutWidget_11)
        self.gridLayoutordercomplete3.setObjectName(u"gridLayoutordercomplete3")
        self.gridLayoutordercomplete3.setContentsMargins(0, 0, 0, 0)
        self.ordercomplete3 = QWidget(self.gridLayoutWidget_11)
        self.ordercomplete3.setObjectName(u"ordercomplete3")

        self.gridLayoutordercomplete3.addWidget(self.ordercomplete3, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_complete)

        self.scrollArea_complete.setWidget(self.scrollAreaWidgetContents_complete)

        self.verticalLayout_5.addWidget(self.scrollArea_complete)

        self.stackedWidget_order.addWidget(self.completepage)
        self.stackedWidget.addWidget(self.orderpage)
        self.stackedWidget_order.raise_()
        self.ordernavcontainer.raise_()
        self.searchcontainer_2.raise_()
        self.gridLayoutWidget_2.raise_()
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
        self.settingbutton.setStyleSheet(u"image: url(:/pic/realimages/settingpic.png);\n"
"border: none;")
        self.settingbutton.setIconSize(QSize(30, 30))
        self.exitbutton = QPushButton(self.navbar)
        self.exitbutton.setObjectName(u"exitbutton")
        self.exitbutton.setGeometry(QRect(140, 630, 41, 41))
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
        icon = QIcon()
        icon.addFile(u"../../assets/images/newres/newarrival.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon1.addFile(u"../../assets/images/newres/onsales.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon2.addFile(u"../../assets/images/newres/buyagain.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon3.addFile(u"../../assets/images/newres/bestselling.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.myorderspage = QWidget()
        self.myorderspage.setObjectName(u"myorderspage")
        self.myordersnavcontainer = QWidget(self.myorderspage)
        self.myordersnavcontainer.setObjectName(u"myordersnavcontainer")
        self.myordersnavcontainer.setGeometry(QRect(0, 0, 1031, 139))
        self.myordersnavcontainer.setStyleSheet(u"background-color: #FAF9F6;")
        self.myorderslabel = QLabel(self.myordersnavcontainer)
        self.myorderslabel.setObjectName(u"myorderslabel")
        self.myorderslabel.setGeometry(QRect(60, 0, 150, 51))
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
        self.stackedWidget.addWidget(self.userprofile)

        self.retranslateUi(Main)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_order.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Form", None))
        self.Logolabel_4.setText(QCoreApplication.translate("Main", u"ChopShop", None))
        self.homebutton_4.setText(QCoreApplication.translate("Main", u"Home", None))
        self.favbutton_4.setText(QCoreApplication.translate("Main", u"Favorites", None))
        self.orderbutton_4.setText(QCoreApplication.translate("Main", u"My Orders", None))
        self.messbutton_4.setText(QCoreApplication.translate("Main", u"Messages", None))
        self.settingbutton_4.setText("")
        self.exitbutton_4.setText("")
        self.searchbox_2.setPlaceholderText(QCoreApplication.translate("Main", u"Search..", None))
        self.loginsignoutbutton_2.setText(QCoreApplication.translate("Main", u"Log In", None))
        self.cartbutton_2.setText("")
        self.profilebutton_2.setText("")
        self.reviewlabel.setText(QCoreApplication.translate("Main", u"Reviews", None))
        self.tobeshipbutton.setText(QCoreApplication.translate("Main", u"To be shipped", None))
        self.toberecievebutton.setText(QCoreApplication.translate("Main", u"To be recieved", None))
        self.completebutton.setText(QCoreApplication.translate("Main", u"Completed", None))
        self.label_3.setText(QCoreApplication.translate("Main", u"Testship", None))
        self.label.setText(QCoreApplication.translate("Main", u"Testreceive", None))
        self.label_2.setText(QCoreApplication.translate("Main", u"Testcomplete", None))
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
        self.myorderslabel.setText(QCoreApplication.translate("Main", u"Reviews", None))
        self.tobeshippedbutton.setText(QCoreApplication.translate("Main", u"To be shipped", None))
        self.toberecievedbutton.setText(QCoreApplication.translate("Main", u"To be recieved", None))
        self.completedbutton.setText(QCoreApplication.translate("Main", u"Completed", None))
        self.tobeshippedlabel.setText(QCoreApplication.translate("Main", u"to be shipped", None))
        self.toberecievedlabel.setText(QCoreApplication.translate("Main", u"to be recieved", None))
        self.completedlabel.setText(QCoreApplication.translate("Main", u"completed", None))
    # retranslateUi

