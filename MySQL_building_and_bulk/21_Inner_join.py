import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'ashix',
    passwd = 'P@ssw0rd',
    database = 'publisher',    
)

myCursor = conn.cursor()
#join 3 table with inner join
sql = "select title , price, afname, alname from autbook as a inner join authors au on a.atID = au.atID inner join books b on b.ISBN = a.ISBN"
myCursor.execute(sql)
myResult = myCursor.fetchall()
for x in myResult:
    print(x)