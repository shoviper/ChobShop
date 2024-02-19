import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from Signup import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Apply CSS styles
        self.setStyleSheet("""
            /* Central widget styling */
            QWidget#centralwidget {
                background-color: #FAF9F6;
            }

            /* Label styling */
            QLabel#label {
                color: #000;
                font-family: Inter;
                font-size: 30px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            }
                           
            QLabel#label_2 {
                color: #CD4662;
                font-family: Inter;
                font-size: 12px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            }
                           
            QLabel#label_3 {
                color: green;
                font-family: Inter;
                font-size: 12px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            }

            /* Push button styling */
            QPushButton#pushButton {
                background-color: #CD4662;
                color: #FFF;
                text-align: center;
                font-family: Inter;
                font-size: 15px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            }

            QPushButton#pushButton:hover {
                background-color: #0056b3;
            }

            /* LineEdit styling */
            QLineEdit#lineEdit {
                width: 500px;
                height: 80px;
                flex-shrink: 0;
                border-bottom: 3px solid #000;
                background-color: #FAF9F6
            }
            
            QLineEdit#lineEdit_2 {
                width: 500px;
                height: 80px;
                flex-shrink: 0;
                border-bottom: 3px solid #000;
                background-color: #FAF9F6
            }
                           
            QLineEdit#lineEdit_3 {
                width: 500px;
                height: 80px;
                flex-shrink: 0;
                border-bottom: 3px solid #000;
                background-color: #FAF9F6
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
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())