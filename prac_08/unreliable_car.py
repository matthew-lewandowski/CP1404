""""
cp1404 practrical
unreliable car class"""

from prac_08.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability=0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = randint(0, 101)
        if random_number > self.reliability:
            distance_driven = super().drive(0)
        else:
            distance_driven = super().drive(distance)
        return distance_driven
