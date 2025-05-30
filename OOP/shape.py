

class Shape():
    def __init__(self , color , isFilled):
        self.color = color
        self.isFilled = isFilled

    def describe(self):
        print(f"the shape has {self.color} color and it is  {"filled" if self.isFilled == True else "not filled"}")


class Circle(Shape):
    def __init__(self , color , isFilled , radius):
        super().__init__(color,isFilled)
        self.radius = radius
        

    def describe(self):
        super().describe()
        print(f"Area of circle is {3.14 * (self.radius * self.radius)}")


class Square(Shape):
    def __init__(self , color , isFilled , width):
        super().__init__(color , isFilled)
        self.width = width
       

    def describe(self):
        super().describe()
        print(f"Area of a square is {self.width * self.width} cm^2")


class Triangle(Shape):
    def __init__(self , color , isFilled , width , height):
        super().__init__(color , isFilled)
        self.width = width
        self.height = height
        

    def describe(self):
        super().describe()
        print(f"Area of a square is {(self.width * self.height) / 2} cm^2")





circle = Circle("Red", False, 10)
circle.describe()
square = Square("Blue", False, 5)
square.describe()
triangle = Triangle("Green", True, 3, 4)
triangle.describe()
