# -*- coding: utf-8 -*-
# @Time    : 2019/6/7 0:37
# @Author  : GUO Huimin
# @Email   : guohuimin2619@foxmail.com
# @FileName: Create&Connect.py

# Python MySQL Tutorials from https://pynative.com/python-mysql-tutorial/

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='root',
                                         password='root1234')
    if connection.is_connected():
        db_INFO = connection.get_server_info()
        print('Connected to MySQL database... MySQL Server version on ",db_Info')
        cursor = connection.cursor()
        cursor.execute('select database();')
        record = cursor.fetchone()
        print('Your connected to - ',record)
except Error as e:
    print('Error',e)
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print('MySQL is closed')
