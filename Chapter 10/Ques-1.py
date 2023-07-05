# Write a Python program to create an instance of a specified class and display the namespace of the said instance.

class Student:
    def __init__(self, name, age):
        print("The name of student is", name)
        print("The age of student is", age)

student = Student("Arjun", 19)

