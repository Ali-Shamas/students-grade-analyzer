def display_student_summary():
    student_number = int(input("Enter the number of students: "))
    students = []   
    attempt = 1
    while attempt <= student_number:
        name = input("Enter the name of student : ")
        grade = float(input("Enter the grade of student , out of 100 " + name + ": "))
        students.append((name, grade))
        attempt += 1
    for student in students:
        print("Name:" + student[0]  +  " , Grade: " + str(student[1])) 
        
    return students 
def get_avg_grade(students):
    total = 0
    for student in students:
        total += student[1]
    return total / len(students)

def get_heighest_grade(students):
    highest = students[0]
    for student in students:
        if student[1] > highest[1]:
            highest = student
    return highest
def count_passed(students):
    count = 0
    for student in students:
        if student[1] >= 50:
            count += 1
    return count

students = display_student_summary()
average = get_avg_grade(students)
highest = get_heighest_grade(students)
passed_count = count_passed(students)
print("Average Grade for this class :", average)
print("Highest Grade in this class  :", highest[0], "with", highest[1])
print("Number of Students Who Passed:", passed_count)