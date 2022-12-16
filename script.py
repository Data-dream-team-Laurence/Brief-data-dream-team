import sqlite3
import pandas as pd
from sqlite3 import Error

def create_connection(db_file):    
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("connexion établie")
        return conn
    except Error as e:
        print(e)

    return conn

customers_table = pd.read_csv(r'data/olist_customers_dataset.csv')
geolocation_table = pd.read_csv(r'data/olist_geolocation_dataset.csv')
items_table = pd.read_csv(r'data/olist_order_items_dataset.csv')
payments_table = pd.read_csv(r'data/olist_order_payments_dataset.csv')
reviews_table = pd.read_csv(r'data/olist_order_reviews_dataset.csv')
orders_table = pd.read_csv(r'data/olist_orders_dataset.csv')
products_table = pd.read_csv(r'data/olist_products_dataset.csv')
sellers_table = pd.read_csv(r'data/olist_sellers_dataset.csv')

#Create tables with sql file
with open('orders.sql', 'r') as sql_file:
    sql_script = sql_file.read()

#Insert csv values in tables
conn = sqlite3.connect('data/marketplaces.db')
cur = conn.cursor()
cur.executescript(sql_script)
customers_table.to_sql("Customers", conn, if_exists="append", index=False)
geolocation_table.to_sql("Geolocations", conn, if_exists="append", index=False)
items_table.to_sql("Items", conn, if_exists="append", index=False)
payments_table.to_sql("Payments", conn, if_exists="append", index=False)
reviews_table.to_sql("Reviews", conn, if_exists="append", index=False)

orders_table.to_sql("Orders", conn, if_exists="append", index=False)
products_table.to_sql("Products", conn, if_exists="append", index=False)
sellers_table.to_sql("Sellers", conn, if_exists="append", index=False)
conn.commit()
conn.close()
