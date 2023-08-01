--2) Знайти студента із найвищим середнім балом з певного предмета.
SELECT u.name AS student, AVG(m.mark) AS average_mark, s.subject 
FROM users AS u, subjects AS s
INNER JOIN marks AS m ON u.id = m.student_name AND m.subject_ = s.id
WHERE s.subject = 'astronomy' 
GROUP BY u.id
ORDER BY average_mark DESC
LIMIT 1;