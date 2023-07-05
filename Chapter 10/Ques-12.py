# CLASS to book train ticket

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of train is {self.name}")
        print(f"The seats available in the train are {self.seats}")

    def FareInfo(self):
        print(f"The price --> {self.fare}")
    
    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket have been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        
        else:
            print("Tatkal mein book karaye")


intercity = Train("Intercity Express", 90, 300)
intercity.getStatus()
intercity.FareInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
print("------------------------------")
intercity.getStatus()