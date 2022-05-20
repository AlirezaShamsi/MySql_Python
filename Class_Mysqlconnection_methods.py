import mysql.connector
#Connect as alireza
con = mysql.connector.MySQLConnection(user= 'alireza', database= 'test')

#then write these commands to connect as root 'reconnect method is very method'
con.config(user='root')
con.reconnect()

#add a record to employee and then commited it to database
#NOTE: commit must be enter every time you change a query from databse using poython this is not automaticaly
cursor.execute("INSERT INTO emoployees (first name) VALUES (%s)", ('alireza'))
con.commit()

