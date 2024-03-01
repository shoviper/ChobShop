import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap
# from Homepage import Ui_MainWindow
from .Homepage_newres_ui import *
from app.template.order.Orderrun import *
from app.db.database import *
# from .Homepagdsadse import *

# import app.assets.realsourceimg.real

active_button_style = """
    QPushButton{
        color: #FAF9F6;
        font-family: Suwannaphum;
        font-size: 16px;
        font-style: normal;
        font-weight: 500;
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
    QPushButton{
        color: #000;
        font-family: Suwannaphum;
        font-size: 16px;
        font-style: normal;
        font-weight: 500;
        line-height: normal;
        background-color: #E1E3E7;
        border-radius: 10px;
    }
    QPushButton:hover {
        background-color: #F4DBDB;
        color: black;
    }
"""


#order
inactive_orderbutton_style = """
    QPushButton{
        color: #545454;
        text-align: center;
        font-family: Suwannaphum;
        font-size: 20px;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
        border: none;
    }
    QPushButton:hover{
        background-color: #F4DBDB;
        color: #545454;
    }
"""

active_orderbutton_style = """
    QPushButton{
        color: #CD4662;
        text-align: center;
        font-family: Suwannaphum;
        font-size: 20px;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
        border: none;
        border-bottom: 3px solid #CD4662;
    }
    QPushButton:hover{
        background-color: #F4DBDB;
        color: #545454;
        border: none;
    }
"""

class HomepageWindow(QMainWindow):
    def __init__(self):
        super(HomepageWindow, self).__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        if root.LoggedInUser.logged_in == False:
            self.ui.loginsignoutbutton.setText("Log in")
            self.ui.profilebutton.clicked.connect(lambda: self.show_error("Please log in to view profile"))
            self.ui.loginsignoutbutton.clicked.connect(self.back_to_login)
        else:   
            print(root.LoggedInUser.user.username.title())
            self.ui.loginsignoutbutton.setText(root.LoggedInUser.user.username)
            self.ui.profilebutton.clicked.connect(self.go_to_userprofile)
            self.ui.loginsignoutbutton.clicked.connect(self.go_to_userprofile)
            
        #stackmain
        self.ui.exitbutton.clicked.connect(self.back_to_login)
        self.ui.homebutton.clicked.connect(self.go_to_home)
        self.ui.favbutton.clicked.connect(self.go_to_favorite)
        self.ui.orderbutton.clicked.connect(self.go_to_order)

        #orderpage
        self.ui.tobeshippedbutton.clicked.connect(self.go_to_order_ship)
        self.ui.toberecievedbutton.clicked.connect(self.go_to_order_receive)
        self.ui.completedbutton.clicked.connect(self.go_to_order_complete)

        #editprofile
        self.ui.backbutton_2.clicked.connect(self.go_to_userprofile)

        #profile
        self.ui.editprofilebutton.clicked.connect(self.go_to_usereditprofile)
        self.ui.backbutton.clicked.connect(self.go_to_home)
        self.ui.tobeshipbutton.clicked.connect(self.go_to_order)
        self.ui.tobereceivebutton.clicked.connect(self.go_to_order_receive)
        self.ui.completebutton.clicked.connect(self.go_to_order_complete)

    def back_to_login(self):
        print(root.LoggedInUser.logged_in)
        if root.LoggedInUser.logged_in == True:
            if self.show_yes_no("Are you sure you want to log out?") == QMessageBox.Yes:
                from app.template.login.Loginrun import LoginWindow
                self.login = LoginWindow()
                self.close()
                self.login.show()
        else:
            from app.template.login.Loginrun import LoginWindow
            self.login = LoginWindow()
            self.close()
            self.login.show()
    
    # def back_to_login(self):
    #     from app.template.login.Loginrun import LoginWindow
    #     self.login = LoginWindow()
    #     # self.show_goodbye("Log out successful, See you again")
    #     self.close()
    #     self.login.show()

    def go_to_home(self):
        print("go to home")
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.homepage)
        self.ui.homebutton.setStyleSheet(active_button_style)
        self.ui.favbutton.setStyleSheet(inactive_button_style)
        self.ui.orderbutton.setStyleSheet(inactive_button_style)
        self.ui.messbutton.setStyleSheet(inactive_button_style)

    def go_to_favorite(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.favpage)
        
        self.ui.homebutton.setStyleSheet(inactive_button_style)
        self.ui.favbutton.setStyleSheet(active_button_style)
        self.ui.orderbutton.setStyleSheet(inactive_button_style)
        self.ui.messbutton.setStyleSheet(inactive_button_style)

    def go_to_userprofile(self):
        print("go to profile")
        self.ui.stackedWidget.setCurrentWidget(self.ui.userprofile)
        self.ui.usernamelabel.setText(root.LoggedInUser.user.username.title())

    def go_to_usereditprofile(self):
        self.ui.editnameprofile.setText(root.LoggedInUser.user.username.title())
        self.ui.userbox.setText(root.LoggedInUser.user.username.title())
        self.ui.firstnamebox.setText(root.LoggedInUser.user.name)
        self.ui.lastnamebox.setText(root.LoggedInUser.user.surname)
        self.ui.genderbox.setText(root.LoggedInUser.user.gender)
        self.ui.birthdaydateEdit.setDate(root.LoggedInUser.user.birthday)
        self.ui.emailbox.setText(root.LoggedInUser.user.email)
        self.ui.phonebox.setText(root.LoggedInUser.user.phone)
        self.ui.stackedWidget.setCurrentWidget(self.ui.editprofile)

    def go_to_order(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.myorderspage)
        self.ui.homebutton.setStyleSheet(inactive_button_style)
        self.ui.favbutton.setStyleSheet(inactive_button_style)
        self.ui.orderbutton.setStyleSheet(active_button_style)
        self.ui.messbutton.setStyleSheet(inactive_button_style)

    def go_to_order_ship(self):
        self.ui.tobeshippedbutton.setStyleSheet(active_orderbutton_style)
        self.ui.toberecievedbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.completedbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.stackedWidget_myorders.setCurrentWidget(self.ui.tobeshippedpage)

    def go_to_order_receive(self):
        self.ui.toberecievedbutton.setStyleSheet(active_orderbutton_style)
        self.ui.tobeshippedbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.completedbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.stackedWidget_myorders.setCurrentWidget(self.ui.toberecievedpage)

    def go_to_order_complete(self):
        self.ui.completedbutton.setStyleSheet(active_orderbutton_style)
        self.ui.tobeshippedbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.toberecievedbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.stackedWidget_myorders.setCurrentWidget(self.ui.completedpage)

    def show_yes_no(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText(message)
        msg.setWindowTitle("Log out")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.exec()
        return msg.result()
        
    def show_goodbye(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Login Succesful")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
    
    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("Login Error")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomepageWindow()
    window.show()
    sys.exit(app.exec())
