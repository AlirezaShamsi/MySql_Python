import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'ashix',
    passwd = 'P@ssw0rd',
    database = 'mydatabase',
)

myCursor = conn.cursor()
sql = "drop table if exists customers"


myCursor.execute(sql)

#there is no need to commit
#commit just for submit data in record