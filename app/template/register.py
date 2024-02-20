from app.db.database import *
# from app.db.database import UserDatabase as db

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

# from .loginUI import Ui_MainWindow
from app.logintest.Login import Ui_MainWindow

# acc = root
# conn = Connection()

class Register(QMainWindow):
    def __init__(self):
        super(Register, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.login_window)
        # self.ui.signUpButton.clicked.connect(self.register_window)

        # self.setStyleSheet("""
        #     /* Central widget styling */
        #     QWidget#centralwidget {
        #         background-color: #f0f0f0;
        #     }

        #     /* Label styling */
        #     QLabel#login_label {
        #         color: #000;
        #         font-family: Inter;
        #         font-size: 25px;
        #         font-style: normal;
        #         font-weight: 700;
        #         line-height: normal;
        #     }
                           
        #     QLabel#label_2 {
        #         color: #CD4662;
        #         font-family: Inter;
        #         font-size: 10px;
        #         font-style: normal;
        #         font-weight: 700;
        #         line-height: normal;
        #     }
                           
        #     QLabel#label_3 {
        #         color: green;
        #         font-family: Inter;
        #         font-size: 10px;
        #         font-style: normal;
        #         font-weight: 700;
        #         line-height: normal;
        #     }

        #     /* Push button styling */
        #     QPushButton#pushButton {
        #         background-color: #CD4662;
        #         text-align: center;
        #         font-family: Inter;
        #         font-size: 15px;
        #         font-style: normal;
        #         font-weight: 700;
        #         line-height: normal;
        #     }

        #     QPushButton#pushButton:hover {
        #         background-color: #0056b3;
        #     }

        #     /* LineEdit styling */
        #     QLineEdit#username_edit {
        #         width: 500px;
        #         height: 30px;
        #         flex-shrink: 0;
        #         border-bottom: 3px solid #000;
        #     }
            
        #     QLineEdit#password_edit {
        #         width: 500px;
        #         height: 30px;
        #         flex-shrink: 0;
        #         border-bottom: 3px solid #000;
        #     }

        #     /* MenuBar styling */
        #     QMenuBar#menubar {
        #         background-color: #ffffff;
        #         border-bottom: 1px solid #cccccc;
        #     }

        #     /* StatusBar styling */
        #     QStatusBar#statusbar {
        #         background-color: #ffffff;
        #         border-top: 1px solid #cccccc;
        #     }
        # """)
        
    def register_window(self):
        username = self.ui.username_edit.text()
        password = self.ui.password_edit.text()
        
        if register(username, "email@example.com", password):
            print("User registered successfully")
            print_database_contents(username)
        else:
            print("User registration failed")

    def login_window(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        if login(username, password):
            print("Login Successful")
        else:
            print("Login Failed")
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Register()
    window.show()
    sys.exit(app.exec_())
        