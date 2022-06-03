import mysql.connector
from mysql.connector import Error

def write_file(data, filename):
    #convert binary data to proper format and write it on hard disk
    with open(filename, 'wb') as file:
        file.write(data)

def readBLOB(emp_id, photo, bioData):
    print("Reading BLOB data from python_employee table")
    print("Inserting BLOB into Employee table")
    try:
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'ashix',
            passwd = 'P@ssw0rd',
            database = 'mydatabase',
        )
        cursor = conn.cursor()
        sql_fetch_blob_query = """select * from employee where id = %s"""
        cursor.execute(sql_fetch_blob_query, (emp_id, ))
        record = cursor.fetchall()
        for row in record:
            print("ID = ", row[0])
            print("name = ", row[1])
            image = row[2]
            file = row [3]
            print("storing employee image and bio-data on disk \n")
            write_file(image, photo)
            write_file(file, bioData)
    except mysql.connector.Error as error:
        print("Faild to read BLOB data from MySQL table {}".format(error))
    finally:
        if(conn.is_connected()):
            cursor.close()
            conn.close()
            print("MySql connection is closed")

id = int(input("Enter ID: "))
imageFile = input("Enter Image path and file name: ")
bioFile = input("Enter Bio-data path and file name: ")
readBLOB(id, imageFile,bioFile)