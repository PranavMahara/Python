class Greet:
    def __init__(self, tim):
        if(tim==1):
            print("HELLO GM")

        elif(tim==2):
            print("HELLO GA")

        elif(tim==3):
            print("HELLO GN")

a = int(input("Enter number (1, 2, 3) --> "))
Arjun = Greet(a)

