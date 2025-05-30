
from abc import ABC , abstractmethod

class Shape :
    @abstractmethod
    def area(self):
        pass
        

class Circle(Shape):

    def __init__(self , radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius **2


class Square(Shape):
      def __init__(self , side): 
          self.side = side
         
      
      def area(self):
        return self.side ** 2

class Triangle(Shape):
      
      def __init__(self , base , height):
          self.base = base
          self.height = height

      def area(self):
        return self.base * self.height * 0.5



class Pizza (Circle):
    def __init__(self, toping , radius):
        super().__init__(radius)
        self.toping = toping
        


shapes = [Circle(4) , Square(10) , Triangle(10,89) , Pizza("abcd" , 15)]


for shape in shapes:
    print(f"{shape.area()} cm^2")