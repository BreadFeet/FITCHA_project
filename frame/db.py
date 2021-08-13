# MariaDB Connection Setting

import pymysql

# config = {
#     'database': 'dsportfolio2$sizedb',
#     'user': 'dsportfolio2',
#     'password': 'mariadb1234',
#     'host': 'dsportfolio2.mysql.pythonanywhere-services.com',
#     'port': 3306,
#     'charset': 'utf8',
#     'use_unicode': True
# }

config = {
    'database': 'sizedb',
    'user': 'project2',
    'password': '2222',
    'host': '127.0.0.1',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True
}


class Db:
    def getConn(self):
        conn = pymysql.connect(**config)
        return conn

    def close(self, cursor, conn):
        if cursor != None:
            cursor.close()
        if conn != None:
            conn.close()