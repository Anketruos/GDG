class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print('name: ', self.name)
        print('age: ', self.age)

person2 = Person('sosina', 21)
person2.introduce()