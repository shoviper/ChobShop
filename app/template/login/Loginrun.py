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
         
        self.ui.signfornoaccbutton.clicked.connect(self.open_signup_window)
        self.ui.logforhaveaccbutton.clicked.connect(self.open_login_window)
        self.ui.homebutton.clicked.connect(self.go_to_homepage)
        self.ui.signupbutton.clicked.connect(self.signup_window)
        self.ui.loginbutton.clicked.connect(self.login_window)

    def open_signup_window(self):
        print("opening Signup Window")
        self.ui.stackedWidget.setCurrentWidget(self.ui.Signuppage)

    def open_login_window(self):
        print("opening Login Window")
        self.ui.stackedWidget.setCurrentWidget(self.ui.Loginpage)

    def go_to_homepage(self):
        from app.template.homepage.Homepagerun import HomepageWindow
        self.home = HomepageWindow()
        self.close()
        self.home.show()

    def open_homepage(self):
        self.close()
        from app.template.homepage.Homepagerun import HomepageWindow
        self.homepagewindow = HomepageWindow()
        self.homepagewindow.show()
        
    def login_window(self):
        print("Logging in")
        admin = False
        if self.ui.admincheckbox.isChecked():
            admin = True

        username = self.ui.username_login.text()
        password = self.ui.password_login.text()
        
        if username == "" or password == "":
            self.show_error("Please fill all fields")
            return
        
        print("Username login: ", username)
        print("Password login: ", password)
        
        print("username_login login: ", self.ui.username_login.text())
        print(self.ui.username_login.text())
        print("password_login login: ", self.ui.password_login.text())

        if login(username, password, admin):
            print("Login Successful")
            self.show_success("Login successful, welcome")
            # print_all_users()
            self.open_homepage()
            
        else:
            print("Login Failed")
            self.ui.username_login.clear()
            self.ui.password_login.clear()
            # self.open_signup_window()
            self.show_error("Login failed, please try again")

    def signup_window(self):
        print("Signing up")
        username = self.ui.username_signup.text()
        email = self.ui.email_signup.text()
        password = self.ui.password_signup.text()
        
        if username == "" or email == "" or password == "":
            self.show_error("Please fill all fields")
            return
        
        if register(username, email, password):
            print("Signup Successful")
            self.show_success("Signup successful, welcome")
            # self.login_window(log="signup")
            admin = False
            if self.ui.admincheckbox.isChecked():
                admin = True
            
            if login(username, password, admin):
                print("Login Successful")
                # self.show_success("Login successful, welcome")
                self.open_homepage()
                return
            self.open_homepage()
        else:
            print("Signup Failed")
            self.ui.username_signup.clear()
            self.ui.email_signup.clear()
            self.ui.password_signup.clear()
            self.show_error("Username or Email already exists")

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
    
    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Return:
    #         self.login_window()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())