# Animal base class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


# Mammal class (inherits from Animal)
class Mammal(Animal):
    def walk(self):
        print(f"{self.name} is walking")


# Flyer class (does NOT inherit from Animal)
# This is a mixin class that only adds flying ability
class Flyer:
    def fly(self):
        print(f"{self.name} is flying")


# Bat is a Mammal that can also fly
class Bat(Mammal, Flyer):
    def special_ability(self):
        print(f"{self.name} is a mammal and can fly")
