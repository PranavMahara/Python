# Changing class methods

class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    # def changeSalary(self, sal):     # Method - 1
    #     self.__class__.salary = sal
 
    @classmethod                       # Method - 2
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)
