menu = """(H)ello
(G)oodbye
(Q)uit"""
users_name = input("Enter name: ")
menu_choice = input(print(menu)).upper()
while menu_choice != "Q":
    if menu_choice == "H":
        print("Hello {}".format(users_name))
    elif menu_choice == "G":
        print(""
              "Goodbye {}".format(users_name))
    else:
        print("Invalid choice")
    menu_choice = input(print(menu)).upper()
print("Finished.")