import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from app.template.homepage.Homepage_newres_ui import *

class Userprofile(QMainWindow):
    def __init__(self):
        super(Userprofile,self).__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        print("Userprofile")
        self.ui.homebutton_userprofile.clicked.connect(self.go_to_homepage)
        self.ui.editprofilebutton_1.clicked.connect(self.go_to_profiledit)
        self.ui.editprofilebutton_2.clicked.connect(self.go_to_profiledit)

    def go_to_homepage(self):
        print("go to homepage")
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)

    def go_to_profiledit(self):
        # self.ui.stackedWidget.setCurrentWidget(self.ui.)
        print("go to edit profile")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Userprofile()
    window.show()
    sys.exit(app.exec())