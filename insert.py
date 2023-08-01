from sqlite3 import Error

from connect import create_connection, database
from faker import Faker
import random
from random import randint, sample
from datetime import date

fake = Faker()

def create_table(conn, create_table_sql, params):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql, params)
        conn.commit()
    except Error as e:
        print(e)


if __name__ == '__main__':
    sql_create_users_table = """
    INSERT INTO users (name, email) VALUES (?,?)
    """

    sql_create_groups_table = """
    INSERT INTO groups (student_name, number_group) VALUES (?,?)
    """

    sql_create_tutors_table = """
    INSERT INTO tutors (tutor_name) VALUES (?);
    """

    sql_create_subjects_table = """
    INSERT INTO subjects (subject, tutor) VALUES (?,?)
    """

    sql_create_marks_table = """
    INSERT INTO marks (student_name, subject_, mark, date_mark) VALUES (?,?,?,?)
    """

    with create_connection(database) as conn:
        if conn is not None:
            
            [create_table(conn, sql_create_users_table, params = (fake.name(), fake.email())) for _ in range(45)]

            students_number = sample(range(45), 45)
            for i in range(45):
                create_table(conn, sql_create_groups_table, params = (students_number[i], randint(1, 3)))
            
            [create_table(conn, sql_create_tutors_table, params = (fake.name(),)) for _ in range(5)]

            subjects = ['math', 'art', 'physics', 'philosophy', 'history', 'chemistry', 'economics', 'astronomy']            
            [create_table(conn, sql_create_subjects_table, params = (subjects[i], randint(1, 5))) for i in range(8)]

            for i in range(0, 45):
                [create_table(conn, sql_create_marks_table, params = (students_number[i], randint(1, 8), randint(1, 10), fake.date_between(end_date='today', start_date='-200d'))) for _ in range(20)]
           
        else:
            print("Error! cannot create the database connection.")