# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Profile.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import app.assets.sourceimg.all

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet(u"background-color: #FAF9F6;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.backbutton = QPushButton(self.centralwidget)
        self.backbutton.setObjectName(u"backbutton")
        self.backbutton.setGeometry(QRect(47, 48, 21, 39))
        self.backbutton.setStyleSheet(u"background-color: #FAF9F6;\n"
"color: #CD4662;\n"
"font-size: 39px;\n"
"border: none;\n"
"")
        self.usernamecontainer = QWidget(self.centralwidget)
        self.usernamecontainer.setObjectName(u"usernamecontainer")
        self.usernamecontainer.setGeometry(QRect(88, 68, 1782, 266))
        self.usernamecontainer.setStyleSheet(u"background-color: #FAF9F6;")
        self.picprofile = QLabel(self.usernamecontainer)
        self.picprofile.setObjectName(u"picprofile")
        self.picprofile.setGeometry(QRect(33, 0, 212, 212))
        self.picprofile.setStyleSheet(u"image: url(:/pic/images/profile.png);\n"
"image: url(:/pic/images/profile.png);\n"
"background-color: #CD4662;\n"
"border-radius: 50%;")
        self.usernamelabel = QLabel(self.usernamecontainer)
        self.usernamelabel.setObjectName(u"usernamelabel")
        self.usernamelabel.setGeometry(QRect(332, 0, 1449, 71))
        self.usernamelabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 40px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.favlabel = QLabel(self.usernamecontainer)
        self.favlabel.setObjectName(u"favlabel")
        self.favlabel.setGeometry(QRect(332, 71, 1449, 71))
        self.favlabel.setStyleSheet(u"color: #AEC289;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.editprofilebutton = QPushButton(self.usernamecontainer)
        self.editprofilebutton.setObjectName(u"editprofilebutton")
        self.editprofilebutton.setGeometry(QRect(332, 141, 1449, 71))
        self.editprofilebutton.setStyleSheet(u"color: #CD4662;\n"
"font-family: Suwannaphum;\n"
"font-size: 36px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;\n"
"margin-right: 1275px;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.editprofilebutton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backbutton.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.picprofile.setText("")
        self.usernamelabel.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.favlabel.setText(QCoreApplication.translate("MainWindow", u"3 Favorites", None))
        self.editprofilebutton.setText(QCoreApplication.translate("MainWindow", u"Edit Profile", None))
    # retranslateUi

