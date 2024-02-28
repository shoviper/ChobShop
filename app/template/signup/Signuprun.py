import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from ..login.Login_Signup_ui import *
# from .test import *
# from Signup import *
# from Login import *
# from app.logintest.Loginrun import *
from app.db.database import *

class SignupWindow(QMainWindow):
    def __init__(self):
        super(SignupWindow,self).__init__()
        self.ui = Ui_Login_Signup()
        self.ui.setupUi(self)
        
        self.ui.signupbutton.clicked.connect(self.register_check)
        self.ui.logforhaveaccbutton.clicked.connect(self.open_login_window)
        self.ui.homebutton.clicked.connect(self.go_to_homepage)

    def open_login_window(self):
        from app.template.login.Loginrun import LoginWindow
        # self.ui.stackedWidget.setCurrentWidget(self.ui.page1login)
        self.Login = LoginWindow()
        self.close()
        self.Login.show()

    def go_to_homepage(self):
        from app.template.homepage.Homepagerun import HomepageWindow
        self.home = HomepageWindow()
        self.close()
        self.home.show()

    
    def register_check(self):
        username = self.ui.username_signup.text()
        email = self.ui.email_signup.text()
        password = self.ui.password_signup.text()
#-------------------------------------------------------------
        # admin = False
        # if self.ui.checkbox.isChecked():
        #     admin = True
        #     registerAsAdmin(username, email, password)
        #     printAdminContent(username)
        #     self.show_success("User registered as Admin successfully")
#-------------------------------------------------------------
        if register(username, email, password):
            print("User registered successfully")
            print_database_contents(username)
            self.show_success("User registered successfully")
            self.open_login_window()
        else:
            print("User registration failed")
            self.show_error("User registration failed")


    def show_success(self, message):
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

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.register_check()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SignupWindow()
    window.show()
    sys.exit(app.exec())