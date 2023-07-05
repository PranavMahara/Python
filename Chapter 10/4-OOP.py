class Employee:
    company = "Google"
    def GetSalary(self):
        print(f"Salary is {self.salary} and company is {self.company}")

arjun = Employee()
arjun.salary = 23322 # Employee.GetSalary(arjun)

arjun.GetSalary()
    