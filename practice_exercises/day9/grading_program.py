student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

def get_grade(student_score):
    if student_score >= 91 and student_score <= 100:
        print("Outstanding")
    elif student_score >= 81 and student_score <= 90:
        print("Exceeds Expectations")
    elif student_score >= 71 and student_score <= 80:
        print("Acceptable")
    elif student_score <= 70:
        print("Fail")

# loop through each student
for student in student_scores:
    print(student)
    individual_score = student_scores[student]
    print(get_grade(individual_score))

# add student name : corresponding grade value
    

# 🚨 Don't change the code below 👇
# print(student_grades)