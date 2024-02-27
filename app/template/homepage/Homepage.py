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
    QStackedWidget, QVBoxLayout, QWidget)

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
"                line-height: normal;\n"
"		 padding-left: 20px;\n"
"")
        self.profilebutton = QPushButton(self.searchcontainer)
        self.profilebutton.setObjectName(u"profilebutton")
        self.profilebutton.setGeometry(QRect(1292, 78, 68, 48))
        self.profilebutton.setStyleSheet(u"image: url(:/pic/images/profile.png);\n"
"border: none;")
        self.cartbutton = QPushButton(self.searchcontainer)
        self.cartbutton.setObjectName(u"cartbutton")
        self.cartbutton.setGeometry(QRect(1186, 78, 68, 48))
        self.cartbutton.setStyleSheet(u"image: url(:/pic/images/cart.png);\n"
"border: none;")
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
        self.stackedWidget = QStackedWidget(self.main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setStyleSheet(u"background-color: #FAF9F6;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 1521, 921))
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
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1506, 5000))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 5000))
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 1531, 5000))
        self.frame.setMinimumSize(QSize(1531, 5000))
        self.frame.setStyleSheet(u"border: none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.stylelabbutton = QPushButton(self.frame)
        self.stylelabbutton.setObjectName(u"stylelabbutton")
        self.stylelabbutton.setGeometry(QRect(70, 30, 1421, 335))
        self.stylelabbutton.setStyleSheet(u"color: #FFF;\n"
"                text-align: center;\n"
"                font-family: Supermercado;\n"
"                font-size: 96px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                border-radius: 10px;\n"
"                background-color: #CD4662;")
        self.onsalebutton = QPushButton(self.frame)
        self.onsalebutton.setObjectName(u"onsalebutton")
        self.onsalebutton.setGeometry(QRect(1210, 420, 282, 64))
        self.onsalebutton.setStyleSheet(u"border-radius: 10px;\n"
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
        self.buyagainbutton = QPushButton(self.frame)
        self.buyagainbutton.setObjectName(u"buyagainbutton")
        self.buyagainbutton.setGeometry(QRect(450, 420, 282, 64))
        self.buyagainbutton.setStyleSheet(u"border-radius: 10px;\n"
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
        self.bestsellbutton = QPushButton(self.frame)
        self.bestsellbutton.setObjectName(u"bestsellbutton")
        self.bestsellbutton.setGeometry(QRect(830, 420, 282, 64))
        self.bestsellbutton.setStyleSheet(u"border-radius: 10px;\n"
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
        self.newarrivalbutton = QPushButton(self.frame)
        self.newarrivalbutton.setObjectName(u"newarrivalbutton")
        self.newarrivalbutton.setGeometry(QRect(70, 420, 282, 64))
        self.newarrivalbutton.setStyleSheet(u"border-radius: 10px;\n"
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
        self.product_3 = QWidget(self.frame)
        self.product_3.setObjectName(u"product_3")
        self.product_3.setGeometry(QRect(1100, 670, 381, 502))
        self.product_3.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct3 = QPushButton(self.product_3)
        self.picproduct3.setObjectName(u"picproduct3")
        self.picproduct3.setGeometry(QRect(43, 43, 295, 295))
        self.picproduct3.setStyleSheet(u"background-color: #FFF;")
        self.product_2 = QWidget(self.frame)
        self.product_2.setObjectName(u"product_2")
        self.product_2.setGeometry(QRect(580, 670, 381, 502))
        self.product_2.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct2 = QPushButton(self.product_2)
        self.picproduct2.setObjectName(u"picproduct2")
        self.picproduct2.setGeometry(QRect(43, 43, 295, 295))
        self.picproduct2.setStyleSheet(u"background-color: #FFF;")
        self.product_1 = QWidget(self.frame)
        self.product_1.setObjectName(u"product_1")
        self.product_1.setGeometry(QRect(70, 670, 381, 502))
        self.product_1.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1 = QPushButton(self.product_1)
        self.picproduct1.setObjectName(u"picproduct1")
        self.picproduct1.setGeometry(QRect(43, 43, 295, 295))
        self.picproduct1.setStyleSheet(u"background-color: #FFF;")
        self.suggestlabel = QLabel(self.frame)
        self.suggestlabel.setObjectName(u"suggestlabel")
        self.suggestlabel.setGeometry(QRect(70, 540, 250, 72))
        self.suggestlabel.setStyleSheet(u"color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 40px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.product_6 = QWidget(self.frame)
        self.product_6.setObjectName(u"product_6")
        self.product_6.setGeometry(QRect(590, 1260, 381, 502))
        self.product_6.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct2_5 = QPushButton(self.product_6)
        self.picproduct2_5.setObjectName(u"picproduct2_5")
        self.picproduct2_5.setGeometry(QRect(43, 43, 295, 295))
        self.picproduct2_5.setStyleSheet(u"background-color: #FFF;")
        self.product_5 = QWidget(self.frame)
        self.product_5.setObjectName(u"product_5")
        self.product_5.setGeometry(QRect(80, 1260, 381, 502))
        self.product_5.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1_5 = QPushButton(self.product_5)
        self.picproduct1_5.setObjectName(u"picproduct1_5")
        self.picproduct1_5.setGeometry(QRect(43, 43, 295, 295))
        self.picproduct1_5.setStyleSheet(u"background-color: #FFF;")
        self.product_4 = QWidget(self.frame)
        self.product_4.setObjectName(u"product_4")
        self.product_4.setGeometry(QRect(1110, 1260, 381, 502))
        self.product_4.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct3_5 = QPushButton(self.product_4)
        self.picproduct3_5.setObjectName(u"picproduct3_5")
        self.picproduct3_5.setGeometry(QRect(43, 43, 295, 295))
        self.picproduct3_5.setStyleSheet(u"background-color: #FFF;")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)

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
"	color: #FAF9F6;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 24px;\n"
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
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }")
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
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }")
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
"                background-color: #F4DBDB;\n"
"                color: black;\n"
"            }")
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
        self.stylelabbutton.setText(QCoreApplication.translate("MainWindow", u"Style lab", None))
        self.onsalebutton.setText(QCoreApplication.translate("MainWindow", u"On Sales", None))
        self.buyagainbutton.setText(QCoreApplication.translate("MainWindow", u"Buy Again", None))
        self.bestsellbutton.setText(QCoreApplication.translate("MainWindow", u"Best Selling", None))
        self.newarrivalbutton.setText(QCoreApplication.translate("MainWindow", u"New Arrival", None))
        self.picproduct3.setText("")
        self.picproduct2.setText("")
        self.picproduct1.setText("")
        self.suggestlabel.setText(QCoreApplication.translate("MainWindow", u"Suggestions", None))
        self.picproduct2_5.setText("")
        self.picproduct1_5.setText("")
        self.picproduct3_5.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"ChopShop", None))
        self.homebutton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.favbutton.setText(QCoreApplication.translate("MainWindow", u"Favorites", None))
        self.orderbutton.setText(QCoreApplication.translate("MainWindow", u"My Orders", None))
        self.messbutton.setText(QCoreApplication.translate("MainWindow", u"Messages", None))
        self.settingsbutton.setText("")
        self.exitbutton.setText("")
    # retranslateUi

