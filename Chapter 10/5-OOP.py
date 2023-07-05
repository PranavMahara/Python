class Employee:
    company = "Google"

    def greet(self):
        print("GM, sir")
        
    @staticmethod  # No need for self now
    def gree():
        print("GoP, sir")


arjun = Employee()
arjun.greet()
arjun.gree()

    