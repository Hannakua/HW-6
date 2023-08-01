--7) Знайти оцінки студентів в окремій групі з певного предмета.
SELECT u.name, g.number_group, m.mark, m.date_mark  
from users AS u, subjects AS s
INNER JOIN groups AS g ON g.student_name = u.id 
INNER JOIN marks AS m ON m.student_name = u.id
WHERE g.number_group = '3' AND s.subject = "physics" 
ORDER BY m.date_mark;