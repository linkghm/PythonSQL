# -*- coding: utf-8 -*-
# @Time    : 2019/6/7 0:37
# @Author  : GUO Huimin
# @Email   : guohuimin2619@foxmail.com
# @FileName: Create&Connect.py

# Python MySQL Tutorials from https://pynative.com/python-mysql-tutorial/

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# 1 simple example
# try:
#     connection = mysql.connector.connect(host='localhost',
#                                          database='python_db',
#                                          user='root',
#                                          password='root1234')
#     if connection.is_connected():
#         db_INFO = connection.get_server_info()
#         print('Connected to MySQL database... MySQL Server version on', db_INFO)
#         cursor = connection.cursor()
#         cursor.execute('select database();')
#         record = cursor.fetchone()
#         print('Your connected to - ', record)
# except Error as e:
#     print('Error', e)
# finally:
#     if (connection.is_connected()):
#         cursor.close()
#         connection.close()
#         print('MySQL is closed')

# 2 Use the Dictionary to keep MySQL Connection arguments in Python
# connection_config_dict = {
#     'user': 'root',
#     'password': 'root1234',
#     'host': 'localhost',
#     'database': 'python_db',
#     'raise_on_warnings': True,
#     'use_pure': False,
#     'autocommit': True,
#     'pool_size': 5
# }
# try:
#     connection = mysql.connector.connect(**connection_config_dict)
#     if connection.is_connected():
#         db_INFO = connection.get_server_info()
#         print('Connected to MySQL database... MySQL Server version on', db_INFO)
#         cursor = connection.cursor()
#         cursor.execute('select database();')
#         record = cursor.fetchone()
#         print('Your connected to - ', record)
# except Error as e:
#     print('Error', e)
# finally:
#     if (connection.is_connected()):
#         cursor.close()
#         connection.close()

# 3 Change the MySQL connection timeout when connecting through Python
try:
    connection = mysql.connector.connect(user='root', password='root1234', \
                                         host='localhost',
                                         database='python_db',
                                         connection_timeout=180)
    if connection.is_connected():
        db_INFO = connection.get_server_info()
        print('Connected to the server, the version is ', db_INFO)
        cursor = connection.cursor()
        global_connection_timeout = 'SET GLOBAL connect_timeout=180'
        global_wait_timeout = 'SET GLOBAL connect_timeout=180'
        global_interactive_timeout = 'SET GLOBAL connect_timeout=180'

        cursor.execute(global_connection_timeout)
        cursor.execute(global_wait_timeout)
        cursor.execute(global_interactive_timeout)

        connection.commit()

    pass
except Error as e:
    print('Error', e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
# 4 Python Connect to MySQL Using Connector Python C Extension
# “use_pure” connection argument determines whether to connect using a pure Python interface to MySQL, or a C Extension.
connection = mysql.connector.connect(host='localhost',
                                     database='python_db',
                                     user='pynative',
                                     password='pynative@#29', use_pure=True)
