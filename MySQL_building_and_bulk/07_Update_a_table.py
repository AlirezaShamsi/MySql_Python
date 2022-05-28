from audioop import add
import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'ashix',
    passwd = 'P@ssw0rd',
    database = 'mydatabase',
)

myCursor = conn.cursor()
ID = int(input("Enter Customer ID : "))
name = input("Enter Customer name : ")
address = input("Enter Customer address : ")
val = (name, address)
sql = "update customers set name = '" + name + "'" + ", " +"address = " + "'" + address +"'"
sql += " where custID = " + str(ID)

myCursor.execute(sql)
conn.commit()
print(myCursor.rowcount, "records(s) affected")