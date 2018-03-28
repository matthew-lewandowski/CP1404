def main():
    username = input("Enter your name")
    while not is_not_blank(username):
        username = input("Incorrect input. Enter name: ")
    prints_name(username)


def is_not_blank(name):
    return len(name) > 0


def prints_name(name):
    for i in range(1, len(name), 2):
        print(name[i])


main()
