import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from app.db.database import *
# from app.template.register import *

from app.template.login.Loginrun import *

from app.template.signup.Signuprun import *

from app.template.homepage.Homepagerun import *

from app.template.favorite.Favoriterun import *

from app.template.product.Productrun import *

from app.template.order.Orderrun import *

#-------------------------Run the folder template#-------------------------
# class Main(LoginWindow):
#     def __init__(self):
#         super().__init__()
#-------------------------Run the folder template#-------------------------

#-------------------------Run the folder login#-------------------------
# For running LoginWindow
# class Main(LoginWindow):
#     def __init__(self):
#         super().__init__()
#-------------------------Run the folder login#-------------------------
        
#-------------------------Run the folder signup#------------------------
# For running SignupWindow
class Main(SignupWindow):
    def __init__(self):
        super().__init__()
#-------------------------Run the folder signup#-------------------------

#-------------------------Run the folder homepage#------------------------
# For running HomepageWindow
# class Main(HomepageWindow):
#     def __init__(self):
#         super().__init__()
#-------------------------Run the folder homepage#-------------------------

#-------------------------Run the folder favorite#------------------------
# For running FavoriteWindow
# class Main(FavoriteWindow):
#     def __init__(self):
#         super().__init__()
#-------------------------Run the folder favorite#-------------------------

#-------------------------Run the folder product#------------------------
# For running ProductWindow
# class Main(ProductWindow):
#     def __init__(self):
#         super().__init__()
#-------------------------Run the folder product#-------------------------
        
#-------------------------Run the folder order#------------------------
# For running OrderWindow
# class Main(OrderWindow):
#     def __init__(self):
#         super().__init__()
#-------------------------Run the folder order#-------------------------

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
