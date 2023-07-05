# PascalCase
# EmployeeName     First word and aage vale are Capital

# camelCase
# isNumeric, isFloat  First word is small

class RailwayForm:
    formType = "Railway"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

Arjun = RailwayForm()    # Arjun is now an object 
Arjun.name = "arjun"
Arjun.train = "LOL"
Arjun.printData()
print(Arjun.formType)