# import os
# import sqlite3
# from sqlite3 import Error
# from sqlite3 import Connection


# def create_connection(db_file):    
#     """ create a database connection to the SQLite database
#         specified by db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#         print("connexion établie")
#         return conn
#     except Error as e:
#         print(e)

#     return conn

# #the name of the database
# db_name : str = 'marketplaces.db'      
# database = r"../db_name"

# # create a database connection
# conn  = create_connection(database)
 
# # create tables
# if conn != None :
#     with open('orders_sqlite.sql') as f:
#         conn.executescript(f.read())
#         cur = conn.cursor()



# # if conn is not None:
# #     cur.execute('''PRAGMA foreign_keys = ON;''')
# #     # create exchange table
# #     cur.execute(sql_create_exchange_table)         
# #     # create company table
# #     cur.execute(sql_create_company_table)             
# #     # create security table
# #     cur.execute(sql_create_security_table)            
# #     # create security_price table
# #     cur.execute(sql_create_security_price_table) 


# if conn != None :
#     conn.close()

import sqlite3

with open('orders.sql', 'r') as sql_file:
    sql_script = sql_file.read()

db = sqlite3.connect('database.db')
cursor = db.cursor()
cursor.executescript(sql_script)
db.commit()
db.close()