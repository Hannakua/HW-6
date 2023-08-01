--10) писок курсів, які певному студенту читає певний викладач.
SELECT u.name AS student, s.subject, t.tutor_name
FROM users AS u, subjects AS s 
INNER JOIN marks AS m ON m.subject_= s.id AND u.id = m.student_name
INNER JOIN tutors AS t ON t.id = s.tutor
WHERE  u.name = 'Jessica Johnson' AND t.tutor_name = 'Danielle Garner'
GROUP BY s.subject;