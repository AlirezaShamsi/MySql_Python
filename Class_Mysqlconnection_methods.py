from os import kill
import mysql.connector
#Connect as alireza
con = mysql.connector.MySQLConnection(user= 'alireza', database= 'test')

#then write these commands to connect as root 'reconnect method is very method'
con.config(user='root')
con.reconnect()

#add a record to employee and then commited it to database
#NOTE: commit must be enter every time you change a query from databse using poython this is not automaticaly
mysql.connector.MySQLConnection.cursor.execute("INSERT INTO emoployees (first name) VALUES (%s)", ('alireza'))
con.commit()

#Cursor method
mysql.connector.MySQLConnection.cursor(buffered=None, raw=None, cursor_class=None)

#cmd methods:
#1.Write debugging in log(must be SUPER user)
mysql.connector.MySQLConnection.cmd_debug()

#2.use defined database in there "AlirezaBase" initial database
mysql.connector.MySQLConnection.cmd_init_db(AlirezaBase)

#Checks connection to dbmsServer
#NOTE: DONT USE IT DIRECTLY
mysql.connector.MySQLConnection.cmd_ping()

#Show informatin in INFORMATION_SCHEMA in database
mysql.connector.MySQLConnection.cmd_process_info()


#first command kill 123 thread
#second command delete thread 123
con.cmd_process_kill(123)

