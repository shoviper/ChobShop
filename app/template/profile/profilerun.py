import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from app.template.profile.Profile import *

class Profile(QMainWindow):
    def __init__(self):
        super(Profile,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.backbutton.clicked.connect(self.go_to_homepage)
        self.ui.editprofilebutton.clicked.connect(self.go_to_profiledit)

    def go_to_homepage(self):
        from app.template.homepage.Homepagerun import HomepageWindow
        self.home = HomepageWindow()
        self.close()
        self.home.show()

    def go_to_profiledit(self):
        from app.template.profile.profileeditrun import ProfileEdit
        self.home = ProfileEdit()
        self.close()
        self.home.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Profile()
    window.show()
    sys.exit(app.exec())