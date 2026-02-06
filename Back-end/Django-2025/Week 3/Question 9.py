class Vehicle():
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def info(self):
        pass
    
class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def info(self):
        print('this car\'s brand is ', self.brand, 'and year is ', self.year, 'it has a model ', self.model)

c = Car('toyota', 2020, 'corola')
c.info()