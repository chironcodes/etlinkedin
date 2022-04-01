import sqlite3
from sqlite3 import Error


class interface_db:
    
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
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            conn, cursor = self.get_conn()
            cursor.execute(create_table_sql)
            self.close_conn(conn, cursor)
        except Error as e:
            print(e)
            
            
            
            
            
            
    #░▄▀▀░░▒█▀▄░░░█▒█░░░█▀▄░░▒█▀░█▒█░█▄░█░▄▀▀░▀█▀░█░▄▀▄░█▄░█░▄▀▀
    #░▀▄▄░▄░█▀▄░▄░▀▄█░▄▒█▄▀▒░░█▀░▀▄█░█▒▀█░▀▄▄░▒█▒░█░▀▄▀░█▒▀█▒▄██

    
    def insertInto(self, table:str, **kwargs):
        try:
            conn, cursor = self.get_conn()
            columns=""
            values=""
            count =1
            for kwkey, kwvalue in kwargs.items():
                count+=1
                columns+="{0}, ".format(kwkey)
                if isinstance(kwvalue, int):
                    values += "{0}, ".format(kwvalue)
                else:
                    values += "'{0}', ".format(kwvalue)

            columns = columns[:-2]
            values = values[:-2]

            query = "INSERT INTO {} ({}) VALUES ({})".format(table,columns,values)
            print(query)
            cursor.execute(query)
            self.close_conn(conn,cursor)
        except Exception as e:
            print(str(e))
    
    def get_id_by_any_from_any(self, table:str, **kwargs):
        # usage sample
        # get_id_by_any_from_any("actor", by="actor_id", condition="actor_url", value="http://www.profile/url")
        try:
            conn, cursor = self.get_conn()
            if isinstance(kwargs.get("value"), int):    
                query = "SELECT {} FROM {} WHERE {}={}" \
                .format(kwargs.get("by"), table,kwargs.get("condition"),kwargs.get("value"))
            else:
                query = "SELECT {} FROM {} WHERE {}='{}'" \
                .format(kwargs.get("by"), table,kwargs.get("condition"),kwargs.get("value"))
            print(query)
            self.close_conn(conn,cursor)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
        
        