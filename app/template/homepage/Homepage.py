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
        self.stackedWidget_main = QStackedWidget(self.centralwidget)
        self.stackedWidget_main.setObjectName(u"stackedWidget_main")
        self.stackedWidget_main.setGeometry(QRect(0, 0, 1921, 1081))
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.menu = QWidget(self.main_page)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(0, 0, 373, 1080))
        self.menu.setStyleSheet(u"background-color: #FAF9F6;")
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
        self.homebutton.setCheckable(True)
        self.homebutton.setAutoExclusive(True)
        self.favbutton = QPushButton(self.menu)
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
        self.favbutton.setCheckable(True)
        self.favbutton.setAutoExclusive(True)
        self.orderbutton = QPushButton(self.menu)
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
        self.orderbutton.setCheckable(True)
        self.orderbutton.setAutoExclusive(True)
        self.messbutton = QPushButton(self.menu)
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
        self.messbutton.setCheckable(True)
        self.messbutton.setAutoExclusive(True)
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
        self.searchcontainer = QWidget(self.main_page)
        self.searchcontainer.setObjectName(u"searchcontainer")
        self.searchcontainer.setGeometry(QRect(370, 0, 1547, 161))
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
"				padding-left: 20px;\n"
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
"                margin-bottom: 15px;\n"
"				text-align: center;")
        self.stackedWidget = QStackedWidget(self.main_page)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QRect(368, 160, 1551, 921))
        self.stackedWidget.setStyleSheet(u"background-color: #FAF9F6;")
        self.page1home = QWidget()
        self.page1home.setObjectName(u"page1home")
        self.scrollArea = QScrollArea(self.page1home)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 10, 1541, 911))
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1526, 2000))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 2000))
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -1, 1541, 2491))
        self.frame.setMinimumSize(QSize(0, 1080))
        self.frame.setStyleSheet(u"border: none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.stylelabbutton = QPushButton(self.frame)
        self.stylelabbutton.setObjectName(u"stylelabbutton")
        self.stylelabbutton.setGeometry(QRect(80, 30, 1421, 335))
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
        self.onsalebutton.setGeometry(QRect(1220, 430, 282, 64))
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
        self.buyagainbutton.setGeometry(QRect(460, 430, 282, 64))
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
        self.bestsellbutton.setGeometry(QRect(840, 430, 282, 64))
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
        self.newarrivalbutton.setGeometry(QRect(80, 430, 282, 64))
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
        self.product_3.setGeometry(QRect(1120, 690, 381, 502))
        self.product_3.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct3 = QPushButton(self.product_3)
        self.picproduct3.setObjectName(u"picproduct3")
        self.picproduct3.setGeometry(QRect(43, 43, 295, 295))
        self.picproduct3.setStyleSheet(u"background-color: #FFF;")
        self.product_2 = QWidget(self.frame)
        self.product_2.setObjectName(u"product_2")
        self.product_2.setGeometry(QRect(610, 690, 381, 502))
        self.product_2.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct2 = QPushButton(self.product_2)
        self.picproduct2.setObjectName(u"picproduct2")
        self.picproduct2.setGeometry(QRect(43, 43, 295, 295))
        self.picproduct2.setStyleSheet(u"background-color: #FFF;")
        self.product_1 = QWidget(self.frame)
        self.product_1.setObjectName(u"product_1")
        self.product_1.setGeometry(QRect(80, 690, 381, 502))
        self.product_1.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1 = QPushButton(self.product_1)
        self.picproduct1.setObjectName(u"picproduct1")
        self.picproduct1.setGeometry(QRect(43, 43, 295, 295))
        self.picproduct1.setStyleSheet(u"background-color: #FFF;")
        self.suggestlabel = QLabel(self.frame)
        self.suggestlabel.setObjectName(u"suggestlabel")
        self.suggestlabel.setGeometry(QRect(80, 560, 250, 72))
        self.suggestlabel.setStyleSheet(u"color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 40px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.product_6 = QWidget(self.frame)
        self.product_6.setObjectName(u"product_6")
        self.product_6.setGeometry(QRect(610, 1260, 381, 502))
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
        self.product_4.setGeometry(QRect(1120, 1260, 381, 502))
        self.product_4.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct3_5 = QPushButton(self.product_4)
        self.picproduct3_5.setObjectName(u"picproduct3_5")
        self.picproduct3_5.setGeometry(QRect(43, 43, 295, 295))
        self.picproduct3_5.setStyleSheet(u"background-color: #FFF;")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.page1home)
        self.page2fav = QWidget()
        self.page2fav.setObjectName(u"page2fav")
        self.verticalLayout_2 = QVBoxLayout(self.page2fav)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea_2 = QScrollArea(self.page2fav)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
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
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 67, 2518))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 2500))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.favoritelabel = QLabel(self.frame_2)
        self.favoritelabel.setObjectName(u"favoritelabel")
        self.favoritelabel.setGeometry(QRect(58, 0, 190, 72))
        self.favoritelabel.setStyleSheet(u"color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 40px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.container1 = QWidget(self.frame_2)
        self.container1.setObjectName(u"container1")
        self.container1.setGeometry(QRect(58, 132, 381, 502))
        self.container1.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic1 = QPushButton(self.container1)
        self.pic1.setObjectName(u"pic1")
        self.pic1.setGeometry(QRect(43, 43, 295, 295))
        self.pic1.setStyleSheet(u"background-color: #FFF;")
        self.container2 = QWidget(self.frame_2)
        self.container2.setObjectName(u"container2")
        self.container2.setGeometry(QRect(582, 132, 381, 502))
        self.container2.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic2 = QPushButton(self.container2)
        self.pic2.setObjectName(u"pic2")
        self.pic2.setGeometry(QRect(43, 43, 295, 295))
        self.pic2.setStyleSheet(u"background-color: #FFF;")
        self.container3 = QWidget(self.frame_2)
        self.container3.setObjectName(u"container3")
        self.container3.setGeometry(QRect(1107, 132, 381, 502))
        self.container3.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic3 = QPushButton(self.container3)
        self.pic3.setObjectName(u"pic3")
        self.pic3.setGeometry(QRect(43, 43, 295, 295))
        self.pic3.setStyleSheet(u"background-color: #FFF;")
        self.container4 = QWidget(self.frame_2)
        self.container4.setObjectName(u"container4")
        self.container4.setGeometry(QRect(58, 697, 381, 502))
        self.container4.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic4 = QPushButton(self.container4)
        self.pic4.setObjectName(u"pic4")
        self.pic4.setGeometry(QRect(43, 43, 295, 295))
        self.pic4.setStyleSheet(u"background-color: #FFF;")
        self.container5 = QWidget(self.frame_2)
        self.container5.setObjectName(u"container5")
        self.container5.setGeometry(QRect(582, 697, 381, 502))
        self.container5.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic5 = QPushButton(self.container5)
        self.pic5.setObjectName(u"pic5")
        self.pic5.setGeometry(QRect(43, 43, 295, 295))
        self.pic5.setStyleSheet(u"background-color: #FFF;")
        self.container6 = QWidget(self.frame_2)
        self.container6.setObjectName(u"container6")
        self.container6.setGeometry(QRect(1107, 697, 381, 502))
        self.container6.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic6 = QPushButton(self.container6)
        self.pic6.setObjectName(u"pic6")
        self.pic6.setGeometry(QRect(43, 43, 295, 295))
        self.pic6.setStyleSheet(u"background-color: #FFF;")
        self.container7 = QWidget(self.frame_2)
        self.container7.setObjectName(u"container7")
        self.container7.setGeometry(QRect(58, 1262, 381, 502))
        self.container7.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic7 = QPushButton(self.container7)
        self.pic7.setObjectName(u"pic7")
        self.pic7.setGeometry(QRect(43, 43, 295, 295))
        self.pic7.setStyleSheet(u"background-color: #FFF;")
        self.container8 = QWidget(self.frame_2)
        self.container8.setObjectName(u"container8")
        self.container8.setGeometry(QRect(582, 1262, 381, 502))
        self.container8.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic8 = QPushButton(self.container8)
        self.pic8.setObjectName(u"pic8")
        self.pic8.setGeometry(QRect(43, 43, 295, 295))
        self.pic8.setStyleSheet(u"background-color: #FFF;")
        self.container9 = QWidget(self.frame_2)
        self.container9.setObjectName(u"container9")
        self.container9.setGeometry(QRect(1107, 1262, 381, 502))
        self.container9.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic9 = QPushButton(self.container9)
        self.pic9.setObjectName(u"pic9")
        self.pic9.setGeometry(QRect(43, 43, 295, 295))
        self.pic9.setStyleSheet(u"background-color: #FFF;")

        self.verticalLayout_3.addWidget(self.frame_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.page2fav)
        self.page3order = QWidget()
        self.page3order.setObjectName(u"page3order")
        self.verticalLayout_4 = QVBoxLayout(self.page3order)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget.addWidget(self.page3order)
        self.stackedWidget_main.addWidget(self.main_page)
        self.editprofile_page = QWidget()
        self.editprofile_page.setObjectName(u"editprofile_page")
        self.stackedWidget_main.addWidget(self.editprofile_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ChopShop", None))
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
        self.favoritelabel.setText(QCoreApplication.translate("MainWindow", u"Favorites", None))
        self.pic1.setText("")
        self.pic2.setText("")
        self.pic3.setText("")
        self.pic4.setText("")
        self.pic5.setText("")
        self.pic6.setText("")
        self.pic7.setText("")
        self.pic8.setText("")
        self.pic9.setText("")
    # retranslateUi

