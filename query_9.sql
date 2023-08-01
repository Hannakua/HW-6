--9) Знайти список курсів, які відвідує студент.
SELECT u.name AS student, s.subject 
FROM marks AS m
INNER JOIN subjects AS s ON m.subject_= s.id   
INNER JOIN users AS u ON u.id = m.student_name
WHERE  u.name = 'Jaclyn Long' 
GROUP BY s.subject;