-- 6) Знайти список студентів у певній групі
SELECT u.name AS student, g.number_group 
from users AS u
INNER JOIN groups AS g ON g.student_name = u.id 
WHERE g.number_group = '3';