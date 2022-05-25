from multiprocessing import connection
import mysql.connector
#Connect as alireza
con = mysql.connector.MySQLConnection(user= 'alireza', database= 'test')

#then write these commands to connect as root 'reconnect method is very method'
con.config(user='root')
con.reconnect()


