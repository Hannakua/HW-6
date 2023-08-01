--3) Знайти середній бал у групах з певного предмета.
SELECT g.number_group, AVG(m.mark) AS average_mark, s.subject 
FROM users AS u, subjects AS s
INNER JOIN marks AS m ON u.id = m.student_name AND m.subject_ = s.id
INNER JOIN groups AS g ON g.student_name  = u.id
WHERE s.subject = 'physics'  
GROUP BY g.number_group;