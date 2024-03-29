import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap
# from Homepage import Ui_MainWindow
# from .Homepage_newres_ui import *
from .realhomepage_ui import *
from app.template.order.Orderrun import *
from app.db.database import *
from app.backend.customerUser.editprofile import *
from app.backend.adminUser.adminmain import *
from app.backend.adminUser.products_admin import *
# from .Homepagdsadse import *

# import app.assets.realsourceimg.real

active_button_style = """
    QPushButton{
        color: #FAF9F6;
        font-family: Suwannaphum;
        font-size: 16px;
        font-style: normal;
        font-weight: 500;
        line-height: normal;
        background-color: #AEC289;
        border-radius: 10px;
    }
    QPushButton:hover {
        background-color: #F4DBDB;
        color: black;
    }
"""

inactive_button_style = """
    QPushButton{
        color: #000;
        font-family: Suwannaphum;
        font-size: 16px;
        font-style: normal;
        font-weight: 500;
        line-height: normal;
        background-color: #E1E3E7;
        border-radius: 10px;
    }
    QPushButton:hover {
        background-color: #F4DBDB;
        color: black;
    }
"""


#order
inactive_orderbutton_style = """
    QPushButton{
        color: #545454;
        text-align: center;
        font-family: Suwannaphum;
        font-size: 20px;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
        border: none;
    }
    QPushButton:hover{
        background-color: #F4DBDB;
        color: #545454;
    }
"""

active_orderbutton_style = """
    QPushButton{
        color: #CD4662;
        text-align: center;
        font-family: Suwannaphum;
        font-size: 20px;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
        border: none;
        border-bottom: 3px solid #CD4662;
    }
    QPushButton:hover{
        background-color: #F4DBDB;
        color: #545454;
        border: none;
    }
"""

