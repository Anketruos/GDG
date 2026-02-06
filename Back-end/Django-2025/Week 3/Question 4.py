class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(self.width * self.height)

r1 = Rectangle(10, 20)
r1.area()