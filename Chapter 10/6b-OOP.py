class Time:
    def ti(self, time):
        print(f"Time is {time}")

Morning = Time()
Morning.ti(8)


class Timee:
    def tii(self):
        print(f"Time is {self.time}")

Morning = Timee()
Morning.time = 7
Morning.tii()

