

class Animal():
    isAlive = True


class Dog(Animal):
    def speak(self):
        print("WOOF!")



class Cat(Animal):
    def speak(self):
        print("MEAW!")


class Car():

    isAlive = False
    def speak(self):
        print("HONK!")


animals = [Dog() , Cat() , Car()]

for animal in animals:
    animal.speak()