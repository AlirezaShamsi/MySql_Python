import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'ashix',
    passwd = 'P@ssw0rd',
    database = 'publisher',    
)

myCursor = conn.cursor()

name = input("Enter Publisher name:")

sql = 'select * from publishers where pname = %s'
val = (name, )
myCursor.execute(sql, val)

myResult = myCursor.fetchall()
for x in myResult:
    print(x)