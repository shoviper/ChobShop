import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from .Login_Signup_ui import *
# from Login import *
# from app.signuptest.Signuprun import *
from app.db.database import *

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow,self).__init__()
        self.ui = Ui_Login_Signup()
        self.ui.setupUi(self)
        
        self.ui.loginbutton.clicked.connect(self.login_window) 
        self.ui.signfornoaccbutton.clicked.connect(self.open_signup_window) 
        self.ui.homebutton.clicked.connect(self.go_to_homepage)

    
    def open_signup_window(self):
        self.close()
        from app.template.signup.Signuprun import SignupWindow
        self.signup = SignupWindow()
        self.signup.show()

    def go_to_homepage(self):
        from app.template.homepage.Homepagerun import HomepageWindow
        self.home = HomepageWindow()
        self.close()
        self.home.show()

    def open_homepage(self):
        self.close()
        from app.template.homepage.Homepagerun import HomepageWindow
        self.login_window = HomepageWindow()
        self.login_window.show()
        
    def login_window(self):
        username = self.ui.username_login.text()
        password = self.ui.password_login.text()
        admin = False
        if self.ui.admincheckbox.isChecked():
            admin = True
        if login(username, password, admin):
            print("Login Successful")
            self.show_success("Login successful, welcome")
            self.open_homepage()
            
        else:
            print("Login Failed")
            self.ui.username_login.clear()
            self.ui.password_login.clear()
            # self.open_signup_window()
            self.show_error("Login failed, please try again")

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
            self.login_window()
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())