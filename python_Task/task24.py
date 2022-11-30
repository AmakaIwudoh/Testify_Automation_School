# Python Abstract Class and Interface

import abc

class Vehicle(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def drive_direction(self):
        pass

class Car(Vehicle):
    def drive_direction(self):
         return "Car: " + "Drive forward"

class Plane(Vehicle):
    def drive_direction(self):
        return "Plane: " + "Drive Upward"

car = Car()
print(car.drive_direction())


plane = Plane()
print(plane.drive_direction())