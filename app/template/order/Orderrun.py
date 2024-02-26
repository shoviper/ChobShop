import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap
# from Homepage import Ui_MainWindow
# from .Ordertoberecieved import *
# from .Ordertobeshipped import *
from .Ordercompleted import *
from app.db.database import *
# from .Homepagdsadse import *

class OrderWindow(QMainWindow):
    def __init__(self):
        super(OrderWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        if root.LoggedInUser.logged_in == False:
            self.ui.signinsignoutbutton.setText("Log in")
        else:
            self.ui.signinsignoutbutton.setText(root.LoggedInUser.user.username)

        self.ui.signinsignoutbutton.clicked.connect(self.back_to_login)
        self.ui.exitbutton.clicked.connect(self.back_to_login)
        self.ui.favbutton.clicked.connect(self.go_to_favorite)
        self.ui.homebutton.clicked.connect(self.go_to_homepage)

        
    def back_to_login(self):
        from app.template.login.Loginrun import LoginWindow
        self.login = LoginWindow()
        # self.show_goodbye("Log out successful, See you again")
        self.close()
        self.login.show()

    def go_to_homepage(self):
        from app.template.homepage.Homepagerun import HomepageWindow
        self.home = HomepageWindow()
        self.close()
        self.home.show()

    def go_to_favorite(self):
        from app.template.favorite.Favoriterun import FavoriteWindow
        self.fav = FavoriteWindow()
        self.close()
        self.fav.show()
        
    def show_goodbye(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Login Succesful")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OrderWindow()
    window.show()
    sys.exit(app.exec())