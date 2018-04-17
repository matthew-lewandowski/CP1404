from prac_07.guitar import Guitar


def main():
    guitars = []
    print("My Guitars!")
    name = input("Name: ")
    guitar_number = 0
    while len(name) > 0:
        year = get_year()
        cost = get_cost()
        guitars.append(Guitar(name, year, cost))
        print("{} added.".format(Guitar.__str__(guitars[guitar_number])))
        guitar_number += 1
        name = input("Name: ")
    print_guitars(guitars)


def get_cost():
    valid_input = False
    while not valid_input:
        try:
            cost = float(input("Cost: "))
            valid_input = True
        except ValueError:
            print("Invalid cost")
    return cost


def get_year():
    valid_input = False
    while not valid_input:
        try:
            year = int(input("Year: "))
            valid_input = True
        except ValueError:
            print("invalid year")
    return year


def print_guitars(guitars):
    i = 1
    for guitar in guitars:
        print("Guitar {}: {:>15} ({}), worth ${:10,.2f} {}".format(i, guitar.name, guitar.year, guitar.cost,
                                                                   guitar.vintage_string()))
        i += 1

main()