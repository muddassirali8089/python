
from abc import ABC , abstractmethod

class vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass



class Car(vehicle):

    def start(self):
        print("you start the car..")

    def stop(self):
        print("you stop the car..")



car = Car()

car.start()
car.stop()

    
