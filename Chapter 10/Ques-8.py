# Write a Python class named Student with two attributes student_id, student_name. 
# Add a new attribute student_class. Create a function to display the entire attribute and their values in Student class.

class Student:
    Student_ID = '21BBS0110'
    Student_Name = 'Arjun MAL'
    
    def display(self):
        print(f'Student id: {self.Student_ID}\nStudent Name: {self.Student_Name}')

arjun = Student()
print("Original attributes and their values of the Student class:")
arjun.display()