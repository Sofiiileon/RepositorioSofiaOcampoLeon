student_scores = {
    'Harry':88,
    'Ron':78,
    'Hermione':95,
    'Draco':75,
    'Neville':60
}
student_grades = {}
for estudiante in student_scores:
    nota = student_scores[estudiante]
    if nota >= 91 and nota <=100:
        student_grades[estudiante] = 'Outstanding'
    elif nota >= 81 and nota <=90:
        student_grades[estudiante] = 'Exceeds Expectations'
    elif nota >= 71 and nota <= 80:
        student_grades[estudiante] = 'Acceptable'
    else:
        student_grades[estudiante] = 'Fail'
        print('Diccionario final de calificaciones:')
        print(student_grades)
