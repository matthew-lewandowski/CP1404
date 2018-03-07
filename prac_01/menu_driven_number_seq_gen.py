menu = """
1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares from x to y
4. Exit the program"""
menu_choice = int(input(print(menu)))
x = int(input("Enter x: "))
y = int(input("Enter y: "))
while menu_choice != 4:
    if menu_choice == 1:
        for i in range(x, y + 1):
            if i % 2 == 0:
                print(i, end=' ')
    elif menu_choice == 2:
        for i in range(x, y + 1):
            if i % 2 == 1:
                print(i, end=' ')
    elif menu_choice == 3:
        for i in range(x, y):
            a = i * i
            if a >= y+1:
                break
            print(a)
    menu_choice = int(input(print(menu)))
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
