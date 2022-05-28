import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'ashix',
    passwd = 'P@ssw0rd',
)

myCursor = conn.cursor()
sql = "drop database if exists mydatabase"


myCursor.execute(sql)

#there is no need to commit
#commit just for submit data in record