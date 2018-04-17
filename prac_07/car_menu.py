from prac_07.car import Car

MENU = """Menu:
d) drive
r) refuel
q) quit"""
CHOICES = "DRQ"


def main():
    menu_choice = ""
    car_name = get_car_name()
    fuel = 100
    my_car = Car(fuel, car_name)
    while menu_choice != "Q":
        print(my_car)
        print(MENU)
        menu_choice = checks_menu()
        if menu_choice == "D":
            drives_car(my_car)
        elif menu_choice == "R":
            add_fuel(my_car)
    print("Goodbye {} driver".format(car_name))


def get_car_name():
    name = input("Enter your car name: ")
    while len(name) <= 0:
        print("Your car has to have a name")
        name = input("Enter your car name: ")
    return name


def checks_menu():
    menu_choice = input("Enter your choice: ").upper()
    while menu_choice not in CHOICES:
        print("invalid choice")
        menu_choice = input("Enter your choice: ").upper()
    return menu_choice


def drives_car(my_car):
    question = "How many kilometres do you wish to drive?"
    distance = check_for_int(question)
    if distance > my_car.fuel:
        print("{} drove {} and then ran out of fuel".format(my_car.name, my_car.fuel))
    else:
        print("{} drove {}km".format(my_car.name, distance))
    Car.drive(my_car, distance)


def add_fuel(my_car):
    question = "How many units of fuel do you want to add to the car?"
    fuel = check_for_int(question)
    my_car.add_fuel(fuel)
    print("Added {} units of fuel".format(fuel))


def check_for_int(string):
    valid_input = False
    while not valid_input:
        try:
            number = int(input(string))
            valid_input = True
        except ValueError:
            print("Invalid input")
    return number


main()
