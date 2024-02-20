import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
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
                           
            QWidget#widget {
                background-color: #FAF9F6;
            }
                           
            QWidget#widget_2 {
                background-color: #E1E3E7;
                margin-left: 27px;
                border-radius: 25px;
            }

            /* Label styling */
            QLabel#label {
                color: #000;
                font-family: Inter;
                font-size: 48px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            }
                           
            QLabel#label_2 {
                color: #CD4662;
                text-align: center;
                font-family: Inter;
                font-size: 20px;
                font-style: normal;
                font-weight: 400;
                line-height: normal;
                margin-left: 75px;
            }
                           
            QPushButton#pushButton2 {
                border: none;
                color: #AEC289;
                font-family: Inter;
                font-size: 20px;
                font-style: bold;
                font-weight: 700;
                line-height: normal;
                margin-right: 350px;
            }
                           
            QPushButton#pushButton2:hover {
                color: #CD4662;
            }
            
            QLabel#label_5 {
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
            QPushButton#pushButton {
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

            QPushButton#pushButton:hover {
                background-color: #AEC289;
            }

            /* LineEdit styling */
            QLineEdit#lineEdit {
                font-size: 24px;
                width: 500px;
                height: 80px;
                border: none;
                border-bottom: 3px solid #000;
                background-color: #FAF9F6;
            }
            
            QLineEdit#lineEdit_2 {
                font-size: 24px;
                width: 500px;
                height: 80px;
                border: none;
                border-bottom: 3px solid #000;
                background-color: #FAF9F6;
            }
            
            QLineEdit#lineEdit_3 {
                font-size: 24px;
                width: 500px;
                height: 80px;
                border: none;
                border-bottom: 3px solid #000;
                background-color: #FAF9F6;
            }
                           
            QCheckBox#checkBox {
                color: #CD4662;
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
        self.ui.pushButton.clicked.connect(self.register_check)
        self.ui.label_3.clicked.connect(self.open_login_window)

    def display_image(self):
        image_path = "app/assets/images/loginpic.png"
        pixmap = QPixmap(image_path)

        label = QLabel(self.ui.widget_2)
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, 947, 827)
        label.setScaledContents(True)

    def open_login_window(self):
        self.close()
        from app.logintest.Loginrun import LoginWindow
        self.login = LoginWindow()
        self.login.show()

    
    def register_check(self):
        username = self.ui.lineEdit_3.text()
        email = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        
        if register(username, email, password):
            print("User registered successfully")
            print_database_contents(username)
            self.open_login_window()
        else:
            print("User registration failed")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SignupWindow()
    window.show()
    sys.exit(app.exec())