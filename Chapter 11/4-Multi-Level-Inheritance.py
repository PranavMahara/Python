class Person:
    country = "India"

    def TakeBreak(self):
        print("I am Breathing..")

class Employee:
    company = "HONDA"

    def GetSalary(self):
        print(f"Salary --> {self.salary}")

    def TakeBreak(self):
        print("EMPLOYEE hu")
    
class Programmer(Employee):
    company = "Fiverr"

    def GetSalary(self):
        print("NO SALARY :/")

p = Person()
p.TakeBreak()
e = Employee()
e.TakeBreak()
pr = Programmer()
pr.TakeBreak()
print(pr.company)