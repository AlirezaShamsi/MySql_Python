from __future__ import print_function
from lib2to3.pgen2.token import STRING
import mysql.connector
from mysql.connector import FieldType


#creat mysqlcursor
con = mysql.connector.connect(user='scott', database='test')
cursor = con.curser()

#execute method return data from table
cursor.execute("SELECT DATE(NOW()) AS 'c1', TIME(NOW()) as 'c2', " "NOW() AS 'c3', 'a STRING' AS 'c4', 42 AS 'c5'")

#fetch remaining row from table
rows = cursor.fetchall()
for desc in cursor.descriprion:
    colname =  desc[0]
    coltype = desc[1]
    print("Column {} has type {}".format(colname, FieldType.get_info(coltype)))
    #close all result and ensure that cursor object have no connection with DB(mysql)
    cursor.close()
    con.close()



