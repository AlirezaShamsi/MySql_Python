import mysql.connector

conn = mysql.connector.connect (
    host = 'localhost',
    user = 'ashix',
    passwd = 'P@ssw0rd',
    database = 'publisher',
)

myCursor = conn.cursor()
myCursor.execute('select * from groupbook')

#this build a list from fetching records
myResult = myCursor.fetchall()

#this divided each index in one line
print(myResult)
for x in myResult :
    print(x)