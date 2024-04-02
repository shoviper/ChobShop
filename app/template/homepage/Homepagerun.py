import shutil
import os
import xml.etree.ElementTree as ET
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QSizePolicy, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6 import QtCore
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
        self.ui.logoutsettingsbutton.clicked.connect(self.back_to_login)
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
        self.ui.tobeshipbutton.clicked.connect(self.go_to_order_ship_fromprofile)
        self.ui.tobereceivebutton.clicked.connect(self.go_to_order_receive_fromprofile)
        self.ui.completebutton.clicked.connect(self.go_to_order_complete_fromprofile)
        self.ui.viewallfavbutton.clicked.connect(self.go_to_favorite)


        #settings
        self.ui.settingbutton.clicked.connect(self.go_to_setting)
        self.ui.backbutton_settings.clicked.connect(self.setting_to_home)
        self.ui.accountbutton.clicked.connect(self.go_to_account)
        self.ui.changepassbutton.clicked.connect(self.go_to_changepassword)
        self.ui.editprobutton.clicked.connect(self.go_to_editprofile)
        self.ui.rulebutton.clicked.connect(self.go_to_rule)
        self.ui.backtomainsettingbutton.clicked.connect(self.go_to_setting)
        self.ui.backtomainsettingbutton_2.clicked.connect(self.go_to_setting)
        self.ui.backtomainsettingbutton_3.clicked.connect(self.go_to_setting)
        self.ui.backtomainsettingbutton_4.clicked.connect(self.go_to_setting)



        #settingsAdmin
        




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
            

    #settingspage--------------------------------------------------------------------------------------------
    def go_to_setting(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.settings)
        self.ui.stackedWidget_settings.setCurrentWidget(self.ui.settingsmainpage)
    def setting_to_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.homepage)
    def go_to_account(self):
        self.ui.stackedWidget_settings.setCurrentWidget(self.ui.accountpage)
    def go_to_changepassword(self):
        self.ui.stackedWidget_settings.setCurrentWidget(self.ui.changepasswordpage)
    def go_to_editprofile(self):
        self.ui.stackedWidget_settings.setCurrentWidget(self.ui.editprofilesettingspage)
    def go_to_rule(self):
        self.ui.stackedWidget_settings.setCurrentWidget(self.ui.rulepage)
    #settingspage--------------------------------------------------------------------------------------------
        
    #settingsAdminpage--------------------------------------------------------------------------------------------
    
    #settingsAdminpage--------------------------------------------------------------------------------------------

    def go_to_home(self):
        print("go to home")
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.homepage)
        self.ui.homebutton.setStyleSheet(active_button_style)
        self.ui.favbutton.setStyleSheet(inactive_button_style)
        self.ui.orderbutton.setStyleSheet(inactive_button_style)
        self.ui.messbutton.setStyleSheet(inactive_button_style)
    
    def go_to_order_ship_fromprofile(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.myorderspage)
        self.ui.completedbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.tobeshippedbutton.setStyleSheet(active_orderbutton_style)
        self.ui.toberecievedbutton.setStyleSheet(inactive_orderbutton_style)

    def go_to_order_receive_fromprofile(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.myorderspage)
        self.ui.completedbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.tobeshippedbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.toberecievedbutton.setStyleSheet(active_orderbutton_style)
        self.ui.stackedWidget_myorders.setCurrentWidget(self.ui.toberecievedpage)

    def go_to_order_complete_fromprofile(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.myorderspage)
        self.ui.completedbutton.setStyleSheet(active_orderbutton_style)
        self.ui.tobeshippedbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.toberecievedbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.stackedWidget_myorders.setCurrentWidget(self.ui.completedpage)
        

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
        self.ui.viewallproductbutton_admin.clicked.connect(self.go_to_productspage_admin)
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
        self.ui.producttypesbutton_admin.setStyleSheet(inactive_orderbutton_style)
        self.ui.allproductbutton_admin.setStyleSheet(active_orderbutton_style)

        self.ui.producttypesbutton_admin.clicked.connect(self.go_to_producttype_admin)

    def go_to_producttype_admin(self):
            self.ui.stackedWidget_allandtype_admin.setCurrentWidget(self.ui.adminproducttypespage)
            self.ui.producttypesbutton_admin.setStyleSheet(active_orderbutton_style)
            self.ui.allproductbutton_admin.setStyleSheet(inactive_orderbutton_style)
            self.ui.allproductbutton_admin.clicked.connect(self.go_to_productspage_admin)

    def go_to_addproduct_admin(self):
        self.ui.stackedWidget_adminmain.setCurrentWidget(self.ui.productspage_admin)
        self.ui.stackedWidget_adminproducts.setCurrentWidget(self.ui.addproductpage_admin)

        self.ui.homebutton_admin.clicked.connect(self.go_to_homepage_admin)

        self.ui.addsizeproductbutton.clicked.connect(self.add_size)
        self.size_len = 0
        self.ui.addoptionproductbutton.clicked.connect(self.add_option)
        self.option_len = 0
        
        self.product_img = 1
        self.ui.img_1.setVisible(False)
        self.ui.delete_pic_button_1.setVisible(False)
        self.ui.delete_pic_button_1.clicked.connect(lambda: self.delete_product_img(self.ui.addimagebutton, self.ui.img_1, self.ui.delete_pic_button_1))
        # self.ui.img_2.setVisible(False)
        # self.ui.delete_pic_button_2.setVisible(False)
        # self.ui.delete_pic_button_2.clicked.connect(lambda: self.delete_product_img(self.ui.addimagebutton_2, self.ui.img_2, self.ui.delete_pic_button_2))
        # self.ui.img_3.setVisible(False)
        # self.ui.delete_pic_button_3.setVisible(False)
        # self.ui.delete_pic_button_3.clicked.connect(lambda: self.delete_product_img(self.ui.addimagebutton_3, self.ui.img_3, self.ui.delete_pic_button_3))
        # self.ui.img_4.setVisible(False)
        # self.ui.delete_pic_button_4.setVisible(False)
        # self.ui.delete_pic_button_4.clicked.connect(lambda: self.delete_product_img(self.ui.addimagebutton_4, self.ui.img_4, self.ui.delete_pic_button_4))
        # self.ui.img_5.setVisible(False)
        # self.ui.delete_pic_button_5.setVisible(False)
        # self.ui.delete_pic_button_5.clicked.connect(lambda: self.delete_product_img(self.ui.addimagebutton_5, self.ui.img_5, self.ui.delete_pic_button_5))
        # self.ui.img_6.setVisible(False)
        # self.ui.delete_pic_button_6.setVisible(False)
        # self.ui.delete_pic_button_6.clicked.connect(lambda: self.delete_product_img(self.ui.addimagebutton_6, self.ui.img_6, self.ui.delete_pic_button_6))
        
        self.ui.addimagebutton.clicked.connect(self.add_img)
        # self.ui.addimagebutton.clicked.connect(lambda: self.add_product_img(self.ui.addimagebutton, self.ui.img_1, self.ui.delete_pic_button_1))
        # self.ui.addimagebutton_2.clicked.connect(lambda: self.add_product_img(self.ui.addimagebutton_2, self.ui.img_2, self.ui.delete_pic_button_2))
        # self.ui.addimagebutton_3.clicked.connect(lambda: self.add_product_img(self.ui.addimagebutton_3, self.ui.img_3, self.ui.delete_pic_button_3))
        # self.ui.addimagebutton_4.clicked.connect(lambda: self.add_product_img(self.ui.addimagebutton_4, self.ui.img_4, self.ui.delete_pic_button_4))
        # self.ui.addimagebutton_5.clicked.connect(lambda: self.add_product_img(self.ui.addimagebutton_5, self.ui.img_5, self.ui.delete_pic_button_5))
        # self.ui.addimagebutton_6.clicked.connect(lambda: self.add_product_img(self.ui.addimagebutton_6, self.ui.img_6, self.ui.delete_pic_button_6))
        
        self.ui.addproductbutton.clicked.connect(self.add_product)
        self.ui.canceladdproductbutton.clicked.connect(self.go_to_homepage_admin)
    
    def add_img(self):
        if self.add_product_img(self.ui.addimagebutton, self.ui.img_1, self.ui.delete_pic_button_1):
            addoption_geometry = self.ui.addimagebutton.geometry()
            x_coordinate = addoption_geometry.x()
            y_coordinate = addoption_geometry.y()
            width = addoption_geometry.width()
            height = addoption_geometry.height()
            self.ui.addimagebutton.setGeometry(x_coordinate + 201, y_coordinate, width, height)
            self.product_img += 1
            imgbutton = QPushButton()
            # imgbutton.setAlignment(QtCore.Qt.AlignCenter)
            imgbutton.setObjectName(f"addimagebutton_{self.option_len}")
            imgbutton.setGeometry(x_coordinate, y_coordinate, width, height)
            imgbutton.setMinimumHeight(151)
            imgbutton.setMinimumWidth(151)
            imgbutton.setMaximumHeight(151)
            imgbutton.setMaximumWidth(151)
            imgbutton.setStyleSheet("border: 3px dashed #D9D9D9; font-size: 46px; background: #FAF9F6; color: #D9D9D9;")

            frame_layout = self.ui.frame_options.layout()
            frame_layout.insertWidget(self.option_len - 1, imgbutton)

    
    def add_product_img(self, button, img, delete):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.png)")
        
        pixmap = QPixmap(fname[0])
        if fname and (pixmap.width() != 0 or pixmap.height() != 0):
            print("fname: ", fname)
            
            if pixmap.width() > pixmap.height():
                aspect_ratio = pixmap.height() / pixmap.width()
                label_width = 141
                label_height = int(label_width * aspect_ratio)
                img.setFixedSize(label_width, label_height)
            else:
                aspect_ratio = pixmap.width() / pixmap.height()
                label_height = 141
                label_width = int(label_height * aspect_ratio)
                img.setFixedSize(label_width, label_height)
            
            img.setAlignment(QtCore.Qt.AlignCenter)
            
            self.product_img += 1
            img.setVisible(True)
            delete.setVisible(True)
            button.setVisible(False)
            img.setPixmap(pixmap)
            img.setScaledContents(True)
            
            self.add_img_to_folder(fname)
            self.add_img_to_stylesheet(fname)

            return True
        return False
            
    def delete_product_img(self, button, img, delete):
        geometry = self.ui.addimagebutton.geometry()
        self.ui.addimagebutton.setGeometry(geometry.x() - 201, geometry.y(), 141, 141)
        img.setVisible(False)
        button.setVisible(True)
        self.product_img -= 1
        delete.setVisible(False)
        
    def add_img_to_folder(self, img):
        # Copy the image file to the product_img folder
        shutil.copy(img[0], 'app/assets/product_img/')
        
        qrc_file_path = 'app/assets/realsourceimg/realpicforuse.qrc'
        tree = ET.parse(qrc_file_path)
        root = tree.getroot()
        
        # Check if the file already exists in the .qrc file
        existing_files = [file_elem.text for file_elem in root.findall("./qresource[@prefix='pic']/file")]
        img_basename = os.path.basename(img[0])
        if img_basename not in existing_files:
            # Create a new <file> element with the path of the copied image file
            new_file_element = ET.Element("file")
            new_file_element.text = f"../product_img/{img_basename}"
            
            # Append the new <file> element to the existing <qresource> element
            qresource_element = root.find("./qresource[@prefix='pic']")
            qresource_element.append(new_file_element)
            
            # Write the modified XML back to the .qrc file
            tree.write(qrc_file_path)

        
    def add_img_to_stylesheet(self, img):
        # Open the realhomepage_ui.py file for reading
        file_path = 'app/template/homepage/realhomepage_ui.py'  # Replace with the actual path to your realhomepage_ui.py file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Find the line number where to insert the stylesheet
        insert_line_number = None
        for i, line in enumerate(lines):
            if 'self.img_1.setGeometry(' in line:
                insert_line_number = i + 1
                break

        # Insert the new line
        if insert_line_number is not None:
            lines.insert(insert_line_number, f'        self.img_1.setStyleSheet(u"image: url(:/pic/product_img/{os.path.basename(img[0])})")\n')

            # Write the modified content back to the file
            with open(file_path, 'w') as file:
                file.writelines(lines)
        else:
            print("Error: Line to insert stylesheet not found.")

    def add_size(self):
        print("add size")
        addsize_geometry = self.ui.addsizeproductbutton.geometry()
        x_coordinate = addsize_geometry.x()
        y_coordinate = addsize_geometry.y()
        width = addsize_geometry.width()
        height = addsize_geometry.height()
        self.ui.addsizeproductbutton.setGeometry(x_coordinate + width + 10, y_coordinate, width, height)
        self.size_len += 1
        size = QLineEdit()
        size.setAlignment(QtCore.Qt.AlignCenter) 
        size.setObjectName(f"size_{self.size_len}")
        size.setGeometry(x_coordinate, y_coordinate, width, height)
        size.setMinimumHeight(38)
        size.setMinimumWidth(108)
        size.setMaximumHeight(38)
        size.setMaximumWidth(108)
        size.setStyleSheet("border-radius: 5px; background: #EDEDED; padding: 5px; font-size: 16px; text-align: center;")

        frame_layout = self.ui.frame_sizes.layout()
        frame_layout.insertWidget(self.size_len - 1, size)

    def add_option(self):
        print("add option")
        addoption_geometry = self.ui.addoptionproductbutton.geometry()
        x_coordinate = addoption_geometry.x()
        y_coordinate = addoption_geometry.y()
        width = addoption_geometry.width()
        height = addoption_geometry.height()
        self.ui.addoptionproductbutton.setGeometry(x_coordinate + width + 10, y_coordinate, width, height)
        self.option_len += 1
        option = QLineEdit()
        option.setAlignment(QtCore.Qt.AlignCenter) 
        option.setObjectName(f"option_{self.option_len}")
        option.setGeometry(x_coordinate, y_coordinate, width, height)
        option.setMinimumHeight(38)
        option.setMinimumWidth(108)
        option.setMaximumHeight(38)
        option.setMaximumWidth(108)
        option.setStyleSheet("border-radius: 5px; background: #EDEDED; padding: 5px; font-size: 16px; text-align: center;")

        frame_layout = self.ui.frame_options.layout()
        frame_layout.insertWidget(self.option_len - 1, option)

    def add_categories(self):
        print("add categories")
        men = self.ui.checkBox_men.isChecked()
        women = self.ui.checkBox_women.isChecked()
        kids = self.ui.checkBox_kids.isChecked()
        top = self.ui.checkBox_top.isChecked()
        bottom = self.ui.checkBox_bottom.isChecked()
        dress = self.ui.checkBox_dress.isChecked()
        footwear = self.ui.checkBox_footwear.isChecked()
        headwear = self.ui.checkBox_headwear.isChecked()
        accessories = self.ui.checkBox_accessories.isChecked()

        categories = []

        if men == True:
            categories.append("Men")
        if women == True:
            categories.append("Women")
        if kids == True:
            categories.append("Kids")
        if top == True:
            categories.append("Top")
        if bottom == True:
            categories.append("Bottom")
        if dress == True:
            categories.append("Dress")
        if footwear == True:
            categories.append("Footwear")
        if headwear == True:
            categories.append("Headwear")
        if accessories == True:
            categories.append("Accessories")

        return categories

    def add_product(self):
        productname = self.ui.addproductnametextbox.text()
        description = self.ui.addproductdescriptiontextbox.toPlainText()
        price = self.ui.addproductpricespinbox.value()
        sizes = []
        options = []
        for i in range(1, self.size_len + 1):
            size = self.ui.frame_sizes.findChild(QLineEdit, f"size_{i}")
            sizes.append(size.text())
        for i in range(1, self.option_len + 1):
            option = self.ui.frame_options.findChild(QLineEdit, f"option_{i}")
            options.append(option.text())
        stock = self.ui.addproductstockspinbox.value()
        categories = self.add_categories()
        

        addproduct(productname, description, price, sizes, options, stock, categories)
        print("product added")

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
