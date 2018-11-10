import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def update_task(conn, task):

    sql=''' UPDATE tasks
            SET priority = ?,
                begin_date = ?,
                end_date = ?
            WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)

def main():
    database = 'C:\\Users\\Ja\\Desktop\\pythonSql\\db\\pythonsqlite.db'

    conn = create_connection(database)
    with conn:
        update_task(conn, (2,'2015-01-04','2015-01-06',2))

if __name__=='__main__':
    main()
