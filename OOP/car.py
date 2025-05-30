
class Car:

    carCount = 0
    def __init__(self , model , year , color , forSale):
        self.model = model
        self.year = year
        self.color = color
        self.forSale = forSale
        Car.carCount+=1

    def drive(self):
        print("you drive the car...")
    
    def stop(self):
        print("you stop the car...")

    def describe(self):
        print(f"details of car : \n model {self.model} \n year : {self.year}\n Color : {self.color}\n Total Cars : {Car.carCount} \n")

        