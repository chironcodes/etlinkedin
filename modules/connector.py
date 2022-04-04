# _author_ = ["Diego Alves", "Adilton Costa Anna"]
# _license_ = "Beerware"
# _version_ = "0.0.1"
"""
    Class to connect to SQLite database
    Through this class :class:`InterfaceDB`, we can make the connection
    with the database SQLite, query data and insert data.
    To use the :class:`InterfaceDB`, the implementation occurs as follows:
    .. autoattribute:: builder
    :annotation:
    Example of the constructor method
    ----------------------------
    >>> object = InterfaceDB(host, database)
    Method to connect to the database
    ----------------------------
    >>> object.get_conn(self)
    Method to close the connection in the database
    ----------------------------
    >>> object.close_conn(self, conn, curso)
    Method to create a table
    ----------------------------
    >>> object.create_table(self, create_table_sql)
    Method to insert record in table
    ----------------------------
    >>> object.insert_into(self, table: str, **kwargs)
    xxxxx
    ----------------------------
    >>> object.get_id_by_any_from_any(self, table: str, **kwargs)
    xxxxx
    ----------------------------
    >>> object.get_id_by_any_from_any(self, table: str, **kwargs)
    """

import sqlite3
from sqlite3 import Error
import pandas as pd  


class InterfaceDB():

    def __init__(self, database):
        try:
            self.database = database
            print(database)
        except Exception as e:
            print(str(e))

    def get_conn(self):
        try:
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()
            return conn, cursor
        except Exception as e:
            print(str(e))

    def close_conn(self, conn, cursor):
        try:
            cursor.close()
            conn.commit()
            conn.close()
        except Exception as e:
            print(str(e))

    def create_table(self, create_table_sql):
        try:
            conn, cursor = self.get_conn()
            cursor.execute(create_table_sql)
            self.close_conn(conn, cursor)
        except Error as e:
            print(e)

    def insert_into(self, table: str, **kwargs):
        try:
            conn, cursor = self.get_conn()
            columns = ""
            values = ""
            count = 1
            for kwkey, kwvalue in kwargs.items():
                count += 1
                columns += "{0}, ".format(kwkey)
                if isinstance(kwvalue, int):
                    values += "{0}, ".format(kwvalue)
                else:
                    values += "'{0}', ".format(kwvalue.replace("'"," "))

            columns = columns[:-2]
            values = values[:-2]

            query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
            print(query)
            cursor.execute(query)
            inserted_id = cursor.lastrowid
            self.close_conn(conn, cursor)
            return inserted_id
        except Exception as e:
            print(str(e))

    def get_id_by_any_from_any(self, table: str, **kwargs):
        try:
            conn, cursor = self.get_conn()
            if isinstance(kwargs.get("value"), int):
                query = "SELECT {} FROM {} WHERE {}={}" \
                    .format(kwargs.get("by"), table, kwargs.get("condition"), kwargs.get("value"))
            else:
                query = "SELECT {} FROM {} WHERE {}='{}'" \
                    .format(kwargs.get("by"), table, kwargs.get("condition"), kwargs.get("value"))
            print(query)
            self.close_conn(conn, cursor)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))

    def dump_tables(self, tables:list):
        try:
            conn, cursor = self.get_conn()
            for table in tables:
                df = pd.read_sql_query(f"SELECT * FROM {table}",conn)
                df.to_csv(f'{table}.csv', index=False)
            self.close_conn(conn, cursor)
        except Exception as e:
            print(str(e))
