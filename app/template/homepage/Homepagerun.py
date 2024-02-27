import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap
# from Homepage import Ui_MainWindow
from .Homepage import *
from app.db.database import *
# from .Homepagdsadse import *

active_button_style = """
    QPushButton {
        color: #FAF9F6;
        font-family: Suwannaphum;
        font-size: 24px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        background-color: #AEC289;
        border-radius: 10px;
    }
    QPushButton:hover {
        background-color: #F4DBDB;
        color: black;
    }
"""

inactive_button_style = """
    QPushButton {
        color: #000;
        font-family: Suwannaphum;
        font-size: 24px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        background-color: #E1E3E7;
        border-radius: 10px;
    }
    QPushButton:hover {
        background-color: #F4DBDB;
        color: black;
    }
"""


class HomepageWindow(QMainWindow):
    def __init__(self):
        super(HomepageWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        if root.LoggedInUser.logged_in == False:
            self.ui.signinsignoutbutton.setText("Log in")
        else:   
            self.ui.signinsignoutbutton.setText(root.LoggedInUser.user.username)

        self.ui.signinsignoutbutton.clicked.connect(self.back_to_login)
        self.ui.exitbutton.clicked.connect(self.back_to_login)
        self.ui.favbutton.clicked.connect(self.go_to_favorite)
        self.ui.orderbutton.clicked.connect(self.go_to_order)

    def go_to_order(self):
        from app.template.order.Orderrun import OrderWindow
        self.order = OrderWindow()
        self.close()
        self.order.show()

    def back_to_login(self):
        from app.template.login.Loginrun import LoginWindow
        self.login = LoginWindow()
        # self.show_goodbye("Log out successful, See you again")
        self.close()
        self.login.show()

    def go_to_favorite(self):
        from app.template.favorite.Favoriterun import FavoriteWindow
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

        favbutton_style = self.ui.favbutton.styleSheet()

    def go_to_favorite(self):
        from app.template.favorite.Favoriterun import FavoriteWindow
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        
        self.ui.homebutton.setStyleSheet(inactive_button_style)
        self.ui.favbutton.setStyleSheet(active_button_style)
        print(active_button_style)
        self.ui.orderbutton.setStyleSheet(inactive_button_style)
        self.ui.messbutton.setStyleSheet(inactive_button_style)
        
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
