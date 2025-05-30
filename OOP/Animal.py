

class Animal:
    def __init__(self , name):
        self.name = name
        isAlive = True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")



class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat (Animal):
    def speak(self):
        print("MEOW")


        
