import mysql.connector
conn = mysql.connector.connect(
    host = 'localhost',
    user = 'ashix',
    passwd = 'P@ssw0rd',
    database = 'mydatabase'
)

myCursor = conn.cursor()
if myCursor:
    myCursor.execute("create table Customers (custID int auto_increment primary key, name varchar(255), address varchar(255))")
    print('table customers was created')
else:
    print("error!")