from app.db.database import *
# from app.db.database import UserDatabase as db

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
# from loginUI import Ui_MainWindow
from .loginUI import Ui_MainWindow

# acc = root
# conn = Connection()

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.signInButton.clicked.connect(self.login_window)
        self.ui.signUpButton.clicked.connect(self.register_window)
        
    def register_window(self):
        username = self.ui.username_edit.text()
        password = self.ui.password_edit.text()
        
        if register(username, "email@example.com", password):
            print("User registered successfully")
            print_database_contents(username)
        else:
            print("User registration failed")

    def login_window(self):
        username = self.ui.username_edit.text()
        password = self.ui.password_edit.text()
        if login(username, password):
            print("Login Successful")
        else:
            print("Login Failed")
            # self.ui.username_edit.clear()
            # self.ui.password_edit.clear()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())