import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from app.db.database import *
from app.template.register import *

from app.logintest.Loginrun import *

from app.signuptest.Signuprun import *

#-------------------------Run the folder template#-------------------------
# class Main(LoginWindow):
#     def __init__(self):
#         super().__init__()
#-------------------------Run the folder template#-------------------------

#-------------------------Run the folder logintest#-------------------------
# For running LoginWindow
class Main(LoginWindow):
    def __init__(self):
        super().__init__()
#-------------------------Run the folder logintest#-------------------------
        
#-------------------------Run the folder signuptest#------------------------
# For running SignupWindow
# class Main(SignupWindow):
#     def __init__(self):
#         super().__init__()
#-------------------------Run the folder signuptest#-------------------------

# if acc.register("username", "email@example.com", "password"):
#     print("User registered successfully")
# else:
#     print("User registration failed")

# user = acc.login(username="username", password="password")
# if user:
#     print("Login successful")
#     print(user)
# else:
#     print("Login failed")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
