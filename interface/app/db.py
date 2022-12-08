import sqlite3
from sqlite3 import Error


database = r"..\Ressources\Sources_data.db"
#test
def create_connection():
    """ Create a database connection to the SQLite crdatabase
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(database=database)
        return conn
    except Error as e:
        print(e)

    return conn

