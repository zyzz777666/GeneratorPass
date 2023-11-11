import sqlite3
from sqlite3 import Error


class ConnectBD:
    @staticmethod
    def create_connection(path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection


class ExecuteQuery:
    @staticmethod
    def execute_query(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query executed successfully")

            cursor.close()
        except Error as e:
            print(f"The error '{e}' occurred")
        finally:
            if connection:
                connection.close()
                print('BD close')


sqlite_insert_with_param = f"""
  INSERT INTO passwordz (password) 
  VALUES (?);"""

