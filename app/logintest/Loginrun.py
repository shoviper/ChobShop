import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from .Login import *
# from Login import *
# from app.signuptest.Signuprun import *
from app.db.database import *

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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
            QLabel#loginlabel {
                color: #000;
                font-family: Inter;
                font-size: 48px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            }
                           
            QLabel#noacclabel {
                color: #CD4662;
                text-align: center;
                font-family: Inter;
                font-size: 20px;
                font-style: normal;
                font-weight: 400;
                line-height: normal;
                margin-left: 100px;
            }
                           
            QPushButton#signfornoaccbutton {
                color: #AEC289;
                font-family: Inter;
                font-size: 20px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
                margin-right: 350px;
            }
            
            QLabel#adminlabel {
                color: #CD4662;
                text-align: center;
                font-family: Inter;
                font-size: 18px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
                margin-left: 280px;
            }

            /* Push button styling */
            QPushButton#loginbutton {
                background-color: #CD4662;
                color: #FFF;
                text-align: center;
                font-family: Inter;
                font-size: 24px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
                border-radius: 25px;
            }

            QPushButton#loginbutton:hover {
                background-color: #0056b3;
            }

            /* LineEdit styling */
            QLineEdit#username {
                font-size: 24px;
                width: 500px;
                height: 80px;
                border-bottom: 3px solid #000;
                background-color: #FAF9F6;
            }
            
            QLineEdit#password {
                font-size: 24px;
                width: 500px;
                height: 80px;
                border-bottom: 3px solid #000;
                background-color: #FAF9F6;
            }
                           
            QCheckBox#checkbox {
                color: #CD4662;
            }

            /* MenuBar styling */
            QMenuBar#menubar {
                background-color: #ffffff;
                border-bottom: 1px solid #cccccc;
            }

            /* StatusBar styling */
            QStatusBar#statusbar {
                background-color: #ffffff;
                border-top: 1px solid #cccccc;
            }
        """)
        
        self.display_image()
        # self.ui.pushButton.clicked.connect(self.open_signup_window)
        self.ui.loginbutton.clicked.connect(self.login_window) # login button clicked
        self.ui.signfornoaccbutton.clicked.connect(self.open_signup_window) # login button clicked

    def display_image(self):
        image_path = "pic/loginpic.png"
        pixmap = QPixmap(image_path)

        label = QLabel(self.ui.rightcontainer)
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, 947, 827)
        label.setScaledContents(True)
    
    def open_signup_window(self):
        self.close()
        from app.signuptest.Signuprun import SignupWindow
        self.signup = SignupWindow()
        self.signup.show()

        
    def open_homepage(self):
        # from loginProgram import Login
        # self.close()
        # self.login_window = Login()
        # self.login_window.show()
        pass
        
    def login_window(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        if login(username, password):
            print("Login Successful")
            # self.open_homepage()
            self.open_signup_window()
            
        else:
            print("Login Failed")
            self.ui.username.clear()
            self.ui.password.clear()
            # self.open_signup_window()
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())