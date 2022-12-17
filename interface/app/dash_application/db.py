import sqlite3
from sqlite3 import Error
import os

database =  os.getcwd() +r"/data/marketplaces.db"

def create_connection():
    """ Create a database connection to the SQLite crdatabase
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(database=database)
        print("connexion")
        return conn
    except Error as e:
        print(e)

    return conn

def get_freight_data():
    conn = create_connection()
    if conn != None :
        cur = conn.cursor()
        target = cur.execute('''SELECT freight_value FROM Items''').fetchall()
        features = cur.execute('''SELECT price, product_weight_g, product_length_cm, product_height_cm, product_width_cm FROM Items NATURAL JOIN Products ''').fetchall()    
        print('requête ok')
        conn.close()
    return target, features

