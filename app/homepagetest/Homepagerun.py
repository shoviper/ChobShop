import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap
# from Homepage import Ui_MainWindow
from .Homepage import *
# from .Homepagdsadse import *

class HomepageWindow(QMainWindow):
    def __init__(self):
        super(HomepageWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setStyleSheet("""
            QLabel#label{
                font-family: Supermercado;
                font-size: 64px;
                font-weight: 400;
                line-height: 77px;
                letter-spacing: 0em;
                text-align: center;
                color: #000000;
            }
            QWidget#menu{
                background-color: #FAF9F6;
            }
            QPushButton#homebutton{
                font-family: Suwannaphum;
                font-size: 24px;
                font-weight: 700;
                line-height: 43px;
                letter-spacing: 0em;
                text-align: middle;
                color: #ffffff;
                background-color: #AEC289;
                border-radius: 10px;
            }
            QPushButton#homebutton:hover{
                background-color: #000;
                color: #E1E3E7;
            }
            QPushButton#favbutton{
                color: #000;
                font-family: Suwannaphum;
                font-size: 24px;
                font-style: normal;
                font-weight: 400;
                line-height: normal;
                background-color: #E1E3E7;
                border-radius: 10px;
            }
            QPushButton#favbutton:hover{
                background-color: #ffffff;
                color: #000;
            }
            QPushButton#orderbutton{
                color: #000;
                font-family: Suwannaphum;
                font-size: 24px;
                font-style: normal;
                font-weight: 400;
                line-height: normal;
                background-color: #E1E3E7;
                border-radius: 10px;
            }
            QPushButton#orderbutton:hover{
                background-color: #ffffff;
                color: #000;
            }
            QPushButton#messbutton{
                color: #000;
                font-family: Suwannaphum;
                font-size: 24px;
                font-style: normal;
                font-weight: 400;
                line-height: normal;
                background-color: #E1E3E7;
                border-radius: 10px;
            }
            QPushButton#messbutton:hover{
                background-color: #ffffff;
                color: #000;
            }
            QPushButton#settingsbutton {
                border: None;
            }
            QPushButton#exitbutton {
                border: None;
            }
            QLineEdit#search{
                border-radius: 50px;
                background-color: #fff;
                color: #CD4662;
                font-family: Suwannaphum;
                font-size: 24px;
                font-style: normal;
                font-weight: 400;
                line-height: normal;
            }
            QPushButton#profilebutton {
                border: None;
            }
            QPushButton#cartbutton {
                border: None;
            }
            QPushButton#signinsignoutbutton{
                color: #000;
                text-align: right;
                font-family: Suwannaphum;
                font-size: 32px;
                font-style: normal;
                font-weight: 400;
                line-height: normal;
                border: none;
                margin-bottom: 15px;
            }
            QPushButton#stylelabbutton{
                color: #FFF;
                text-align: center;
                font-family: Supermercado;
                font-size: 96px;
                font-style: normal;
                font-weight: 400;
                line-height: normal;
                border-radius: 10px;
                background-color: #CD4662;
            }
            QPushButton#newarrivalbutton,  QPushButton#onsalebutton,  QPushButton#bestsellbutton, QPushButton#buyagainbutton{
                border-radius: 10px;
                border: 2px solid #000;
                opacity: 0.2;
                background-color: #F7F2EB;
                color: #545454;
                text-align: center;
                font-family: Suwannaphum;
                font-size: 32px;
                font-style: normal;
                font-weight: 400;
                line-height: normal;
            }
            QLabel#suggestlabel {
                color: #545454;
                text-align: center;
                font-family: Suwannaphum;
                font-size: 40px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            }
            QWidget#container1, QWidget#container2, QWidget#container3, QWidget#container4, QWidget#container5, QWidget#container6{
                border-radius: 10px;
                background: #D9D9D9;
            }
        """)

        self.ui.exitbutton.clicked.connect(self.back_to_login)
        self.set_button_icon()

    def set_button_icon(self):
        setpixmap = QPixmap("app/assets/images/settings.png")
        seticon = self.ui.settingsbutton.sizeHint()
        seticon.setHeight(40)
        seticon.setWidth(40)
        self.ui.settingsbutton.setIconSize(seticon)
        
        exitpixmap = QPixmap("app/assets/images/exit.png")
        exiticon = self.ui.exitbutton.sizeHint()
        exiticon.setHeight(40)
        exiticon.setWidth(40)
        self.ui.exitbutton.setIconSize(exiticon)

        profilepixmap = QPixmap("app/assets/images/profile.png")
        profileicon = self.ui.profilebutton.sizeHint()
        profileicon.setHeight(40)
        profileicon.setWidth(40)
        self.ui.profilebutton.setIconSize(profileicon)

        cartpixmap = QPixmap("app/assets/images/cart.png")
        carticon = self.ui.cartbutton.sizeHint()
        carticon.setHeight(40)
        carticon.setWidth(40)
        self.ui.cartbutton.setIconSize(carticon)

        self.ui.settingsbutton.setIcon(setpixmap)
        self.ui.exitbutton.setIcon(exitpixmap)
        self.ui.profilebutton.setIcon(profilepixmap)
        self.ui.cartbutton.setIcon(cartpixmap)

    def back_to_login(self):
        from app.logintest.Loginrun import LoginWindow
        self.login = LoginWindow()
        self.show_goodbye("Log out successful, See you again")
        self.close()
        self.login.show()

    def show_goodbye(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Login Succesful")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomepageWindow()
    window.show()
    sys.exit(app.exec())
