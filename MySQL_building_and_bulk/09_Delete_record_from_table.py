import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'ashix',
    passwd = 'P@ssw0rd',
    database = 'mydatabase'
)

myCursor = conn.cursor()


#sql = input("Please enter command:")

ID = int(input("Enter customer ID : "))
sql = "delete from customers where custID = %s"

#val must be a tupple
val = (ID , )
myCursor.execute(sql, val)
conn.commit()
print(myCursor.rowcount, "record(s) deleted")