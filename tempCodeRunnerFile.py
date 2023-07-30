from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5.QtPrintSupport import QPrinter 
from datetime import date
import sys
import sqlite3

ui, _ = loadUiType("Cafe.ui")

class MainApp(QMainWindow,ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)
        self.LOGINBUTTON.clicked.connect(self.login)
    ## ADMIN LOGIN ##
    def login(self):
        un = self.USERNAME.text()
        pw = self.PASSWORD.text()
        if(un =="Admin" and pw == "Admin@123"):
            self.USERNAME.setText("")
            self.PASSWORD.setText("")
            self.tabWidget.setCurrentIndex(1)
        else:
            self.LOGININFO.setText("Invalid Details")

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()