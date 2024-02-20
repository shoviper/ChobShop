import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
# from .Signup import Ui_MainWindow
from Signup import *

class SignupWindow(QMainWindow):
    def __init__(self):
        super(SignupWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Apply CSS styles
        self.setStyleSheet("""
            /* Central widget styling */
            QWidget#centralwidget {
                background-color: #FAF9F6;
            }
                           
            QWidget#widget {
                background-color: #FAF9F6;
            }
                           
            QWidget#widget_2 {
                background-color: #E1E3E7;
                margin-left: 27px;
                border-radius: 25px;
            }

            /* Label styling */
            QLabel#label {
                color: #000;
                font-family: Inter;
                font-size: 48px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            }
                           
            QLabel#label_2 {
                color: #CD4662;
                text-align: center;
                font-family: Inter;
                font-size: 20px;
                font-style: normal;
                font-weight: 400;
                line-height: normal;
                margin-left: 75px;
            }
                           
            QLabel#label_3 {
                color: #AEC289;
                font-family: Inter;
                font-size: 20px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            }
            
            QLabel#label_5 {
                color: #CD4662;
                text-align: center;
                font-family: Inter;
                font-size: 18px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
                margin-left: 280px;
            }

            /* Push button styling */
            QPushButton#pushButton {
                background-color: #CD4662;
                color: #FFF;
                text-align: center;
                font-family: Inter;
                font-size: 24px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
                border-radius: 25px;
            }

            QPushButton#pushButton:hover {
                background-color: #0056b3;
            }

            /* LineEdit styling */
            QLineEdit#lineEdit {
                font-size: 24px;
                width: 500px;
                height: 80px;
                border-bottom: 3px solid #000;
                background-color: #FAF9F6;
            }
            
            QLineEdit#lineEdit_2 {
                font-size: 24px;
                width: 500px;
                height: 80px;
                border-bottom: 3px solid #000;
                background-color: #FAF9F6;
            }
            
            QLineEdit#lineEdit_3 {
                font-size: 24px;
                width: 500px;
                height: 80px;
                border-bottom: 3px solid #000;
                background-color: #FAF9F6;
            }
                           
            QCheckBox#checkBox {
                color: #CD4662;
            }

            /* MenuBar styling */
            QMenuBar#menubar {
                background-color: #ffffff;
                border-bottom: 1px solid #cccccc;
            }

            /* StatusBar styling */
            QStatusBar#statusbar {
                background-color: #ffffff;
                border-top: 1px solid #cccccc;
            }
        """)
        self.display_image()
        self.ui.label_3.mousePressEvent = self.open_login_window

    def display_image(self):
        image_path = "pic/loginpic.png"
        pixmap = QPixmap(image_path)

        label = QLabel(self.ui.widget_2)
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, 947, 827)
        label.setScaledContents(True)

    def open_login_window(self, event):
        pass
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SignupWindow()
    window.show()
    sys.exit(app.exec())