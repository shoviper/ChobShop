# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Signup.ui'
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
    QPushButton, QSizePolicy, QWidget)
import app.assets.sourceimg.all

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #FAF9F6;")
        self.rightcontainer = QWidget(self.centralwidget)
        self.rightcontainer.setObjectName(u"rightcontainer")
        self.rightcontainer.setGeometry(QRect(900, 127, 893, 827))
        self.label = QLabel(self.rightcontainer)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-40, 0, 970, 827))
        self.label.setStyleSheet(u"image: url(:/pic/images/loginpic.png);")
        self.homebutton = QPushButton(self.centralwidget)
        self.homebutton.setObjectName(u"homebutton")
        self.homebutton.setGeometry(QRect(10, 70, 172, 33))
        self.homebutton.setStyleSheet(u"QPushButton {\n"
"               color: #CD4662;\n"
"                font-family: Inter;\n"
"                font-size: 24px;\n"
"                font-style: normal;\n"
"                font-weight: 500;\n"
"                line-height: normal;\n"
"                border: none;\n"
"            }\n"
"            QPushButton:hover {\n"
"               color: #AEC289;\n"
"            }")
        self.leftcontainer = QWidget(self.centralwidget)
        self.leftcontainer.setObjectName(u"leftcontainer")
        self.leftcontainer.setGeometry(QRect(127, 127, 646, 827))
        self.leftcontainer.setStyleSheet(u"background-color: #FAF9F6;")
        self.signuplabel = QLabel(self.leftcontainer)
        self.signuplabel.setObjectName(u"signuplabel")
        self.signuplabel.setGeometry(QRect(73, 36, 500, 95))
        self.signuplabel.setStyleSheet(u"color: #000;\n"
"                font-family: Inter;\n"
"                font-size: 48px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.signupbutton = QPushButton(self.leftcontainer)
        self.signupbutton.setObjectName(u"signupbutton")
        self.signupbutton.setGeometry(QRect(73, 620, 500, 80))
        self.signupbutton.setStyleSheet(u"QPushButton {\n"
"                background-color: #CD4662;\n"
"                color: #FFF;\n"
"                text-align: center;\n"
"                font-family: Inter;\n"
"                font-size: 24px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;\n"
"                border-radius: 25px;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #AEC289;\n"
"            }")
        self.logforhaveaccbutton = QLabel(self.leftcontainer)
        self.logforhaveaccbutton.setObjectName(u"logforhaveaccbutton")
        self.logforhaveaccbutton.setGeometry(QRect(80, 748, 493, 38))
        self.logforhaveaccbutton.setStyleSheet(u"color: #CD4662;\n"
"                text-align: center;\n"
"                font-family: Inter;\n"
"                font-size: 20px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                margin-left: 80px;")
        self.username = QLineEdit(self.leftcontainer)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(73, 190, 500, 80))
        self.username.setStyleSheet(u"font-size: 24px;\n"
"                width: 500px;\n"
"                height: 80px;\n"
"                border: none;\n"
"                border-bottom: 3px solid #000;\n"
"                background-color: #FAF9F6;")
        self.password = QLineEdit(self.leftcontainer)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(73, 449, 500, 80))
        self.password.setStyleSheet(u"font-size: 24px;\n"
"                width: 500px;\n"
"                height: 80px;\n"
"                border: none;\n"
"                border-bottom: 3px solid #000;\n"
"                background-color: #FAF9F6;")
        self.signfornoaccbutton = QPushButton(self.leftcontainer)
        self.signfornoaccbutton.setObjectName(u"signfornoaccbutton")
        self.signfornoaccbutton.setGeometry(QRect(400, 748, 80, 38))
        self.signfornoaccbutton.setStyleSheet(u"QPushButton {\n"
"                border: none;\n"
"                color: #AEC289;\n"
"                font-family: Inter;\n"
"                font-size: 20px;\n"
"                font-style: bold;\n"
"                font-weight: 700;\n"
"                border: none;\n"
"                line-height: normal;\n"
"            }\n"
"                           \n"
"            QPushButton:hover {\n"
"                color: #CD4662;\n"
"            }")
        self.email = QLineEdit(self.leftcontainer)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(73, 319, 500, 80))
        self.email.setStyleSheet(u"font-size: 24px;\n"
"                width: 500px;\n"
"                height: 80px;\n"
"                border: none;\n"
"                border-bottom: 3px solid #000;\n"
"                background-color: #FAF9F6;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.homebutton.setText(QCoreApplication.translate("MainWindow", u"< Home", None))
        self.signuplabel.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.signupbutton.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.logforhaveaccbutton.setText(QCoreApplication.translate("MainWindow", u"Already have an account?", None))
        self.signfornoaccbutton.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
    # retranslateUi

