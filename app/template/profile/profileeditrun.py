import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from app.template.profile.ProfileEdit import *

class ProfileEdit(QMainWindow):
    def __init__(self):
        super(ProfileEdit,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.backbutton.clicked.connect(self.go_to_profile)

    def go_to_profile(self):
        from app.template.profile.profilerun import Profile
        self.home = Profile()
        self.close()
        self.home.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProfileEdit()
    window.show()
    sys.exit(app.exec())