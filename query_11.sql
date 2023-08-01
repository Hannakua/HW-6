--11 Середній бал, який певний викладач ставить певному студентові.
SELECT t.tutor_name, s.subject, AVG(m.mark), u.name 
FROM subjects AS s , users AS u 
INNER JOIN marks AS m ON m.subject_= s.id AND m.student_name = u.id
INNER JOIN tutors AS t ON t.id = s.tutor
WHERE t.tutor_name = "Danielle Garner" AND u.name = 'Denise Hernandez'  
GROUP BY s.subject;