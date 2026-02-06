class Animal():
    def make_sound(self):
        print('animal makes sound')

class Cat(Animal):
    def make_sound(self):
        print('meow')

c = Cat()
c.make_sound()