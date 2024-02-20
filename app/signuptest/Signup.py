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
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

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
        #signup label name
        self.signuplabel = QLabel(self.leftcontainer)
        self.signuplabel.setObjectName(u"signuplabel")
        self.signuplabel.setGeometry(QRect(73, 36, 500, 95))
        #signup button
        self.signupbutton = QPushButton(self.leftcontainer)
        self.signupbutton.setObjectName(u"signupbutton")
        self.signupbutton.setGeometry(QRect(73, 620, 500, 80))
        #already have account label name
        self.haveacclabel = QLabel(self.leftcontainer)
        self.haveacclabel.setObjectName(u"haveacclabel")
        self.haveacclabel.setGeometry(QRect(80, 748, 493, 38))
        #go to log in page for no account
        self.logforhaveaccbutton = QPushButton(self.leftcontainer)
        self.logforhaveaccbutton.setObjectName(u"logforhaveaccbutton")
        self.logforhaveaccbutton.setGeometry(QRect(80 * 5, 748, 493, 38))
        #email textbox
        self.email = QLineEdit(self.leftcontainer)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(73, 319, 500, 80))
        self.email.setPlaceholderText("Email")
        #password textbox
        self.password = QLineEdit(self.leftcontainer)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(73, 449, 500, 80))
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        #username
        self.username = QLineEdit(self.leftcontainer)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(73, 190, 500, 80))
        self.username.setPlaceholderText("Username")
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
<<<<<<< HEAD
        self.signuplabel.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.signupbutton.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.haveacclabel.setText(QCoreApplication.translate("MainWindow", u"Already have an account?", None))
        self.logforhaveaccbutton.setText(QCoreApplication.translate("MainWindow", u"Sign in", None))
=======
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Already have an account?", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
>>>>>>> 29c573862955d8e70ee85b469088afadeae4a0ac
    # retranslateUi

