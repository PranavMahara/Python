# Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said attributes.

class Student:
    student_name = 'ATG'
    marks = 93  

stu = Student()
stud = Student()
print(f"Student Name: {stu.student_name}")
print(f"Marks: {stu.marks}")

stu.student_name = "ARJUN"
stu.marks = 69

print(f"Student Name: {stu.student_name}")
print(f"Marks: {stu.marks}")

setattr(Student, 'marks', 55)
print(f"Marks: {stud.marks}")