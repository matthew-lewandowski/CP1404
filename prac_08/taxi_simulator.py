from prac_08.taxi import Taxi
from prac_08.silver_taxi_service import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0.0
    taxi_num = 0
    print("Let's drive!")
    menu_option = input(MENU).upper()
    while menu_option != "Q":
        if menu_option == "C":
            print("taxis available")
            choose_taxi(taxis)
            taxi_num = int(input("Choose taxi"))
        elif menu_option == "D":
            drive(taxis, taxi_num)
            bill += taxis[taxi_num].get_fare()
        print("Bill to date: ${:.2f}".format(bill))
        menu_option = input(MENU).upper()
    print("Total trip cost: ${:.2f}".format(bill))
    print("Your taxis are now: ")
    choose_taxi(taxis)


def choose_taxi(taxis):
    i = 0
    for taxi in taxis:
        print("{} - {}".format(i, taxi))
        i += 1


def drive(taxis, taxi_number):
    distance = int(input("Drive how far?"))
    Taxi.drive(taxis[taxi_number], distance)
    print("your {} trip cost you {:.2f}".format(taxis[taxi_number].name, taxis[taxi_number].get_fare()))


main()