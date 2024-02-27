import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from .Signup import *
# from Signup import *
# from Login import *
# from app.logintest.Loginrun import *
from app.db.database import *

class SignupWindow(QMainWindow):
    def __init__(self):
        super(SignupWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.signupbutton.clicked.connect(self.register_check)
        self.ui.signfornoaccbutton.clicked.connect(self.open_login_window)
        self.ui.homebutton.clicked.connect(self.go_to_homepage)

    def open_login_window(self):
        from app.template.login.Loginrun import LoginWindow
        self.Login = LoginWindow()
        self.close()
        self.Login.show()

    def go_to_homepage(self):
        from app.template.homepage.Homepagerun import HomepageWindow
        self.home = HomepageWindow()
        self.close()
        self.home.show()

<<<<<<< HEAD
    
=======
    def display_image(self):
        image_path = "app/assets/images/loginpic.png"
        pixmap = QPixmap(image_path)

        label = QLabel(self.ui.rightcontainer)
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, 947, 827)
        label.setScaledContents(True)

    def open_login_window(self):
        self.close()
        from app.template.login.Loginrun import LoginWindow
        self.login = LoginWindow()
        self.login.show()


>>>>>>> e62c11795f86ac88b7a2639683897ce35e25da10
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