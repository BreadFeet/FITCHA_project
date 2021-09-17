# MariaDB Connection Setting
import os, json
import pymysql
from django.core.exceptions import ImproperlyConfigured
from config.settings import BASE_DIR

secret_file = os.path.join(BASE_DIR, 'secret.json')   # secrets.json 파일 위치를 명시

with open(secret_file) as f:
    secrets = json.loads(f.read())     # python object로 바꿈

# 비밀번호를 가져오기 위한 함수
def get_secret(setting, secrets=secrets):
    """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
    try:
        print("확인:", secrets[setting])
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


# Python Anywhere 계정 연결
# config = {
#     'database': 'dsportfolio2$sizedb',
#     'user': 'dsportfolio2',
#     'password': get_secret("PA_PASSWORD"),
#     'host': 'dsportfolio2.mysql.pythonanywhere-services.com',
#     'port': 3306,
#     'charset': 'utf8',
#     'use_unicode': True
# }

# 로컬 계정 연결
config = {
    'database': 'sizedb',
    'user': 'root',
    'password': get_secret("LOCAL_PASSWORD"),
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