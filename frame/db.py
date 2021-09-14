# MariaDB Connection Setting

import pymysql

# 아래 본인 연결계정 입력하세요
config = {
    'database': 'sizedb',
    'user': 'root',
    'password': '0000',
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