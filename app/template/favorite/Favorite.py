# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Favorite.ui'
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
        MainWindow.setEnabled(True)
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
        self.scrollArea = QScrollArea(self.main)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1512, 5018))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 5000))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.favoritelabel = QLabel(self.frame)
        self.favoritelabel.setObjectName(u"favoritelabel")
        self.favoritelabel.setGeometry(QRect(58, 0, 190, 72))
        self.favoritelabel.setStyleSheet(u"color: #545454;\n"
"                text-align: center;\n"
"                font-family: Suwannaphum;\n"
"                font-size: 40px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.container1 = QWidget(self.frame)
        self.container1.setObjectName(u"container1")
        self.container1.setGeometry(QRect(58, 132, 381, 502))
        self.container1.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic1 = QPushButton(self.container1)
        self.pic1.setObjectName(u"pic1")
        self.pic1.setGeometry(QRect(43, 43, 295, 295))
        self.pic1.setStyleSheet(u"background-color: #FFF;")
        self.container2 = QWidget(self.frame)
        self.container2.setObjectName(u"container2")
        self.container2.setGeometry(QRect(582, 132, 381, 502))
        self.container2.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic2 = QPushButton(self.container2)
        self.pic2.setObjectName(u"pic2")
        self.pic2.setGeometry(QRect(43, 43, 295, 295))
        self.pic2.setStyleSheet(u"background-color: #FFF;")
        self.container3 = QWidget(self.frame)
        self.container3.setObjectName(u"container3")
        self.container3.setGeometry(QRect(1107, 132, 381, 502))
        self.container3.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic3 = QPushButton(self.container3)
        self.pic3.setObjectName(u"pic3")
        self.pic3.setGeometry(QRect(43, 43, 295, 295))
        self.pic3.setStyleSheet(u"background-color: #FFF;")
        self.container4 = QWidget(self.frame)
        self.container4.setObjectName(u"container4")
        self.container4.setGeometry(QRect(58, 697, 381, 502))
        self.container4.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic4 = QPushButton(self.container4)
        self.pic4.setObjectName(u"pic4")
        self.pic4.setGeometry(QRect(43, 43, 295, 295))
        self.pic4.setStyleSheet(u"background-color: #FFF;")
        self.container5 = QWidget(self.frame)
        self.container5.setObjectName(u"container5")
        self.container5.setGeometry(QRect(582, 697, 381, 502))
        self.container5.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic5 = QPushButton(self.container5)
        self.pic5.setObjectName(u"pic5")
        self.pic5.setGeometry(QRect(43, 43, 295, 295))
        self.pic5.setStyleSheet(u"background-color: #FFF;")
        self.container6 = QWidget(self.frame)
        self.container6.setObjectName(u"container6")
        self.container6.setGeometry(QRect(1107, 697, 381, 502))
        self.container6.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic6 = QPushButton(self.container6)
        self.pic6.setObjectName(u"pic6")
        self.pic6.setGeometry(QRect(43, 43, 295, 295))
        self.pic6.setStyleSheet(u"background-color: #FFF;")
        self.container7 = QWidget(self.frame)
        self.container7.setObjectName(u"container7")
        self.container7.setGeometry(QRect(58, 1262, 381, 502))
        self.container7.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic7 = QPushButton(self.container7)
        self.pic7.setObjectName(u"pic7")
        self.pic7.setGeometry(QRect(43, 43, 295, 295))
        self.pic7.setStyleSheet(u"background-color: #FFF;")
        self.container8 = QWidget(self.frame)
        self.container8.setObjectName(u"container8")
        self.container8.setGeometry(QRect(582, 1262, 381, 502))
        self.container8.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic8 = QPushButton(self.container8)
        self.pic8.setObjectName(u"pic8")
        self.pic8.setGeometry(QRect(43, 43, 295, 295))
        self.pic8.setStyleSheet(u"background-color: #FFF;")
        self.container9 = QWidget(self.frame)
        self.container9.setObjectName(u"container9")
        self.container9.setGeometry(QRect(1107, 1262, 381, 502))
        self.container9.setStyleSheet(u"border-radius: 10px;\n"
"                background: #D9D9D9;")
        self.pic9 = QPushButton(self.container9)
        self.pic9.setObjectName(u"pic9")
        self.pic9.setGeometry(QRect(43, 43, 295, 295))
        self.pic9.setStyleSheet(u"background-color: #FFF;")

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
    # retranslateUi

