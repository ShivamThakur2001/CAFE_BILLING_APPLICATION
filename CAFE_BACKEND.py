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
    items = ["ITEMS"]
    price = [0]
    images = ["IMAGES"]
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)
        self.LOGINBUTTON.clicked.connect(self.login)
        self.LOGOUT.clicked.connect(self.logout)
        self.FOODBUTTON1.clicked.connect(lambda : self.addproducts(1))
        self.FOODBUTTON2.clicked.connect(lambda : self.addproducts(2))
        self.FOODBUTTON3.clicked.connect(lambda : self.addproducts(3))
        self.FOODBUTTON4.clicked.connect(lambda : self.addproducts(4))
        self.FOODBUTTON5.clicked.connect(lambda : self.addproducts(5))
        self.FOODBUTTON6.clicked.connect(lambda : self.addproducts(6))
        self.FOODBUTTON7.clicked.connect(lambda : self.addproducts(7))
        self.FOODBUTTON8.clicked.connect(lambda : self.addproducts(8))
        self.FOODBUTTON9.clicked.connect(lambda : self.addproducts(9))
        self.FOODBUTTON10.clicked.connect(lambda : self.addproducts(10))
        self.PRINTBILL.clicked.connect(self.printreceipt)
        self.DONTPRINTBILL.clicked.connect(self.dontprintreceipt)
        self.SETTINGS.clicked.connect(self.gosettings)
        self.ITEMSLIST.currentIndexChanged.connect(self.show_item_name)
        self.MODIFYBUTTON.clicked.connect(self.modifyitem)
        self.BACKBUTTON.clicked.connect(self.go_back)

    ## ADMIN LOGIN ##
    def login(self):
        un = self.USERNAME.text()
        pw = self.PASSWORD.text()
        if(un =="Admin" and pw == "Admin@123"):
            self.USERNAME.setText("")
            self.PASSWORD.setText("")
            self.getbill_number()
            self.tabWidget.setCurrentIndex(1)
        else:
            self.LOGININFO.setText("Invalid Details")

    ## LOGOUT ##
    def logout(self):
        self.tabWidget.setCurrentIndex(0)
    
    ## GENERATING BILL NUMBER AND DATE ##
    def getbill_number(self):
        con = sqlite3.connect("Cafe.db")
        cursor = con.execute("SELECT MAX(billno) FROM billitems")
        result = cursor.fetchall()
        if result:
            try:   
                for data in result:
                    billno = int(data[0]) + 1
            except:
                billno = 1
        else:
            billno = 1
        self.BILLNO.setText(str(billno))
        self.DATE.setText(str(date.today()))
        self.configureitems()

    ## ADD ITEMS ##
    def configureitems(self):
        self.items = ["ITEMS"]
        self.images = ["IMAGES"]
        self.price = [0]
        con = sqlite3.connect("Cafe.db")
        cursor = con.execute("SELECT * FROM products")
        result = cursor.fetchall()
        if result:
            for prod in result:
                self.items.append(str(prod[0]))
                self.images.append(str(prod[1]))
                self.price.append(str(prod[2]))
        con.close()

        ## FIRST ITEM ##
        self.FOODNAME1.setText(self.items[1])
        self.FOODPRICE1.setText("RS : " + self.price[1])
        filename = "./" + self.images[1]
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.FOODIMAGE1.setPixmap(pm)
        
        ## SECOND ITEM ##
        self.FOODNAME2.setText(self.items[2])
        self.FOODPRICE2.setText("RS : " + self.price[2])
        filename = "./" + self.images[2]
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.FOODIMAGE2.setPixmap(pm)

        ## THIRD ITEM ##
        self.FOODNAME3.setText(self.items[3])
        self.FOODPRICE3.setText("RS : " + self.price[3])
        filename = "./" + self.images[3]
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.FOODIMAGE3.setPixmap(pm)

        ## FOURTh ITEM ##
        self.FOODNAME4.setText(self.items[4])
        self.FOODPRICE4.setText("RS : " + self.price[4])
        filename = "./" + self.images[4]
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.FOODIMAGE4.setPixmap(pm)

        ## FiFTH ITEM ##
        self.FOODNAME5.setText(self.items[5])
        self.FOODPRICE5.setText("RS : " + self.price[5])
        filename = "./" + self.images[5]
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.FOODIMAGE5.setPixmap(pm)

        ## SIXTH ITEM ##
        self.FOODNAME6.setText(self.items[6])
        self.FOODPRICE6.setText("RS : " + self.price[6])
        filename = "./" + self.images[6]
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.FOODIMAGE6.setPixmap(pm)

        ## SEVENTH ITEM ##
        self.FOODNAME7.setText(self.items[7])
        self.FOODPRICE7.setText("RS : " + self.price[7])
        filename = "./" + self.images[7]
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.FOODIMAGE7.setPixmap(pm)

        ## EIGTH ITEM ##
        self.FOODNAME8.setText(self.items[8])
        self.FOODPRICE8.setText("RS : " + self.price[8])
        filename = "./" + self.images[8]
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.FOODIMAGE8.setPixmap(pm)

        ## NINTH ITEM ##
        self.FOODNAME9.setText(self.items[9])
        self.FOODPRICE9.setText("RS : " + self.price[9])
        filename = "./" + self.images[9]
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.FOODIMAGE9.setPixmap(pm)

        ## TENTH ITEM ##
        self.FOODNAME10.setText(self.items[10])
        self.FOODPRICE10.setText("RS : " + self.price[10])
        filename = "./" + self.images[10]
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.FOODIMAGE10.setPixmap(pm)

    ## ADDING PRODUCTS TO TABLE ##
    def addproducts(self,id):
        billno = int(self.BILLNO.text())
        itemname = str(self.items[id])
        unitprice = self.price[id]
        quantity = "1"
        con = sqlite3.connect("Cafe.db")
        cursor = con.execute("SELECT * FROM billitems WHERE itemname = '" + itemname +"' and billno =  "+ str(billno) +" ")
        result = cursor.fetchall()
        if result:
            con.execute("UPDATE billitems SET quantity = quantity + 1, totalprice = totalprice + "+ str(unitprice) +" WHERE itemname = '"+ itemname +"' and billno = "+ str(billno) +" ")
            con.commit()
        else:
            con.execute("INSERT INTO billitems (billno,itemname,unitprice,quantity,totalprice) values("+ str(billno) +", '"+ itemname +"',"+ str(unitprice) +","+ quantity +","+ str(unitprice) +")")
            con.commit()
        self.filltable()

    ## SHOW ITEMS IN THE TABLE ##
    def filltable(self):
        total = 0
        self.billitems.setRowCount(0)
        self.billitems.clear()
        self.billitems.setColumnWidth(0,110)
        self.billitems.setColumnWidth(1,60)
        self.billitems.setColumnWidth(2,60)
        self.billitems.setColumnWidth(3,60)
        con = sqlite3.connect("Cafe.db")
        cursor = con.execute("SELECT itemname, unitprice, quantity, totalprice FROM billitems WHERE billno = "+ self.BILLNO.text() +"")
        result = cursor.fetchall()
        r = 0
        c = 0
        for row_number, row_data in enumerate(result):
            r += 1
            c = 0
            for column_number, data in enumerate(row_data):
                c += 1
        self.billitems.setColumnCount(c)
        for row_number, row_data in enumerate(result):
            self.billitems.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.billitems.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        self.billitems.verticalHeader().setVisible(False)
        self.billitems.horizontalHeader().setVisible(False)
        cursor = con.execute("SELECT * FROM billitems WHERE billno = "+ str(self.BILLNO.text()) +" ")
        result = cursor.fetchall()
        if result:
            for prod in result:
                total = total + int(prod[4])
        self.TOTAL.setText("%.2f" % (total))
        self.TAX.setText("%.2f" % (total*0.05))
        self.GRANDTOTAL.setText("%.2f" % (total + (total * 0.05) ))

    ## PRINTING RECEIPT ##
    def printreceipt(self):
        if(self.GRANDTOTAL.text() != "0.00"):
            printer = QPrinter()
            painter = QPainter()
            painter.begin(printer)
            screen = self.PRINTAREA.grab()
            painter.drawPixmap(10,10,screen)
            painter.end()
            self.getbill_number()
            self.filltable()

    ## NOT PRINTING RECEIPT ##
    def dontprintreceipt(self):
        if(self.GRANDTOTAL.text() != "0.00"):
            self.getbill_number()
            self.filltable()

    ## GO TO SETTINGS ##
    def gosettings(self):
        self.tabWidget.setCurrentIndex(2)
        con = sqlite3.connect("Cafe.db")
        cursor = con.execute("SELECT * FROM products")
        result = cursor.fetchall()
        if result:
            for prod in result:
                self.ITEMSLIST.addItem(str(prod[0]))
    
    def show_item_name(self):
        con = sqlite3.connect("Cafe.db")
        cursor = con.execute("SELECT * FROM products WHERE itemname = '"+ self.ITEMSLIST.currentText() +"' ")
        result = cursor.fetchall()
        if result:
            for prod in result:
                self.ITEMNAME.setText(str(prod[0]))
                self.ITEMIMAGE.setText(str(prod[1]))
                self.ITEMPRICE.setText(str(prod[2]))
                self.SETTINGNAME.setText(str(prod[0]))
                self.SETTINGPRICE.setText("RS : " + str(prod[2]))
                filename = "./" + str(prod[1])
                image = QImage(filename)
                pm = QPixmap.fromImage(image)
                self.SETTINGIMAGE.setPixmap(pm)

    ## MODIFY ITEMS ##
    def modifyitem(self):
        con = sqlite3.connect("Cafe.db")
        cursor = con.execute("UPDATE products SET itemname = '"+ self.ITEMNAME.text() +"', imagename = '"+ self.ITEMIMAGE.text() +"', unitprice = '"+ self.ITEMPRICE.text() +"' WHERE itemname = '"+ self.ITEMSLIST.currentText() +"'")
        con.commit()
        con.close()
        self.SETTINGNAME.setText(self.ITEMNAME.text())
        self.SETTINGPRICE.setText("RS : " + self.ITEMPRICE.text())
        filename = "./" + self.ITEMIMAGE.text()
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.SETTINGIMAGE.setPixmap(pm)
        self.configureitems()
        self.MODIFYINFO.setText("MODIFY SUCCESSFULLY")

    ## GO BACK ##
    def go_back(self):
        self.tabWidget.setCurrentIndex(1)

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()