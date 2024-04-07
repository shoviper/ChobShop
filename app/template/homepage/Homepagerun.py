import shutil
import os
import xml.etree.ElementTree as ET
import sys
import functools
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QSizePolicy, QFileDialog, QInputDialog
from PySide6.QtGui import QPixmap
from PySide6 import QtCore
# from Homepage import Ui_MainWindow
# from .Homepage_newres_ui import *
from .realhomepage_ui import *
from app.template.order.Orderrun import *
from app.db.database import *
from app.backend.customerUser.editprofile import *
from app.backend.customerUser.buyproduct import *
from app.backend.adminUser.adminmain import *
from app.backend.adminUser.products_admin import *
# from .Homepagdsadse import *

import random as r

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
        print("root.LoggedInUser.logged_in: ", root.LoggedInUser)
        # print("root.LoggedInUser.user.username: ", root.LoggedInUser.user.username)

        if root.LoggedInUser.logged_in == False:
            self.ui.loginsignoutbutton.setText("Log in")
            self.ui.profilebutton.clicked.connect(lambda: self.show_error("Please log in to view profile"))
            self.ui.loginsignoutbutton.clicked.connect(self.back_to_login)
        else:
            self.ui.loginsignoutbutton.setText(root.LoggedInUser.user.username)
            self.ui.profilebutton.clicked.connect(self.go_to_userprofile)
            self.ui.loginsignoutbutton.clicked.connect(self.go_to_userprofile)
            
        self.go_to_home()
        
        #stackmain
        self.ui.logoutsettingsbutton.clicked.connect(self.back_to_login)
        self.ui.homebutton.clicked.connect(self.go_to_home)
        self.ui.favbutton.clicked.connect(self.go_to_favorite)
        self.ui.orderbutton.clicked.connect(self.go_to_order_ship)
        
        # self.display_product()
        
        print("-----------Print All Product This User Sell----------------")
        # print("root.LoggedInUser.logged_in: ", root.LoggedInUser.logged_in)
        # for i in get_products_for_user(root.LoggedInUser.user.username):
        #     print("product name and id: ", (get_product_name(root.LoggedInUser.user.username, i.id)), i.id)
        print("-----------------------------------------------------------")
        
        # # delete product by id
        # delete_product_by_id(2)

        # self.print_cart()
        
        
        #orderpage
        # self.ui.tobeshippedbutton.clicked.connect(functools.partial(self.go_to_order_ship))
        # self.ui.toberecievedbutton.clicked.connect(self.go_to_order_receive)
        # self.ui.completedbutton.clicked.connect(self.go_to_order_complete)

        #orderAdmin
        self.ui.orderstatusbutton_admin.clicked.connect(self.orderstatus_tobeship)
        self.ui.toshipadminbutton.clicked.connect(self.orderstatus_tobeship)

        #Adminmainpage
        # self.ui.orderstatusbutton_admin.clicked.connect(self.orderstatus_tobeship)
        # self.ui.toshipadminbutton.clicked.connect(self.adminmain_to_orderstatus_tobeship)
        self.img_button_clicked = False
            

        #editprofile
        self.ui.backbutton_2.clicked.connect(self.go_to_userprofile)

        #profile
        self.ui.backbutton.clicked.connect(self.go_to_home)
        # self.ui.tobeshippedbutton.clicked.connect(self.go_to_order_ship_fromprofile)
        # self.ui.tobereceivebutton.clicked.connect(self.go_to_order_receive_fromprofile)
        self.ui.completebutton.clicked.connect(self.go_to_order_ship_fromprofile)
        # self.ui.viewallfavbutton.clicked.connect(self.go_to_favorite)
        
        #settings
        self.ui.settingbutton.clicked.connect(self.go_to_setting)
        self.ui.backbutton_settings.clicked.connect(self.setting_to_home)
        self.ui.accountbutton.clicked.connect(self.go_to_account)
        self.ui.changepassbutton.clicked.connect(self.go_to_changepassword)
        self.ui.editprobutton.clicked.connect(self.go_to_editprofile)
        self.ui.rulebutton.clicked.connect(self.go_to_rule)
        self.ui.addressbutton.clicked.connect(self.go_to_address)
        self.ui.editaddressbutton.clicked.connect(self.go_to_editaddress)
        self.ui.backtomainsettingbutton.clicked.connect(self.go_to_setting)
        self.ui.backtomainsettingbutton_2.clicked.connect(self.go_to_setting)
        self.ui.backtomainsettingbutton_3.clicked.connect(self.go_to_setting)
        self.ui.backtomainsettingbutton_4.clicked.connect(self.go_to_setting)
        self.ui.backtomainsettingbutton_5.clicked.connect(self.go_to_setting)
        self.ui.backtoeditarresssettingbutton.clicked.connect(self.go_to_address)
        
        #settingsAdmin
        self.ui.settingbutton_admin.clicked.connect(self.go_to_settingAdmin)
        self.ui.backbutton_settingsadmin.clicked.connect(self.settingadmin_to_homeadmin)
        self.ui.shopaccountbutton.clicked.connect(self.go_to_shopaccount)
        self.ui.editshopbutton.clicked.connect(self.go_to_editshop)
        self.ui.ruleadminbutton.clicked.connect(self.go_to_ruleshop)
        self.ui.logoutsettingsadminbutton.clicked.connect(self.back_to_login)
        self.ui.exitshopbutton.clicked.connect(self.exit_shop)
        self.ui.backbutton_settingsadmin_6.clicked.connect(self.go_to_settingAdmin)
        self.ui.backbutton_settingsadmin_2.clicked.connect(self.go_to_settingAdmin)
        self.ui.backbutton_settingsadmin_7.clicked.connect(self.go_to_settingAdmin)

        #cart
        self.addedproduct_cart = []
        self.ui.cartbutton.clicked.connect(functools.partial(self.go_to_cart))
        # self.ui.purchasecartbutton.clicked.connect(self.purchase_cartpage)
        # self.ui.removecartbutton.clicked.connect(self.removeorder)
        self.ui.backtocartbutton.clicked.connect(self.back_to_cart)
        self.button_bug_fix(self.ui.purchaseallcartbutton)
        
        self.ui.purchaseallcartbutton.clicked.connect(functools.partial(self.purchase_cartpage, "cartpage"))
        
        # purchase page
        # self.ui.purchasebutton.clicked.connect(self.purchase_final)
        self.ui.purchasebutton_2.clicked.connect(self.go_to_home)
        # self.ui.purchasebutton_3.clicked.connect(self.go_to_home)
        
    def button_bug_fix(self, button):
        try:
            button.clicked.disconnect()
        except RuntimeError:
            pass  
    
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

    
    def purchase_final(self, page, id=None):
        if not (self.ui.promptpaybutton.isChecked() or self.ui.cashdeliverybutton.isChecked() or self.ui.pickupstorebutton.isChecked()):
            self.show_error("Please choose payment method")
            return

        if self.ui.promptpaybutton.isChecked():
            self.ui.promptpaybutton.setChecked(False)
            print("Promptpay")
            self.go_to_promtpay(page, id)
        else:
            self.show_success("Purchase successful")
            print("Purchase successful")
            self.print_cart()
            self.go_to_purchase_complete()
            
    def go_to_promtpay(self, page, id=None):
        self.ui.stackedWidget.setCurrentWidget(self.ui.purchasepage)
        self.ui.stackedWidget_purchase.setCurrentWidget(self.ui.promppaymethod)
        
        self.ui.purchasebutton_2.clicked.connect(lambda: self.go_to_purchase_complete())
        
        self.button_bug_fix(self.ui.backtochoosingtypebutton)
        self.ui.backtochoosingtypebutton.clicked.connect(functools.partial(self.purchase_cartpage, page, id))
        
        
        if page == "cartpage":
            self.ui.orderlabel_7.setText(f"{str(self.add_total_price_in_cart())}")
        else:
            self.ui.orderlabel_7.setText(f"{str(get_product_price_by_id(id))}")
            
        self.ui.orderlabel_8.setText("")
        
        img_path = "app/assets/images/promptpay.jpg"
        self.ui.orderlabel_8.setStyleSheet(f"background-color: #FFF; image: url({img_path}); border-radius: 0px; padding: 0;")
        
        
    def go_to_purchase_complete(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.purchasepage)
        self.ui.stackedWidget_purchase.setCurrentWidget(self.ui.purchasecomplete)
        
        self.purchaseClicked = True
        
        self.ui.orderlabel_9.setText("")
        img_path = "app/assets/images/success.png"
        self.ui.orderlabel_9.setStyleSheet(f"background-color: #FFF; image: url({img_path}); border-radius: 0px; padding: 0;")
        
        self.ui.backtohomebutton.clicked.connect(lambda: self.go_to_home())
        
        # add to order
        for i in get_user_cart():
            addToOrder(i[0], i[1], i[2], i[3])
            
        print("Order added")
        # print order
        for i in get_user_order():
            print("Order: ", i)
        
        # genetate order id
        # order_id = getOrderID()
        # self.ui.orderlabel_10.setText(f"Order ID: {order_id}")
            

    #cartpage--------------------------------------------------------------------------------------------

    def purchase_cartpage(self, page, id=None, curr_row=None):
        self.ui.listWidget.clear()
        self.ui.promptpaybutton.setChecked(False)
        # self.ui.creditcardbutton.setChecked(False)
        self.ui.cashdeliverybutton.setChecked(False)
        self.ui.pickupstorebutton.setChecked(False)
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.purchasepage)
        self.ui.stackedWidget_purchase.setCurrentWidget(self.ui.choosingtypeofpurchase)
        
        self.ui.firstnameaddressdisplay_2.setText(root.LoggedInUser.user.name)
        self.ui.lastnameaddressdisplay_2.setText(root.LoggedInUser.user.lastname)
        self.ui.phoneaddressdisplay_2.setText(root.LoggedInUser.user.phone)
        self.ui.homenumaddressdisplay_2.setText(root.LoggedInUser.user.address)
        
        if page == "productpage":
            self.button_bug_fix(self.ui.backtocartbutton)
            self.ui.backtocartbutton.clicked.connect(functools.partial(self.go_to_productpage, id))
            self.ui.totalprice.setText(f"{str(get_product_price_by_id(id))}")
            item = f"{get_product_name_by_id(id)} x 1 -------> {get_product_price_by_id(id)}"
            self.ui.listWidget.addItem(item)
            
        elif page == "cartpage_oneitem":
            self.ui.backtocartbutton.clicked.connect(functools.partial(self.go_to_cart))
            product_in_cart = get_user_cart()
            curr_product = product_in_cart[curr_row-1]
            product_details = []
            self.ui.totalprice.setText(f"{str((get_product_price_by_id(curr_product[0])*curr_product[1]))}")

            if curr_product[2] != "":
                product_details.append(curr_product[2])

            if curr_product[3] != "":
                product_details.append(curr_product[3]) 

            details_str = f" ({', '.join(product_details)})" if product_details else ""
            
            item = f"{get_product_name_by_id(curr_product[0])} {details_str}, x {curr_product[1]} -------> {get_product_price_by_id(curr_product[0])}"
            self.ui.listWidget.addItem(item)

            
        else:
            self.ui.backtocartbutton.clicked.connect(functools.partial(self.go_to_cart))
            self.ui.totalprice.setText(f"{str(self.add_total_price_in_cart())}")

            for i in get_user_cart():
                product_details = []

                if i[2] != "":
                    product_details.append(i[2])

                if i[3] != "":
                    product_details.append(i[3]) 

                details_str = f" ({', '.join(product_details)})" if product_details else ""
                
                item = f"{get_product_name_by_id(i[0])} {details_str}, x {i[1]} -------> {get_product_price_by_id(i[0])}"
                self.ui.listWidget.addItem(item)
        
            
        self.purchaseClicked = False
        self.button_bug_fix(self.ui.purchasebutton)
        self.ui.purchasebutton.clicked.connect(functools.partial(self.purchase_final, page, id))
        
            
    def back_to_cart(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.cartpage)
    # def removeorder(self):
    #cartpage--------------------------------------------------------------------------------------------

    #settingspage--------------------------------------------------------------------------------------------
    def go_to_setting(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.settings)
        self.ui.stackedWidget_settings.setCurrentWidget(self.ui.settingsmainpage)
        self.current_index = 0
    def setting_to_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.homepage)
    def go_to_account(self):
        self.ui.stackedWidget_settings.setCurrentWidget(self.ui.accountpage)
        
        self.ui.username.setText(root.LoggedInUser.user.username)
        self.ui.email.setText(root.LoggedInUser.user.email)
        self.ui.phone.setText(root.LoggedInUser.user.phone)
        self.ui.lastname.setText(root.LoggedInUser.user.lastname)
        self.ui.gender.setText(root.LoggedInUser.user.gender)
        self.ui.firstname.setText(root.LoggedInUser.user.name)
        self.ui.birthday.setText(root.LoggedInUser.user.birthday)
        
    def go_to_changepassword(self):
        self.ui.stackedWidget_settings.setCurrentWidget(self.ui.changepasswordpage)
        
        self.ui.savechangebutton_4.clicked.connect(self.save_change_password)
        
    def go_to_editprofile(self):
        self.ui.stackedWidget_settings.setCurrentWidget(self.ui.editprofilesettingspage)
        
        self.ui.userbox_2.setText(root.LoggedInUser.user.username)
        
        if root.LoggedInUser.user.name is not None:
            self.ui.firstnamebox_2.setText(root.LoggedInUser.user.name)
        if root.LoggedInUser.user.lastname is not None:
            self.ui.lastnamebox_2.setText(root.LoggedInUser.user.lastname)
        if root.LoggedInUser.user.gender is not None:
            self.ui.genderbox_2.setText(root.LoggedInUser.user.gender)
        if root.LoggedInUser.user.birthday is not None:
            birthday_date = QDate.fromString(root.LoggedInUser.user.birthday, "yyyy-MM-dd")
            self.ui.birthdaydateEdit_2.setDate(birthday_date)
        if root.LoggedInUser.user.phone is not None:
            self.ui.phonebox_2.setText(root.LoggedInUser.user.phone)
        if root.LoggedInUser.user.email is not None:
            self.ui.emailbox_2.setText(root.LoggedInUser.user.email)
        
        self.ui.savechangebutton_3.clicked.connect(self.save_edit_profile)
        self.ui.deleteaccbutton_2.clicked.connect(self.delete_account)
    def go_to_rule(self):
        self.ui.stackedWidget_settings.setCurrentWidget(self.ui.rulepage)
    def go_to_address(self):
        self.ui.stackedWidget_settings.setCurrentWidget(self.ui.addresssettingspage)
        
        if root.LoggedInUser.user.name is not None:
            self.ui.firstnameaddressdisplay_3.setText(root.LoggedInUser.user.name)
        if root.LoggedInUser.user.lastname is not None:
            self.ui.lastnameaddressdisplay_3.setText(root.LoggedInUser.user.lastname)
        if root.LoggedInUser.user.phone is not None:
            self.ui.phoneaddressdisplay_3.setText(root.LoggedInUser.user.phone)
            
        if root.LoggedInUser.user.address is not None:
            self.ui.addressaddressdisplay_3.setText(root.LoggedInUser.user.address)
        else:
            self.ui.addressaddressdisplay_3.setText("No address set")
        
    def go_to_editaddress(self):
        self.ui.stackedWidget_settings.setCurrentWidget(self.ui.editaddresssettingspage)
        
        if root.LoggedInUser.user.name is not None:
            self.ui.firstnameeditaddrbox.setText(root.LoggedInUser.user.name)
        if root.LoggedInUser.user.lastname is not None:
            self.ui.lastnameeditaddrbox.setText(root.LoggedInUser.user.lastname)
        if root.LoggedInUser.user.phone is not None:
            self.ui.phoneeditaddrbox.setText(root.LoggedInUser.user.phone)
        if root.LoggedInUser.user.address is not None:
            self.ui.addresseditaddrbox.setText(root.LoggedInUser.user.address)
        
        self.ui.savechangeeditaddrbutton.clicked.connect(self.save_edit_address)
        
    def save_change_password(self):
        if changePassword(root.LoggedInUser.user.username, self.ui.curpasstextbox.text(), self.ui.newpasstextbox.text()):
            self.show_success("Password changed")
            self.ui.curpasstextbox.clear()
            self.ui.newpasstextbox.clear()
        else:
            self.show_error("Incorrect password")

        
    def delete_account(self):
        if self.show_yes_no("Are you sure you want to delete your account?") == QMessageBox.Yes:
            deleteProfile(root.LoggedInUser.user.username)
            self.show_goodbye("Account deleted")
            self.back_to_login()
        
    def save_edit_profile(self):
        # root.LoggedInUser.user.name = self.ui.firstnamebox_2.text()
        # root.LoggedInUser.user.lastname = self.ui.lastnamebox_2.text()
        # root.LoggedInUser.user.gender = self.ui.genderbox_2.text()
        # root.LoggedInUser.user.birthday = self.ui.birthdaydateEdit_2.text()
        # root.LoggedInUser.user.phone = self.ui.phonebox_2.text()
        # root.LoggedInUser.user.email = self.ui.emailbox_2.text()
        
        if self.show_yes_no("Are you sure you want to save changes?") == QMessageBox.Yes:
            birthday_date = self.ui.birthdaydateEdit_2.date()
            birthday_date_str = birthday_date.toString("yyyy-MM-dd")
            if editProfile(root.LoggedInUser.user.username, self.ui.firstnamebox_2.text(), self.ui.lastnamebox_2.text(), self.ui.genderbox_2.text(), birthday_date_str, self.ui.emailbox_2.text(), self.ui.phonebox_2.text()):
                self.show_success("Changes saved")
            else:
                self.show_error("Changes not saved")
        else:
            self.show_error("Changes not saved")
        
    def save_edit_address(self):
        # root.LoggedInUser.user.name = self.ui.firstnameeditaddrbox.text()
        # root.LoggedInUser.user.lastname = self.ui.lastnameeditaddrbox.text()
        # root.LoggedInUser.user.phone = self.ui.phoneeditaddrbox.text()
        # root.LoggedInUser.user.address = self.ui.editaddress.text()
        
        if self.show_yes_no("Are you sure you want to save changes?") == QMessageBox.Yes:
            if editAddress(root.LoggedInUser.user.username, self.ui.addresseditaddrbox.text()):
                self.show_success("Changes saved")
                self.go_to_address()
            else:
                self.show_error("Changes not saved")
                
        else:
            self.show_error("Changes not saved")
            self.go_to_address()
        
    #settingspage--------------------------------------------------------------------------------------------
        

    #settingsAdminpage--------------------------------------------------------------------------------------------
    def go_to_settingAdmin(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.settings_admin)
        self.ui.stackedWidget_settingadmin.setCurrentWidget(self.ui.settingsadminmainpage)
    def settingadmin_to_homeadmin(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.adminwidget)
        self.ui.stackedWidget_adminwidget.setCurrentWidget(self.ui.adminmain)
        self.ui.stackedWidget_adminmain.setCurrentWidget(self.ui.homepage_admin)
    def go_to_shopaccount(self):
        self.ui.stackedWidget_settingadmin.setCurrentWidget(self.ui.shopaccountadminpage)
        
        # self.ui.username.setText(root.LoggedInUser.user.username)
        # self.ui.email.setText(root.LoggedInUser.user.email)
        # self.ui.phone.setText(root.LoggedInUser.user.phone)
        # self.ui.lastname.setText(root.LoggedInUser.user.lastname)
        # self.ui.gender.setText(root.LoggedInUser.user.gender)
        # self.ui.firstname.setText(root.LoggedInUser.user.name)
        # self.ui.birthday.setText(root.LoggedInUser.user.birthday)
        
    def go_to_editshop(self):
        self.ui.stackedWidget_settingadmin.setCurrentWidget(self.ui.editshopaccountadminpage)
        
        self.ui.shopnamebox_2.setText(root.LoggedInUser.user.shopname)
        
        if root.LoggedInUser.user.name is not None:
            self.ui.firstnamebox_admin_2.setText(root.LoggedInUser.user.name)
        if root.LoggedInUser.user.lastname is not None:
            self.ui.lastnamebox_admin_2.setText(root.LoggedInUser.user.lastname)
        if root.LoggedInUser.user.description is not None:
            self.ui.descriptionbox_admin_2.setText(root.LoggedInUser.user.description)
        if root.LoggedInUser.user.address is not None:
            self.ui.addressbox_admin_2.setText(root.LoggedInUser.user.address)
        if root.LoggedInUser.user.phone is not None:
            self.ui.phonebox_admin_2.setText(root.LoggedInUser.user.phone)
        if root.LoggedInUser.user.email is not None:
            self.ui.emailbox_admin_2.setText(root.LoggedInUser.user.email)
            
        self.ui.adminregisterbutton_2.clicked.connect(self.save_edit_shop)
        # self.ui.deleteaccbutton_5.clicked.connect(self.delete_account)
    
        
    def go_to_ruleshop(self):
        self.ui.stackedWidget_settingadmin.setCurrentWidget(self.ui.ruleadminpage)
    def exit_shop(self):
        changeLoggedinUserToCustomer(root.LoggedInUser.user.username)
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.homepage)
        self.display_product(True, "homepage_customer")
        
    def save_edit_shop(self):
        if self.show_yes_no("Are you sure you want to save changes?") == QMessageBox.Yes:
            if editShopProfile(root.LoggedInUser.user.username, self.ui.firstnamebox_admin_2.text(), self.ui.lastnamebox_admin_2.text(), self.ui.descriptionbox_admin_2.text(), self.ui.addressbox_admin_2.text(), self.ui.phonebox_admin_2.text(), self.ui.emailbox_admin_2.text()):
                self.show_success("Changes saved")
            else:
                self.show_error("Changes not saved")
        else:
            self.show_error("Changes not saved")
            
    def delete_shop_account(self):
        if self.show_yes_no("Are you sure you want to delete your account?") == QMessageBox.Yes:
            deleteShopProfile(root.LoggedInUser.user.username)
            self.show_goodbye("Account deleted")
            self.back_to_login()
    #settingsAdminpage--------------------------------------------------------------------------------------------

    #orderAdminspage--------------------------------------------------------------------------------------------
    def go_to_orderstatus(self):
        print("go to order status")
        self.ui.stackedWidget_orderadmin.setCurrentWidget(self.ui.tobeshipadminpage)
        self.ui.homebutton_admin.setStyleSheet(inactive_button_style)
        self.ui.productsbutton_admin.setStyleSheet(inactive_button_style)
        self.ui.orderstatusbutton_admin.setStyleSheet(active_button_style)
        self.ui.homebutton_admin.clicked.connect(self.go_to_homepage_admin)
        self.ui.productsbutton_admin.clicked.connect(self.go_to_productspage_admin)
        self.orderstatus_tobeship()
        
    def orderstatus_tobeship(self):
        self.ui.stackedWidget_adminmain.setCurrentWidget(self.ui.orderstatus_admin)
        self.ui.stackedWidget_orderadmin.setCurrentWidget(self.ui.tobeshipadminpage)
        self.ui.toshipadminbutton.setStyleSheet(active_orderbutton_style)
        self.order_ship(True, "tobeship")
    def orderstatus_complete(self):
        self.ui.stackedWidget_orderadmin.setCurrentWidget(self.ui.completeadminpage)
        self.ui.toshipadminbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.canceladminvutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.reviewsadminvutton.setStyleSheet(inactive_orderbutton_style)


    def display_orderstatus(self, page):
        if page == "tobeship":
            self.ui.tobeshipadminpage.clear()
            
    #orderAdminspage--------------------------------------------------------------------------------------------

    def adminmain_to_orderstatus_tobeship(self):
        self.ui.stackedWidget_adminmain.setCurrentWidget(self.ui.orderstatus_admin)
        self.ui.stackedWidget_orderadmin.setCurrentWidget(self.ui.tobeshipadminpage)
        self.ui.toshipadminbutton.setStyleSheet(active_orderbutton_style)
        self.ui.homebutton_admin.setStyleSheet(inactive_button_style)
        self.ui.productsbutton_admin.setStyleSheet(inactive_button_style)
        self.ui.orderstatusbutton_admin.setStyleSheet(active_button_style)
        self.order_ship(True, "tobeship")

    def go_to_productpage(self, id):
        print("==============go to product page==============")
        print("id: ", id)

        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.productviewpage)

        self.ui.homebutton.setStyleSheet(inactive_button_style)
        self.ui.favbutton.setStyleSheet(inactive_button_style)
        self.ui.orderbutton.setStyleSheet(inactive_button_style)

        self.ui.homebutton.clicked.connect(self.go_to_home)
        self.ui.favbutton.clicked.connect(self.go_to_favorite)
        # self.ui.orderbutton.clicked.connect(functools.partial(self.go_to_order_ship))
        self.ui.settingbutton.clicked.connect(self.go_to_setting)
        # self.ui.cartbutton.clicked.connect(self.go_to_cart)
        self.ui.profilebutton.clicked.connect(self.go_to_userprofile)
        # self.ui.loginsignoutbutton.clicked.connect(self.back_to_login)
        # self.ui.viewshopbutton.clicked.connect(self.go_to_shoppage)

        self.ui.productname.setText(get_product_name_by_id(id))
        self.ui.productprice.setText(f"{str(get_product_price_by_id(id))}")
        img_path = get_first_img_for_product(id)
        pixmap = QPixmap(img_path)
        self.ui.mainpic.setPixmap(pixmap)
        self.ui.mainpic.setScaledContents(True)
        self.ui.numberofsold.setText(f"{str(get_product_sold_by_id(id))} Sold")
        
        self.ui.shopname.setText(get_shopname_by_product_id(id))
        shopproduct_len = str(len(get_products_for_user(get_shopname_by_product_id(id))))
        self.ui.numproduct_3.setText(shopproduct_len)
        self.ui.numreview_3.setText(str(get_shop_reviews_by_product_id(id)))
        self.ui.descriptioninfolabel_productviewpage.setText(get_product_description_by_id(id))
        
        # click next and prev image button
        try:
            self.ui.prevpicbutton.clicked.disconnect()
        except RuntimeError:
            pass  # Do nothing if no connections were present
        try:
            self.ui.nextpicbutton.clicked.disconnect()
        except RuntimeError:
            pass  # Do nothing if no connections were present
        
        if len(get_product_img_by_id(id)) > 1:
            self.ui.prevpicbutton.show()
            self.ui.nextpicbutton.show()
            self.current_index = 0
            
            self.ui.prevpicbutton.clicked.connect(functools.partial(self.change_pic, id, "prev"))
            self.ui.nextpicbutton.clicked.connect(functools.partial(self.change_pic, id, "next"))
        else:
            self.ui.prevpicbutton.hide()
            self.ui.nextpicbutton.hide()
            
        # display size
        self.selectedSizeButton = None
        self.selectedSizeText = ""
        
        size_widget = []
        column = 1
        row = 1
        while self.ui.gridLayout_size_productviewpage.count():
            item = self.ui.gridLayout_size_productviewpage.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        if get_product_sizes_by_id(id) != []:
            sizes = get_product_sizes_by_id(id)
            for size in sizes:
                if column > 4:
                    horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
                    self.ui.gridLayout_size_productviewpage.addItem(horizontalSpacer, row, column, 1, 1)
                    column = 1
                    row += 1
                sbutton = QPushButton(self.ui.frame_size_productviewpage)
                sbutton.setObjectName(f"sbutton_{size}")
                sbutton.setText(size)
                sbutton.setMinimumSize(QSize(70, 21))
                sbutton.setMaximumSize(QSize(70, 21))
                sbutton.setStyleSheet(u"QPushButton {	\n"
                "	color:#545454;\n"
                "	font-family: Suwannaphum;\n"
                "	background: #F4F2EF;\n"
                "	font-size: 16px;\n"
                "	font-style: normal;\n"
                "	font-weight: 400;\n"
                "	line-height: normal;\n"
                "	border-radius: 5px;\n"
                "	border: 1px solid #545454;\n"
                "}\n"
                "QPushButton:hover {\n"
                "	background: #F4DBDB;\n"
                "}")
                
                self.button_bug_fix(sbutton)
                sbutton.clicked.connect(functools.partial(self.buttonSizeClicked, sbutton))
        

                self.ui.gridLayout_size_productviewpage.addWidget(sbutton, row, column, 1, 1)
                column += 1
            horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            self.ui.gridLayout_size_productviewpage.addItem(horizontalSpacer, row, column + 1, 1, 1)
            
        # -----------------------------------------------------------------------------------------
        
        
        
        
        
        
        
        # -----------------------------------------------------------------------------------------
        # display options
        
        self.selectedOptionButton = None
        self.selectedOptionText = ""
        
        column = 1
        row = 1
        while self.ui.gridLayout_option_productviewpage.count():
            item = self.ui.gridLayout_option_productviewpage.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        if get_product_options_by_id(id) != []:
            options = get_product_options_by_id(id)
            for opt in options:
                if column > 3:
                    horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
                    self.ui.gridLayout_option_productviewpage.addItem(horizontalSpacer, row, column, 1, 1)
                    column = 1
                    row += 1
                optbutton = QPushButton(self.ui.frame_size_productviewpage)
                optbutton.setObjectName(f"optbutton_{opt}")
                optbutton.setText(opt)
                optbutton.setMinimumSize(QSize(100, 25))
                optbutton.setMaximumSize(QSize(100, 25))
                optbutton.setStyleSheet(u"QPushButton {	\n"
                "	color:#545454;\n"
                "	font-family: Suwannaphum;\n"
                "	background: #F4F2EF;\n"
                "	font-size: 16px;\n"
                "	font-style: normal;\n"
                "	font-weight: 400;\n"
                "	line-height: normal;\n"
                "	border-radius: 5px;\n"
                "	border: 1px solid #545454;\n"
                "}\n"
                "QPushButton:hover {\n"
                "	background: #F4DBDB;\n"
                "}")
                
                
                self.button_bug_fix(optbutton)
                optbutton.clicked.connect(functools.partial(self.buttonOptionClicked, optbutton))

                self.ui.gridLayout_option_productviewpage.addWidget(optbutton, row, column, 1, 1)
                column += 1
            horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            self.ui.gridLayout_option_productviewpage.addItem(horizontalSpacer, row, column + 1, 1, 1) 

        try:
            self.ui.addtocartbutton.clicked.disconnect()
        except RuntimeError:
            pass 
        try:
            self.ui.buynowbutton.clicked.disconnect()
        except RuntimeError:
            pass 

        
        self.ui.addtocartbutton.clicked.connect(functools.partial(self.add_to_cart, id))
        self.ui.buynowbutton.clicked.connect(functools.partial(self.purchase_cartpage, "productpage", id))

    def buttonSizeClicked(self, button):
        # Reset the previously selected button's style if it exists and is not the current button
        if self.selectedSizeButton and self.selectedSizeButton != button:
            self.selectedSizeButton.setStyleSheet(u"QPushButton {	\n"
                                              "	color:#545454;\n"
                                              "	font-family: Suwannaphum;\n"
                                              "	background: #F4F2EF;\n"
                                              "	font-size: 16px;\n"
                                              "	font-style: normal;\n"
                                              "	font-weight: 400;\n"
                                              "	line-height: normal;\n"
                                              "	border-radius: 5px;\n"
                                              "	border: 1px solid #545454;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "	background: #F4DBDB;\n"
                                              "}")
        
        # Apply the selected style to the new button
        button.setStyleSheet(u"QPushButton {	\n"
                             "	color:#545454;\n"
                             "	font-family: Suwannaphum;\n"
                             "	background: #F4DBDB;\n"  # Use the hover background color
                             "	font-size: 16px;\n"
                             "	font-style: normal;\n"
                             "	font-weight: 400;\n"
                             "	line-height: normal;\n"
                             "	border-radius: 5px;\n"
                             "	border: 1px solid #545454;\n"
                             "}")
        
        # Update the selectedButton attribute to reference the newly clicked button
        self.selectedSizeButton = button
        self.selectedSizeText = button.text()
        
        print(f"Selected size: {self.selectedSizeText}")
        
    
    def buttonOptionClicked(self, button):
        # Reset the previously selected button's style if it exists and is not the current button
        if self.selectedOptionButton and self.selectedOptionButton != button:
            self.selectedOptionButton.setStyleSheet(u"QPushButton {	\n"
                                              "	color:#545454;\n"
                                              "	font-family: Suwannaphum;\n"
                                              "	background: #F4F2EF;\n"
                                              "	font-size: 16px;\n"
                                              "	font-style: normal;\n"
                                              "	font-weight: 400;\n"
                                              "	line-height: normal;\n"
                                              "	border-radius: 5px;\n"
                                              "	border: 1px solid #545454;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "	background: #F4DBDB;\n"
                                              "}")
        
        # Apply the selected style to the new button
        button.setStyleSheet(u"QPushButton {	\n"
                             "	color:#545454;\n"
                             "	font-family: Suwannaphum;\n"
                             "	background: #F4DBDB;\n"  # Use the hover background color
                             "	font-size: 16px;\n"
                             "	font-style: normal;\n"
                             "	font-weight: 400;\n"
                             "	line-height: normal;\n"
                             "	border-radius: 5px;\n"
                             "	border: 1px solid #545454;\n"
                             "}")
        
        # Update the selectedButton attribute to reference the newly clicked button
        self.selectedOptionButton = button
        self.selectedOptionText = button.text()
        
        print(f"Selected option: {self.selectedOptionText}")
    

    def change_pic(self, id, direction):
        print("===========changing pic===========")
        print("product id: ", id)
        img_paths = get_product_img_by_id(id)
        print("img_paths: ", img_paths)
        
        print("current index: ", self.current_index)

        if direction == "prev":
            print("prev")
            print("current index: ", self.current_index)
            if self.current_index == 0:
                self.current_index = len(img_paths)
            self.current_index -= 1
            print("prev (curr ind): ", self.current_index)
        elif direction == "next":
            print("next")
            print("current index: ", self.current_index)
            if self.current_index == len(img_paths) - 1:
                self.current_index = -1
            self.current_index += 1
            print("next (curr ind): ", self.current_index)
            
        print("curr index: ",self.current_index)
        next_img_path = img_paths[self.current_index]
        print("next_img_path: ", next_img_path)
        self.ui.mainpic.setPixmap(QPixmap(next_img_path))
        self.ui.mainpic.setScaledContents(True)
        # img_paths = []
        print("===========change pic===========")

    def go_to_home(self):
        print("go to home")
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.homepage)
        self.ui.homebutton.setStyleSheet(active_button_style)
        self.ui.favbutton.setStyleSheet(inactive_button_style)
        self.ui.orderbutton.setStyleSheet(inactive_button_style)
        
        total_num_of_products = len(get_all_products())
        if total_num_of_products > 0:
            # self.display_product_main(6)
            self.display_product(False, "homepage_customer")
            # self.display_product_main(get_random_product_id())

        self.current_index = 0
            
    def print_cart(self):
        print("------------------CART------------------")
        if root.LoggedInUser.logged_in:
            for i in get_user_cart():
                print("products in cart and id: ", (get_product_name_by_id(i[0])), i[1])
                print("product size: ", i[2])
                print("product option: ", i[3])
                print("Total product price in cart: ", self.add_total_price_in_cart())
        print("---------------------------------------")
    
    def add_total_price_in_cart(self):
        total_price = 0
        for i in get_user_cart():
            total_price += (i[1] * (get_product_price_by_id(i[0])))
        return total_price

    def add_to_cart(self, id):
        
        if addToCart(id, self.selectedSizeText, self.selectedOptionText):
            self.show_success("Product added to cart")
            print("Product added to cart")
            self.print_cart()
            self.go_to_productpage(id)

            
    # def go_to_buy(self):
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.purchasepage)
    #     self.ui.stackedWidget_purchase.setCurrentWidget(self.ui.choosingtypeofpurchase)
    #     self.ui.backtocartbutton.clicked.connect(self.go_to_cart)
    
    def remove_item_from_cart(self, product_id):
        if removeFromCart(product_id):
            transaction.commit()
            self.show_success("Product removed from cart")
            print("Product removed from cart")
            self.print_cart()
        else:
            self.show_error("Product remove failed")
            print("Product remove failed")
            self.print_cart()
    
    def go_to_cart(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.cartpage)
        
        # get cart
        user = root.LoggedInUser.user.username
        cart_products = get_user_cart()
        
        self.print_cart()
        
        self.display_cart(cart_products)
        
        # for i in cart_products:
        #     self.ui.shopnameforcart.setText(get_shopname_by_product_id(i[0]))
        #     self.ui.productcartname.setText(get_product_name_by_id(i[0]))
        #     self.ui.productcartdescrip.setText(get_product_description_by_id(i[0]))
        #     self.ui.totalpricecartnumlabel.setText(str(get_product_price_by_id(i[0]) * i[1]))
        #     self.ui.productnum.setText(f"{i[1]} piece")
        #     self.ui.cartorderpic.setPixmap(QPixmap(get_first_img_for_product(i[0])))
        #     self.ui.cartorderpic.setScaledContents(True)
            
        #     self.ui.removecartbutton.clicked.connect(lambda: self.remove_item_from_cart(i[0]))
        #     self.ui.purchasecartbutton.clicked.connect(lambda: self.purchase_cartpage("cartpage"))
        self.current_index = 0

    def display_cart(self, cart_products):
        row = len(cart_products) - 1

        products_to_remove = []

        for product in cart_products:
            for add in self.addedproduct_cart:
                if add == product:
                    products_to_remove.append(product)
        for product in products_to_remove:
            cart_products.remove(product)


        for product in cart_products:
            row += 1
            if row > 1:
                self.ui.scrollAreaWidgetContents_4.setMinimumHeight(400 * row)
            self.ui.frame_cartpage.setMinimumHeight(400 * row)
            self.ui.frame_cartshop.setMinimumHeight(289 * row)

            self.cartshopcontainer = QWidget(self.ui.frame_cartshop)
            self.cartshopcontainer.setObjectName(f"cartshopcontainer_{product[0]}")
            self.cartshopcontainer.setMinimumSize(QSize(891, 270))
            self.cartshopcontainer.setMaximumSize(QSize(891, 270))
            self.cartshopcontainer.setStyleSheet(u"border-bottom: 2px solid #CD4662;\n"
    "background: #FAF9F6;\n"
    "")
            self.gridLayout_cartshopcontainer = QGridLayout(self.cartshopcontainer)
            self.gridLayout_cartshopcontainer.setObjectName(u"gridLayout_cartshopcontainer")
            self.gridLayout_cartshopcontainer.setHorizontalSpacing(25)
            self.gridLayout_cartshopcontainer.setVerticalSpacing(15)
            self.gridLayout_cartshopcontainer.setContentsMargins(20, 0, 0, 0)
            self.frame_cartshopinfo = QFrame(self.cartshopcontainer)
            self.frame_cartshopinfo.setObjectName(u"frame_cartshopinfo")
            self.frame_cartshopinfo.setMinimumSize(QSize(651, 135))
            self.frame_cartshopinfo.setMaximumSize(QSize(651, 135))
            self.frame_cartshopinfo.setStyleSheet(u"border: none;")
            self.frame_cartshopinfo.setFrameShape(QFrame.StyledPanel)
            self.frame_cartshopinfo.setFrameShadow(QFrame.Raised)
            self.gridLayout_cartshopinfo = QGridLayout(self.frame_cartshopinfo)
            self.gridLayout_cartshopinfo.setObjectName(u"gridLayout_cartshopinfo")
            self.gridLayout_cartshopinfo.setHorizontalSpacing(10)
            self.gridLayout_cartshopinfo.setVerticalSpacing(32)
            self.gridLayout_cartshopinfo.setContentsMargins(0, 0, 0, 0)
            self.horizontalSpacer_12 = QSpacerItem(70, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            self.gridLayout_cartshopinfo.addItem(self.horizontalSpacer_12, 0, 4, 1, 1)

            self.totalpricecartnumlabel = QLabel(self.frame_cartshopinfo)
            self.totalpricecartnumlabel.setObjectName(u"totalpricecartnumlabel")
            self.totalpricecartnumlabel.setMinimumSize(QSize(69, 22))
            self.totalpricecartnumlabel.setMaximumSize(QSize(100, 22))
            self.totalpricecartnumlabel.setStyleSheet(u"border: none;\n"
    "color: #cd4662;\n"
    "font-family: Suwannaphum;\n"
    "font-size: 16px;\n"
    "font-style: normal;\n"
    "font-weight: 400;\n"
    "line-height: normal;")

            self.gridLayout_cartshopinfo.addWidget(self.totalpricecartnumlabel, 2, 3, 1, 2)

            horizontalSpacer_11 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            self.gridLayout_cartshopinfo.addItem(horizontalSpacer_11, 1, 4, 1, 1)

            self.totalpricecartlabel = QLabel(self.frame_cartshopinfo)
            self.totalpricecartlabel.setObjectName(u"totalpricecartlabel")
            self.totalpricecartlabel.setMinimumSize(QSize(80, 28))
            self.totalpricecartlabel.setMaximumSize(QSize(80, 28))
            self.totalpricecartlabel.setStyleSheet(u"border: none;\n"
    "color: #000;\n"
    "font-family: Suwannaphum;\n"
    "font-size: 16px;\n"
    "font-style: normal;\n"
    "font-weight: 400;\n"
    "line-height: normal;")

            self.gridLayout_cartshopinfo.addWidget(self.totalpricecartlabel, 2, 1, 1, 1)

            # self.horizontalSpacer_10 = QSpacerItem(178, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            # self.gridLayout_cartshopinfo.addItem(self.horizontalSpacer_10, 1, 1, 1, 3)

            self.productcartname = QLabel(self.frame_cartshopinfo)
            self.productcartname.setObjectName(u"productcartname")
            self.productcartname.setMinimumSize(QSize(391, 28))
            self.productcartname.setMaximumSize(QSize(391, 28))
            self.productcartname.setStyleSheet(u"border: none;\n"
    "color: #000;\n"
    "font-family: Suwannaphum;\n"
    "font-size: 16px;\n"
    "font-style: normal;\n"
    "font-weight: 400;\n"
    "line-height: normal;")

            self.gridLayout_cartshopinfo.addWidget(self.productcartname, 0, 0, 1, 1)

            self.horizontalSpacer_9 = QSpacerItem(178, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            self.gridLayout_cartshopinfo.addItem(self.horizontalSpacer_9, 0, 1, 1, 3)

            self.productcartdescrip = QLabel(self.frame_cartshopinfo)
            self.productcartdescrip.setObjectName(u"productcartdescrip")
            self.productcartdescrip.setMinimumSize(QSize(391, 28))
            self.productcartdescrip.setMaximumSize(QSize(391, 28))
            self.productcartdescrip.wordWrap = False
            self.productcartdescrip.setStyleSheet(u"border: none;\n"
    "color: #545454;\n"
    "font-family: Suwannaphum;\n"
    "font-size: 16px;\n"
    "font-style: normal;\n"
    "font-weight: 400;\n"
    "line-height: normal;")

            self.gridLayout_cartshopinfo.addWidget(self.productcartdescrip, 1, 0, 1, 1)

            self.productnum = QLabel(self.frame_cartshopinfo)
            self.productnum.setObjectName(u"productnum")
            self.productnum.setMinimumSize(QSize(391, 28))
            self.productnum.setMaximumSize(QSize(391, 28))
            self.productnum.setStyleSheet(u"border: none;\n"
    "color: #545454;\n"
    "font-family: Suwannaphum;\n"
    "font-size: 16px;\n"
    "font-style: normal;\n"
    "font-weight: 400;\n"
    "line-height: normal;")

            self.gridLayout_cartshopinfo.addWidget(self.productnum, 2, 0, 1, 1)

            # self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            # self.gridLayout_cartshopinfo.addItem(self.horizontalSpacer_37, 2, 2, 1, 1)


            self.gridLayout_cartshopcontainer.addWidget(self.frame_cartshopinfo, 1, 2, 1, 3)

            self.horizontalSpacer_14 = QSpacerItem(31, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            self.gridLayout_cartshopcontainer.addItem(self.horizontalSpacer_14, 0, 1, 1, 1)

            self.horizontalSpacer_15 = QSpacerItem(656, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            self.gridLayout_cartshopcontainer.addItem(self.horizontalSpacer_15, 0, 2, 1, 3)

            self.cartorderpic = QLabel(self.cartshopcontainer)
            self.cartorderpic.setObjectName(u"cartorderpic")
            self.cartorderpic.setMinimumSize(QSize(135, 135))
            self.cartorderpic.setMaximumSize(QSize(135, 135))
            self.cartorderpic.setStyleSheet(u"border: none;\n"
    "border-radius: 70px;\n"
    "background: #cd4662;")

            self.gridLayout_cartshopcontainer.addWidget(self.cartorderpic, 1, 0, 1, 1)

            self.horizontalSpacer_13 = QSpacerItem(31, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            self.gridLayout_cartshopcontainer.addItem(self.horizontalSpacer_13, 1, 1, 1, 1)

            self.shopnameforcart = QLabel(self.cartshopcontainer)
            self.shopnameforcart.setObjectName(u"shopnameforcart")
            self.shopnameforcart.setStyleSheet(u"border: none;\n"
    "color: #000;\n"
    "font-family: Suwannaphum;\n"
    "font-size: 20px;\n"
    "font-style: normal;\n"
    "font-weight: 700;\n"
    "line-height: normal;")

            self.gridLayout_cartshopcontainer.addWidget(self.shopnameforcart, 0, 0, 1, 1)

            self.horizontalSpacer_16 = QSpacerItem(31, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            self.gridLayout_cartshopcontainer.addItem(self.horizontalSpacer_16, 2, 1, 1, 1)

            self.horizontalSpacer_17 = QSpacerItem(294, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            self.gridLayout_cartshopcontainer.addItem(self.horizontalSpacer_17, 2, 2, 1, 1)

            self.removecartbutton = QPushButton(self.cartshopcontainer)
            self.removecartbutton.setObjectName(u"removecartbutton")
            self.removecartbutton.setText("Remove")
            self.removecartbutton.setMinimumSize(QSize(156, 42))
            self.removecartbutton.setMaximumSize(QSize(156, 42))
            self.removecartbutton.setStyleSheet(u"color: #FFF;\n"
    "background-color: #cd4662;\n"
    "border: none;\n"
    "text-align: center;\n"
    "font-family: Suwannaphum;\n"
    "font-size: 16px;\n"
    "font-style: normal;\n"
    "font-weight: 700;\n"
    "line-height: normal;\n"
    "border-radius: 5px;")

            self.gridLayout_cartshopcontainer.addWidget(self.removecartbutton, 2, 3, 1, 1)

            self.verticalSpacer = QSpacerItem(20, 76, QSizePolicy.Minimum, QSizePolicy.Expanding)

            self.gridLayout_cartshopcontainer.addItem(self.verticalSpacer, 2, 0, 1, 1)

            self.purchasecartbutton = QPushButton(self.cartshopcontainer)
            self.purchasecartbutton.setObjectName(u"purchasecartbutton")
            self.purchasecartbutton.setText("Purchase")
            self.purchasecartbutton.setMinimumSize(QSize(156, 42))
            self.purchasecartbutton.setMaximumSize(QSize(156, 42))
            self.purchasecartbutton.setStyleSheet(u"color: #FFF;\n"
    "background-color: #AEC289;\n"
    "border: none;\n"
    "text-align: center;\n"
    "font-family: Suwannaphum;\n"
    "font-size: 16px;\n"
    "font-style: normal;\n"
    "font-weight: 700;\n"
    "line-height: normal;\n"
    "border-radius: 5px;")

            self.gridLayout_cartshopcontainer.addWidget(self.purchasecartbutton, 2, 4, 1, 1)
            self.ui.verticalLayout_cartshop.addWidget(self.cartshopcontainer)


            # setText
            
            product_details = []

            if product[2] != "":
                product_details.append(product[2])

            if product[3] != "":
                product_details.append(product[3])

            details_str = f" ({', '.join(product_details)})" if product_details else ""

            self.productcartname.setText(f"{get_product_name_by_id(product[0])}{details_str}")
            
            self.shopnameforcart.setText(get_shopname_by_product_id(product[0]))
            self.productcartdescrip.setText(get_product_description_by_id(product[0]))
            self.totalpricecartlabel.setText("Total Price:")
            self.totalpricecartnumlabel.setText("฿ " + str(get_product_price_by_id(product[0]) * product[1]))
            self.productnum.setText(f"{product[1]} piece")
            self.cartorderpic.setPixmap(QPixmap(get_first_img_for_product(product[0])))
            self.cartorderpic.setScaledContents(True)

            # remove and purchase button
            self.purchasecartbutton.clicked.connect(functools.partial(self.purchase_item_from_cart, product[0], row))
            self.removecartbutton.clicked.connect(functools.partial(self.remove_item_from_cart, product[0], row))

        for i in cart_products:
            self.addedproduct_cart.append(i)
        # print("addedproduct_cart: ", self.addedproduct_cart)
        
    def purchase_item_from_cart(self, product_id, curr_row):
        print("curr_row", curr_row)
        print("product_id", product_id)
        self.purchase_cartpage("cartpage_oneitem", product_id, curr_row)
        
        if self.purchaseClicked:
            if removeFromCart(product_id):
                transaction.commit()
                # self.show_success("Product removed from cart")
                print("Product removed from cart")
                self.print_cart()

                cartshopcontainer = self.findChild(QWidget, f"cartshopcontainer_{product_id}")
                cartshopcontainer.deleteLater()
                if curr_row > 1:
                    self.ui.scrollAreaWidgetContents_4.setMinimumHeight(400 * (curr_row - 1))
                    self.ui.frame_cartpage.setMinimumHeight(400 * (curr_row - 1))
                    self.ui.frame_cartshop.setMinimumHeight(289 * (curr_row - 2))

                    geometry = self.ui.scrollAreaWidgetContents_4.geometry()
                    self.ui.scrollAreaWidgetContents_4.setGeometry(QRect(geometry.x, geometry.y, geometry.width, 400 * (curr_row - 1)))
                    geometry = self.ui.frame_cartpage.geometry()
                    self.ui.frame_cartpage.setGeometry(QRect(geometry.x, geometry.y, geometry.width, 400 * (curr_row - 1)))
                    geometry = self.ui.frame_cartshop.geometry()
                    self.ui.frame_cartshop.setGeometry(QRect(geometry.x, geometry.y, geometry.width, 289  * (curr_row - 2)))
                    geometry = self.ui.purchaseallcartbutton.geometry()
                    self.ui.purchaseallcartbutton.setGeometry(QRect(geometry.x, geometry.y - 400, geometry.width, geometry.height))

                self.go_to_cart()
            else:
                self.show_error("Product remove failed")
                print("Product remove failed")
                self.print_cart()
        
        
    def remove_item_from_cart(self, product_id, curr_row):
        if removeFromCart(product_id):
            transaction.commit()
            self.show_success("Product removed from cart")
            print("Product removed from cart")
            self.print_cart()

            cartshopcontainer = self.findChild(QWidget, f"cartshopcontainer_{product_id}")
            cartshopcontainer.deleteLater()
            if curr_row > 1:
                self.ui.scrollAreaWidgetContents_4.setMinimumHeight(400 * (curr_row - 1))
                self.ui.frame_cartpage.setMinimumHeight(400 * (curr_row - 1))
                self.ui.frame_cartshop.setMinimumHeight(289 * (curr_row - 2))

                geometry = self.ui.scrollAreaWidgetContents_4.geometry()
                self.ui.scrollAreaWidgetContents_4.setGeometry(QRect(geometry.x(), geometry.y(), geometry.width(), 400 * (curr_row - 1)))
                geometry = self.ui.frame_cartpage.geometry()
                self.ui.frame_cartpage.setGeometry(QRect(geometry.x(), geometry.y(), geometry.width(), 400 * (curr_row - 1)))
                geometry = self.ui.frame_cartshop.geometry()
                self.ui.frame_cartshop.setGeometry(QRect(geometry.x(), geometry.y(), geometry.width(), 289  * (curr_row - 2)))
                geometry = self.ui.purchaseallcartbutton.geometry()
                self.ui.purchaseallcartbutton.setGeometry(QRect(geometry.x(), geometry.y() - 400, geometry.width(), geometry.height))


            self.go_to_cart()
        else:
            self.show_error("Product remove failed")
            print("Product remove failed")
            self.print_cart()
        
    def purchase_all_cart(self):                
        self.button_bug_fix(self.ui.buynowbutton)
        
        self.ui.buynowbutton.clicked.connect(functools.partial(self.purchase_cartpage, "cartpage"))
    
    def check_status_ship(self, message, status, order=[], admin=False):
        self.input_trackno = False
        self.word = "word"
        if not admin:
            print("not admin")
            if status == "Processing":
                self.word = "is being processed"
            elif status == "Shipped":
                self.word = f"Tracking number: {message}"
        else:
            print("admin")
            if status == "Processing":
                self.input_trackno = True
            elif status == "Shipped":
                self.word = f"Tracking number: {message}"

        if self.input_trackno:
            text, ok_pressed = QInputDialog.getText(self, "Input tracking no.", "Enter:")
            if ok_pressed:
                tracking = add_tracking_no(text, order)
                print("tracking: ", tracking)
                order[5] = "Shipped"
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(self.word)
            msg.setWindowTitle("Order Status")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
    
    def order_ship(self, admin=False, page=""):
        print("order_ship called")
        if admin and page == "tobeship":
            product_order = get_order_by_adminname(root.LoggedInUser.user.username)
            curr_frame_tobeship = self.ui.frame_tobeshipped_2
            curr_scroll = self.ui.scrollAreaWidgetContents_tobeshipped_2
            curr_vertical = self.ui.verticalLayout_shiporder_2
        else:
            product_order = get_user_order()
            curr_frame_tobeship = self.ui.frame_tobeshipped
            curr_scroll = self.ui.scrollAreaWidgetContents_tobeshipped
            curr_vertical = self.ui.verticalLayout_shiporder

        
        for i in reversed(range(curr_frame_tobeship.layout().count())):
            curr_frame_tobeship.layout().itemAt(i).widget().setParent(None)
            
        print("product_order: ", product_order)
        
        for count, i in enumerate(product_order, start=1):
            print("i: ", i, "count:", count)
            img_path = get_first_img_for_product(i[0])
            print(img_path)

            curr_frame_tobeship.setMinimumHeight(300 * count)
            curr_scroll.setMinimumHeight(300 * count)

            shipordercontainer = QWidget(curr_frame_tobeship)
            shipordercontainer.setObjectName(f"shipordercontainer_{count}")
            shipordercontainer.setMinimumSize(QSize(912, 269))
            shipordercontainer.setMaximumSize(QSize(912, 269))
            shipordercontainer.setStyleSheet(u"border-bottom: 1px solid #CD4662;\n"
    "background: #FAF9F6;\n"
    "")
            gridLayout_shipordercontainer = QGridLayout(shipordercontainer)
            gridLayout_shipordercontainer.setObjectName(u"gridLayout_shipordercontainer")
            gridLayout_shipordercontainer.setHorizontalSpacing(26)
            gridLayout_shipordercontainer.setVerticalSpacing(6)
            gridLayout_shipordercontainer.setContentsMargins(23, 10, -1, 15)
            shopnameforcart_2 = QLabel(shipordercontainer)
            shopnameforcart_2.setObjectName(u"shopnameforcart_2")
            shopnameforcart_2.setMinimumSize(QSize(131, 41))
            shopnameforcart_2.setMaximumSize(QSize(131, 41))
            shopnameforcart_2.setStyleSheet(u"border: none;\n"
    "color: #000;\n"
    "font-family: Suwannaphum;\n"
    "font-size: 20px;\n"
    "font-style: normal;\n"
    "font-weight: 700;\n"
    "line-height: normal;")

            gridLayout_shipordercontainer.addWidget(shopnameforcart_2, 0, 0, 1, 1)

            horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            gridLayout_shipordercontainer.addItem(horizontalSpacer_11, 0, 1, 1, 1)

            horizontalSpacer_12 = QSpacerItem(691, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            gridLayout_shipordercontainer.addItem(horizontalSpacer_12, 0, 2, 1, 5)

            cartorderpic_2 = QLabel(shipordercontainer)
            cartorderpic_2.setObjectName(u"cartorderpic_2")
            cartorderpic_2.setMinimumSize(QSize(134, 134))
            cartorderpic_2.setMaximumSize(QSize(134, 134))
            cartorderpic_2.setStyleSheet(u"border: none;\n"
    "border-radius: 70px;\n"
    "background: #cd4662;")

            gridLayout_shipordercontainer.addWidget(cartorderpic_2, 1, 0, 3, 1)

            productcartname_2 = QLabel(shipordercontainer)
            productcartname_2.setObjectName(u"productcartname_2")
            productcartname_2.setMinimumSize(QSize(672, 28))
            productcartname_2.setMaximumSize(QSize(672, 28))
            productcartname_2.setStyleSheet(u"border: none;\n"
    "color: #000;\n"
    "font-family: Suwannaphum;\n"
    "font-size: 16px;\n"
    "font-style: normal;\n"
    "font-weight: 400;\n"
    "line-height: normal;")

            gridLayout_shipordercontainer.addWidget(productcartname_2, 1, 2, 1, 5)

            productcartdescrip_2 = QLabel(shipordercontainer)
            productcartdescrip_2.setObjectName(u"productcartdescrip_2")
            productcartdescrip_2.setMinimumSize(QSize(672, 28))
            productcartdescrip_2.setMaximumSize(QSize(672, 28))
            productcartdescrip_2.setStyleSheet(u"border: none;\n"
    "color: #545454;\n"
    "font-family: Suwannaphum;\n"
    "font-size: 16px;\n"
    "font-style: normal;\n"
    "font-weight: 400;\n"
    "line-height: normal;")

            gridLayout_shipordercontainer.addWidget(productcartdescrip_2, 2, 2, 1, 5)

            productnum_2 = QLabel(shipordercontainer)
            productnum_2.setObjectName(u"productnum_2")
            productnum_2.setMinimumSize(QSize(461, 28))
            productnum_2.setMaximumSize(QSize(461, 28))
            productnum_2.setStyleSheet(u"border: none;\n"
    "color: #545454;\n"
    "font-family: Suwannaphum;\n"
    "font-size: 16px;\n"
    "font-style: normal;\n"
    "font-weight: 400;\n"
    "line-height: normal;")

            gridLayout_shipordercontainer.addWidget(productnum_2, 3, 2, 1, 1)

            totalpricecartlabel_2 = QLabel(shipordercontainer)
            totalpricecartlabel_2.setObjectName(u"totalpricecartlabel_2")
            totalpricecartlabel_2.setMinimumSize(QSize(81, 28))
            totalpricecartlabel_2.setStyleSheet(u"border: none;\n"
    "color: #000;\n"
    "font-family: Suwannaphum;\n"
    "font-size: 16px;\n"
    "font-style: normal;\n"
    "font-weight: 400;\n"
    "line-height: normal;")

            gridLayout_shipordercontainer.addWidget(totalpricecartlabel_2, 3, 3, 1, 2)

            horizontalSpacer_9 = QSpacerItem(33, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            gridLayout_shipordercontainer.addItem(horizontalSpacer_9, 3, 5, 1, 1)

            totalpricecartnumlabel_2 = QLabel(shipordercontainer)
            totalpricecartnumlabel_2.setObjectName(u"totalpricecartnumlabel_2")
            totalpricecartnumlabel_2.setMinimumSize(QSize(71, 28))
            totalpricecartnumlabel_2.setMaximumSize(QSize(71, 28))
            totalpricecartnumlabel_2.setStyleSheet(u"border: none;\n"
    "color: #cd4662;\n"
    "font-family: Suwannaphum;\n"
    "font-size: 16px;\n"
    "font-style: normal;\n"
    "font-weight: 400;\n"
    "line-height: normal;")

            gridLayout_shipordercontainer.addWidget(totalpricecartnumlabel_2, 3, 6, 1, 1)

            horizontalSpacer_13 = QSpacerItem(665, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            gridLayout_shipordercontainer.addItem(horizontalSpacer_13, 4, 0, 1, 4)

            checkstatusshipbutton = QPushButton(shipordercontainer)
            checkstatusshipbutton.setObjectName(u"checkstatusshipbutton")
            checkstatusshipbutton.setMinimumSize(QSize(156, 42))
            checkstatusshipbutton.setMaximumSize(QSize(156, 42))
            checkstatusshipbutton.setStyleSheet(u"color: #FFF;\n"
    "background-color: #cd4662;\n"
    "border: none;\n"
    "text-align: center;\n"
    "font-family: Suwannaphum;\n"
    "font-size: 16px;\n"
    "font-style: normal;\n"
    "font-weight: 700;\n"
    "line-height: normal;\n"
    "border-radius: 5px;")

            gridLayout_shipordercontainer.addWidget(checkstatusshipbutton, 4, 4, 1, 3)

            curr_vertical.addWidget(shipordercontainer)

            # setText
            if not admin:
                shopnameforcart_2.setText(get_shopname_by_product_id(i[0]))
                if i[4] == "":
                    checkstatusshipbutton.clicked.connect(functools.partial(self.check_status_ship, i[4], i[5]))
                else:
                    checkstatusshipbutton.clicked.connect(functools.partial(self.check_status_ship, i[4], i[5]))
            else:
                order_customer = get_user_by_order(i)
                shopnameforcart_2.setText(order_customer)
                if i[4] == "":
                    checkstatusshipbutton.clicked.connect(functools.partial(self.check_status_ship, i[4], i[5] ,i ,True))
            productcartname_2.setText(get_product_name_by_id(i[0]))
            productcartdescrip_2.setText(f"Size:  {i[2]}   | Option:  {i[3]}")
            productnum_2.setText(f"{i[1]} piece")
            totalpricecartlabel_2.setText("Total Price:")
            totalpricecartnumlabel_2.setText("฿ " + str(get_product_price_by_id(i[0]) * i[1]))
            cartorderpic_2.setPixmap(QPixmap(img_path))
            cartorderpic_2.setScaledContents(True)
            checkstatusshipbutton.setText("Check Status")

            
    
    def go_to_order_ship_fromprofile(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.myorderspage)
        self.ui.completedbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.tobeshippedbutton.setStyleSheet(active_orderbutton_style)
        self.ui.toberecievedbutton.setStyleSheet(inactive_orderbutton_style)
        
        self.order_ship()

    # def go_to_order_receive_fromprofile(self):
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.main)
    #     self.ui.stackedWidget_main.setCurrentWidget(self.ui.myorderspage)
    #     self.ui.completedbutton.setStyleSheet(inactive_orderbutton_style)
    #     self.ui.tobeshippedbutton.setStyleSheet(inactive_orderbutton_style)
    #     self.ui.toberecievedbutton.setStyleSheet(active_orderbutton_style)
    #     self.ui.stackedWidget_myorders.setCurrentWidget(self.ui.toberecievedpage)
        
        # self.order_ship()

    # def go_to_order_complete_fromprofile(self):
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.main)
    #     self.ui.stackedWidget_main.setCurrentWidget(self.ui.myorderspage)
    #     self.ui.completedbutton.setStyleSheet(active_orderbutton_style)
    #     self.ui.tobeshippedbutton.setStyleSheet(inactive_orderbutton_style)
    #     self.ui.toberecievedbutton.setStyleSheet(inactive_orderbutton_style)
    #     self.ui.stackedWidget_myorders.setCurrentWidget(self.ui.completedpage)
        
    #     self.ui.buyagaincompletebutton.hide()
    #     self.ui.givereviewcompletebutton.hide()
        
        # self.order_ship()
        
        

    def go_to_favorite(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.favpage)
        
        self.ui.homebutton.setStyleSheet(inactive_button_style)
        self.ui.favbutton.setStyleSheet(active_button_style)
        self.ui.orderbutton.setStyleSheet(inactive_button_style)

        self.display_product(False, "allproducts_customer")

        self.current_index = 0

    def go_to_userprofile(self):
        print("go to profile")
        self.ui.stackedWidget.setCurrentWidget(self.ui.userprofile)
        # self.ui.usernamelabel.setText(root.LoggedInUser.user.username.title())
        self.ui.usernamelabel.setText(root.LoggedInUser.user.username)
        self.ui.openshopbutton.clicked.connect(self.go_to_adminregister)

        self.current_index = 0

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
            self.go_to_homepage_admin()
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

        self.ui.homebutton_admin.clicked.connect(self.go_to_homepage_admin)
        self.ui.productsbutton_admin.clicked.connect(self.go_to_productspage_admin)
        self.ui.viewallproductbutton_admin.clicked.connect(self.go_to_productspage_admin)
        self.ui.addproduct_admin.clicked.connect(self.go_to_addproduct_admin)
        
        # check how many product this user own
        num_of_products = count_products_for_user(root.LoggedInUser.user.username)
        if num_of_products > 0:
            self.display_product(True, "homepage_admin")

    def display_product(self, admin, widget):
        print("display product")
        if widget == "homepage_admin":
            print("homepage_admin")
            self.curr_widget = self.ui.frame_products_admin
            self.curr_layout = self.ui.gridLayout_products_admin
        elif widget == "allproducts_admin":
            print("allproducts_admin")
            self.curr_widget = self.ui.frame_allproducts_admin
            self.curr_layout = QGridLayout()
            self.curr_widget.setLayout(self.curr_layout)
        elif widget == "homepage_customer":
            print("homepage_customer")
            self.curr_widget = self.ui.frame_homepage_product
            self.curr_layout = QGridLayout()
            self.curr_widget.setLayout(self.curr_layout)
        elif widget == "allproducts_customer":
            print("allproducts_customer")
            self.curr_widget = self.ui.frame_allproducts
            self.curr_layout = QGridLayout()
            self.curr_widget.setLayout(self.curr_layout)
        # widget.setVisible(True)
        
        products = []
        if root.LoggedInUser.logged_in == False or admin == False:
            products = get_all_products()
            products = r.sample(products, len(products))
            # print("products if: ", products)
        else:
            products = get_products_for_user(root.LoggedInUser.user.username)
            # print("products else: ", products)

        product_widgets = []
        column = 1
        row = 1

        for product in products:
            # print("product: ", product)
            if column > 3:
                column = 1
                row += 1
                if widget == "homepage_admin":
                    self.ui.frame_homepage_admin.setMinimumHeight(1100 + (320 * (row - 1))) 
                elif widget == "allproducts_admin":
                    self.ui.productcontainer_admin.setMinimumHeight(440 + (320 * (row - 1)))
                elif widget == "homepage_customer":
                    self.ui.frame_homepage.setMinimumHeight(900 + (320 * (row - 1)))
                    self.ui.scrollAreaWidgetContents.setMinimumHeight(900 + (320 * (row - 1)))
                elif widget == "allproducts_customer":
                    self.ui.frame_favpage.setMinimumHeight(500 + (320 * (row - 1))) #widget
                    self.ui.scrollAreaWidgetContents_2.setMinimumHeight(500 + (320 * (row - 1))) #widget
                self.curr_widget.setMinimumHeight(380 + (320 * (row - 1))) 

            # img_path = get_first_product_img(root.LoggedInUser.user.username, product.id)
            # print("image path: ", img_path)
            # pixmap = QPixmap(img_path)
            # print("pixmap: ", pixmap)

            product_widget = QWidget(self.curr_widget)
            product_widget.setObjectName(u"product_widget")
            product_widget.setMinimumSize(QSize(251, 320))
            product_widget.setMaximumSize(QSize(251, 320))
            product_widget.setStyleSheet(u"border-radius: 10px;\n"
            "background: #D9D9D9;\n"
            "padding: 28px;")
            product_gridLayout = QGridLayout(product_widget)
            product_gridLayout.setObjectName(u"product_gridLayout")
            productdetails_frame = QFrame(product_widget)
            productdetails_frame.setObjectName(u"productdetails_frame")
            productdetails_frame.setMinimumSize(QSize(191, 71))
            productdetails_frame.setMaximumSize(QSize(191, 71))
            productdetails_frame.setStyleSheet(u"padding: 0;\n"
            "margin: 0;")
            productdetails_frame.setFrameShape(QFrame.StyledPanel)
            productdetails_frame.setFrameShadow(QFrame.Raised)
            productsold_label = QLabel(productdetails_frame)
            productsold_label.setObjectName(u"productsold_label")
            productsold_label.setGeometry(QRect(100, 40, 91, 22))
            productsold_label.setMinimumSize(QSize(83, 22))
            productsold_label.setMaximumSize(QSize(16777215, 1000000))
            productsold_label.setLayoutDirection(Qt.LeftToRight)
            productsold_label.setStyleSheet(u"font-size: 12px;\n"
            "padding: 0;")
            productsold_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
            productprice_button = QPushButton(productdetails_frame)
            productprice_button.setObjectName(u"productprice_button")
            productprice_button.setGeometry(QRect(-4, 40, 83, 22))
            productprice_button.setMinimumSize(QSize(83, 22))
            productprice_button.setMaximumSize(QSize(16777215, 16777215))
            productprice_button.setLayoutDirection(Qt.LeftToRight)
            productprice_button.setStyleSheet(u"font-size: 20px;\n"
            "color: #CD4662;\n"
            "text-align: left;\n"
            "padding: 0;")
            picproduct = QPushButton(product_widget)
            picproduct.setObjectName(f"picproduct_{product.id}")
            picproduct.setMinimumSize(QSize(191, 188))
            picproduct.setMaximumSize(QSize(191, 188))
            picproduct.setStyleSheet(u"background-color: #FFF;\n"
            "image: url(:/pic/product_img/102165.jpg);\n"
            "border-radius: 0px;\n"
            "padding: 0;")
            product_gridLayout.addWidget(picproduct, 0, 0, 1, 1)
            icon4 = QIcon()
            icon4.addFile(u":/pic/images/newres/baht.png", QSize(), QIcon.Normal, QIcon.Off)
            productprice_button.setIcon(icon4)
            productprice_button.setIconSize(QSize(19, 19))
            productname_label = QLabel(productdetails_frame)
            productname_label.setObjectName(u"productname_label")
            productname_label.setGeometry(QRect(0, 2, 121, 21))
            productname_label.setMinimumSize(QSize(0, 0))
            productname_label.setMaximumSize(QSize(16777215, 16777215))
            productname_label.setStyleSheet(u"font-size: 16px;\n"
            "padding: 0;")

            product_gridLayout.addWidget(productdetails_frame, 1, 0, 1, 1)

            self.curr_layout.addWidget(product_widget, row, column, 1, 1)

            product_widgets.append(product_widget)
            
            column += 1

        for i, product_widget in enumerate(product_widgets):
            # print(products[i].)
            productsold_label = product_widget.findChild(QLabel, "productsold_label")
            productprice_button = product_widget.findChild(QPushButton, "productprice_button")
            productname_label = product_widget.findChild(QLabel, "productname_label")
            picproduct = product_widget.findChild(QPushButton, f"picproduct_{products[i].id}")
            
            productname_label.setText(get_product_name_by_id(products[i].id))
            productprice_button.setText(f"{str(get_product_price_by_id(products[i].id))}")
            productsold_label.setText(f"{products[i].sold} sold")
            img_path = get_product_img_by_id(products[i].id)[0]
            picproduct.setStyleSheet(f"background-color: #FFF; image: url({img_path}); border-radius: 0px; padding: 0;")

            # picproduct.clicked.connect(functools.partial(self.go_to_productpage(products[i].id)))
            clicked_button = self.sender()
            if picproduct == clicked_button:
                self.current_index = 0
                print("current index: pic product", self.current_index)
            if widget == "allproducts_admin" or widget == "homepage_admin":
                picproduct.clicked.connect(functools.partial(self.go_to_showproductforadmin, products[i].id))
            else:
                picproduct.clicked.connect(functools.partial(self.go_to_productpage, products[i].id))
            # go_to_productpage(products[i].id)
            
        # self.curr_widget.update()
        # self.curr_widget.adjustSize()
        
    def go_to_viewshop(self, username):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.viewshoppage)
        
        self.ui.homebutton.setStyleSheet(inactive_button_style)
        self.ui.favbutton.setStyleSheet(inactive_button_style)
        self.ui.orderbutton.setStyleSheet(inactive_button_style)
        
        self.ui.shopnamelabel_admin_2.setText(get_shopname_by_product_id(username))
        shopproduct_len = str(len(get_products_for_user(get_shopname_by_product_id(username))))
        self.ui.numproducts_2.setText(shopproduct_len)
        self.ui.numreviews_2.setText(str(get_shop_reviews_by_product_id(username)))
        self.ui.descriptioninfolabel_productviewpage.setText(get_product_description_by_id(username))
        
        num_of_products = count_products_for_user(root.LoggedInUser.user.username)
        if num_of_products > 0:
            self.display_product(True, "allproducts_customer")
            
        
        
        
    def go_to_showproductforadmin(self, id):
        self.ui.stackedWidget_adminmain.setCurrentWidget(self.ui.productspage_admin)
        self.ui.stackedWidget_adminproducts.setCurrentWidget(self.ui.showproductforadmin)
        
        self.ui.productsbutton_admin.setStyleSheet(active_button_style)
        self.ui.homebutton_admin.setStyleSheet(inactive_button_style)
        self.ui.orderstatusbutton_admin.setStyleSheet(inactive_button_style)
        
        self.ui.homebutton_admin.clicked.connect(self.go_to_homepage_admin)
        self.ui.productsbutton_admin.clicked.connect(self.go_to_productspage_admin)
        
        self.ui.productname_2.setText(get_product_name_by_id(id))
        self.ui.productprice_2.setText(f"{str(get_product_price_by_id(id))}")
        img_path = get_first_img_for_product(id)
        print("get_first_img_for_product", img_path)
        pixmap = QPixmap(img_path)
        self.ui.mainpic_2.setPixmap(pixmap)
        self.ui.mainpic_2.setScaledContents(True)
        self.ui.numberofsold_2.setText(f"{str(get_product_sold_by_id(id))} Sold")
        
        self.button_bug_fix(self.ui.nextpicrightsidebutton_2)
        self.button_bug_fix(self.ui.nextpicrightsidebutton)

        
        if len(get_product_img_by_id(id)) > 1:
            self.ui.nextpicrightsidebutton_2.show()
            self.ui.nextpicrightsidebutton.show()
            self.current_index = 0
            
            self.ui.nextpicrightsidebutton_2.clicked.connect(functools.partial(self.change_pic, id, "prev"))
            self.ui.nextpicrightsidebutton.clicked.connect(functools.partial(self.change_pic, id, "next"))
        else:
            self.ui.nextpicrightsidebutton_2.hide()
            self.ui.nextpicrightsidebutton.hide()
            
            
        # ------------------------------------- SU SU WS --------------------------------
        # # display size
        # size_widget = []
        # column = 1
        # row = 1
        # while self.ui.gridLayout_size_productviewpage.count():
        #     item = self.ui.gridLayout_size_productviewpage.takeAt(0)
        #     widget = item.widget()
        #     if widget:
        #         widget.deleteLater()
        # if get_product_sizes_by_id(id) != []:
        #     sizes = get_product_sizes_by_id(id)
        #     for size in sizes:
        #         if column > 4:
        #             horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        #             self.ui.gridLayout_size_productviewpage.addItem(horizontalSpacer, row, column, 1, 1)
        #             column = 1
        #             row += 1
        #         sbutton = QPushButton(self.ui.frame_size_productviewpage)
        #         sbutton.setObjectName(f"sbutton_{size}")
        #         sbutton.setText(size)
        #         sbutton.setMinimumSize(QSize(70, 21))
        #         sbutton.setMaximumSize(QSize(70, 21))
        #         sbutton.setStyleSheet(u"QPushButton {	\n"
        #         "	color:#545454;\n"
        #         "	font-family: Suwannaphum;\n"
        #         "	background: #F4F2EF;\n"
        #         "	font-size: 16px;\n"
        #         "	font-style: normal;\n"
        #         "	font-weight: 400;\n"
        #         "	line-height: normal;\n"
        #         "	border-radius: 5px;\n"
        #         "	border: 1px solid #545454;\n"
        #         "}\n"
        #         "QPushButton:hover {\n"
        #         "	background: #F4DBDB;\n"
        #         "}")

        #         self.ui.gridLayout_size_productviewpage.addWidget(sbutton, row, column, 1, 1)
        #         column += 1
        #     horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        #     self.ui.gridLayout_size_productviewpage.addItem(horizontalSpacer, row, column + 1, 1, 1)
        
        # display options
        # column = 1
        # row = 1
        # while self.ui.gridLayout_option_productviewpage.count():
        #     item = self.ui.gridLayout_option_productviewpage.takeAt(0)
        #     widget = item.widget()
        #     if widget:
        #         widget.deleteLater()
        # if get_product_options_by_id(id) != []:
        #     options = get_product_options_by_id(id)
        #     for opt in options:
        #         if column > 3:
        #             horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        #             self.ui.gridLayout_option_productviewpage.addItem(horizontalSpacer, row, column, 1, 1)
        #             column = 1
        #             row += 1
        #         optbutton = QPushButton(self.ui.frame_size_productviewpage)
        #         optbutton.setObjectName(f"optbutton_{opt}")
        #         optbutton.setText(opt)
        #         optbutton.setMinimumSize(QSize(100, 25))
        #         optbutton.setMaximumSize(QSize(100, 25))
        #         optbutton.setStyleSheet(u"QPushButton {	\n"
        #         "	color:#545454;\n"
        #         "	font-family: Suwannaphum;\n"
        #         "	background: #F4F2EF;\n"
        #         "	font-size: 16px;\n"
        #         "	font-style: normal;\n"
        #         "	font-weight: 400;\n"
        #         "	line-height: normal;\n"
        #         "	border-radius: 5px;\n"
        #         "	border: 1px solid #545454;\n"
        #         "}\n"
        #         "QPushButton:hover {\n"
        #         "	background: #F4DBDB;\n"
        #         "}")

        #         self.ui.gridLayout_option_productviewpage.addWidget(optbutton, row, column, 1, 1)
        #         column += 1
        #     horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        #     self.ui.gridLayout_option_productviewpage.addItem(horizontalSpacer, row, column + 1, 1, 1) 

        # --------------------------------------------------------------------------------

        
        self.button_bug_fix(self.ui.editproductbutton)
        self.button_bug_fix(self.ui.deleteproductbutton)
        
        self.ui.editproductbutton.clicked.connect(functools.partial(self.go_to_editproductspage_admin, id))
        self.ui.deleteproductbutton.clicked.connect(functools.partial(self.delete_product, id))
        
    
    def go_to_editproductspage_admin(self, id):
        self.ui.stackedWidget_adminmain.setCurrentWidget(self.ui.productspage_admin)
        self.ui.stackedWidget_adminproducts.setCurrentWidget(self.ui.editproductspage_admin)


        self.button_bug_fix(self.ui.addproductbutton_4)
        self.ui.addproductbutton_4.clicked.connect(functools.partial(self.edit_product, id))
        self.ui.editproductnametextbox.setText(get_product_name_by_id(id))
        self.ui.editproductdescriptiontextbox_3.setPlainText(get_product_description_by_id(id))
        self.ui.editproductpricespinbox.setText(str(get_product_price_by_id(id)))
        self.ui.editproductpricespinbox.setValue(get_product_price_by_id(id))
        self.ui.editproductstockspinbox_3.setValue(get_product_stock_by_id(id))
        categories = get_product_categories_by_id(id)
        if "Men" in categories:
            self.ui.checkBox_men_3.setChecked(True)
        if "Women" in categories:
            self.ui.checkBox_women_3.setChecked(True)
        if "Kids" in categories:
            self.ui.checkBox_kids_3.setChecked(True)
        if "Top" in categories:
            self.ui.checkBox_top_3.setChecked(True)
        if "Bottom" in categories:
            self.ui.checkBox_bottom_3.setChecked(True)
        if "Dress" in categories:
            self.ui.checkBox_dress_3.setChecked(True)
        if "Footwear" in categories:
            self.ui.checkBox_footwear_3.setChecked(True)
        if "Headwear" in categories:
            self.ui.checkBox_headwear_3.setChecked(True)
        if "Accessories" in categories:
            self.ui.checkBox_accessories_3.setChecked(True)

        sizes = get_product_sizes_by_id(id)  
        if sizes != []:
            size_len = len(sizes)
            for i in range(size_len - 1):
                self.frame_sizes_3 = QFrame(self.scrollAreaWidgetContents_25)
                self.frame_sizes_3.setObjectName(f"frame_sizes_{id}_{sizes[i]}")
                self.frame_sizes_3.setGeometry(QRect(0, 0, 941, 58))
                self.frame_sizes_3.setMinimumSize(QSize(941, 40))
                self.frame_sizes_3.setMaximumSize(QSize(16777215, 16777215))
                self.frame_sizes_3.setFrameShape(QFrame.StyledPanel)
                self.frame_sizes_3.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_15 = QHBoxLayout(self.frame_sizes_3)
                self.horizontalLayout_15.setSpacing(10)
                self.horizontalLayout_15.setObjectName(f"horizontalLayout_{id}_{sizes[i]}")
                self.horizontalLayout_15.setSizeConstraint(QLayout.SetDefaultConstraint)
                self.horizontalLayout_15.setContentsMargins(9, -1, -1, -1)
                self.frame_size_each = QFrame(self.frame_sizes_3)
                self.frame_size_each.setObjectName(f"frame_size_each_{id}_{sizes[i]}")
                self.frame_size_each.setMinimumSize(QSize(155, 38))
                self.frame_size_each.setMaximumSize(QSize(155, 38))
                self.frame_size_each.setStyleSheet(u"boder-radius: 5px;")
                self.frame_size_each.setFrameShape(QFrame.StyledPanel)
                self.frame_size_each.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_size_each = QHBoxLayout(self.frame_size_each)
                self.horizontalLayout_size_each.setSpacing(0)
                self.horizontalLayout_size_each.setObjectName(f"horizontalLayout_size_each_{id}_{sizes[i]}")
                self.horizontalLayout_size_each.setContentsMargins(0, 0, 0, 0)
                self.size_1 = QLineEdit(self.frame_size_each)
                self.size_1.setObjectName(f"size_{id}_{sizes[i]}")
                self.size_1.setMinimumSize(QSize(108, 38))
                self.size_1.setMaximumSize(QSize(108, 38))
                self.size_1.setStyleSheet(u"border-radius: 5px;\n"
        "background: #EDEDED;\n"
        "padding: 5px;\n"
        "font-size: 16px;")

                self.horizontalLayout_size_each.addWidget(self.size_1)

                self.deletesizebutton = QPushButton(self.frame_size_each)
                self.deletesizebutton.setObjectName(f"deletesizebutton__{id}_{sizes[i]}")
                self.deletesizebutton.setMinimumSize(QSize(55, 38))
                self.deletesizebutton.setMaximumSize(QSize(55, 38))
                self.deletesizebutton.setStyleSheet(u"background: #CD4662;\n"
        "border-radius: 5px;\n"
        "padding: 5px;\n"
        "border: none;")
                icon7 = QIcon()
                icon7.addFile(u":/pic/images/newres/trashcan.png", QSize(), QIcon.Normal, QIcon.Off)
                self.deletesizebutton.setIcon(icon7)
                self.deletesizebutton.setIconSize(QSize(30, 30))

                self.horizontalLayout_size_each.addWidget(self.deletesizebutton)

                self.deletesizebutton.raise_()
                self.size_1.raise_()

                self.horizontalLayout_15.addWidget(self.frame_size_each) 

                self.deletesizebutton.clicked.connect(functools.partial(self.delete_size, id, i))

            self.ui.addsizeproductbutton_3.clicked.connect(self.add_size)

    def delete_size(self, id, size):
        print("delete size")
        frame_size = self.findChild(QFrame, f"frame_sizes_{id}_{size}")
        frame_size.deleteLater()
        self.delete_size(id, size)
        transaction.commit()
        self.show_success("Size deleted")
        print("Size deleted")
        
    def edit_product(self, id):
        pass

    def go_to_productspage_admin(self):
        self.ui.stackedWidget_adminmain.setCurrentWidget(self.ui.productspage_admin)
        self.ui.stackedWidget_adminproducts.setCurrentWidget(self.ui.alltypesproductspage_admin)
        self.ui.stackedWidget_allandtype_admin.setCurrentWidget(self.ui.adminallproductpage)

        self.ui.homebutton_admin.clicked.connect(self.go_to_homepage_admin)
        self.ui.productsbutton_admin.clicked.connect(self.go_to_productspage_admin)
        self.ui.viewallproductbutton_admin.clicked.connect(self.go_to_productspage_admin)
        self.ui.addproduct_admin.clicked.connect(self.go_to_addproduct_admin)
        
        self.ui.productsbutton_admin.setStyleSheet(active_button_style)
        self.ui.homebutton_admin.setStyleSheet(inactive_button_style)
        self.ui.orderstatusbutton_admin.setStyleSheet(inactive_button_style)

        self.ui.allproductbutton_admin.setStyleSheet(active_orderbutton_style)
        
        num_of_products = count_products_for_user(root.LoggedInUser.user.username)
        if num_of_products > 0:
            self.display_product(True, "allproducts_admin")

    def go_to_addproduct_admin(self):
        self.ui.stackedWidget_adminmain.setCurrentWidget(self.ui.productspage_admin)
        self.ui.stackedWidget_adminproducts.setCurrentWidget(self.ui.addproductpage_admin)

        self.ui.homebutton_admin.clicked.connect(self.go_to_homepage_admin)

        self.button_bug_fix(self.ui.addsizeproductbutton)
        self.ui.addsizeproductbutton.clicked.connect(functools.partial(self.add_size))
        self.size_len = 0
        self.button_bug_fix(self.ui.addoptionproductbutton)
        self.ui.addoptionproductbutton.clicked.connect(self.add_option)
        self.option_len = 0

        self.product_img = 0
        self.ui.img_1.setVisible(False)
        self.ui.delete_pic_button_1.setVisible(False)

        self.button_bug_fix(self.ui.addimagebutton_5)
        self.ui.addimagebutton_5.clicked.connect(self.add_img)
        
        self.button_bug_fix(self.ui.addproductbutton)
        self.ui.addproductbutton.clicked.connect(self.add_product)
        self.ui.canceladdproductbutton.clicked.connect(self.go_to_homepage_admin)
    
    def add_img(self):
        if self.add_product_img(self.ui.addimagebutton_5, self.ui.img_1, self.ui.delete_pic_button_1) and not self.img_button_clicked:
            print("add img")

            self.img_button_clicked = True

    def add_product_img(self, button, img, delete):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.png)")
        if fname[0]:
            print("f[0]: ", fname[0])
            self.product_img += 1
            
            addoption_geometry2 = self.ui.img_1.geometry()
            x_coordinate = addoption_geometry2.x()
            y_coordinate = addoption_geometry2.y()
            width = addoption_geometry2.width()
            height = addoption_geometry2.height()
            
            imglabel = QLabel(self.ui.frame_addimageproduct)
            imglabel.setObjectName(f"imglabel_{self.product_img}")
            imglabel.setGeometry(QRect(5, 50, 141, 141))
            imglabel.setMinimumSize(141, 141)
            imglabel.setMaximumSize(141, 141)
            imglabel.setGeometry(x_coordinate + (201*(self.product_img - 1)), y_coordinate, width, height)

            addoption_geometry3 = self.ui.delete_pic_button_1.geometry()
            x_coordinate = addoption_geometry3.x()
            y_coordinate = addoption_geometry3.y()
            width = addoption_geometry3.width()
            height = addoption_geometry3.height()
            
            delete_img_button = QPushButton(self.ui.frame_addimageproduct)
            delete_img_button.setObjectName(f"delete_pic_button_{self.product_img}")
            delete_img_button.setEnabled(True)
            delete_img_button.setGeometry(QRect(130, 30, 31, 32))
            delete_img_button.setGeometry(x_coordinate + (201*(self.product_img - 1)), y_coordinate, width, height)
            delete_img_button.setCursor(QCursor(Qt.PointingHandCursor))
            delete_img_button.setAutoFillBackground(False)
            delete_img_button.setStyleSheet(u"QPushButton {\n"
            "	border-radius: 25px;\n"
            "	border-color: rgb(217, 217, 217);\n"
            "	border-width: 2px;\n"
            "	background: #FAF9F6;\n"
            "	color: #D9D9D9;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	border-color: #CD4662;\n"
            "	color: rgb(116,23,17);\n"
            "	background-color: rgb(237,106,94);\n"
            "}")
            
            print("fname[0]", fname[0])
            pixmap = QPixmap(fname[0])
            print("pixmap product: ", pixmap)
            if fname and (pixmap.width() != 0 or pixmap.height() != 0):
                print("fname: ", fname)
                
                print(f"imglabel_{self.product_img}")
                pic = self.ui.frame_addimageproduct.findChild(QLabel, f"imglabel_{self.product_img}")
                delete_butt = self.ui.frame_addimageproduct.findChild(QPushButton, f"delete_pic_button_{self.product_img}")
                
                if pixmap.width() > pixmap.height():
                    aspect_ratio = pixmap.height() / pixmap.width()
                    label_width = 141
                    label_height = int(label_width * aspect_ratio)
                    pic.setFixedSize(label_width, label_height)
                else:
                    aspect_ratio = pixmap.width() / pixmap.height()
                    label_height = 141
                    label_width = int(label_height * aspect_ratio)
                    pic.setFixedSize(label_width, label_height)
                
                pic.setAlignment(QtCore.Qt.AlignCenter)
                pic.setVisible(True)
                delete_butt.setVisible(True)
                delete_butt.clicked.connect(lambda: self.delete_product_img(button, pic, delete_butt, fname[0]))
                pic.setPixmap(pixmap)
                pic.setScaledContents(True)
                
                img_path = self.add_img_to_folder(fname)
                img_path = img_path.replace('..', 'app/assets')
                print("img_path: ", img_path)
                pic.setProperty("image_path", img_path)

                return True
        return False
            
    def delete_product_img(self, button, img, delete, img_path):
        geometry = button.geometry()
        button.setGeometry(geometry.x() - 201, geometry.y(), 141, 141)
        img.setVisible(False)
        self.product_img -= 1
        delete.setVisible(False)

        img_name = os.path.basename(img_path)
        img_path = f"app/assets/product_img/{img_name}"
        try:
            os.remove(img_path)
            print(f"Deleted image file: {img_path}")
        except OSError as e:
            print(f"Error deleting image file {img_path}: {e}")
        # update_qrc_file(img_name)
        
    def add_img_to_folder(self, img):
        shutil.copy(img[0], 'app/assets/product_img/')
        
        qrc_file_path = 'app/assets/realsourceimg/realpicforuse.qrc'
        tree = ET.parse(qrc_file_path)
        root = tree.getroot()
        
        existing_files = [file_elem.text for file_elem in root.findall("./qresource[@prefix='pic']/file")]
        img_basename = os.path.basename(img[0])
        if img_basename not in existing_files:
            new_file_element = ET.Element("file")
            new_file_element.text = f"../product_img/{img_basename}"
            
            qresource_element = root.find("./qresource[@prefix='pic']")
            # qresource_element.append(new_file_element)
            
            # tree.write(qrc_file_path)
            return new_file_element.text
        
    def add_img_to_stylesheet(self, img):
        file_path = 'app/template/homepage/realhomepage_ui.py'  
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
        except UnicodeDecodeError:
            print("Error: Unable to decode the file with utf-8 encoding.")

        insert_line_number = None
        for i, line in enumerate(lines):
            if 'self.img_1.setGeometry(' in line:
                insert_line_number = i + 1
                break

        if insert_line_number is not None:
            lines.insert(insert_line_number, f'        self.img_1.setStyleSheet(u"image: url(:/pic/product_img/{os.path.basename(img[0])})")\n')

            with open(file_path, 'w') as file:
                file.writelines(lines)
            # return f"image: url(:/pic/product_img/{os.path.basename(img[0])})"
        else:
            print("Error: Line to insert stylesheet not found.")

    def add_size(self, page=""):
        print("add size")
        if page == "edit":
            addsize_geometry = self.ui.addsizeproductbutton_3.geometry()
        else:
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
        print("option len: ", self.option_len)
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
        # self.addproduct_admin_clear()
        productname = self.ui.addproductnametextbox.text()
        description = self.ui.addproductdescriptiontextbox.toPlainText()
        price = self.ui.addproductpricespinbox.value()
        sizes = []
        options = []
        imgs = []
        
        for i in range(1, self.size_len + 1):
            size = self.ui.frame_sizes.findChild(QLineEdit, f"size_{i}")
            sizes.append(size.text())
        for i in range(1, self.option_len + 1):
            option = self.ui.frame_options.findChild(QLineEdit, f"option_{i}")
            options.append(option.text())
        stock = self.ui.addproductstockspinbox.value()
        categories = self.add_categories()
        
        for i in range(1, self.product_img + 1):
            img = self.ui.frame_addimageproduct.findChild(QLabel, f"imglabel_{i}")
            img_path = img.property("image_path")
            imgs.append(img_path)

        addproduct(productname, description, price, sizes, options, stock, categories, imgs)
        print("product added")
        self.show_success("Product added successfully")
        self.go_to_homepage_admin()

    def addproduct_admin_clear(self):
        self.ui.addproductnametextbox.clear()
        self.ui.addproductdescriptiontextbox.clear()
        self.ui.addproductpricespinbox.setValue(0)
        self.ui.addproductstockspinbox.setValue(0)
        self.ui.addsizeproductbutton.setGeometry(10, 10, 108, 38)
        for i in range(1, self.size_len):
            size = self.ui.frame_sizes.findChild(QLineEdit, f"size_{i}")
            size.setParent(None)
            size.deleteLater()
        self.size_len = 0
        self.ui.addoptionproductbutton.setGeometry(10, 10, 108, 38)
        for i in range(1, self.option_len):
            option = self.ui.frame_options.findChild(QLineEdit, f"option_{i}")
            option.setParent(None)
            option.deleteLater()
        self.option_len = 0
        self.ui.addimagebutton.setGeometry(0, 45, 151, 151)
        for i in range(1, self.product_img):
            img = self.ui.frame_addimageproduct.findChild(QLabel, f"imglabel_{i}")
            img.setParent(None)
            img.deleteLater()
            delete = self.ui.frame_addimageproduct.findChild(QPushButton, f"delete_pic_button_{i}")
            delete.setParent(None)
            delete.deleteLater()
        self.product_img = 0
        self.ui.checkBox_men.setChecked(False)
        self.ui.checkBox_women.setChecked(False)
        self.ui.checkBox_kids.setChecked(False)
        self.ui.checkBox_top.setChecked(False)
        self.ui.checkBox_bottom.setChecked(False)
        self.ui.checkBox_dress.setChecked(False)
        self.ui.checkBox_footwear.setChecked(False)
        self.ui.checkBox_headwear.setChecked(False)
        self.ui.checkBox_accessories.setChecked(False)
        
    def delete_product(self, product_id):
        if self.show_yes_no("Are you sure?") == QMessageBox.Yes:
            if delete_product_by_id(product_id):
                transaction.commit()
                self.show_success("Product deleted")
                total_num_of_products = len(get_all_products())
                
                if total_num_of_products > 0:
                    self.display_product(False, "homepage_customer")
                    
                print("Product deleted")
            else:
                self.show_error("Product delete failed")
                print("Product delete failed")

        
    
    # click product from admin page
    def product_click_for_edit(self):
        pass

    def go_to_order(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.myorderspage)
        self.ui.homebutton.setStyleSheet(inactive_button_style)
        self.ui.favbutton.setStyleSheet(inactive_button_style)
        self.ui.orderbutton.setStyleSheet(active_button_style)
        
        # self.go_to_order_ship()

        self.current_index = 0

    def go_to_order_ship(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.myorderspage)
        self.ui.stackedWidget_myorders.setCurrentWidget(self.ui.tobeshippedpage)
        
        self.order_ship()

    # def go_to_order_receive(self):
    #     self.ui.toberecievedbutton.setStyleSheet(active_orderbutton_style)
    #     self.ui.tobeshippedbutton.setStyleSheet(inactive_orderbutton_style)
    #     self.ui.completedbutton.setStyleSheet(inactive_orderbutton_style)
    #     self.ui.stackedWidget_myorders.setCurrentWidget(self.ui.toberecievedpage)
        
        # self.order_ship(self.ui.cartorderpic_3, self.ui.shopnameforcart_3, self.ui.productcartname_3, self.ui.productcartdescrip_3, self.ui.totalpricecartnumlabel_3, self.ui.productnum_3, self.ui.checkstatusreceivebutton)

    # def go_to_order_complete(self):
    #     self.ui.completedbutton.setStyleSheet(active_orderbutton_style)
    #     self.ui.tobeshippedbutton.setStyleSheet(inactive_orderbutton_style)
    #     self.ui.toberecievedbutton.setStyleSheet(inactive_orderbutton_style)
    #     self.ui.stackedWidget_myorders.setCurrentWidget(self.ui.completedpage)
        
    #     self.ui.buyagaincompletebutton.hide()
    #     self.ui.givereviewcompletebutton.hide()
        
        # self.order_ship(self.ui.cartorderpic_4, self.ui.shopnameforcart_4, self.ui.productcartname_4, self.ui.productcartdescrip_4, self.ui.totalpricecartnumlabel_4, self.ui.productnum_4)


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
