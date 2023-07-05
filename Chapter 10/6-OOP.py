class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

arjun = Employee()
arjun.salary = 100000
arjun.getSalary("Thanks!") # Employee.getSalary(harry)
arjun.greet() # Employee.greet()
arjun.time()

