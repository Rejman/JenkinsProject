import sqlite3
from sqlite3 import Error
path = 'pythonsqlite.db'
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__=='__main__':
    create_connection(path)
