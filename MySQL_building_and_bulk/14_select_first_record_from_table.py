import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'ashix',
    passwd = 'P@ssw0rd',
    database = 'publisher',    
)

myCursor = conn.cursor()
sql = 'select * from publishers'
myCursor.execute(sql)

myResult = myCursor.fetchone()

print(myResult)

for x in myResult:
    print(x)