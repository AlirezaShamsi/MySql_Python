import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'ashix',
    passwd = 'P@ssw0rd',
    database = 'publisher',    
)

myCursor = conn.cursor()

sql = 'select title, price from books order by price'
myCursor.execute(sql)

myResult = myCursor.fetchall()
for x in myResult:
    print(x)