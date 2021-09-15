# Customer Table 접속
from frame.sql import Sql
from frame.db import Db
from frame.vo import CustVO


class CustDB(Db):
    def selectOne(self, id):
        conn  = super().getConn()
        cursor = conn.cursor()
        cursor.execute(Sql.custselone %id)
        c = cursor.fetchone()
        cust = CustVO(c[0], c[1], c[2], c[3], c[4], c[5], c[6])
        super().close(cursor, conn)
        return cust

    def selectAll(self):
        custall = []       # 반환할 CustVO 객체 리스트
        conn = super().getConn()
        cursor = conn.cursor()
        cursor.execute(Sql.custselall)
        cs = cursor.fetchall()
        for c in cs:
            cust = CustVO(c[0], c[1], c[2], c[3], c[4], c[5], c[6])
            custall.append(cust)
        super().close(cursor, conn)
        return custall

    def insert6(self, id, pwd, name, age, height, weight):
        conn = super().getConn()
        cursor = conn.cursor()
        cursor.execute(Sql.custinsert6 %(id, pwd, name, age, height, weight))
        conn.commit()
        super().close(cursor, conn)

    def insert7(self, id, pwd, name, age, height, weight, size):
        conn = super().getConn()
        cursor = conn.cursor()
        cursor.execute(Sql.custinsert7 %(id, pwd, name, age, height, weight, size))
        conn.commit()
        super().close(cursor, conn)

    def update6(self, id, pwd, name, age, height, weight):
        conn = super().getConn()
        cursor = conn.cursor()
        cursor.execute(Sql.custupdate6 %(pwd, name, age, height, weight, id))
        conn.commit()
        super().close(cursor, conn)

    def update7(self, id, pwd, name, age, height, weight, size):
        conn = super().getConn()
        cursor = conn.cursor()
        cursor.execute(Sql.custupdate7 %(pwd, name, age, height, weight, size, id))
        conn.commit()
        super().close(cursor, conn)

    def delete(self, id):
        conn = super().getConn()
        cursor = conn.cursor()
        try:
            cursor.execute(Sql.custdelete %(id))
            conn.commit()
        except Exception as err:
            conn.rollback()
            print(err)
        finally:
            super().close(cursor, conn)



if __name__ == '__main__':
    # cust = CustDB().selectOne('id01')
    # print(cust)

    # custall = CustDB().selectAll()
    # for cust in custall:
    #     print(cust)

    # CustDB().insert('id02', 'pwd02', '김철수', 41, 171.9, 74)

    # CustDB().delete('id02')

    CustDB().update('id02', 'pwd02', '이말희', 21, 164.8, 56)
