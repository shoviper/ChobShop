# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProfileEdit.ui'
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
        MainWindow.resize(1921, 1080)
        MainWindow.setStyleSheet(u"background-color: #FAF9F6;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.container = QWidget(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(88, 87, 1782, 942))
        self.picprofile = QLabel(self.container)
        self.picprofile.setObjectName(u"picprofile")
        self.picprofile.setGeometry(QRect(49, 0, 250, 250))
        self.picprofile.setStyleSheet(u"image: url(:/pic/images/profile.png);\n"
"background-color: #CD4662;\n"
"border-radius: 50%;")
        self.nameprofile = QLabel(self.container)
        self.nameprofile.setObjectName(u"nameprofile")
        self.nameprofile.setGeometry(QRect(49, 286, 250, 71))
        self.nameprofile.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 40px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.nameprofile.setAlignment(Qt.AlignCenter)
        self.textboxcontainer = QWidget(self.container)
        self.textboxcontainer.setObjectName(u"textboxcontainer")
        self.textboxcontainer.setGeometry(QRect(390, 0, 1354, 906))
        self.textboxcontainer.setStyleSheet(u"border-radius: 20px;\n"
"background: #F4DBDB;\n"
"box-shadow: 0px 0px 50px 0px rgba(0, 0, 0, 0.25);")
        self.editprofilelabel = QLabel(self.textboxcontainer)
        self.editprofilelabel.setObjectName(u"editprofilelabel")
        self.editprofilelabel.setGeometry(QRect(63, 54, 244, 71))
        self.editprofilelabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 40px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.usernamelabel = QLabel(self.textboxcontainer)
        self.usernamelabel.setObjectName(u"usernamelabel")
        self.usernamelabel.setGeometry(QRect(63, 143, 244, 57))
        self.usernamelabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.firstnamelabel = QLabel(self.textboxcontainer)
        self.firstnamelabel.setObjectName(u"firstnamelabel")
        self.firstnamelabel.setGeometry(QRect(63, 308, 244, 57))
        self.firstnamelabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.lastnamelabel = QLabel(self.textboxcontainer)
        self.lastnamelabel.setObjectName(u"lastnamelabel")
        self.lastnamelabel.setGeometry(QRect(722, 308, 277, 57))
        self.lastnamelabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.genderlabel = QLabel(self.textboxcontainer)
        self.genderlabel.setObjectName(u"genderlabel")
        self.genderlabel.setGeometry(QRect(63, 473, 244, 57))
        self.genderlabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.birthdaylabel = QLabel(self.textboxcontainer)
        self.birthdaylabel.setObjectName(u"birthdaylabel")
        self.birthdaylabel.setGeometry(QRect(721, 473, 244, 57))
        self.birthdaylabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.phonelabel = QLabel(self.textboxcontainer)
        self.phonelabel.setObjectName(u"phonelabel")
        self.phonelabel.setGeometry(QRect(64, 638, 244, 57))
        self.phonelabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.emaillabel = QLabel(self.textboxcontainer)
        self.emaillabel.setObjectName(u"emaillabel")
        self.emaillabel.setGeometry(QRect(722, 638, 244, 57))
        self.emaillabel.setStyleSheet(u"color: #000;\n"
"\n"
"font-family: Suwannaphum;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.username = QLineEdit(self.textboxcontainer)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(63, 200, 569, 61))
        self.username.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.firstname = QLineEdit(self.textboxcontainer)
        self.firstname.setObjectName(u"firstname")
        self.firstname.setGeometry(QRect(63, 365, 569, 61))
        self.firstname.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.lastname = QLineEdit(self.textboxcontainer)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setGeometry(QRect(722, 365, 569, 61))
        self.lastname.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.gender = QLineEdit(self.textboxcontainer)
        self.gender.setObjectName(u"gender")
        self.gender.setGeometry(QRect(63, 530, 569, 61))
        self.gender.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.birthday = QLineEdit(self.textboxcontainer)
        self.birthday.setObjectName(u"birthday")
        self.birthday.setGeometry(QRect(722, 530, 569, 61))
        self.birthday.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.phone = QLineEdit(self.textboxcontainer)
        self.phone.setObjectName(u"phone")
        self.phone.setGeometry(QRect(63, 695, 569, 61))
        self.phone.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.email = QLineEdit(self.textboxcontainer)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(722, 695, 569, 61))
        self.email.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #CD4662;\n"
"background: #F4F2EF;\n"
"color: #545454;\n"
"font-family: Suwannaphum;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.savechangebutton = QPushButton(self.textboxcontainer)
        self.savechangebutton.setObjectName(u"savechangebutton")
        self.savechangebutton.setGeometry(QRect(974, 803, 317, 61))
        self.savechangebutton.setStyleSheet(u"color: #FFF;\n"
"background: #AEC289;\n"
"text-align: center;\n"
"font-family: Suwannaphum;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.backbutton = QPushButton(self.centralwidget)
        self.backbutton.setObjectName(u"backbutton")
        self.backbutton.setGeometry(QRect(47, 48, 21, 39))
        self.backbutton.setStyleSheet(u"background-color: #FAF9F6;\n"
"color: #CD4662;\n"
"font-size: 39px;\n"
"border: none;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.picprofile.setText("")
        self.nameprofile.setText(QCoreApplication.translate("MainWindow", u"User1", None))
        self.editprofilelabel.setText(QCoreApplication.translate("MainWindow", u"Edit profile", None))
        self.usernamelabel.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.firstnamelabel.setText(QCoreApplication.translate("MainWindow", u"First name", None))
        self.lastnamelabel.setText(QCoreApplication.translate("MainWindow", u"Last name", None))
        self.genderlabel.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.birthdaylabel.setText(QCoreApplication.translate("MainWindow", u"Birthday", None))
        self.phonelabel.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.emaillabel.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User1", None))
        self.firstname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"None", None))
        self.lastname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"None", None))
        self.gender.setPlaceholderText(QCoreApplication.translate("MainWindow", u"None", None))
        self.birthday.setPlaceholderText(QCoreApplication.translate("MainWindow", u"None", None))
        self.phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"None", None))
        self.email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User1@gmail.com", None))
        self.savechangebutton.setText(QCoreApplication.translate("MainWindow", u"Save changes", None))
        self.backbutton.setText(QCoreApplication.translate("MainWindow", u"<", None))
    # retranslateUi

