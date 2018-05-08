from prac_08.taxi import Taxi
from prac_08.silver_taxi_service import SilverServiceTaxi


def main():
    # taxis = []
    # taxis.append(Taxi("Prius 1", 100))
    # print(taxis[0])
    # taxis[0].drive(40)
    # print(taxis[0])
    # print(taxis[0].get_fare())
    # taxis[0].start_fare()
    # taxis[0].drive(100)
    # print(taxis[0])
    # print(taxis[0].get_fare())

    hummer = SilverServiceTaxi("hummer", 200, 2)
    hummer.start_fare()
    hummer.drive(18)
    hummer.get_fare()
    print(hummer)
    print(hummer.get_fare())




main()
