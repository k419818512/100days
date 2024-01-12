student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grade = {}

for key in student_scores:
    if student_scores[key] >= 91:
        student_grade[key] = "Outstanding"
    if student_scores[key] < 91 and student_scores[key] >= 81:
        student_grade[key] = "Exceeds Expectations"
    if student_scores[key] < 81 and student_scores[key] >= 70:
        student_grade[key] = "Acceptable"
    if student_scores[key] < 70:
        student_grade[key] = "Fail"

print(student_grade)

