from __future__ import print_function
from distutils.command.config import config
import sys
import mysql.connector
from mysql.connector.constants import ClientFlag
config = {
    'user': 'root',
    'password': '565565',
    'host': '127.0.0.1',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': '/opt/mysql/ssl/ca-cert.pem',
    'ssl_cert': '/opt/mysql/ssl/client-cert.pem',
    'ssl_key': '/opt/mysql/ssl/client-key.pem',
}

con = mysql.connector.connect(**config)
cur = con.cursor(buffered=True)
cur.execute("SHOW STATUS LIKE 'Ssl_clipher'")
print(cur.fetchone())
cur.close()
con.close()