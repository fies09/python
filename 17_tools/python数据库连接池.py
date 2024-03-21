#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/8/10 14:28
# @Author     : fany
# @Project    : PyCharm
# @File       : python数据库连接池.py
# @description:
'''
数据库连接池：
在Python中，可以通过第三方库来实现数据库连接池功能，常见的库包括pymysql、psycopg2、pyodbc等。这些库提供了连接池的功能，
可以在多线程或多进程环境下管理数据库连接，从而提高数据库访问性能。
步骤:
1. 导入DBUtils相关模块：在Python代码中导入DBUtils相关模块，通常需要导入PooledDB和对应数据库的连接模块（如pymysql、psycopg2等）。
2. 创建数据库连接池：使用PooledDB类来创建数据库连接池，配置连接参数和连接池大小等。
3. 从连接池获取连接：通过连接池的connection()方法来获取数据库连接。
4. 使用连接执行数据库操作：使用获取的连接执行数据库操作，然后将连接释放回连接池。
'''
import pymysql
# 持久化连接,连接在使用后不被立即关闭
from dbutils.persistent_db import PersistentDB
# 管理连接池，支持连接的重用、超时、限制最大连接数等功能，以及在高并发情况下能够更好地管理连接
from dbutils.pooled_db import PooledDB
from config import db_params

# 创建数据库连接池
db_pool = PersistentDB(pymysql, 10,  **db_params)

# 从连接池获取连接
def get_connection():
    return db_pool.connection()

# 释放连接回连接池
def release_connection(conn):
    conn.close()

# 执行SQL查询
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
print(result)

'''
在上面的示例中，我们使用DBUtils.PooledDB的PooledDB类来创建了一个数据库连接池，并使用pymysql作为数据库API。通过get_connection()函数从连接池中获取连接，执行数据库查询，
然后通过release_connection()函数释放连接回连接池。
需要注意的是，DBUtils库提供了连接池的管理功能，避免了频繁创建和销毁数据库连接，从而提高数据库访问性能。同时，连接池还可以设置最大连接数、连接的回收和复用等参数，以满足实际应用的需求。
'''