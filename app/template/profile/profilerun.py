import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from app.template.homepage.Homepage_newres_ui import *
from app.db.database import *

class Userprofile(QMainWindow):
    def __init__(self):
        super(Userprofile,self).__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        
        self.ui.homebutton_userprofile.clicked.connect(self.go_to_homepage)
        self.ui.editprofilebutton_1.clicked.connect(self.go_to_profiledit)
        self.ui.editprofilebutton_2.clicked.connect(self.go_to_profiledit)
        self.ui.openshopbutton.clicked.connect(self.admin_register)

    def go_to_homepage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)

    def go_to_profiledit(self):
        # self.ui.stackedWidget.setCurrentWidget(self.ui.)
        print("go to edit profile")

    def go_to_admin_register(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.adminwidget)
        self.ui.stackedWidget_adminwidget.setCurrentWidget(self.ui.adminregisterpage)

        self.ui.adminregisterbutton.clicked.connect(self.admin_register)

    def adminregister(self):
        print("Registering as admin")
        username = root.LoggedInUser.user.username
        password = root.LoggedInUser.user.password
        shopname = self.ui.shopnamebox.text()
        firstname = self.ui.firstnamebox_admin.text()
        lastname = self.ui.lastnamebox_admin.text()
        description = self.ui.descriptionbox_admin.toPlainText()
        address = self.ui.addressbox_admin.toPlainText()
        email = self.ui.emailbox_admin.text()
        phone = self.ui.phonebox_admin.text()
        if registerAdmin(username, shopname, firstname, lastname, description, address, email, phone, password):
            print("Admin registered successfully")
            self.show_success("Admin registered successfully")
            self.go_to_homepage()
        else:
            print("Admin registration failed")
            self.show_error("Admin registration failed")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Userprofile()
    window.show()
    sys.exit(app.exec())