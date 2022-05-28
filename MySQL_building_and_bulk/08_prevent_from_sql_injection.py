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
val = (name, address, ID)

#for prevent sql injection use argument specifiers instead of sql complete syntax
sql = "update customers set name = %s, address =%s where custID = %s"

myCursor.execute(sql, val)
conn.commit()
print(myCursor.rowcount, "records(s) affected")