class HomepageWindow(QMainWindow):
    def __init__(self):
        super(HomepageWindow, self).__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        # print("root.LoggedInUser.logged_in: ", root.LoggedInUser)
        # print("root.LoggedInUser.user.username: ", root.LoggedInUser.user.username)

        if root.LoggedInUser.logged_in == False:
            self.ui.loginsignoutbutton.setText("Log in")
            self.ui.profilebutton.clicked.connect(lambda: self.show_error("Please log in to view profile"))
            self.ui.loginsignoutbutton.clicked.connect(self.back_to_login)
        else:
            self.ui.loginsignoutbutton.setText(root.LoggedInUser.user.username)
            self.ui.profilebutton.clicked.connect(self.go_to_userprofile)
            self.ui.loginsignoutbutton.clicked.connect(self.go_to_userprofile)
            
        #stackmain
        self.ui.exitbutton.clicked.connect(self.back_to_login)
        self.ui.homebutton.clicked.connect(self.go_to_home)
        self.ui.favbutton.clicked.connect(self.go_to_favorite)
        self.ui.orderbutton.clicked.connect(self.go_to_order)

        #orderpage
        self.ui.tobeshippedbutton.clicked.connect(self.go_to_order_ship)
        self.ui.toberecievedbutton.clicked.connect(self.go_to_order_receive)
        self.ui.completedbutton.clicked.connect(self.go_to_order_complete)

        #editprofile
        self.ui.backbutton_2.clicked.connect(self.go_to_userprofile)

        #profile
        self.ui.editprofilebutton.clicked.connect(self.go_to_usereditprofile)
        self.ui.backbutton.clicked.connect(self.go_to_home)
        self.ui.tobeshipbutton.clicked.connect(self.go_to_order)
        self.ui.tobereceivebutton.clicked.connect(self.go_to_order_receive)
        self.ui.completebutton.clicked.connect(self.go_to_order_complete)

        #cart
        self.ui.cartbutton.clicked.connect(self.go_to_cart)

    #Log out function
    def back_to_login(self):
        if root.LoggedInUser.logged_in == True:
            if self.show_yes_no("Are you sure you want to log out?") == QMessageBox.Yes:
                logout(root.LoggedInUser.user.username)
                # print("root.LoggedInUser.user.username: ", root.LoggedInUser.user.username)
                from app.template.login.Loginrun import LoginWindow
                self.login = LoginWindow()
                print("root.LoggedInUser.logged_in: ", root.LoggedInUser.logged_in)
                root.LoggedInUser.logged_in = False
                self.close()
                self.login.show()
        else:
            from app.template.login.Loginrun import LoginWindow
            self.login = LoginWindow()
            print("back_to_login else root.LoggedInUser.logged_in: ", root.LoggedInUser.logged_in)
            self.close()
            self.login.show()
    
    # def back_to_login(self):
    #     from app.template.login.Loginrun import LoginWindow
    #     self.login = LoginWindow()
    #     # self.show_goodbye("Log out successful, See you again")
    #     self.close()
    #     self.login.show()

    def go_to_home(self):
        print("go to home")
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.homepage)
        self.ui.homebutton.setStyleSheet(active_button_style)
        self.ui.favbutton.setStyleSheet(inactive_button_style)
        self.ui.orderbutton.setStyleSheet(inactive_button_style)
        self.ui.messbutton.setStyleSheet(inactive_button_style)

    def go_to_favorite(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.favpage)
        
        self.ui.homebutton.setStyleSheet(inactive_button_style)
        self.ui.favbutton.setStyleSheet(active_button_style)
        self.ui.orderbutton.setStyleSheet(inactive_button_style)
        self.ui.messbutton.setStyleSheet(inactive_button_style)

    def go_to_userprofile(self):
        print("go to profile")
        self.ui.stackedWidget.setCurrentWidget(self.ui.userprofile)
        # self.ui.usernamelabel.setText(root.LoggedInUser.user.username.title())
        self.ui.usernamelabel.setText(root.LoggedInUser.user.username)
        self.ui.openshopbutton.clicked.connect(self.go_to_adminregister)

    def go_to_usereditprofile(self):
        print("go to edit profile")
        # self.ui.editnameprofile.setText(root.LoggedInUser.user.username.title())
        self.ui.editnameprofile.setText(root.LoggedInUser.user.username)
        # self.ui.userbox.setText(root.LoggedInUser.user.username.title())
        self.ui.userbox.setText(root.LoggedInUser.user.username)
        self.ui.firstnamebox.setText(root.LoggedInUser.user.name)
        self.ui.lastnamebox.setText(root.LoggedInUser.user.lastname)
        self.ui.genderbox.setText(root.LoggedInUser.user.gender)
        self.ui.birthdaydateEdit.setDate(root.LoggedInUser.user.birthday)
        self.ui.emailbox.setText(root.LoggedInUser.user.email)
        self.ui.phonebox.setText(root.LoggedInUser.user.phone)

        self.ui.stackedWidget.setCurrentWidget(self.ui.editprofile)
        self.ui.savechangebutton_2.clicked.connect(self.save_editprofile)
        self.ui.deleteaccbutton.clicked.connect(self.delete_profile)

    def save_editprofile(self):
        print("save edit profile")
        newusername = self.ui.userbox.text()
        username = self.ui.editnameprofile.text()
        firstname = self.ui.firstnamebox.text()
        lastname = self.ui.lastnamebox.text()
        gender = self.ui.genderbox.text()
        birthday = self.ui.birthdaydateEdit.date()
        email = self.ui.emailbox.text()
        phone = self.ui.phonebox.text()

        if editProfile(username, newusername, firstname, lastname, gender, birthday, email, phone):
            self.show_success("Edit Profile successful")
            print_all_users()
            self.go_to_userprofile()
        else:
            self.show_error("Edit Profile failed")
            # self.ui.editnameprofile.setText(root.LoggedInUser.user.username.title())
            self.ui.editnameprofile.setText(root.LoggedInUser.user.username)
            # self.ui.userbox.setText(root.LoggedInUser.user.username.title())
            self.ui.userbox.setText(root.LoggedInUser.user.username)
            self.ui.firstnamebox.setText(root.LoggedInUser.user.name)
            self.ui.lastnamebox.setText(root.LoggedInUser.user.lastname)
            self.ui.genderbox.setText(root.LoggedInUser.user.gender)
            self.ui.birthdaydateEdit.setDate(root.LoggedInUser.user.birthday)
            self.ui.emailbox.setText(root.LoggedInUser.user.email)
            self.ui.phonebox.setText(root.LoggedInUser.user.phone)
    
    def delete_profile(self):
        print("deleting profile")
        user = root.LoggedInUser.user.username
        if self.show_yes_no("Are you sure?") == QMessageBox.Yes:
            if deleteProfile(user):
                self.show_goodbye("Delete Profile successful, Goodbye")
                # print_all_users()
                # self.back_to_login()
                from app.template.login.Loginrun import LoginWindow
                self.login = LoginWindow()
                root.LoggedInUser.logged_in = False
                transaction.commit()
                self.close()
                self.login.show()
            else:
                self.show_error("Delete Profile failed")


    def go_to_adminregister(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.adminwidget)

        if openshop():
            self.go_to_homepage_admin()
        else:
            self.ui.stackedWidget_adminwidget.setCurrentWidget(self.ui.adminregisterpage)
            self.ui.backbutton_adminregister.clicked.connect(self.go_to_userprofile)
            self.ui.adminregisterbutton.clicked.connect(self.admin_register)
        
    def admin_register(self):
        print("Registering as admin")
        username = root.LoggedInUser.user.username
        password = root.LoggedInUser.user.password
        shopname = self.ui.shopnamebox.text()
        firstname = self.ui.firstnamebox_admin.text()
        lastname = self.ui.lastnamebox_admin.text()
        description = self.ui.descriptionbox_admin.text()
        address = self.ui.addressbox_admin.text()
        email = self.ui.emailbox_admin.text()
        phone = self.ui.phonebox_admin.text()
        if registerAdmin(username, shopname, firstname, lastname, description, address, email, phone, password):
            print("Admin registered successfully")
            self.show_success("Admin registered successfully")
            self.go_to_home()
        else:
            print("Admin registration failed")
            self.show_error("Admin registration failed")

    def go_to_homepage_admin(self):
        changeLoggedinUser(root.LoggedInUser.user.username)
        self.ui.stackedWidget_adminwidget.setCurrentWidget(self.ui.adminmain)
        self.ui.stackedWidget_adminmain.setCurrentWidget(self.ui.homepage_admin)
        self.ui.shopnamelabel_admin.setText(root.LoggedInUser.user.shopname)
        self.ui.loginsignoutbutton_admin.setText(root.LoggedInUser.user.username)
        
        self.ui.homebutton_admin.setStyleSheet(active_button_style)
        self.ui.orderstatusbutton_admin.setStyleSheet(inactive_button_style)
        self.ui.productsbutton_admin.setStyleSheet(inactive_button_style)
        self.ui.messbutton_admin.setStyleSheet(inactive_button_style)

        self.ui.productsbutton_admin.clicked.connect(self.go_to_productspage_admin)

        self.ui.addproduct_admin.clicked.connect(self.go_to_addproduct_admin)

    def go_to_productspage_admin(self):
        self.ui.stackedWidget_adminmain.setCurrentWidget(self.ui.productspage_admin)
        self.ui.stackedWidget_adminproducts.setCurrentWidget(self.ui.alltypesproductspage_admin)
        self.ui.stackedWidget_allandtype_admin.setCurrentWidget(self.ui.adminallproductpage)
        
        self.ui.homebutton_admin.setStyleSheet(inactive_button_style)
        self.ui.orderstatusbutton_admin.setStyleSheet(inactive_button_style)
        self.ui.productsbutton_admin.setStyleSheet(active_button_style)
        self.ui.messbutton_admin.setStyleSheet(inactive_button_style)

        self.ui.homebutton_admin.clicked.connect(self.go_to_homepage_admin)

    def go_to_addproduct_admin(self):
        self.ui.stackedWidget_adminmain.setCurrentWidget(self.ui.productspage_admin)
        self.ui.stackedWidget_adminproducts.setCurrentWidget(self.ui.addproductpage_admin)

        self.ui.homebutton_admin.clicked.connect(self.go_to_homepage_admin)

        self.ui.addproductbutton.clicked.connect(self.add_product)
        self.ui.canceladdproductbutton.clicked.connect(self.go_to_homepage_admin)

    def add_product(self):
        productname = self.ui.addproductnametextbox.text()
        description = self.ui.addproductdescriptiontextbox.toPlainText()
        price = self.ui.addproductpricespinbox.value()
        sizes = ["S", "M", "L", "XL"]
        options = ["Red", "Blue", "Green"]
        stock = self.ui.addproductstockspinbox.value()
        categories = ["men", "top"]
        addproduct(productname, description, price, sizes, options, stock, categories)

    def go_to_order(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.myorderspage)
        self.ui.homebutton.setStyleSheet(inactive_button_style)
        self.ui.favbutton.setStyleSheet(inactive_button_style)
        self.ui.orderbutton.setStyleSheet(active_button_style)
        self.ui.messbutton.setStyleSheet(inactive_button_style)

    def go_to_order_ship(self):
        self.ui.tobeshippedbutton.setStyleSheet(active_orderbutton_style)
        self.ui.toberecievedbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.completedbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.stackedWidget_myorders.setCurrentWidget(self.ui.tobeshippedpage)

    def go_to_order_receive(self):
        self.ui.toberecievedbutton.setStyleSheet(active_orderbutton_style)
        self.ui.tobeshippedbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.completedbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.stackedWidget_myorders.setCurrentWidget(self.ui.toberecievedpage)

    def go_to_order_complete(self):
        self.ui.completedbutton.setStyleSheet(active_orderbutton_style)
        self.ui.tobeshippedbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.toberecievedbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.stackedWidget_myorders.setCurrentWidget(self.ui.completedpage)

    def go_to_cart(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.cartpage)

    def show_success(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Login Succesful")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
    
    def show_yes_no(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText(message)
        msg.setWindowTitle("Log out")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.exec()
        return msg.result()
        
    def show_goodbye(self, message):
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
    window = HomepageWindow()
    window.show()
    sys.exit(app.exec())
