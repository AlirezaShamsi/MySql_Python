import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'ashix',
    passwd = 'P@ssw0rd',
    database = 'publisher',    
)

myCursor = conn.cursor()

lname = input("Enter Author last name: ")

sql = 'select * from authors where alname like "%'+ lname + '%"'

myCursor.execute(sql)
myResult = myCursor.fetchall()
for x in myResult:
    print(x)