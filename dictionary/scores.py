student_scores = {
    "Harry" : 75,
    "Ram" : 60,
    "Ankit": 90,
    "Akib" : 80,
    "Anup" :95,
}
student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else :
        student_grades[student] = "Fail"

print(student_grades)