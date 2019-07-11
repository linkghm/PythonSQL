# -*- coding: utf-8 -*-
# @Time    : 2019/6/7 16:22
# @Author  : GUO Huimin
# @Email   : guohuimin2619@foxmail.com
# @FileName: SelectData.py

# Python MySQL Tutorials from https://pynative.com/python-mysql-tutorial/

import mysql.connector
from mysql.connector import Error
from datetime import datetime


# Insert data into database
# try:
#     connection = mysql.connector.connect(
#         user='root',
#         password='root1234',
#         host='localhost',
#         database='python_db',
#         use_pure=True
#     )
#     current_date = datetime.now()
#     current_date_formated = current_date.strftime('%Y-%m-%d')
#     insert_records = [
#         (1, 'kelly', current_date_formated, 7000),
#         (2, 'Bob', current_date_formated, 9000),
#         (3, 'john', current_date_formated, 6000),
#     ]
#     insert_query = """ INSERT INTO `python_developers` (`id`,`name`,`join_date`,`salary`) VALUES (%s,%s,%s,%s)"""
#     cursor = connection.cursor(prepared=True)
#     result = cursor.executemany(insert_query, insert_records)
#     connection.commit()
#     print(cursor.rowcount, 'Insert successfully')
# except Error as e:
#     connection.rollback()
#     print('Error', e)
# finally:
#     if (connection.is_connected()):
#         cursor.close()
#         connection.close()
#         print('MySQL is closed')

# Select data
# 1 Python MySQL SELECT Query example to fetch rows from MySQL table.
# try:
#     connection = mysql.connector.connect(
#         user='root',
#         password='root1234',
#         host='localhost',
#         database='python_db',
#         use_pure=True
#     )
#     select_query = "select * from python_developers"
#     cursor = connection.cursor()
#     cursor.execute(select_query)
#     records = cursor.fetchall()
#     print('Printing each row of table:')
#     for row in records:
#         print('ID = ', row[0])
#         print('Name = ', row[1])
#         print('JoinDate = ', row[2])
#         print('Salary = ', row[3])
#         print('\n')
#         cursor.close()
# except Error as e:
#     connection.rollback()
#     print('Error', e)
# finally:
#     if (connection.is_connected()):
#         connection.close()
#         print('MySQL is closed')

# 2 Use Python variables as parameters in MySQL Select Query
def getDeveloperDetails(ID):
    try:
        connection = mysql.connector.connect(
            user='root',
            password='root1234',
            host='localhost',
            database='python_db',
            use_pure=True
        )
        cursor = connection.cursor(prepared=True)
        select_query = """select * from python_developers where id=%s"""
        cursor.execute(select_query, (ID,))
        records = cursor.fetchall()

        for row in records:
            print('Id = ', row[0])
            print('Name = ', row[1])
            print('JoinDate = ', row[2])
            print('Salary = ', row[3])
            print('\n')
    except Error as e:
        print('Error', e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print('MySQL is closed')

getDeveloperDetails(1)

# 3 Select limited rows from MySQL table using fetchmany and fetchone
