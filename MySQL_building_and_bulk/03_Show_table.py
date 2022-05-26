import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'ashix',
    passwd = 'P@ssw0rd',
    database = 'mydatabase'
)

myCursor = conn.cursor()
myCursor.execute('show tables')
for x in myCursor:
    print(x)