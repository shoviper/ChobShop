import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap
# from Homepage import Ui_MainWindow
from .Favorite import *
# from .Homepagdsadse import *

class FavoriteWindow(QMainWindow):
    def __init__(self):
        super(FavoriteWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setStyleSheet("""
                            QPushButton {
                                background-color: #FFFFFF;
                                border: black;
                            }
                           
                            QPushButton:hover {
                                background-color: #F4DBDB;
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
        profileicon = self.ui.profile.sizeHint()
        profileicon.setHeight(40)
        profileicon.setWidth(40)
        self.ui.profile.setIconSize(profileicon)

        cartpixmap = QPixmap("app/assets/images/cart.png")
        carticon = self.ui.cartbutton.sizeHint()
        carticon.setHeight(40)
        carticon.setWidth(40)
        self.ui.cartbutton.setIconSize(carticon)

        self.ui.settingsbutton.setIcon(setpixmap)
        self.ui.exitbutton.setIcon(exitpixmap)
        self.ui.profile.setIcon(profilepixmap)
        self.ui.cartbutton.setIcon(cartpixmap)

    def back_to_login(self):
        from app.template.login.Loginrun import LoginWindow
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
    window = FavoriteWindow()
    window.show()
    sys.exit(app.exec())
