class Employee:
    company = "VISA"
    eCode = 120

class Freelancer:
    company = "Fiverr"
    level = 1
    def upgrade(self):
        self.level = self.level+1

class Programmer(Employee, Freelancer):  # If it was Freelancer, Employee then p.company would have print Fiverr
    name = "ATG"

p = Programmer()
p.upgrade()
print(p.level)
print(p.company)