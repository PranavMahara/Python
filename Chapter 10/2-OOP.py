class Employee:
    company = "Google"

Arjun = Employee()
Malhotra = Employee()

print("Before changing --> ", Arjun.company)
# Arjun.company = "GULEGULE" # Changing Object Attributes
Employee.company = "FB" # Changing Class Attributes  --> changes happen to all objects**
print("After changing --> ", Arjun.company)
