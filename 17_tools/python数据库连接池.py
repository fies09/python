#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/8/10 15:14
# @Author     : fany
# @Project    : PyCharm
# @File       : python数据库连接池2.py
# @description:
import pymysql
from dbutils.pooled_db import PooledDB

# 虚拟的连接获取函数
def get_connection():
    pool = PooledDB(
        creator=pymysql,
        mincached=2,
        maxcached=10,
        host='localhost',
        user='root',
        password='fy961009',
        database='book',
        autocommit=True
    )
    return pool.connection()

# 虚拟的连接释放函数
def release_connection(connection):
    connection.close()

def execute_query(sql):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        release_connection(conn)

# 示例：查询数据库中的数据
sql = "SELECT * FROM bookinfo;"
result = execute_query(sql)
for row in result:
    print('result', row)
