import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap
# from Homepage import Ui_MainWindow
from .Homepage import *

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
            QPushButton#settingsbutton{
                border: None;
            }
            QPushButton#exitbutton{
                border: None;
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

        self.ui.settingsbutton.setIcon(setpixmap)
        self.ui.exitbutton.setIcon(exitpixmap)

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
