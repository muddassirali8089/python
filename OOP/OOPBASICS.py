


from Animal2 import Animal
from Animal2 import Flyer
from Animal2 import Mammal
from Animal2 import Bat




cow = Mammal("Cow")
cow.eat()
cow.walk()
cow.fly() ❌ This will give error — correct, because cow cannot fly

bat = Bat("Bat")
bat.eat()       # from Animal
bat.walk()      # from Mammal
bat.fly()       # from Flyer
bat.special_ability()



# car1 = Car("bmw" , 2023 , "black" , False)

# car1.describe()

# dog = Dog("tony")

# dog.speak()

# cat = Cat("cat")
# cat.speak()



