# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Homepage.ui'
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
        self.menu.setStyleSheet(u"background-color: #FAF9F6;\n")
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
        self.homebutton.setStyleSheet(u"""
                QPushButton {
                        font-family: Suwannaphum;
                        font-size: 24px;
                        font-weight: 700;
                        line-height: 43px;
                        letter-spacing: 0em;
                        text-align: middle;
                        color: #ffffff;
                        background-color: #AEC289;
                        border-radius: 10px;
                }

                QPushButton:hover {
                        background-color: #F4DBDB; 
                }
                """)
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
"                border-radius: 10px;\n""")
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
        self.settingsbutton.setCursor(Qt.PointingHandCursor)
        self.settingsbutton.setStyleSheet(u"")
        self.exitbutton = QPushButton(self.menu)
        self.exitbutton.setObjectName(u"exitbutton")
        self.exitbutton.setGeometry(QRect(187, 930, 68, 48))
        self.exitbutton.setCursor(Qt.PointingHandCursor)
        self.exitbutton.setStyleSheet(u"")
        self.searchcontainer = QWidget(self.centralwidget)
        self.searchcontainer.setObjectName(u"searchcontainer")
        self.searchcontainer.setGeometry(QRect(373, 0, 1547, 161))
        self.searchcontainer.setStyleSheet(u"background-color: #FAF9F6;")
        self.searchbox = QLineEdit(self.searchcontainer)
        self.searchbox.setObjectName(u"searchbox")
        self.searchbox.setGeometry(QRect(67, 78, 1076, 57))
        self.searchbox.setStyleSheet(u"border-radius: 27%;\n"
"                background-color: #EDEDED;\n"
"                color: #CD4662;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 24px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                padding: 0 30px\n")
        self.profile = QPushButton(self.searchcontainer)
        self.profile.setObjectName(u"profile")
        self.profile.setGeometry(QRect(1292, 78, 68, 48))
        self.profile.setCursor(Qt.PointingHandCursor)
        self.profile.setStyleSheet(u"")
        self.cartbutton = QPushButton(self.searchcontainer)
        self.cartbutton.setObjectName(u"cartbutton")
        self.cartbutton.setGeometry(QRect(1186, 78, 68, 48))
        self.cartbutton.setCursor(Qt.PointingHandCursor)
        self.cartbutton.setStyleSheet(u"")
        self.signinsignoutbutton = QPushButton(self.searchcontainer)
        self.signinsignoutbutton.setObjectName(u"signinsignoutbutton")
        self.signinsignoutbutton.setGeometry(QRect(1384, 78, 113, 58))
        self.signinsignoutbutton.setCursor(Qt.PointingHandCursor)
        self.signinsignoutbutton.setStyleSheet(u"color: #000;\n"
"                text-align: right;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 32px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                border: none;\n"
"                margin-bottom: 15px;\n")
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -695, 1510, 5018))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 5000))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.stylelab_header = QPushButton(self.frame)
        self.stylelab_header.setObjectName(u"stylelab_header")
        self.stylelab_header.setGeometry(QRect(58, 0, 1421, 335))
        self.stylelab_header.setStyleSheet(u"color: #FFF;\n"
"                text-align: center;\n"
"                font-family: Supermercado;\n"
"                font-size: 96px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                border-radius: 10px;\n"
"                background-color: #CD4662;")
        self.newarrival_filter = QPushButton(self.frame)
        self.newarrival_filter.setObjectName(u"newarrival_filter")
        self.newarrival_filter.setGeometry(QRect(58, 398, 282, 64))
        self.newarrival_filter.setStyleSheet(u"border-radius: 10px;\n"
"                border: 2px solid #000;\n"
"                opacity: 0.2;\n"
"                background-color: #F7F2EB;\n"
"                color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 32px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;")
        self.onsales_filter = QPushButton(self.frame)
        self.onsales_filter.setObjectName(u"onsales_filter")
        self.onsales_filter.setGeometry(QRect(1206, 398, 282, 64))
        self.onsales_filter.setStyleSheet(u"border-radius: 10px;\n"
"                border: 2px solid #000;\n"
"                opacity: 0.2;\n"
"                background-color: #F7F2EB;\n"
"                color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 32px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;")
        self.buyagain_filter = QPushButton(self.frame)
        self.buyagain_filter.setObjectName(u"buyagain_filter")
        self.buyagain_filter.setGeometry(QRect(440, 398, 282, 64))
        self.buyagain_filter.setStyleSheet(u"border-radius: 10px;\n"
"                border: 2px solid #000;\n"
"                opacity: 0.2;\n"
"                background-color: #F7F2EB;\n"
"                color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 32px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;")
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(822, 398, 282, 64))
        self.pushButton_5.setStyleSheet(u"border-radius: 10px;\n"
"                border: 2px solid #000;\n"
"                opacity: 0.2;\n"
"                background-color: #F7F2EB;\n"
"                color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 32px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;")
        self.suggestlabel = QLabel(self.frame)
        self.suggestlabel.setObjectName(u"suggestlabel")
        self.suggestlabel.setGeometry(QRect(58, 528, 250, 72))
        self.suggestlabel.setStyleSheet(u"color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 40px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.container1 = QWidget(self.frame)
        self.container1.setObjectName(u"container1")
        self.container1.setGeometry(QRect(58, 663, 381, 502))
        self.container1.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic1 = QPushButton(self.container1)
        self.pic1.setObjectName(u"pic1")
        self.pic1.setGeometry(QRect(43, 43, 295, 295))
        self.pic1.setStyleSheet(u"background-color: #FFF;")
        self.container2 = QWidget(self.frame)
        self.container2.setObjectName(u"container2")
        self.container2.setGeometry(QRect(582, 663, 381, 502))
        self.container2.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic2 = QPushButton(self.container2)
        self.pic2.setObjectName(u"pic2")
        self.pic2.setGeometry(QRect(43, 43, 295, 295))
        self.pic2.setStyleSheet(u"background-color: #FFF;")
        self.container3 = QWidget(self.frame)
        self.container3.setObjectName(u"container3")
        self.container3.setGeometry(QRect(1107, 663, 381, 502))
        self.container3.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic = QPushButton(self.container3)
        self.pic.setObjectName(u"pic")
        self.pic.setGeometry(QRect(43, 43, 295, 295))
        self.pic.setStyleSheet(u"background-color: #FFF;")
        self.container4 = QWidget(self.frame)
        self.container4.setObjectName(u"container4")
        self.container4.setGeometry(QRect(58, 1228, 381, 502))
        self.container4.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic1_3 = QPushButton(self.container4)
        self.pic1_3.setObjectName(u"pic1_3")
        self.pic1_3.setGeometry(QRect(43, 43, 295, 295))
        self.pic1_3.setStyleSheet(u"background-color: #FFF;")
        self.container5 = QWidget(self.frame)
        self.container5.setObjectName(u"container5")
        self.container5.setGeometry(QRect(582, 1228, 381, 502))
        self.container5.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic1_4 = QPushButton(self.container5)
        self.pic1_4.setObjectName(u"pic1_4")
        self.pic1_4.setGeometry(QRect(43, 43, 295, 295))
        self.pic1_4.setStyleSheet(u"background-color: #FFF;")
        self.container6 = QWidget(self.frame)
        self.container6.setObjectName(u"container6")
        self.container6.setGeometry(QRect(1107, 1228, 381, 502))
        self.container6.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic1_5 = QPushButton(self.container6)
        self.pic1_5.setObjectName(u"pic1_5")
        self.pic1_5.setGeometry(QRect(43, 43, 295, 295))
        self.pic1_5.setStyleSheet(u"background-color: #FFF;")
        self.container7 = QWidget(self.frame)
        self.container7.setObjectName(u"container7")
        self.container7.setGeometry(QRect(58, 1793, 381, 502))
        self.container7.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic1_6 = QPushButton(self.container7)
        self.pic1_6.setObjectName(u"pic1_6")
        self.pic1_6.setGeometry(QRect(43, 43, 295, 295))
        self.pic1_6.setStyleSheet(u"background-color: #FFF;")
        self.container8 = QWidget(self.frame)
        self.container8.setObjectName(u"container8")
        self.container8.setGeometry(QRect(582, 1793, 381, 502))
        self.container8.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic1_7 = QPushButton(self.container8)
        self.pic1_7.setObjectName(u"pic1_7")
        self.pic1_7.setGeometry(QRect(43, 43, 295, 295))
        self.pic1_7.setStyleSheet(u"background-color: #FFF;")
        self.container9 = QWidget(self.frame)
        self.container9.setObjectName(u"container9")
        self.container9.setGeometry(QRect(1107, 1793, 381, 502))
        self.container9.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic1_8 = QPushButton(self.container9)
        self.pic1_8.setObjectName(u"pic1_8")
        self.pic1_8.setGeometry(QRect(43, 43, 295, 295))
        self.pic1_8.setStyleSheet(u"background-color: #FFF;")

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
        self.profile.setText("")
        self.cartbutton.setText("")
        self.signinsignoutbutton.setText(QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.stylelab_header.setText(QCoreApplication.translate("MainWindow", u"Style lab", None))
        self.newarrival_filter.setText(QCoreApplication.translate("MainWindow", u"New Arrival", None))
        self.onsales_filter.setText(QCoreApplication.translate("MainWindow", u"On Sales", None))
        self.buyagain_filter.setText(QCoreApplication.translate("MainWindow", u"Buy Again", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Best Selling", None))
        self.suggestlabel.setText(QCoreApplication.translate("MainWindow", u"Suggestions", None))
        self.pic1.setText("")
        self.pic2.setText("")
        self.pic.setText("")
        self.pic1_3.setText("")
        self.pic1_4.setText("")
        self.pic1_5.setText("")
        self.pic1_6.setText("")
        self.pic1_7.setText("")
        self.pic1_8.setText("")
    # retranslateUi

