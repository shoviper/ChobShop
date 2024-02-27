import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from app.template.newloginsignup.Stackloginsignup import *
from app.db.database import *

class StackLoginSignup(QMainWindow):
    def __init__(self):
        super(StackLoginSignup,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.signupbutton.clicked.connect(self.register_check)
        self.ui.signfornoaccbutton.clicked.connect(self.open_signup_window)
        self.ui.loginbutton.clicked.connect(self.login_check)
        self.ui.signfornoaccbutton_2.clicked.connect(self.open_login_window)
        self.ui.homebutton.clicked.connect(self.go_to_homepage)

    def open_signup_window(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page2signup)

    def open_login_window(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page1login)

    def go_to_homepage(self):
        from app.template.homepage.Homepagerun import HomepageWindow
        self.home = HomepageWindow()
        self.close()
        self.home.show()

    
    def register_check(self):
        username = self.ui.username.text()
        email = self.ui.email.text()
        password = self.ui.password.text()
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

    def login_check(self):
        print("Login button clicked")
        username = self.ui.username.text()
        password = self.ui.password.text()
        admin = False
        if self.ui.checkbox.isChecked():
            admin = True
        if login(username, password, admin):
            print("Login Successful")
            self.show_success("Login successful, welcome")
            self.go_to_homepage()
        else:
            print("Login Failed")
            self.ui.username.clear()
            self.ui.password.clear()
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
            self.register_check()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StackLoginSignup()
    window.show()
    sys.exit(app.exec())