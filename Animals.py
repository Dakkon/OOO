class Animal(object):
    def __init__(self, name):
        self.name = name
    def eat(self,food):
        print('%s is eating %s.' % (self.name, food))

class Dog(Animal):
    def fetch(self, thing):
        print('%s goes after the %s!' % (self.name, thing))

    def show_affection(self):
        print('%s wags tail.' % (self.name))

class Cat(Animal):
    def swatstring(self):
        print ('%s shreds the string!' % (self.name))
    def show_affection(self):
        print('%s purrs.' % (self.name))

r = Dog('Rover')
f = Cat('Fluffy')

r.fetch('paper')
f.swatstring()
r.eat('Dog Food')
f.eat('Cat Food')

for a in (Dog('Rover'), Cat('Fluffy'), Cat('Cuddles'), Dog('Scout')):
    a.show_affection()