import mysql.connector
import psycopg2
from mysql.connector import Error
from mysql.connector import errorcode


try:
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'ashix',
        passwd = 'P@ssw0rd',
        database = 'mydatabase',
    )

    conn.autocommit = False
    cursor = conn.cursor()
    id1 = int(input("Enter id1: "))
    id2 = int(input("Enter id2: "))
    amount = int(input("Enter Amount: "))
    query = 'select balance from account where id = ' + str(id1)
    cursor.execute(query)
    record = cursor.fetchone()
    balance_account_A = int(record[0])
    balance_account_A -= amount

    #withraw from account A now
    sql_updata_query = 'update account set balance = % where id = ' + str(id1)
    cursor.execute(query)
    record = cursor.fetchone()
    balance_account_B = int(record[0])
    balance_account_B += amount

    #credit to account B now
    sql_updata_query = 'Update account set balance = %s where id = '+ str(id2)
    cursor.execute(sql_updata_query, (balance_account_B, ))

    #commiting both the transaction to database
    conn.commit()
    print("Transaction completed successfully ")
except(Exception, psycopg2.DatabaseError) as error:
    print("Error in transaction reverting all other operations of a transaction", error)
    conn.rollback()

finally:
    #closing database connection 
    if(conn):
        cursor.close()
        conn.close()
        print("MySql connection in closed")