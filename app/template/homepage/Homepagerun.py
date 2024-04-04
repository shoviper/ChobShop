import shutil
import os
import xml.etree.ElementTree as ET
import sys
import functools
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QSizePolicy, QFileDialog
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
        self.ui.orderbutton.clicked.connect(self.go_to_order)
        
        # self.display_product()
        
        print("-----------Print All Product This User Sell----------------")
        print("root.LoggedInUser.logged_in: ", root.LoggedInUser.logged_in)
        for i in get_products_for_user(root.LoggedInUser.user.username):
            print("product name and id: ", (get_product_name(root.LoggedInUser.user.username, i.id)), i.id)
        print("-----------------------------------------------------------")
        
        # delete product by id
        # delete_product_by_id(2)

        self.print_cart()
        
        
        #orderpage
        self.ui.tobeshippedbutton.clicked.connect(self.go_to_order_ship)
        self.ui.toberecievedbutton.clicked.connect(self.go_to_order_receive)
        self.ui.completedbutton.clicked.connect(self.go_to_order_complete)

        #orderAdmin
        self.ui.orderstatusbutton_admin.clicked.connect(self.go_to_orderstatus)
        self.ui.toshipadminbutton.clicked.connect(self.orderstatus_tobeship)
        self.ui.canceladminvutton.clicked.connect(self.orderstatus_cancel)
        self.ui.completedadminbutton.clicked.connect(self.orderstatus_complete)
        self.ui.reviewsadminvutton.clicked.connect(self.orderstatus_review)

        #Adminmainpage
        self.ui.vieworderstatusbutton_admin.clicked.connect(self.go_to_orderstatus)
        self.ui.tobeshippedbutton_admin.clicked.connect(self.adminmain_to_orderstatus_tobeship)
        self.ui.toberevievedbutton_admin.clicked.connect(self.adminmain_to_orderstatus_cancel)
        self.ui.completedbutton_admin.clicked.connect(self.adminmain_to_orderstatus_complete)
        self.ui.reviewsbutton_admin.clicked.connect(self.adminmain_to_orderstatus_review)
        self.img_button_clicked = False
            

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
        self.ui.cartbutton.clicked.connect(self.go_to_cart)
        # self.ui.purchasecartbutton.clicked.connect(self.purchase_cartpage)
        # self.ui.removecartbutton.clicked.connect(self.removeorder)
        self.ui.backtocartbutton.clicked.connect(self.back_to_cart)
        
        # purchase page
        self.ui.purchasebutton.clicked.connect(self.purchase_final)
        self.ui.purchasebutton_2.clicked.connect(self.go_to_home)
        self.ui.purchasebutton_3.clicked.connect(self.go_to_home)
        

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
    
    def purchase_final(self):
        if not (self.ui.promptpaybutton.isChecked() or self.ui.creditcardbutton.isChecked() or self.ui.cashdeliverybutton.isChecked() or self.ui.pickupstorebutton.isChecked()):
            self.show_error("Please choose payment method")
            return

        if self.ui.promptpaybutton.isChecked():
            print("Promptpay")
            self.go_to_promtpay()
        else:
            self.show_success("Purchase successful")
            print("Purchase successful")
            self.print_cart()
            self.go_to_purchase_complete()
            
    def go_to_promtpay(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.purchasepage)
        self.ui.stackedWidget_purchase.setCurrentWidget(self.ui.promppaymethod)
        
        self.ui.purchasebutton_2.clicked.connect(lambda: self.go_to_purchase_complete())
        
        
    def go_to_purchase_complete(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.purchasepage)
        self.ui.stackedWidget_purchase.setCurrentWidget(self.ui.purchasecomplete)
        
        self.ui.purchasebutton_3.clicked.connect(lambda: self.go_to_home())
            

    #cartpage--------------------------------------------------------------------------------------------
    
    def purchase_cartpage(self, page, id=None):
        self.ui.listWidget.clear()
        self.ui.promptpaybutton.setChecked(False)
        self.ui.creditcardbutton.setChecked(False)
        self.ui.cashdeliverybutton.setChecked(False)
        self.ui.pickupstorebutton.setChecked(False)
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.purchasepage)
        self.ui.stackedWidget_purchase.setCurrentWidget(self.ui.choosingtypeofpurchase)
        
        self.ui.firstnameaddressdisplay_2.setText(root.LoggedInUser.user.name)
        self.ui.lastnameaddressdisplay_2.setText(root.LoggedInUser.user.lastname)
        self.ui.phoneaddressdisplay_2.setText(root.LoggedInUser.user.phone)
        
        if page == "productpage":
            self.ui.backtocartbutton.clicked.connect(lambda: self.go_to_productpage(id))
            self.ui.totalprice.setText(f"{str(get_product_price_by_id(id))}")
            item = f"{get_product_name_by_id(id)} x 1 -------> {get_product_price_by_id(id)}"
            self.ui.listWidget.addItem(item)
            
        else:
            self.ui.backtocartbutton.clicked.connect(lambda: self.go_to_cart)
            self.ui.totalprice.setText(f"{str(self.add_total_price_in_cart())}")

            for i in get_user_cart_product_id():
                item = f"{get_product_name_by_id(i[0])} x {i[1]} -------> {get_product_price_by_id(i[0])}"
                self.ui.listWidget.addItem(item)
        
            
            
    def back_to_cart(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.cartpage)
    # def removeorder(self):
    #cartpage--------------------------------------------------------------------------------------------

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
    def go_to_address(self):
        self.ui.stackedWidget_settings.setCurrentWidget(self.ui.addresssettingspage)
    def go_to_editaddress(self):
        self.ui.stackedWidget_settings.setCurrentWidget(self.ui.editaddresssettingspage)
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
    def go_to_editshop(self):
        self.ui.stackedWidget_settingadmin.setCurrentWidget(self.ui.editshopaccountadminpage)
    def go_to_ruleshop(self):
        self.ui.stackedWidget_settingadmin.setCurrentWidget(self.ui.ruleadminpage)
    def exit_shop(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.homepage)
    #settingsAdminpage--------------------------------------------------------------------------------------------


    #orderAdminspage--------------------------------------------------------------------------------------------
    def go_to_orderstatus(self):
        self.ui.stackedWidget_adminmain.setCurrentWidget(self.ui.orderstatus_admin)
        self.ui.stackedWidget_orderadmin.setCurrentWidget(self.ui.tobeshipadminpage)
        self.ui.homebutton_admin.setStyleSheet(inactive_button_style)
        self.ui.productsbutton_admin.setStyleSheet(inactive_button_style)
        self.ui.orderstatusbutton_admin.setStyleSheet(active_button_style)
        self.ui.messbutton_admin.setStyleSheet(inactive_button_style)
        self.ui.homebutton_admin.clicked.connect(self.go_to_homepage_admin)
        self.ui.productsbutton_admin.clicked.connect(self.go_to_productspage_admin)
    def orderstatus_tobeship(self):
        self.ui.stackedWidget_orderadmin.setCurrentWidget(self.ui.tobeshipadminpage)
        self.ui.toshipadminbutton.setStyleSheet(active_orderbutton_style)
        self.ui.canceladminvutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.completedadminbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.reviewsadminvutton.setStyleSheet(inactive_orderbutton_style)
    def orderstatus_cancel(self):
        self.ui.stackedWidget_orderadmin.setCurrentWidget(self.ui.canceladminpage)
        self.ui.toshipadminbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.canceladminvutton.setStyleSheet(active_orderbutton_style)
        self.ui.completedadminbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.reviewsadminvutton.setStyleSheet(inactive_orderbutton_style)
    def orderstatus_complete(self):
        self.ui.stackedWidget_orderadmin.setCurrentWidget(self.ui.completeadminpage)
        self.ui.toshipadminbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.canceladminvutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.completedadminbutton.setStyleSheet(active_orderbutton_style)
        self.ui.reviewsadminvutton.setStyleSheet(inactive_orderbutton_style)
    def orderstatus_review(self):
        self.ui.stackedWidget_orderadmin.setCurrentWidget(self.ui.reviewsadminpage)
        self.ui.toshipadminbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.canceladminvutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.completedadminbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.reviewsadminvutton.setStyleSheet(active_orderbutton_style)
    #orderAdminspage--------------------------------------------------------------------------------------------

    def adminmain_to_orderstatus_tobeship(self):
        self.ui.stackedWidget_adminmain.setCurrentWidget(self.ui.orderstatus_admin)
        self.ui.stackedWidget_orderadmin.setCurrentWidget(self.ui.tobeshipadminpage)
        self.ui.toshipadminbutton.setStyleSheet(active_orderbutton_style)
        self.ui.canceladminvutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.completedadminbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.reviewsadminvutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.homebutton_admin.setStyleSheet(inactive_button_style)
        self.ui.productsbutton_admin.setStyleSheet(inactive_button_style)
        self.ui.orderstatusbutton_admin.setStyleSheet(active_button_style)
        self.ui.messbutton_admin.setStyleSheet(inactive_button_style)
    def adminmain_to_orderstatus_cancel(self):
        self.ui.stackedWidget_adminmain.setCurrentWidget(self.ui.orderstatus_admin)
        self.ui.stackedWidget_orderadmin.setCurrentWidget(self.ui.canceladminpage)
        self.ui.toshipadminbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.canceladminvutton.setStyleSheet(active_orderbutton_style)
        self.ui.completedadminbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.reviewsadminvutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.homebutton_admin.setStyleSheet(inactive_button_style)
        self.ui.productsbutton_admin.setStyleSheet(inactive_button_style)
        self.ui.orderstatusbutton_admin.setStyleSheet(active_button_style)
        self.ui.messbutton_admin.setStyleSheet(inactive_button_style)
    def adminmain_to_orderstatus_complete(self):
        self.ui.stackedWidget_adminmain.setCurrentWidget(self.ui.orderstatus_admin)
        self.ui.stackedWidget_orderadmin.setCurrentWidget(self.ui.completeadminpage)
        self.ui.toshipadminbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.canceladminvutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.completedadminbutton.setStyleSheet(active_orderbutton_style)
        self.ui.reviewsadminvutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.homebutton_admin.setStyleSheet(inactive_button_style)
        self.ui.productsbutton_admin.setStyleSheet(inactive_button_style)
        self.ui.orderstatusbutton_admin.setStyleSheet(active_button_style)
        self.ui.messbutton_admin.setStyleSheet(inactive_button_style)
    def adminmain_to_orderstatus_review(self):
        self.ui.stackedWidget_adminmain.setCurrentWidget(self.ui.orderstatus_admin)
        self.ui.stackedWidget_orderadmin.setCurrentWidget(self.ui.reviewsadminpage)
        self.ui.toshipadminbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.canceladminvutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.completedadminbutton.setStyleSheet(inactive_orderbutton_style)
        self.ui.reviewsadminvutton.setStyleSheet(active_orderbutton_style)
        self.ui.homebutton_admin.setStyleSheet(inactive_button_style)
        self.ui.productsbutton_admin.setStyleSheet(inactive_button_style)
        self.ui.orderstatusbutton_admin.setStyleSheet(active_button_style)
        self.ui.messbutton_admin.setStyleSheet(inactive_button_style)        

    def go_to_productpage(self, id):
        print("id: ", id)
        print("product name: ", get_product_name_by_id(id))
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.productviewpage)
        self.ui.productname.setText(get_product_name_by_id(id))
        self.ui.productprice.setText(f"{str(get_product_price_by_id(id))}")
        img_path = get_first_img_for_product(id)
        pixmap = QPixmap(img_path)
        self.ui.mainpic.setPixmap(pixmap)
        self.ui.mainpic.setScaledContents(True)
        self.ui.numberofsold.setText(f"{str(get_product_sold_by_id(id))} Sold")
        
        self.ui.shopname.setText(get_shopname_by_product_id(id))
        
        # ----------------------- not done -----------------------
        if len(get_product_img_by_id(id)) > 1:
            self.ui.mainpic.setPixmap(QPixmap(get_product_img_by_id(id)[0]))
            self.ui.mainpic.setScaledContents(True)
        # --------------------------------------------------------
        
        # try:
        #     self.ui.addtocartbutton.clicked.disconnect()
        # except TypeError:
        #     pass
        
        self.ui.addtocartbutton.clicked.connect(self.add_to_cart(id))
        # self.ui.addtocartbutton.clicked.connect(functools.partial(self.add_to_cart, id))
        self.ui.buynowbutton.clicked.connect(lambda: self.purchase_cartpage("productpage", id))


    def go_to_home(self):
        print("go to home")
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.homepage)
        self.ui.homebutton.setStyleSheet(active_button_style)
        self.ui.favbutton.setStyleSheet(inactive_button_style)
        self.ui.orderbutton.setStyleSheet(inactive_button_style)
        self.ui.messbutton.setStyleSheet(inactive_button_style)
        
        total_num_of_products = len(get_all_products())
        print("total_num_of_products: ", total_num_of_products)
        print("all products name and id: \n", get_all_product_name_and_id())
        if total_num_of_products > 0:
            # self.display_product_main(6)
            self.display_product(False, "homepage_customer")
            # self.display_product_main(get_random_product_id())
            
    def print_cart(self):
        print("------------------CART------------------")
        for i in get_user_cart_product_id():
            print("products in cart and id: ", (get_product_name_by_id(i[0])), i[1])
            print("Total product price in cart: ", self.add_total_price_in_cart())
        print("---------------------------------------")
    
    def add_total_price_in_cart(self):
        total_price = 0
        for i in get_user_cart_product_id():
            total_price += (i[1] * (get_product_price_by_id(i[0])))
        return total_price
            
    def add_to_cart(self, id):
        user = root.LoggedInUser.user.username
        if addToCart(id):
            transaction.commit()
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
        cart_products = get_user_cart_product_id()
        
        self.print_cart()
        
        for i in cart_products:
            self.ui.shopnameforcart.setText(get_shopname_by_product_id(i[0]))
            self.ui.productcartname.setText(get_product_name_by_id(i[0]))
            self.ui.productcartdescrip.setText(get_product_description_by_id(i[0]))
            self.ui.totalpricecartnumlabel.setText(str(get_product_price_by_id(i[0]) * i[1]))
            self.ui.productnum.setText(f"{i[1]} piece")
            self.ui.cartorderpic.setPixmap(QPixmap(get_first_img_for_product(i[0])))
            self.ui.cartorderpic.setScaledContents(True)
            
            self.ui.removecartbutton.clicked.connect(lambda: self.remove_item_from_cart(i[0]))
            self.ui.purchasecartbutton.clicked.connect(lambda: self.purchase_cartpage("cartpage"))
            
        
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
        self.ui.messbutton_admin.setStyleSheet(inactive_button_style)

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
            picproduct1_17 = QPushButton(product_widget)
            picproduct1_17.setObjectName(u"picproduct1_17")
            picproduct1_17.setMinimumSize(QSize(191, 188))
            picproduct1_17.setMaximumSize(QSize(191, 188))
            picproduct1_17.setStyleSheet(u"background-color: #FFF;\n"
            "image: url(:/pic/product_img/102165.jpg);\n"
            "border-radius: 0px;\n"
            "padding: 0;")
            product_gridLayout.addWidget(picproduct1_17, 0, 0, 1, 1)
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
            picproduct1_17 = product_widget.findChild(QPushButton, "picproduct1_17")
            
            productname_label.setText(get_product_name_by_id(products[i].id))
            productprice_button.setText(f"฿{str(get_product_price_by_id(products[i].id))}")
            productsold_label.setText(f"{products[i].sold} sold")
            img_path = get_product_img_by_id(products[i].id)[0]
            picproduct1_17.setStyleSheet(f"background-color: #FFF; image: url({img_path}); border-radius: 0px; padding: 0;")

            # picproduct1_17.clicked.connect(functools.partial(self.go_to_productpage(products[i].id)))
            picproduct1_17.clicked.connect(functools.partial(self.go_to_productpage, products[i].id))
            # go_to_productpage(products[i].id)
            
        # self.curr_widget.update()
        # self.curr_widget.adjustSize()

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
        self.ui.messbutton_admin.setStyleSheet(inactive_button_style)

        self.ui.producttypesbutton_admin.setStyleSheet(inactive_orderbutton_style)
        self.ui.allproductbutton_admin.setStyleSheet(active_orderbutton_style)

        self.ui.producttypesbutton_admin.clicked.connect(self.go_to_producttype_admin)
        
        num_of_products = count_products_for_user(root.LoggedInUser.user.username)
        if num_of_products > 0:
            self.display_product(True, "allproducts_admin")

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

        self.product_img = 0
        self.ui.img_1.setVisible(False)
        self.ui.delete_pic_button_1.setVisible(False)

        self.ui.addimagebutton.clicked.connect(self.add_img)

        self.ui.addproductbutton.clicked.connect(self.add_product)
        self.ui.canceladdproductbutton.clicked.connect(self.go_to_homepage_admin)
    
    def add_img(self):
        if self.add_product_img(self.ui.addimagebutton, self.ui.img_1, self.ui.delete_pic_button_1) and not self.img_button_clicked:
            print("add img")

            addoption_geometry = self.ui.addimagebutton.geometry()
            x_coordinate = addoption_geometry.x()
            y_coordinate = addoption_geometry.y()
            width = addoption_geometry.width()
            height = addoption_geometry.height()
            self.ui.addimagebutton.setGeometry(x_coordinate + 201, y_coordinate, width, height)
            imgbutton = QPushButton(self.ui.frame_addimageproduct)
            imgbutton.setObjectName(f"addimagebutton_{self.product_img}")
            imgbutton.setGeometry(x_coordinate, y_coordinate, width, height)
            imgbutton.setMinimumSize(151, 151)
            imgbutton.setMaximumSize(151, 151)
            imgbutton.setStyleSheet("border: 3px dashed #D9D9D9; font-size: 46px; background: #FAF9F6; color: #D9D9D9;")
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
                # self.add_img_to_stylesheet(fname)

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
        
    # click product from admin page
    def product_click_for_edit(self):
        pass

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
