import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'ashix',
    passwd = 'P@ssw0rd',
    database = 'publisher',
)

myCursor = conn.cursor()

num = input("Enter number of rows that you want : ")
#use limit for rows
sql = 'select title, price from books limit ' + num
myCursor.execute(sql)
myResult =  myCursor.fetchall()
for x in myResult:
    print(x)