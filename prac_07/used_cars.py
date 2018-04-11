"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_07.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    limo = Car(100)
    my_car.drive(30)
    print("car fuel =", my_car.fuel)
    print("car odo =", my_car.odometer)
    print("limo fuel =", limo.fuel)
    print("limo odo =", limo.odometer)

    Car.add_fuel(my_car, 20)
    Car.drive(my_car, 115)

    print("Limo {}, {}".format(limo.fuel, limo.odometer))
    print("Limo {self.fuel}, {self.odometer}".format(self=limo))
    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))
    print(Car.__str__(my_car))

main()