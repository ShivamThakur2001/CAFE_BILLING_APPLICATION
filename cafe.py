import sqlite3
connection = sqlite3.connect("Cafe.db")
cursor = connection.cursor()
command = "CREATE TABLE IF NOT EXISTS billitems(billno INTEGER, itemname TEXT, unitprice INTEGER, quantity INTEGER, totalprice INTEGER)"
cursor.execute(command)
command = "CREATE TABLE IF NOT EXISTs products(itemname TEXT, imagename TEXT, unitprice INTEGER)"
cursor.execute(command)
connection.commit

cursor = connection.execute("DELETE FROM PRODUCTS")
connection.execute("INSERT INTO PRODUCTS VALUES('Tea','Tea.jpg',10)")
connection.execute("INSERT INTO PRODUCTS VALUES('Coffee','Coffee.jpg',20)")
connection.execute("INSERT INTO PRODUCTS VALUES('Pizza','Pizza.jpeg',100)")
connection.execute("INSERT INTO PRODUCTS VALUES('Burger','Burger.jpg',60)")
connection.execute("INSERT INTO PRODUCTS VALUES('Sandwich','Sandwich.jpg',50)")
connection.execute("INSERT INTO PRODUCTS VALUES('Fench Fries','Fench Fries.jpg',40)")
connection.execute("INSERT INTO PRODUCTS VALUES('Ice Cream','Ice Cream.jpg',50)")
connection.execute("INSERT INTO PRODUCTS VALUES('Mojito','Mojito.jpg',90)")
connection.execute("INSERT INTO PRODUCTS VALUES('Shake','Shake.jpg',120)")
connection.execute("INSERT INTO PRODUCTS VALUES('Cold Drinks','Cold Drinks.jpg',45)")
connection.commit()
connection.close()