# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)

        #main widget
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        #----------------------------------------left widget#----------------------------------------
        #container
        self.leftcontainer = QWidget(self.centralwidget)
        self.leftcontainer.setObjectName(u"leftcontainer")
        self.leftcontainer.setGeometry(QRect(127, 127, 646, 827))
        #login label name
        self.loginlabel = QLabel(self.leftcontainer)
        self.loginlabel.setObjectName(u"loginlabel")
        self.loginlabel.setGeometry(QRect(73, 36, 500, 95))
        #login button
        self.loginbutton = QPushButton(self.leftcontainer)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setGeometry(QRect(73, 620, 500, 80))
        #no account label name
        self.noacclabel = QLabel(self.leftcontainer)
        self.noacclabel.setObjectName(u"noacclabel")
        self.noacclabel.setGeometry(QRect(80, 748, 493, 38))
        #go to sign up page for no account
        self.signfornoaccbutton = QPushButton(self.leftcontainer)
        self.signfornoaccbutton.setObjectName(u"signfornoaccbutton")
        self.signfornoaccbutton.setGeometry(QRect(80 * 5, 748, 493, 38))
        #username textbox
        self.username = QLineEdit(self.leftcontainer)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(73, 214, 500, 80))
        self.username.setPlaceholderText("Username or Email address")
        #password textbox
        self.password = QLineEdit(self.leftcontainer)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(73, 401, 500, 80))
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        #checkbox for admin
        self.checkbox = QCheckBox(self.leftcontainer)
        self.checkbox.setObjectName(u"checkbox")
        self.checkbox.setGeometry(QRect(547, 507, 26, 26))
        #log in as admin label name
        self.adminlabel = QLabel(self.leftcontainer)
        self.adminlabel.setObjectName(u"adminlabel")
        self.adminlabel.setGeometry(QRect(73, 507, 454, 26))
        #----------------------------------------left widget#----------------------------------------


        #----------------------------------------right widget#----------------------------------------
        #container
        self.rightcontainer = QWidget(self.centralwidget)
        self.rightcontainer.setObjectName(u"rightcontainer")
        self.rightcontainer.setGeometry(QRect(900, 127, 893, 827))
        #picture
        self.picture = QWidget(self.rightcontainer)
        self.picture.setObjectName(u"picture")
        self.picture.setGeometry(QRect(0, 0, 893, 549))
        #----------------------------------------right widget#----------------------------------------


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
        self.loginlabel.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.loginbutton.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.noacclabel.setText(QCoreApplication.translate("MainWindow", u"Don't have an account?", None))
        self.signfornoaccbutton.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.checkbox.setText("")
        self.adminlabel.setText(QCoreApplication.translate("MainWindow", u"Log in as Admin", None))
    # retranslateUi

