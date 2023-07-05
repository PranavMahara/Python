# Class to find square and cube root

class Cal:
    def __init__(self, num):
        self.number = num
    
    def square(self):
        print(f"The value of {self.number} square is {self.number**2}")

    def sqroot(self):
        print(f"The value of {self.number} square is {self.number**0.5}")

    def cube(self):
        print(f"The value of {self.number} square is {self.number**3}")

a = Cal(3)
a.square()
a.sqroot()
a.cube()