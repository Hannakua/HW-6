import sqlite3
from contextlib import contextmanager

database = './study.db'


@contextmanager
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        yield conn
        conn.commit()
    except Exception as err:
        print(err)
        conn.rollback()
    finally:
        conn.close()