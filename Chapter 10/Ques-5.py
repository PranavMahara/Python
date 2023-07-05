# Write a Python program to crate two empty classes, Student and Marks. Now create some instances and check whether they are instances of the said classes or not. 
# Also, check whether the said classes are subclasses of the built-in object class or not.

class Student:
    pass

class Marks:
    pass

stu = Student()
mar = Marks()

print(isinstance(stu, Student))
print(isinstance(mar, Student))
print(isinstance(stu, Marks))
print(isinstance(mar, Marks))

print("--------------------")
print(issubclass(Student, object))
print(issubclass(Marks, object))