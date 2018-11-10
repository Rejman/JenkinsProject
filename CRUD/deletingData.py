import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def delete_task(conn, id):

    sql='DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))

def delete_all_tasks(conn):

    sql='DELETE FROM tasks'
    cur=conn.cursor()
    cur.execute(sql)

def main():
    database = 'C:\\Users\\Ja\\Desktop\\pythonSql\\db\\pythonsqlite.db'

    conn = create_connection(database)
    with conn:
        #delete_task(conn, 2)
        delete_all_tasks(conn)

if __name__=='__main__':
    main()
