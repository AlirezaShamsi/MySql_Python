import imp


import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "123465"
)
myCursor = conn.cursor()
if myCursor:
    print("CONNECTED :)")
else:
    print("Error!")