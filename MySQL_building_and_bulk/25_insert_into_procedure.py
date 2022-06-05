'''
first add this procedure to your DB
mysql> delimiter $$
mysql> use publisher$$
Database changed
mysql> create definer= 'ashix'@'localhost' procedure InsertGroupBookProc (in gId varchar(6), in gName varchar(30), out result varchar(1))
    -> BEGIN
    -> declare c integer default 0;
    -> select count(*) into c from GroupBook where groupID = gId;
    -> if c = 0 then
    -> insert into GroupBook values(gId, gname);
    -> set result :='O';
    -> else
    -> set result := 'E';
    -> end if;
    -> end$$
mysql> delimiter ;
'''

import mysql.connector
from mysql.connector import Error



conn = mysql.connector.connect(
    host = 'localhost',
    user= 'ashix',
    passwd = 'P@ssw0rd',
    database= 'publisher'
)
cursor = conn.cursor()
groupID = input("Enter a group ID : ")
groupName= input("Enter a group Name : ")
para = []
para = list(para)
para.append(groupID)
para.append(groupName)
para.append('0')
para = tuple(para)
para = cursor.callproc('InsertGroupBookProc', para)
if para[2] == 'O':
    print('Record inserted.')
else:
    print('Error in insert...')


cursor.close()
conn.close()
print('Mysql connection is closed.')
