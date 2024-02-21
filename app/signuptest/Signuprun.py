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

        # Apply CSS styles
        self.setStyleSheet("""
            /* Central widget styling */
            QWidget#centralwidget {
                background-color: #FAF9F6;
            }
                           
            QWidget#leftcontainer {
                background-color: #FAF9F6;
            }
                           
            QWidget#rightcontainer {
                background-color: #E1E3E7;
                margin-left: 27px;
                border-radius: 25px;
            }

            /* Label styling */
            QLabel#signuplabel {
                color: #000;
                font-family: Inter;
                font-size: 48px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            }
                           
            QLabel#haveacclabel {
                color: #CD4662;
                text-align: center;
                font-family: Inter;
                font-size: 20px;
                font-style: normal;
                font-weight: 400;
                line-height: normal;
                margin-left: 75px;
            }
                           
            QPushButton#logforhaveaccbutton {
                border: none;
                color: #AEC289;
                font-family: Inter;
                font-size: 20px;
                font-style: bold;
                font-weight: 700;
                line-height: normal;
                margin-right: 400px;
            }
                           
            QPushButton#logforhaveaccbutton:hover {
                color: #CD4662;
            }

            /* Push button styling */
            QPushButton#signupbutton {
                background-color: #CD4662;
                color: #FFF;
                text-align: center;
                font-family: Inter;
                font-size: 24px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
                border-radius: 15px;
            }

            QPushButton#signupbutton:hover {
                background-color: #AEC289;
            }

            /* LineEdit styling */
            QLineEdit#username {
                font-size: 24px;
                width: 500px;
                height: 80px;
                border: none;
                border-bottom: 3px solid #000;
                background-color: #FAF9F6;
            }
            
            QLineEdit#password {
                font-size: 24px;
                width: 500px;
                height: 80px;
                border: none;
                border-bottom: 3px solid #000;
                background-color: #FAF9F6;
            }
            
            QLineEdit#email {
                font-size: 24px;
                width: 500px;
                height: 80px;
                border: none;
                border-bottom: 3px solid #000;
                background-color: #FAF9F6;
            }

            /* MenuBar styling */
            QMenuBar#menubar {
                background-color: #ffffff;
                border: none;
                border-bottom: 1px solid #cccccc;
            }

            /* StatusBar styling */
            QStatusBar#statusbar {
                background-color: #ffffff;
                border-top: 1px solid #cccccc;
            }
        """)
        
        self.display_image()
        self.ui.signupbutton.clicked.connect(self.register_check)
        self.ui.logforhaveaccbutton.clicked.connect(self.open_login_window)

    def display_image(self):
        image_path = "app/assets/images/loginpic.png"
        pixmap = QPixmap(image_path)

        label = QLabel(self.ui.rightcontainer)
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, 947, 827)
        label.setScaledContents(True)

    def open_login_window(self):
        self.close()
        from app.logintest.Loginrun import LoginWindow
        self.login = LoginWindow()
        self.login.show()

    
    def register_check(self):
        username = self.ui.username.text()
        email = self.ui.email.text()
        password = self.ui.password.text()
        
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SignupWindow()
    window.show()
    sys.exit(app.exec())