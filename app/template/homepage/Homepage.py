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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.menu = QWidget(self.centralwidget)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(0, 0, 373, 1080))
        self.label = QLabel(self.menu)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(45, 68, 285, 77))
        self.homebutton = QPushButton(self.menu)
        self.homebutton.setObjectName(u"homebutton")
        self.homebutton.setGeometry(QRect(54, 211, 265, 94))
        self.favbutton = QPushButton(self.menu)
        self.favbutton.setObjectName(u"favbutton")
        self.favbutton.setGeometry(QRect(54, 371, 265, 94))
        self.orderbutton = QPushButton(self.menu)
        self.orderbutton.setObjectName(u"orderbutton")
        self.orderbutton.setGeometry(QRect(54, 531, 265, 94))
        self.messbutton = QPushButton(self.menu)
        self.messbutton.setObjectName(u"messbutton")
        self.messbutton.setGeometry(QRect(54, 691, 265, 94))
        self.settingsbutton = QPushButton(self.menu)
        self.settingsbutton.setObjectName(u"settingsbutton")
        self.settingsbutton.setGeometry(QRect(119, 930, 68, 48))
        self.exitbutton = QPushButton(self.menu)
        self.exitbutton.setObjectName(u"exitbutton")
        self.exitbutton.setGeometry(QRect(187, 930, 68, 48))
        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setGeometry(QRect(344, 0, 1546, 1080))
        self.verticalLayout = QVBoxLayout(self.main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollarea = QScrollArea(self.main)
        self.scrollarea.setObjectName(u"scrollarea")
        self.scrollarea.setMinimumSize(QSize(1546, 1080))
        self.scrollarea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1545, 3000))
        self.search = QLineEdit(self.scrollAreaWidgetContents)
        self.search.setObjectName(u"search")
        self.search.setPlaceholderText("Search..")
        self.search.setGeometry(QRect(67, 78, 1076, 57))
        self.signinsignoutbutton = QPushButton(self.scrollAreaWidgetContents)
        self.signinsignoutbutton.setObjectName(u"signinsignoutbutton")
        self.signinsignoutbutton.setGeometry(QRect(1384, 78, 113, 58))
        self.profilebutton = QPushButton(self.scrollAreaWidgetContents)
        self.profilebutton.setObjectName(u"profilebutton")
        self.profilebutton.setGeometry(QRect(1292, 78, 68, 48))
        self.cartbutton = QPushButton(self.scrollAreaWidgetContents)
        self.cartbutton.setObjectName(u"cartbutton")
        self.cartbutton.setGeometry(QRect(1186, 78, 68, 48))
        self.stylelabbutton = QPushButton(self.scrollAreaWidgetContents)
        self.stylelabbutton.setObjectName(u"stylelabbutton")
        self.stylelabbutton.setGeometry(QRect(67, 210, 1430, 335))
        self.newarrivalbutton = QPushButton(self.scrollAreaWidgetContents)
        self.newarrivalbutton.setObjectName(u"newarrivalbutton")
        self.newarrivalbutton.setGeometry(QRect(67, 608, 282, 64))
        self.onsalebutton = QPushButton(self.scrollAreaWidgetContents)
        self.onsalebutton.setObjectName(u"onsalebutton")
        self.onsalebutton.setGeometry(QRect(449, 608, 282, 64))
        self.bestsellbutton = QPushButton(self.scrollAreaWidgetContents)
        self.bestsellbutton.setObjectName(u"bestsellbutton")
        self.bestsellbutton.setGeometry(QRect(831, 608, 282, 64))
        self.buyagainbutton = QPushButton(self.scrollAreaWidgetContents)
        self.buyagainbutton.setObjectName(u"buyagainbutton")
        self.buyagainbutton.setGeometry(QRect(1215, 608, 282, 64))
        self.suggestlabel = QLabel(self.scrollAreaWidgetContents)
        self.suggestlabel.setObjectName(u"suggestlabel")
        self.suggestlabel.setGeometry(QRect(67, 735, 233, 72))
        self.container1 = QWidget(self.scrollAreaWidgetContents)
        self.container1.setObjectName(u"container1")
        self.container1.setGeometry(QRect(67, 870, 381, 502))
        self.container2 = QWidget(self.scrollAreaWidgetContents)
        self.container2.setObjectName(u"container2")
        self.container2.setGeometry(QRect(591, 870, 381, 502))
        self.container3 = QWidget(self.scrollAreaWidgetContents)
        self.container3.setObjectName(u"container3")
        self.container3.setGeometry(QRect(1116, 870, 381, 502))
        self.container4 = QWidget(self.scrollAreaWidgetContents)
        self.container4.setObjectName(u"container4")
        self.container4.setGeometry(QRect(67, 1435, 381, 502))
        self.container5 = QWidget(self.scrollAreaWidgetContents)
        self.container5.setObjectName(u"container5")
        self.container5.setGeometry(QRect(591, 1435, 381, 502))
        self.container6 = QWidget(self.scrollAreaWidgetContents)
        self.container6.setObjectName(u"container6")
        self.container6.setGeometry(QRect(1116, 1435, 381, 502))

        self.scrollarea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollarea)

        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

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
        self.signinsignoutbutton.setText(QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.profilebutton.setText("")
        self.cartbutton.setText("")
        self.stylelabbutton.setText(QCoreApplication.translate("MainWindow", u"Style Lab", None))
        self.newarrivalbutton.setText(QCoreApplication.translate("MainWindow", u"New Arrival", None))
        self.onsalebutton.setText(QCoreApplication.translate("MainWindow", u"On Sales", None))
        self.bestsellbutton.setText(QCoreApplication.translate("MainWindow", u"Best Selling", None))
        self.buyagainbutton.setText(QCoreApplication.translate("MainWindow", u"Buy Again", None))
        self.suggestlabel.setText(QCoreApplication.translate("MainWindow", u"Suggestion", None))
    # retranslateUi

