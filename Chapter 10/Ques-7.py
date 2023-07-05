# Write a Python class named Student with two attributes student_id, student_name. 
# Add a new attribute student_class and display the entire attribute and their values of the said class. 
# Now remove the student_name attribute and display the entire attribute with values.

class Students:
    Student_ID = "21BBS0110"
    Student_Name = "ARJUN"

    def newAttr(self, attr):
        setattr(self, attr, attr)


Stud = Students()
print(f"Student ID --> {Stud.Student_ID} and Student Name --> {Stud.Student_Name}")

setattr(Students, "Student_Class", 12)
print(f"Student ID --> {Stud.Student_ID}, Student Name --> {Stud.Student_Name} and Student Class --> {Stud.Class}")