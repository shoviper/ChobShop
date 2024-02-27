# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testloginsignup.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)
import app.assets.sourceimg.all

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #FAF9F6;")
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
        self.rightcontainer = QWidget(self.centralwidget)
        self.rightcontainer.setObjectName(u"rightcontainer")
        self.rightcontainer.setGeometry(QRect(900, 127, 893, 827))
        self.rightcontainer.setStyleSheet(u"border-radius: 20px;\n"
"background: #E1E3E7;")
        self.label = QLabel(self.rightcontainer)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-40, 0, 970, 827))
        self.label.setStyleSheet(u"image: url(:/pic/images/loginpic.png);")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(127, 127, 646, 827))
        self.page1login = QWidget()
        self.page1login.setObjectName(u"page1login")
        self.leftcontainer = QWidget(self.page1login)
        self.leftcontainer.setObjectName(u"leftcontainer")
        self.leftcontainer.setGeometry(QRect(0, 0, 646, 827))
        self.leftcontainer.setStyleSheet(u"background-color: #FAF9F6;")
        self.loginlabel = QLabel(self.leftcontainer)
        self.loginlabel.setObjectName(u"loginlabel")
        self.loginlabel.setGeometry(QRect(73, 36, 500, 95))
        self.loginlabel.setStyleSheet(u"color: #000;\n"
"                font-family: Inter;\n"
"                font-size: 48px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.loginbutton = QPushButton(self.leftcontainer)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setGeometry(QRect(73, 620, 500, 80))
        self.loginbutton.setStyleSheet(u"QPushButton {\n"
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
        self.noacclabel = QLabel(self.leftcontainer)
        self.noacclabel.setObjectName(u"noacclabel")
        self.noacclabel.setGeometry(QRect(80, 748, 493, 38))
        self.noacclabel.setStyleSheet(u"color: #CD4662;\n"
"                text-align: center;\n"
"                font-family: Inter;\n"
"                font-size: 20px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                margin-left: 100px;")
        self.username = QLineEdit(self.leftcontainer)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(73, 214, 500, 80))
        self.username.setStyleSheet(u"font-size: 24px;\n"
"                width: 500px;\n"
"                height: 80px;\n"
"                border: none;\n"
"                border-bottom: 3px solid #000;\n"
"                background-color: #FAF9F6;")
        self.password = QLineEdit(self.leftcontainer)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(73, 401, 500, 80))
        self.password.setStyleSheet(u"font-size: 24px;\n"
"                width: 500px;\n"
"                height: 80px;\n"
"                border: none;\n"
"                border-bottom: 3px solid #000;\n"
"                background-color: #FAF9F6;")
        self.checkbox = QCheckBox(self.leftcontainer)
        self.checkbox.setObjectName(u"checkbox")
        self.checkbox.setGeometry(QRect(547, 507, 26, 26))
        self.checkbox.setStyleSheet(u" QCheckBox {\n"
"                color: #CD4662;\n"
"            }\n"
"                           \n"
"            QCheckBox::indicator {\n"
"                border-radius: 3px;\n"
"                background-color: #F4DBDB;\n"
"                width: 26px;\n"
"                height: 26px;\n"
"                border: none;\n"
"            }\n"
"\n"
"            QCheckBox::indicator:checked {\n"
"                background-color: #CD4662;\n"
"            }\n"
"            QCheckBox::indicator:unchecked {\n"
"                background-color: #F4DBDB;\n"
"            }")
        self.adminlabel = QLabel(self.leftcontainer)
        self.adminlabel.setObjectName(u"adminlabel")
        self.adminlabel.setGeometry(QRect(73, 507, 454, 26))
        self.adminlabel.setStyleSheet(u"color: #CD4662;\n"
"                text-align: center;\n"
"                font-family: Inter;\n"
"                font-size: 18px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                margin-left: 310px;")
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
        self.stackedWidget.addWidget(self.page1login)
        self.page2signup = QWidget()
        self.page2signup.setObjectName(u"page2signup")
        self.leftcontainer_2 = QWidget(self.page2signup)
        self.leftcontainer_2.setObjectName(u"leftcontainer_2")
        self.leftcontainer_2.setGeometry(QRect(0, 0, 646, 827))
        self.leftcontainer_2.setStyleSheet(u"background-color: #FAF9F6;")
        self.signuplabel = QLabel(self.leftcontainer_2)
        self.signuplabel.setObjectName(u"signuplabel")
        self.signuplabel.setGeometry(QRect(73, 36, 500, 95))
        self.signuplabel.setStyleSheet(u"color: #000;\n"
"                font-family: Inter;\n"
"                font-size: 48px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.signupbutton = QPushButton(self.leftcontainer_2)
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
        self.logforhaveaccbutton = QLabel(self.leftcontainer_2)
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
        self.username_2 = QLineEdit(self.leftcontainer_2)
        self.username_2.setObjectName(u"username_2")
        self.username_2.setGeometry(QRect(73, 190, 500, 80))
        self.username_2.setStyleSheet(u"font-size: 24px;\n"
"                width: 500px;\n"
"                height: 80px;\n"
"                border: none;\n"
"                border-bottom: 3px solid #000;\n"
"                background-color: #FAF9F6;")
        self.password_2 = QLineEdit(self.leftcontainer_2)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setGeometry(QRect(73, 449, 500, 80))
        self.password_2.setStyleSheet(u"font-size: 24px;\n"
"                width: 500px;\n"
"                height: 80px;\n"
"                border: none;\n"
"                border-bottom: 3px solid #000;\n"
"                background-color: #FAF9F6;")
        self.signfornoaccbutton_2 = QPushButton(self.leftcontainer_2)
        self.signfornoaccbutton_2.setObjectName(u"signfornoaccbutton_2")
        self.signfornoaccbutton_2.setGeometry(QRect(400, 748, 80, 38))
        self.signfornoaccbutton_2.setStyleSheet(u"QPushButton {\n"
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
        self.email = QLineEdit(self.leftcontainer_2)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(73, 319, 500, 80))
        self.email.setStyleSheet(u"font-size: 24px;\n"
"                width: 500px;\n"
"                height: 80px;\n"
"                border: none;\n"
"                border-bottom: 3px solid #000;\n"
"                background-color: #FAF9F6;")
        self.stackedWidget.addWidget(self.page2signup)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.homebutton.setText(QCoreApplication.translate("MainWindow", u"< Home", None))
        self.label.setText("")
        self.loginlabel.setText(QCoreApplication.translate("MainWindow", u"Sign in", None))
        self.loginbutton.setText(QCoreApplication.translate("MainWindow", u"Sign in", None))
        self.noacclabel.setText(QCoreApplication.translate("MainWindow", u"Don't have an account?", None))
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username or Email address", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.checkbox.setText("")
        self.adminlabel.setText(QCoreApplication.translate("MainWindow", u"Log in as Admin", None))
        self.signfornoaccbutton.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.signuplabel.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.signupbutton.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.logforhaveaccbutton.setText(QCoreApplication.translate("MainWindow", u"Already have an account?", None))
        self.username_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.password_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.signfornoaccbutton_2.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
    # retranslateUi

