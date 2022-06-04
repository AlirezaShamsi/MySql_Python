
#first create this table in your MySQL
"""
mysql> delimiter $$
mysql> use publisher$$
Database changed
mysql> create definer='ashix'@'localhost' procedure 'GroupBookProc' (IN groupIdBook varchar(6))
    -> BEGIN
    -> select * from GroupBook where groupID = groupIdBook;
    -> END $$

"""

import mysql.connector
from mysql.connector import Error
try:
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'ashix',
        passwd = 'P@ssw0rd',
        database = 'publisher',
    )
    cursor = conn.cursor()
    groupID = input('Enter a group ID :')
    para = []
    para.append(groupID)
    cursor.callproc('GroupBookProc', para)
    #print results
    print("Printing groupbook details")
    for result in cursor.stored_results():
        print(result.fetchall())
except Error as error:
    print("Faild to execute stored procedure : {}".format(error))

finally:
    if(conn.is_connected()):
        cursor.close()
        conn.close()
        print("MySql connection is closed")
