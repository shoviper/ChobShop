import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap
# from Homepage import Ui_MainWindow
from .Favorite import *
from app.db.database import *
# from .Homepagdsadse import *

class FavoriteWindow(QMainWindow):
    def __init__(self):
        super(FavoriteWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        if root.LoggedInUser.logged_in == False:
            self.ui.signinsignoutbutton.setText("Log in")
        else:
            self.ui.signinsignoutbutton.setText(root.LoggedInUser.user.username)


        self.ui.signinsignoutbutton.clicked.connect(self.back_to_login)
        self.ui.exitbutton.clicked.connect(self.back_to_login)
        self.ui.orderbutton.clicked.connect(self.go_to_order)
        self.ui.homebutton.clicked.connect(self.go_to_homepage)

    def go_to_order(self):
        from app.template.order.Orderrun import OrderWindow
        self.order = OrderWindow()
        self.close()
        self.order.show()
    
    def go_to_homepage(self):
        from app.template.homepage.Homepagerun import HomepageWindow
        self.home = HomepageWindow()
        self.close()
        self.home.show()

    def back_to_login(self):
        from app.template.login.Loginrun import LoginWindow
        self.login = LoginWindow()
        # self.show_goodbye("Log out successful, See you again")
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
