# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login_Signup.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Login_Signup(object):
    def setupUi(self, Login_Signup):
        if not Login_Signup.objectName():
            Login_Signup.setObjectName(u"Login_Signup")
        Login_Signup.resize(1280, 720)
        self.backgroundlabel = QLabel(Login_Signup)
        self.backgroundlabel.setObjectName(u"backgroundlabel")
        self.backgroundlabel.setGeometry(QRect(0, 0, 1291, 721))
        self.backgroundlabel.setStyleSheet(u"image: url(:/pic/realimages/realchop.png);\n"
"background-color: #FAF9F6;")
        self.backgroundlabel.setScaledContents(True)
        self.homebutton = QPushButton(Login_Signup)
        self.homebutton.setObjectName(u"homebutton")
        self.homebutton.setGeometry(QRect(20, 40, 172, 33))
        self.homebutton.setStyleSheet(u"QPushButton {\n"
"               color: #CD4662;\n"
"                font-family: Inter;\n"
"                font-size: 20px;\n"
"                font-style: normal;\n"
"                font-weight: 500;\n"
"                line-height: normal;\n"
"                border: none;\n"
"            }\n"
"            QPushButton:hover {\n"
"               color: #AEC289;\n"
"            }\n"
"")
        self.homebutton.setIconSize(QSize(20, 20))
        self.verticalLayoutWidget = QWidget(Login_Signup)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(90, 90, 431, 551))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.verticalLayoutWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Loginpage = QWidget()
        self.Loginpage.setObjectName(u"Loginpage")
        self.frame_login = QFrame(self.Loginpage)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setGeometry(QRect(-1, -1, 431, 551))
        self.frame_login.setStyleSheet(u"background-color: #FAF9F6;")
        self.frame_login.setFrameShape(QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QFrame.Raised)
        self.signuplabel = QLabel(self.frame_login)
        self.signuplabel.setObjectName(u"signuplabel")
        self.signuplabel.setGeometry(QRect(0, 0, 431, 91))
        self.signuplabel.setStyleSheet(u"color: #000;\n"
"                font-family: Inter;\n"
"                font-size: 40px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.username_login = QLineEdit(self.frame_login)
        self.username_login.setObjectName(u"username_login")
        self.username_login.setGeometry(QRect(0, 140, 431, 61))
        self.username_login.setStyleSheet(u"font-size: 20px;\n"
"                width: 500px;\n"
"                height: 80px;\n"
"                border: none;\n"
"                border-bottom: 2px solid #000;\n"
"                background-color: #FAF9F6;")
        self.password_login = QLineEdit(self.frame_login)
        self.password_login.setObjectName(u"password_login")
        self.password_login.setGeometry(QRect(0, 260, 431, 61))
        self.password_login.setStyleSheet(u"font-size: 20px;\n"
"                width: 500px;\n"
"                height: 80px;\n"
"                border: none;\n"
"                border-bottom: 2px solid #000;\n"
"                background-color: #FAF9F6;")
        self.signfornoacclabel = QLabel(self.frame_login)
        self.signfornoacclabel.setObjectName(u"signfornoacclabel")
        self.signfornoacclabel.setGeometry(QRect(0, 500, 421, 51))
        self.signfornoacclabel.setStyleSheet(u"color: #CD4662;\n"
"                text-align: center;\n"
"                font-family: Inter;\n"
"                font-size: 16px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                margin-left: 80px;")
        self.loginbutton = QPushButton(self.frame_login)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setGeometry(QRect(0, 420, 431, 51))
        self.loginbutton.setStyleSheet(u"QPushButton {\n"
"                background-color: #CD4662;\n"
"                color: #FFF;\n"
"                text-align: center;\n"
"                font-family: Inter;\n"
"                font-size: 20px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;\n"
"                border-radius: 10px;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #AEC289;\n"
"            }")
        self.signfornoaccbutton = QPushButton(self.frame_login)
        self.signfornoaccbutton.setObjectName(u"signfornoaccbutton")
        self.signfornoaccbutton.setGeometry(QRect(280, 510, 61, 31))
        self.signfornoaccbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.signfornoaccbutton.setStyleSheet(u"QPushButton {\n"
"                border: none;\n"
"                color: #AEC289;\n"
"                font-family: Inter;\n"
"                font-size: 16px;\n"
"                font-style: bold;\n"
"                font-weight: 700;\n"
"                border: none;\n"
"                line-height: normal;\n"
"            }\n"
"                           \n"
"            QPushButton:hover {\n"
"                color: #CD4662;\n"
"            }")
        self.admincheckbox = QCheckBox(self.frame_login)
        self.admincheckbox.setObjectName(u"admincheckbox")
        self.admincheckbox.setGeometry(QRect(410, 340, 20, 20))
        self.admincheckbox.setStyleSheet(u" QCheckBox {\n"
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
        self.adminlabel = QLabel(self.frame_login)
        self.adminlabel.setObjectName(u"adminlabel")
        self.adminlabel.setGeometry(QRect(-30, 340, 431, 21))
        self.adminlabel.setStyleSheet(u"color: #CD4662;\n"
"                text-align: center;\n"
"                font-family: Inter;\n"
"                font-size: 16px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                margin-left: 310px;")
        self.stackedWidget.addWidget(self.Loginpage)
        self.Signuppage = QWidget()
        self.Signuppage.setObjectName(u"Signuppage")
        self.frame_signup = QFrame(self.Signuppage)
        self.frame_signup.setObjectName(u"frame_signup")
        self.frame_signup.setGeometry(QRect(-1, -1, 431, 551))
        self.frame_signup.setStyleSheet(u"background-color: rgb(250, 249, 246);")
        self.frame_signup.setFrameShape(QFrame.StyledPanel)
        self.frame_signup.setFrameShadow(QFrame.Raised)
        self.username_signup = QLineEdit(self.frame_signup)
        self.username_signup.setObjectName(u"username_signup")
        self.username_signup.setGeometry(QRect(0, 110, 431, 61))
        self.username_signup.setStyleSheet(u"font-size: 20px;\n"
"                width: 500px;\n"
"                height: 80px;\n"
"                border: none;\n"
"                border-bottom: 2px solid #000;\n"
"                background-color: #FAF9F6;")
        self.email_signup = QLineEdit(self.frame_signup)
        self.email_signup.setObjectName(u"email_signup")
        self.email_signup.setGeometry(QRect(0, 200, 431, 61))
        self.email_signup.setStyleSheet(u"font-size: 20px;\n"
"                width: 500px;\n"
"                height: 80px;\n"
"                border: none;\n"
"                border-bottom: 2px solid #000;\n"
"                background-color: #FAF9F6;")
        self.password_signup = QLineEdit(self.frame_signup)
        self.password_signup.setObjectName(u"password_signup")
        self.password_signup.setGeometry(QRect(0, 300, 431, 61))
        self.password_signup.setStyleSheet(u"font-size: 20px;\n"
"                width: 500px;\n"
"                height: 80px;\n"
"                border: none;\n"
"                border-bottom: 2px solid #000;\n"
"                background-color: #FAF9F6;")
        self.logforhaveacclabel = QLabel(self.frame_signup)
        self.logforhaveacclabel.setObjectName(u"logforhaveacclabel")
        self.logforhaveacclabel.setGeometry(QRect(0, 500, 421, 51))
        self.logforhaveacclabel.setStyleSheet(u"color: #CD4662;\n"
"                text-align: center;\n"
"                font-family: Inter;\n"
"                font-size: 16px;\n"
"                font-style: normal;\n"
"                font-weight: 400;\n"
"                line-height: normal;\n"
"                margin-left: 80px;")
        self.signupbutton = QPushButton(self.frame_signup)
        self.signupbutton.setObjectName(u"signupbutton")
        self.signupbutton.setGeometry(QRect(0, 420, 431, 51))
        self.signupbutton.setStyleSheet(u"QPushButton {\n"
"                background-color: #CD4662;\n"
"                color: #FFF;\n"
"                text-align: center;\n"
"                font-family: Inter;\n"
"                font-size: 20px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;\n"
"                border-radius: 10px;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #AEC289;\n"
"            }")
        self.logforhaveaccbutton = QPushButton(self.frame_signup)
        self.logforhaveaccbutton.setObjectName(u"logforhaveaccbutton")
        self.logforhaveaccbutton.setGeometry(QRect(280, 510, 61, 31))
        self.logforhaveaccbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.logforhaveaccbutton.setStyleSheet(u"QPushButton {\n"
"                border: none;\n"
"                color: #AEC289;\n"
"                font-family: Inter;\n"
"                font-size: 16px;\n"
"                font-style: bold;\n"
"                font-weight: 700;\n"
"                border: none;\n"
"                line-height: normal;\n"
"            }\n"
"                           \n"
"            QPushButton:hover {\n"
"                color: #CD4662;\n"
"            }")
        self.loginlabel = QLabel(self.frame_signup)
        self.loginlabel.setObjectName(u"loginlabel")
        self.loginlabel.setGeometry(QRect(0, 0, 431, 91))
        self.loginlabel.setStyleSheet(u"color: #000;\n"
"                font-family: Inter;\n"
"                font-size: 40px;\n"
"                font-style: normal;\n"
"                font-weight: 700;\n"
"                line-height: normal;")
        self.stackedWidget.addWidget(self.Signuppage)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(Login_Signup)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Login_Signup)
    # setupUi

    def retranslateUi(self, Login_Signup):
        Login_Signup.setWindowTitle(QCoreApplication.translate("Login_Signup", u"Form", None))
        self.backgroundlabel.setText("")
        self.homebutton.setText(QCoreApplication.translate("Login_Signup", u"<   Home", None))
        self.signuplabel.setText(QCoreApplication.translate("Login_Signup", u"Login", None))
        self.username_login.setPlaceholderText(QCoreApplication.translate("Login_Signup", u"Username or Email", None))
        self.password_login.setPlaceholderText(QCoreApplication.translate("Login_Signup", u"Password", None))
        self.signfornoacclabel.setText(QCoreApplication.translate("Login_Signup", u"Don't have an account?", None))
        self.loginbutton.setText(QCoreApplication.translate("Login_Signup", u"Log in", None))
        self.signfornoaccbutton.setText(QCoreApplication.translate("Login_Signup", u"Sign up", None))
        self.admincheckbox.setText("")
        self.adminlabel.setText(QCoreApplication.translate("Login_Signup", u"Log in as Admin", None))
        self.email_signup.setPlaceholderText(QCoreApplication.translate("Login_Signup", u"Email", None))
        self.password_signup.setPlaceholderText(QCoreApplication.translate("Login_Signup", u"Password", None))
        self.logforhaveacclabel.setText(QCoreApplication.translate("Login_Signup", u"Already have an account?", None))
        self.signupbutton.setText(QCoreApplication.translate("Login_Signup", u"Sign up", None))
        self.logforhaveaccbutton.setText(QCoreApplication.translate("Login_Signup", u"Log in", None))
        self.loginlabel.setText(QCoreApplication.translate("Login_Signup", u"Sign up", None))
        self.username_signup.setPlaceholderText(QCoreApplication.translate("Login_Signup", u"Username", None))
    # retranslateUi

