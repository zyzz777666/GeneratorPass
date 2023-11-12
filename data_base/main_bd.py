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


def insert_variable_into_table(password):
    global sqlite_connection
    try:
        sqlite_connection = sqlite3.connect('sm_app.sqlite')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_insert_with_param = f"""
          INSERT INTO passwordz (password) 
          VALUES (?)"""

        data_tuple = (password,)
        cursor.execute(sqlite_insert_with_param, data_tuple, )
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу passworz")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


sqlite_start = '''
CREATE TABLE IF NOT EXISTS passwordz (
password INT
)
'''
