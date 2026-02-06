class Car():
    def __init__(self, make):
        self.make = make

    def get_make(self):
        print(self.make)

c1 = Car('ethiopia')
c1.get_make()