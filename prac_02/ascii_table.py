LOWER = 33
UPPER = 127


def main():
    user_character = str(input("Enter a character: "))
    while len(user_character) != 1:
        user_character = str(input("Invalid entry. Enter a character: "))
    character_convert = ord(user_character)
    print("The ASCII code for {} is {}".format(user_character, character_convert))
    user_number = int(input("Enter a number between {} and {}".format(LOWER, UPPER)))
    while user_number > UPPER or user_number < LOWER:
        user_number = int(input("Invalid entry. Enter a number between {} and {}: ".format(LOWER, UPPER)))
    number_convert = chr(user_number)
    print("The character for {} is {}".format(user_number, number_convert))
    number_of_columns = int(input("Enter number of columns"))
    for number in range(LOWER, UPPER + 1):
        ascii_col = ("{:3} {:<2}  ".format(number, chr(number)))
        print(ascii_col * number_of_columns)


main()
