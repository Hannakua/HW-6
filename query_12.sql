--12) Оцінки студентів у певній групі з певного предмета на останньому занятті.
SELECT u.id , u.name, g.number_group, m.mark, MAX(m.date_mark), s.subject  
from users AS u, subjects AS s  
INNER JOIN groups AS g ON g.student_name = u.id 
INNER JOIN marks AS m ON m.student_name = u.id AND s.id = m.subject_ 
WHERE g.number_group = '3' AND s.subject = "astronomy";  
