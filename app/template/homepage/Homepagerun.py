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
<<<<<<< Updated upstream

        if root.LoggedInUser.logged_in == False:
            self.ui.signinsignoutbutton.setText("Log in")
        else:   
            self.ui.signinsignoutbutton.setText(root.LoggedInUser.user.username)
            self.ui.profilebutton.clicked.connect(self.go_to_editprofile)

        self.ui.signinsignoutbutton.clicked.connect(self.back_to_login)
=======
        
>>>>>>> Stashed changes
        self.ui.exitbutton.clicked.connect(self.back_to_login)
        self.ui.homebutton.clicked.connect(self.go_to_home)
        self.ui.favbutton.clicked.connect(self.go_to_favorite)
        self.ui.orderbutton.clicked.connect(self.go_to_order)

<<<<<<< Updated upstream
    def go_to_order(self):
        from app.template.order.Orderrun import OrderWindow
        self.order = OrderWindow()
        self.close()
        self.order.show()
=======
    def applyHoverEffect(self):
        # Define the style sheet for the hover effect
        hover_style = """
            QPushButton#homebutton:hover {
                background-color: #BEC977; /* Change to the desired hover color */
            }
        """
        self.ui.homebutton.setStyleSheet(hover_style)
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
        carticon = self.ui.cartbutton_2.sizeHint()
        carticon.setHeight(40)
        carticon.setWidth(40)
        self.ui.cartbutton_2.setIconSize(carticon)

        self.ui.settingsbutton.setIcon(setpixmap)
        self.ui.exitbutton.setIcon(exitpixmap)
        self.ui.profile.setIcon(profilepixmap)
        self.ui.cartbutton_2.setIcon(cartpixmap)
>>>>>>> Stashed changes

    # def back_to_login(self):
    #     from app.template.newloginsignup.newlogsignrun import StackLoginSignup
    #     self.login = StackLoginSignup()
    #     # self.show_goodbye("Log out successful, See you again")
    #     self.close()
    #     self.login.show()
    def back_to_login(self):
        from app.template.login.Loginrun import LoginWindow
        self.login = LoginWindow()
        # self.show_goodbye("Log out successful, See you again")
        self.close()
        self.login.show()

    def go_to_home(self):
        from app.template.homepage.Homepagerun import HomepageWindow
        self.ui.stackedWidget.setCurrentWidget(self.ui.page1home)
        self.ui.homebutton.setStyleSheet(active_button_style)
        self.ui.favbutton.setStyleSheet(inactive_button_style)
        self.ui.orderbutton.setStyleSheet(inactive_button_style)
        self.ui.messbutton.setStyleSheet(inactive_button_style)

    def go_to_favorite(self):
        from app.template.favorite.Favoriterun import FavoriteWindow
        self.ui.stackedWidget.setCurrentWidget(self.ui.page2fav)
        
        self.ui.homebutton.setStyleSheet(inactive_button_style)
        self.ui.favbutton.setStyleSheet(active_button_style)
        print(active_button_style)
        self.ui.orderbutton.setStyleSheet(inactive_button_style)
        self.ui.messbutton.setStyleSheet(inactive_button_style)

    def go_to_editprofile(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.editprofile_page)
        # from app.template.profile.profilerun import Profile
        # self.profile = Profile()
        # self.close()
        # self.profile.show()
        
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
