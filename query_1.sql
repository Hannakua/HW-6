--1) Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT  u.id, u.name AS student, AVG(m.mark) AS average_mark
FROM users AS u
INNER JOIN marks AS m ON u.id = m.student_name
GROUP BY u.id
ORDER BY average_mark DESC
LIMIT 5;