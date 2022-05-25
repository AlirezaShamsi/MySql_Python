import mysql.connector

#connect to database
com = mysql.connector.connect(user='root', database='test')

#show DBI level suppurt
print(mysql.connector.apilevel)


#Type of parameter connector/python
print(mysql.connector.paramstyle)


#A integer number who show security level of thread connector/python
print(mysql.connector.threadsafety)


#connector/python Version 
print(mysql.connector.__version__)

#connector/python in array
print(mysql.connector.__version_info__)
