import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'ashix',
    passwd = 'P@ssw0rd',
    database = 'mydatabase'
)

myCursor = conn.cursor()
sql = 'insert into customers (name, address) values (%s, %s)'
n = int(input("Enter number of data: "))
valm = []

for i in range(0, n):
    print("\nEnter customer "+ str(i + 1) + " information")
    print("*********************************************2")
    name = input("Enter customer name : ")
    address = input("Enter customer address : ")
    val = (name, address)
    valm.append(val)
print(valm)
myCursor.executemany(sql,valm)
conn.commit()
print(myCursor.rowcount, "Record insert")
