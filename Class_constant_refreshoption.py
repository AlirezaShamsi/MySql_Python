import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "ashix",
    passwd = "P@ssw0rd",
)
myCursor = conn.cursor()
if myCursor:
    print("CONNECTED :)")
else:
    print("Error!")


""""
type these commands on your mysql command line if u see error:ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)

mysql> create user 'usernew' @'localhost' identified by 'yourpassword';
Query OK, 0 rows affected (0.11 sec)

mysql> GRANT ALL PRIVILEGES ON *.* TO 'usernew'@'localhost';
Query OK, 0 rows affected (0.20 sec)

then replace your user with 'usernew'
"""