--8) Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT t.tutor_name, s.subject, AVG(m.mark)
FROM subjects AS s 
INNER JOIN marks AS m ON m.subject_= s.id
INNER JOIN tutors AS t ON t.id = s.tutor 
WHERE t.tutor_name = "Danielle Garner" 
GROUP BY s.subject;