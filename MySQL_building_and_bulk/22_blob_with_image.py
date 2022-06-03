import mysql.connector
from mysql.connector import Error

def convertToBinaryData(filename):
    #convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(emp_id, name, photo, biodataFile):
    print("Inserting BLOB into Employee table")
    try:
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'ashix',
            passwd = 'P@ssw0rd',
            database = 'myDatabase',
        )

        cursor = conn.cursor()
        sql_insert_blob_query = """insert into employee (id, name, photo, biodata) values (%s, %s, %s,%s)"""
        empPicture = convertToBinaryData(photo)
        file = convertToBinaryData(biodataFile)
        
        #convert data into tuple format
        insert_blob_tuple = (emp_id, name, empPicture, file)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        conn.commit()
        print("Image and file inserted successfully as a BLOB into employee table", result)
    except mysql.connector.Error as error:
        print("Faild inserting BLOB data into MySQL table {}".format(error))
    
    finally:
        if(conn.is_connected()):
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

insertBLOB(1, 'Alfred Becon', 'C:\\Users\\Alireza\\git\\MySql\\MySQL_building_and_bulk\\Data\\22_BLOB_with_image\\1.jpg', 'C:\\Users\\Alireza\\git\\MySql\\MySQL_building_and_bulk\\Data\\22_BLOB_with_image\\1.txt')
insertBLOB(2, 'Hazar ferdinand', 'C:\\Users\\Alireza\\git\\MySql\\MySQL_building_and_bulk\\Data\\22_BLOB_with_image\\2.jpg', 'C:\\Users\\Alireza\\git\\MySql\\MySQL_building_and_bulk\\Data\\22_BLOB_with_image\\2.txt')