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
mysql.connector.MySQLConnection.cmd_init_db("AlirezaBase")

#Checks connection to dbmsServer
#NOTE: DONT USE IT DIRECTLY
mysql.connector.MySQLConnection.cmd_ping()

#first command kill 123 thread
#second command delete thread 123
mysql.connector.MySQLConnection.cmd_process_kill(123)
mysql.connector.MySQLConnection.cmd_query('KILL 123')

#Send multiple command to database
statement = 'SELECT 1; INSERT INTO t1 VALUES(); SELECT 2;'
for result in mysql.connector.MySQLConnection.cmd_query_iter(statement):
    if 'columns' in result:
        columns = result['columns']
        rows = con.get_row()
    else:
        #Do nothing

#Close conection
#in my sql 8 it is doesent work
mysql.connector.MySQLConnection.cmd.quit()

#turrning off Database
mysql.connector.MySQLConnection.cmd_shutdown()

#returns a dictinary include information about MySQL server
mysql.connector.MySQLConnection.cmd_statistics()

#Send QUIT command to DB and close socket without any Exception
mysql.connector.MySQLConnection.disconnect()

#This method retrieves all or remaining rows of a query result set, returning a tuple containing the rows as sequences and the EOF packet information.
mysql.connector.MySQLConnection.get_rows(count=None)

#This method retrieves remaining row
mysql.connector.MySQLConnection.get_row()

#Version of MYSQL
mysql.connector.MySQLConnection.get_server_version()

#checking connection between host and Mysql
mysql.connector.MySQLConnection.is_connected()

#if client flag is activated return true else false
mysql.connector.MySQLConnection.isset_client_flag()

#checking connection with to args for ping
mysql.connector.MySQLConnection.ping(attempts=1, delay=0)

#Reconnect
mysql.connector.MySQLConnection.reconnect(attempts=1, delay=0)

#rollback
mysql.connector.MySQLConnection.rollback()


#Define chars and collation
mysql.connector.MySQLConnection.set_charset_collation(charset=None, collation=None)
#example
con = mysql.connector.MySQLConnection(user= 'alireza')
mysql.connector.MySQLConnection.set_charset_collation('latin1', 'latin1_general_ci')

#config client flag
mysql.connector.MySQLConnection.set_client_flags(flags)

#star a transaction
mysql.connector.MySQLConnection.start_transaction()

#set autocommit false or true (default is false)
mysql.connector.MySQLConnection.autocommit = True

#name of chars
mysql.connector.MySQLConnection.charset_name

#name of collation
mysql.connector.MySQLConnection.collation_name

#return connection id as int
mysql.connector.MySQLConnection.connection_id

#run USE command for choice database
mysql.connector.MySQLConnection.database='Publishers'


#Turn warning on or off
mysql.connector.MySQLConnection.get_warnings

#shown a transactin is disable or enable
mysql.connector.MySQLConnection.in_transaction


#when a warning accourd rais exception
mysql.connector.MySQLConnection.raise_on_warnings

#name of host or ip (string)
mysql.connector.MySQLConnection.server_host

#number of port
mysql.connector.MySQLConnection.server_port

#return sql modes
mysql.connector.MySQLConnection.sql_mode

#time zone configuration
mysql.connector.MySQLConnection.time_zone

#Show informatin in INFORMATION_SCHEMA in database
con.cmd_process_info()






