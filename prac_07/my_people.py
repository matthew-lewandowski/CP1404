from prac_07.person import Person

MENU = """Menu
a) add person
q) quit"""


def main():
    people = []
    i = 0
    print("welcome to your person book!")
    print(MENU)
    menu_choice = check_menu_choice()
    people.append(Person("Tommy", "SuperLongLastName", 99))
    people.append(Person("Jack", "Shortername", 99))
    people.append(Person("Tom", "Short", 99))
    while menu_choice != "Q":
        first_name = input("Enter First name: ")
        last_name = input("Enter Last name: ")
        age = input("Enter age: ")
        people.append(Person(first_name, last_name, age))
        print("{}, added".format(Person.__str__(people[i])))
        i += 1
        print(MENU)
        menu_choice = check_menu_choice()
    print_people(people)


def check_menu_choice():
    choice = input("Enter your choice: ").upper()
    while choice != "A" and choice != "Q":
        print("invalid choice")
        choice = input("Enter your choice: ").upper()
    return choice


def print_people(people):
    for person in people:
        print("{:6} {:20} is {} years old".format(person.first_name, person.last_name, person.age))


main()
