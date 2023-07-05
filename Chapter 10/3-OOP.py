class Employee:
    company = "Google"
    address = 11     # --> Class Attribute

Arjun = Employee()
Malhotra = Employee()

Arjun.salary = 122  # --> Instance Attribute
print(Arjun.salary)
Arjun.address = 12
print(Arjun.address)
