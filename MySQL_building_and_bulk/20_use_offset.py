import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'ashix',
    passwd = 'P@ssw0rd',
    database = 'publisher',    
)

myCursor = conn.cursor()
start = input("Enter number of rows that you want to start : ")
num = input("Enter number of rows that you want : ")

#use offset command to start from it
sql = "select title, price from books limit " + num + " offset " + start

myCursor.execute(sql)
myResult = myCursor.fetchall()
for x in myResult:
    print(x)

