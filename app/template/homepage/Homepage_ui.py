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

# import app.assets.realsourceimg.real

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
        self.page1home = QWidget()
        self.page1home.setObjectName(u"page1home")
        self.scrollArea = QScrollArea(self.page1home)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 1511, 883))
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1496, 2000))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 2000))
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -10, 1531, 2500))
        self.frame.setMinimumSize(QSize(0, 1080))
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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 85, 2518))
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

        self.verticalLayout.addWidget(self.stackedWidget)

        self.menu = QWidget(self.centralwidget)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(0, 0, 1921, 1081))
        self.main_page = QWidget(self.menu)
        self.main_page.setObjectName(u"main_page")
        self.main_page.setGeometry(QRect(0, 0, 1919, 1081))
        self.menu1 = QWidget(self.main_page)
        self.menu1.setObjectName(u"menu1")
        self.menu1.setGeometry(QRect(0, 0, 373, 1080))
        self.menu1.setStyleSheet(u"background-color: #FAF9F6;")
        self.label = QLabel(self.menu1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(45, 68, 285, 77))
        self.label.setStyleSheet(u"font-family: Supermercado;\n"
"                font-size: 64px;\n"
"                font-weight: 400;\n"
"                line-height: 77px;\n"
"                letter-spacing: 0em;\n"
"                text-align: center;\n"
"                color: #000000;")
        self.homebutton = QPushButton(self.menu1)
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
        self.favbutton = QPushButton(self.menu1)
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
        self.orderbutton = QPushButton(self.menu1)
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
        self.messbutton = QPushButton(self.menu1)
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
        self.settingsbutton = QPushButton(self.menu1)
        self.settingsbutton.setObjectName(u"settingsbutton")
        self.settingsbutton.setGeometry(QRect(119, 930, 68, 48))
        self.settingsbutton.setStyleSheet(u"image: url(:/pic/images/settings.png);\n"
"border: none;")
        self.exitbutton = QPushButton(self.menu1)
        self.exitbutton.setObjectName(u"exitbutton")
        self.exitbutton.setGeometry(QRect(187, 930, 68, 48))
        self.exitbutton.setStyleSheet(u"image: url(:/pic/images/exit.png);\n"
"border: none;")
        self.searchcontainer1 = QWidget(self.main_page)
        self.searchcontainer1.setObjectName(u"searchcontainer1")
        self.searchcontainer1.setGeometry(QRect(370, 0, 1547, 161))
        self.searchcontainer1.setStyleSheet(u"background-color: #FAF9F6;")
        self.searchbox1 = QLineEdit(self.searchcontainer1)
        self.searchbox1.setObjectName(u"searchbox1")
        self.searchbox1.setGeometry(QRect(76, 78, 1076, 57))
        self.searchbox1.setStyleSheet(u"border-radius: 27%;\n"
"                background-color: #EDEDED;\n"
"                color: #CD4662;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 24px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"				padding-left: 20px;\n"
"")
        self.profilebutton1 = QPushButton(self.searchcontainer1)
        self.profilebutton1.setObjectName(u"profilebutton1")
        self.profilebutton1.setGeometry(QRect(1292, 78, 68, 48))
        self.profilebutton1.setStyleSheet(u"image: url(:/pic/images/profile.png);\n"
"border: none;")
        self.cartbutton1 = QPushButton(self.searchcontainer1)
        self.cartbutton1.setObjectName(u"cartbutton1")
        self.cartbutton1.setGeometry(QRect(1186, 78, 68, 48))
        self.cartbutton1.setStyleSheet(u"image: url(:/pic/images/cart.png);\n"
"border: none;")
        self.signinsignoutbutton1 = QPushButton(self.searchcontainer1)
        self.signinsignoutbutton1.setObjectName(u"signinsignoutbutton1")
        self.signinsignoutbutton1.setGeometry(QRect(1384, 78, 113, 58))
        self.signinsignoutbutton1.setStyleSheet(u"color: #000;\n"
"                text-align: right;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 32px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                border: none;\n"
"                margin-bottom: 15px;\n"
"				text-align: center;")
        self.stackedWidget1 = QStackedWidget(self.main_page)
        self.stackedWidget1.setObjectName(u"stackedWidget1")
        self.stackedWidget1.setEnabled(True)
        self.stackedWidget1.setGeometry(QRect(368, 160, 1551, 921))
        self.stackedWidget1.setStyleSheet(u"background-color: #FAF9F6;")
        self.page1home1 = QWidget()
        self.page1home1.setObjectName(u"page1home1")
        self.scrollArea1 = QScrollArea(self.page1home1)
        self.scrollArea1.setObjectName(u"scrollArea1")
        self.scrollArea1.setGeometry(QRect(0, 10, 1541, 911))
        self.scrollArea1.setStyleSheet(u"QScrollArea {\n"
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
        self.scrollArea1.setWidgetResizable(True)
        self.scrollAreaWidgetContents1 = QWidget()
        self.scrollAreaWidgetContents1.setObjectName(u"scrollAreaWidgetContents1")
        self.scrollAreaWidgetContents1.setGeometry(QRect(0, 0, 1526, 2000))
        self.scrollAreaWidgetContents1.setMinimumSize(QSize(0, 2000))
        self.frame1 = QFrame(self.scrollAreaWidgetContents1)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setGeometry(QRect(0, -1, 1541, 2491))
        self.frame1.setMinimumSize(QSize(0, 1080))
        self.frame1.setStyleSheet(u"border: none;")
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.stylelabbutton1 = QPushButton(self.frame1)
        self.stylelabbutton1.setObjectName(u"stylelabbutton1")
        self.stylelabbutton1.setGeometry(QRect(80, 30, 1421, 335))
        self.stylelabbutton1.setStyleSheet(u"color: #FFF;\n"
"                text-align: center;\n"
"                font-family: Supermercado;\n"
"                font-size: 96px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                border-radius: 10px;\n"
"                background-color: #CD4662;")
        self.onsalebutton1 = QPushButton(self.frame1)
        self.onsalebutton1.setObjectName(u"onsalebutton1")
        self.onsalebutton1.setGeometry(QRect(1220, 430, 282, 64))
        self.onsalebutton1.setStyleSheet(u"border-radius: 10px;\n"
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
        self.buyagainbutton1 = QPushButton(self.frame1)
        self.buyagainbutton1.setObjectName(u"buyagainbutton1")
        self.buyagainbutton1.setGeometry(QRect(460, 430, 282, 64))
        self.buyagainbutton1.setStyleSheet(u"border-radius: 10px;\n"
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
        self.bestsellbutton1 = QPushButton(self.frame1)
        self.bestsellbutton1.setObjectName(u"bestsellbutton1")
        self.bestsellbutton1.setGeometry(QRect(840, 430, 282, 64))
        self.bestsellbutton1.setStyleSheet(u"border-radius: 10px;\n"
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
        self.newarrivalbutton1 = QPushButton(self.frame1)
        self.newarrivalbutton1.setObjectName(u"newarrivalbutton1")
        self.newarrivalbutton1.setGeometry(QRect(80, 430, 282, 64))
        self.newarrivalbutton1.setStyleSheet(u"border-radius: 10px;\n"
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
        self.product_31 = QWidget(self.frame1)
        self.product_31.setObjectName(u"product_31")
        self.product_31.setGeometry(QRect(1120, 690, 381, 502))
        self.product_31.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct31 = QPushButton(self.product_31)
        self.picproduct31.setObjectName(u"picproduct31")
        self.picproduct31.setGeometry(QRect(43, 43, 295, 295))
        self.picproduct31.setStyleSheet(u"background-color: #FFF;")
        self.product_21 = QWidget(self.frame1)
        self.product_21.setObjectName(u"product_21")
        self.product_21.setGeometry(QRect(610, 690, 381, 502))
        self.product_21.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct21 = QPushButton(self.product_21)
        self.picproduct21.setObjectName(u"picproduct21")
        self.picproduct21.setGeometry(QRect(43, 43, 295, 295))
        self.picproduct21.setStyleSheet(u"background-color: #FFF;")
        self.product_11 = QWidget(self.frame1)
        self.product_11.setObjectName(u"product_11")
        self.product_11.setGeometry(QRect(80, 690, 381, 502))
        self.product_11.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct11 = QPushButton(self.product_11)
        self.picproduct11.setObjectName(u"picproduct11")
        self.picproduct11.setGeometry(QRect(43, 43, 295, 295))
        self.picproduct11.setStyleSheet(u"background-color: #FFF;")
        self.suggestlabel1 = QLabel(self.frame1)
        self.suggestlabel1.setObjectName(u"suggestlabel1")
        self.suggestlabel1.setGeometry(QRect(80, 560, 250, 72))
        self.suggestlabel1.setStyleSheet(u"color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 40px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.product_61 = QWidget(self.frame1)
        self.product_61.setObjectName(u"product_61")
        self.product_61.setGeometry(QRect(610, 1260, 381, 502))
        self.product_61.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct2_51 = QPushButton(self.product_61)
        self.picproduct2_51.setObjectName(u"picproduct2_51")
        self.picproduct2_51.setGeometry(QRect(43, 43, 295, 295))
        self.picproduct2_51.setStyleSheet(u"background-color: #FFF;")
        self.product_51 = QWidget(self.frame1)
        self.product_51.setObjectName(u"product_51")
        self.product_51.setGeometry(QRect(80, 1260, 381, 502))
        self.product_51.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct1_51 = QPushButton(self.product_51)
        self.picproduct1_51.setObjectName(u"picproduct1_51")
        self.picproduct1_51.setGeometry(QRect(43, 43, 295, 295))
        self.picproduct1_51.setStyleSheet(u"background-color: #FFF;")
        self.product_41 = QWidget(self.frame1)
        self.product_41.setObjectName(u"product_41")
        self.product_41.setGeometry(QRect(1120, 1260, 381, 502))
        self.product_41.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.picproduct3_51 = QPushButton(self.product_41)
        self.picproduct3_51.setObjectName(u"picproduct3_51")
        self.picproduct3_51.setGeometry(QRect(43, 43, 295, 295))
        self.picproduct3_51.setStyleSheet(u"background-color: #FFF;")
        self.scrollArea1.setWidget(self.scrollAreaWidgetContents1)
        self.stackedWidget1.addWidget(self.page1home1)
        self.page2fav1 = QWidget()
        self.page2fav1.setObjectName(u"page2fav1")
        self.verticalLayout_21 = QVBoxLayout(self.page2fav1)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.scrollArea_21 = QScrollArea(self.page2fav1)
        self.scrollArea_21.setObjectName(u"scrollArea_21")
        self.scrollArea_21.setStyleSheet(u"QScrollArea {\n"
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
        self.scrollArea_21.setWidgetResizable(True)
        self.scrollAreaWidgetContents_21 = QWidget()
        self.scrollAreaWidgetContents_21.setObjectName(u"scrollAreaWidgetContents_21")
        self.scrollAreaWidgetContents_21.setGeometry(QRect(0, 0, 85, 2518))
        self.verticalLayout_31 = QVBoxLayout(self.scrollAreaWidgetContents_21)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_21 = QFrame(self.scrollAreaWidgetContents_21)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 2500))
        self.frame_21.setStyleSheet(u"")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.favoritelabel1 = QLabel(self.frame_21)
        self.favoritelabel1.setObjectName(u"favoritelabel1")
        self.favoritelabel1.setGeometry(QRect(58, 0, 190, 72))
        self.favoritelabel1.setStyleSheet(u"color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 40px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.container11 = QWidget(self.frame_21)
        self.container11.setObjectName(u"container11")
        self.container11.setGeometry(QRect(58, 132, 381, 502))
        self.container11.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic11 = QPushButton(self.container11)
        self.pic11.setObjectName(u"pic11")
        self.pic11.setGeometry(QRect(43, 43, 295, 295))
        self.pic11.setStyleSheet(u"background-color: #FFF;")
        self.container21 = QWidget(self.frame_21)
        self.container21.setObjectName(u"container21")
        self.container21.setGeometry(QRect(582, 132, 381, 502))
        self.container21.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic21 = QPushButton(self.container21)
        self.pic21.setObjectName(u"pic21")
        self.pic21.setGeometry(QRect(43, 43, 295, 295))
        self.pic21.setStyleSheet(u"background-color: #FFF;")
        self.container31 = QWidget(self.frame_21)
        self.container31.setObjectName(u"container31")
        self.container31.setGeometry(QRect(1107, 132, 381, 502))
        self.container31.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic31 = QPushButton(self.container31)
        self.pic31.setObjectName(u"pic31")
        self.pic31.setGeometry(QRect(43, 43, 295, 295))
        self.pic31.setStyleSheet(u"background-color: #FFF;")
        self.container41 = QWidget(self.frame_21)
        self.container41.setObjectName(u"container41")
        self.container41.setGeometry(QRect(58, 697, 381, 502))
        self.container41.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic41 = QPushButton(self.container41)
        self.pic41.setObjectName(u"pic41")
        self.pic41.setGeometry(QRect(43, 43, 295, 295))
        self.pic41.setStyleSheet(u"background-color: #FFF;")
        self.container51 = QWidget(self.frame_21)
        self.container51.setObjectName(u"container51")
        self.container51.setGeometry(QRect(582, 697, 381, 502))
        self.container51.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic51 = QPushButton(self.container51)
        self.pic51.setObjectName(u"pic51")
        self.pic51.setGeometry(QRect(43, 43, 295, 295))
        self.pic51.setStyleSheet(u"background-color: #FFF;")
        self.container61 = QWidget(self.frame_21)
        self.container61.setObjectName(u"container61")
        self.container61.setGeometry(QRect(1107, 697, 381, 502))
        self.container61.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic61 = QPushButton(self.container61)
        self.pic61.setObjectName(u"pic61")
        self.pic61.setGeometry(QRect(43, 43, 295, 295))
        self.pic61.setStyleSheet(u"background-color: #FFF;")
        self.container71 = QWidget(self.frame_21)
        self.container71.setObjectName(u"container71")
        self.container71.setGeometry(QRect(58, 1262, 381, 502))
        self.container71.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic71 = QPushButton(self.container71)
        self.pic71.setObjectName(u"pic71")
        self.pic71.setGeometry(QRect(43, 43, 295, 295))
        self.pic71.setStyleSheet(u"background-color: #FFF;")
        self.container81 = QWidget(self.frame_21)
        self.container81.setObjectName(u"container81")
        self.container81.setGeometry(QRect(582, 1262, 381, 502))
        self.container81.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic81 = QPushButton(self.container81)
        self.pic81.setObjectName(u"pic81")
        self.pic81.setGeometry(QRect(43, 43, 295, 295))
        self.pic81.setStyleSheet(u"background-color: #FFF;")
        self.container91 = QWidget(self.frame_21)
        self.container91.setObjectName(u"container91")
        self.container91.setGeometry(QRect(1107, 1262, 381, 502))
        self.container91.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic91 = QPushButton(self.container91)
        self.pic91.setObjectName(u"pic91")
        self.pic91.setGeometry(QRect(43, 43, 295, 295))
        self.pic91.setStyleSheet(u"background-color: #FFF;")

        self.verticalLayout_31.addWidget(self.frame_21)

        self.scrollArea_21.setWidget(self.scrollAreaWidgetContents_21)

        self.verticalLayout_21.addWidget(self.scrollArea_21)

        self.stackedWidget1.addWidget(self.page2fav1)
        self.page3order1 = QWidget()
        self.page3order1.setObjectName(u"page3order1")
        self.verticalLayout_41 = QVBoxLayout(self.page3order1)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.stackedWidget1.addWidget(self.page3order1)
        self.editprofile_page = QWidget(self.menu)
        self.editprofile_page.setObjectName(u"editprofile_page")
        self.editprofile_page.setGeometry(QRect(0, 0, 100, 30))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget1.setCurrentIndex(0)


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
        self.label.setText(QCoreApplication.translate("MainWindow", u"ChopShop", None))
        self.homebutton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.favbutton.setText(QCoreApplication.translate("MainWindow", u"Favorites", None))
        self.orderbutton.setText(QCoreApplication.translate("MainWindow", u"My Orders", None))
        self.messbutton.setText(QCoreApplication.translate("MainWindow", u"Messages", None))
        self.settingsbutton.setText("")
        self.exitbutton.setText("")
        self.searchbox1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search..", None))
        self.profilebutton1.setText("")
        self.cartbutton1.setText("")
        self.signinsignoutbutton1.setText(QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.stylelabbutton1.setText(QCoreApplication.translate("MainWindow", u"Style lab", None))
        self.onsalebutton1.setText(QCoreApplication.translate("MainWindow", u"On Sales", None))
        self.buyagainbutton1.setText(QCoreApplication.translate("MainWindow", u"Buy Again", None))
        self.bestsellbutton1.setText(QCoreApplication.translate("MainWindow", u"Best Selling", None))
        self.newarrivalbutton1.setText(QCoreApplication.translate("MainWindow", u"New Arrival", None))
        self.picproduct31.setText("")
        self.picproduct21.setText("")
        self.picproduct11.setText("")
        self.suggestlabel1.setText(QCoreApplication.translate("MainWindow", u"Suggestions", None))
        self.picproduct2_51.setText("")
        self.picproduct1_51.setText("")
        self.picproduct3_51.setText("")
        self.favoritelabel1.setText(QCoreApplication.translate("MainWindow", u"Favorites", None))
        self.pic11.setText("")
        self.pic21.setText("")
        self.pic31.setText("")
        self.pic41.setText("")
        self.pic51.setText("")
        self.pic61.setText("")
        self.pic71.setText("")
        self.pic81.setText("")
        self.pic91.setText("")
    # retranslateUi

