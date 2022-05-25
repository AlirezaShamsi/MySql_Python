import mysql.connector
conn = mysql.connector.connect(
    host= 'localhost',
    user = 'ashix',
    passwd = 'P@ssw0rd'
)

myCursor = conn.cursor()
if myCursor:
    myCursor.execute("CREATE DATABASE myDatabase")
    print("myDatabase is create")

else:
    print('Error!')
