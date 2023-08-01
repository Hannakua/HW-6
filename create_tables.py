from sqlite3 import Error

from connect import create_connection, database


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


if __name__ == '__main__':
    sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     name VARCHAR(128),
     email VARCHAR(128)
    );
    """

    sql_create_groups_table = """
    CREATE TABLE IF NOT EXISTS groups (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     student_name integer,
     number_group integer,
     FOREIGN KEY (student_name) REFERENCES users (id)
    );
    """

    sql_create_tutors_table = """
    CREATE TABLE IF NOT EXISTS tutors (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     tutor_name VARCHAR(128)    
    );
    """

    sql_create_subjects_table = """
    CREATE TABLE IF NOT EXISTS subjects (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     subject VARCHAR(128),
     tutor integer,
     FOREIGN KEY (tutor) REFERENCES tutors (id)
    );
    """

    sql_create_marks_table = """
    CREATE TABLE IF NOT EXISTS marks (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     student_name integer,
     subject_ integer,
     mark integer,
     date_mark date,
     FOREIGN KEY (student_name) REFERENCES users (id),
     FOREIGN KEY (subject_) REFERENCES subjects (id)
    );
    """

    with create_connection(database) as conn:
        if conn is not None:
            create_table(conn, sql_create_users_table)
            create_table(conn, sql_create_groups_table)
            create_table(conn, sql_create_subjects_table)
            create_table(conn, sql_create_tutors_table)
            create_table(conn, sql_create_marks_table)
        else:
            print("Error! cannot create the database connection.")