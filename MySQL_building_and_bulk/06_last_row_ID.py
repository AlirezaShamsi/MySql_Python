import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'ashix',
    passwd = 'P@ssw0rd',
    database = 'mydatabase'
)

myCursor = conn.cursor()
sql = 'insert into customers (name, address) values (%s, %s)'

name = input("Enter customer name : ")
address = input("Enter customer address : ")

val = (name, address)
myCursor.execute(sql, val)
conn.commit()
#show how many row add and show last id number of row
print(myCursor.rowcount, "Record insert", myCursor.lastrowid)