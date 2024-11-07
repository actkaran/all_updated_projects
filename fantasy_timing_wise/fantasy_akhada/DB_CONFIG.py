import os

import pymysql
DB_USER = 'root'
DB_PASS = 'actowiz'
# DB_HOST = '172.27.132.79'
DB_HOST = 'localhost'
DB_NAME = 'fantasy'
MATCH = 'matches'
CONTEST = 'contest'

con = pymysql.connect(user=DB_USER, host=DB_HOST, password=DB_PASS, database=DB_NAME)
ovh_con = pymysql.connect(
        user='root',
        password='actowiz',
        database= DB_NAME,
        host='148.113.1.104'
    )

if not os.path.exists("logs"):
    os.makedirs("logs")