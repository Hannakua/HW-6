--5) Знайти, які курси читає певний викладач.
SELECT t.tutor_name, s.subject 
FROM subjects AS s 
INNER JOIN tutors AS t ON t.id  = s.tutor
WHERE t.tutor_name  = "Eric Wilson";