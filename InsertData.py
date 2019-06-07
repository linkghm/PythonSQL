# -*- coding: utf-8 -*-
# @Time    : 2019/6/7 11:34
# @Author  : GUO Huimin
# @Email   : guohuimin2619@foxmail.com
# @FileName: InsertData.py

# Python MySQL Tutorials from https://pynative.com/python-mysql-tutorial/

# First, you should create MySQL table, named python_user
# Learn about INSERT INTO and key-value

import mysql.connector
from mysql.connector import Error
from datetime import datetime


# 1 Python example to insert a single row/record into MySQL table
# try:
#     connection = mysql.connector.connect(
#         user='root',
#         password='root1234',
#         host='localhost',
#         database='python_db'
#     )
#     # warning: differences between ` and '
#     sql_insert_query = """ INSERT INTO `python_user` (`id`,`name`,`birth_date`,`age`) VALUES (1,'Scott','2019-06-07',26)"""
#     cursor = connection.cursor()
#     result = cursor.execute(sql_insert_query)
#     connection.commit()
#     print('Record inserted successfully into python_user table')
# except Error as e:
#     connection.rollback()
#     print('Error', e)
# finally:
#     if (connection.is_connected()):
#         cursor.close()
#         connection.close()
#         print('MySQL is closed')

# 2 Using Python variables in a MySQL INSERT query
def insertPythonVaribleInTable(UserID, UserName, JoinDate, age):
    try:
        connection = mysql.connector.connect(
            user='root',
            password='root1234',
            host='localhost',
            database='python_db'
        )
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO `python_user` \
        (`id`,`name`,`birth_date`,`age`) VALUES (%s,%s,%s,%s)"""
        insert_tuple = (UserID, UserName, JoinDate, age)
        result = cursor.execute(sql_insert_query, insert_tuple)
        connection.commit()
        print('Record inserted successfully into python_user table')
    except Error as e:
        connection.rollback()
        print('Error', e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print('Connection is closed')


insertPythonVaribleInTable(2, 'GHM', '2019-06-07', 22)
insertPythonVaribleInTable(3, 'GY', '2019-06-07', 22)
