# Class for storing information of programmers

class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"THe name of programmer is {self.name} and product is {self.product}")

Arjun = Programmer("ARJUN", "SKYPE")
BILLA = Programmer("Rushil", "UPSC")
Arjun.getInfo()
BILLA.getInfo()