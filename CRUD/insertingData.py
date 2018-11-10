import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def create_project(conn, project):
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid

def create_task(conn, task):
    sql = """ INSERT INTO tasks(name, priority, status_id, project_id, begin_Date, end_date)
              VALUES(?,?,?,?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid


def main():
    database = 'C:\\Users\\Ja\\Desktop\\pythonSql\\db\\pythonsqlite.db'

    conn = create_connection(database)
    with conn:
        #create a new project
        project = ('Cool App with SQLite & Python', '2018-11-10', '2018-12-31')
        project_id = create_project(conn, project)

        #tasks
        task_1= ('Analyze the requirements of the app', 1, 1, project_id, '2018-11-11', '2018-11-20')
        task_2= ('Confirm with user about the top requirements' , 1, 1, project_id, '2018-11-21', '2018-11-25')

        #create tasks
        create_task(conn, task_1)
        create_task(conn, task_2)

if __name__=='__main__':
    main()
