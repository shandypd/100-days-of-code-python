student_scores = {"Harry": 81, "Ron": 78, "Hermione": 99, "Draco": 74, "Neville": 62}

student_grades = {}

for name in student_scores:
    score = student_scores[name]

    grade = "Fail"
    if score > 90:
        grade = "Outstanding"
    elif score > 80:
        grade = "Exceeds Expectations"
    elif score > 70:
        grade = "Acceptable"

    student_grades[name] = grade

print(student_grades)
