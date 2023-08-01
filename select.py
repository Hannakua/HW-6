import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('study.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    

# 1) Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
sql1 = """
SELECT  u.id, u.name AS student, AVG(m.mark) AS average_mark
FROM users AS u
INNER JOIN marks AS m ON u.id = m.student_name
GROUP BY u.id
ORDER BY average_mark DESC
LIMIT 5;
"""

# 2) Знайти студента із найвищим середнім балом з певного предмета.
sql2 = """
SELECT u.name AS student, AVG(m.mark) AS average_mark, s.subject 
FROM users AS u, subjects AS s
INNER JOIN marks AS m ON u.id = m.student_name AND m.subject_ = s.id
WHERE s.subject = 'astronomy' 
GROUP BY u.id
ORDER BY average_mark DESC
LIMIT 1;
"""


# 3) Знайти середній бал у групах з певного предмета.
sql3 = """
SELECT g.number_group, AVG(m.mark) AS average_mark, s.subject 
FROM users AS u, subjects AS s
INNER JOIN marks AS m ON u.id = m.student_name AND m.subject_ = s.id
INNER JOIN groups AS g ON g.student_name  = u.id
WHERE s.subject = 'physics'  
GROUP BY g.number_group
""" 


# 4) Знайти середній бал на потоці (по всій таблиці оцінок).
sql4 = """
SELECT AVG(mark) AS average_mark
FROM marks;
""" 

# 5) Знайти, які курси читає певний викладач.
sql5 = """
SELECT t.tutor_name, s.subject 
FROM subjects AS s 
INNER JOIN tutors AS t ON t.id  = s.tutor
WHERE t.tutor_name  = "Eric Wilson";
""" 

# 6) Знайти список студентів у певній групі
sql6 = """
SELECT u.name AS student, g.number_group 
from users AS u
INNER JOIN groups AS g ON g.student_name = u.id 
WHERE g.number_group = '3';
""" 

# 7) Знайти оцінки студентів в окремій групі з певного предмета.
sql7 = """
SELECT u.name, g.number_group, m.mark, m.date_mark  
from users AS u, subjects AS s
INNER JOIN groups AS g ON g.student_name = u.id 
INNER JOIN marks AS m ON m.student_name = u.id
WHERE g.number_group = '3' AND s.subject = "physics" 
ORDER BY m.date_mark;
""" 

# 8) Знайти середній бал, який ставить певний викладач зі своїх предметів.
sql8 = """
SELECT t.tutor_name, s.subject, AVG(m.mark)
FROM subjects AS s 
INNER JOIN marks AS m ON m.subject_= s.id
INNER JOIN tutors AS t ON t.id = s.tutor 
WHERE t.tutor_name = "Danielle Garner" 
GROUP BY s.subject;
""" 

#9 Знайти список курсів, які відвідує студент.
sql9 = """
SELECT u.name AS student, s.subject 
FROM marks AS m
INNER JOIN subjects AS s ON m.subject_= s.id   
INNER JOIN users AS u ON u.id = m.student_name
WHERE  u.name = 'Jaclyn Long' 
GROUP BY s.subject;
""" 

#10 Список курсів, які певному студенту читає певний викладач.
sql10 = """
SELECT u.name AS student, s.subject, t.tutor_name
FROM users AS u, subjects AS s 
INNER JOIN marks AS m ON m.subject_= s.id AND u.id = m.student_name
INNER JOIN tutors AS t ON t.id = s.tutor
WHERE  u.name = 'Jessica Johnson' AND t.tutor_name = 'Danielle Garner'
GROUP BY s.subject;
""" 

#11 Середній бал, який певний викладач ставить певному студентові.
sql11 = """
SELECT t.tutor_name, s.subject, AVG(m.mark), u.name 
FROM subjects AS s , users AS u 
INNER JOIN marks AS m ON m.subject_= s.id AND m.student_name = u.id
INNER JOIN tutors AS t ON t.id = s.tutor
WHERE t.tutor_name = "Danielle Garner" AND u.name = 'Denise Hernandez';
"""


#12 Оцінки студентів у певній групі з певного предмета на останньому занятті.
sql12 = """
SELECT u.id , u.name, g.number_group, m.mark, MAX(m.date_mark), s.subject  
from users AS u, subjects AS s  
INNER JOIN groups AS g ON g.student_name = u.id 
INNER JOIN marks AS m ON m.student_name = u.id AND s.id = m.subject_ 
WHERE g.number_group = '1' AND s.subject = "art"  
ORDER BY m.date_mark;
"""

print('------ 1| Знайти 5 студентів із найбільшим середнім балом з усіх предметів:')
print(execute_query(sql1))
print('------ 2|  Знайти студента із найвищим середнім балом з певного предмета:')
print(execute_query(sql2))
print('------ 3| Знайти середній бал у групах з певного предмета:')
print(execute_query(sql3))
print('------ 4| Знайти середній бал на потоці (по всій таблиці оцінок):')
print(execute_query(sql4))
print('------ 5| Знайти, які курси читає певний викладач:')
print(execute_query(sql5))
print('------ 6| Знайти список студентів у певній групі:')
print(execute_query(sql6))
print("------ 7| Знайти оцінки студентів в окремій групі з певного предмета:")
print(execute_query(sql7))
print("------ 8| Знайти середній бал, який ставить певний викладач зі своїх предметів:")
print(execute_query(sql8))
print("------ 9| Знайти список курсів, які відвідує студенt:")
print(execute_query(sql9))
print("------ 10| Список курсів, які певному студенту читає певний викладач:")
print(execute_query(sql10))
print('------ 11| Середній бал, який певний викладач ставить певному студентові')
print(execute_query(sql11))
print('------ 12| Оцінки студентів у певній групі з певного предмета на останньому занятті:')
print(execute_query(sql12))
