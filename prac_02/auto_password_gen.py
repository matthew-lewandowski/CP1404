SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
LOWER = "zxcvbnmasdfghjklqwertyuiop"
UPPER = LOWER.upper()
NUMBERS = "123456789"
import random


def main():
    """Program to get and check a user's password."""
    print("Please enter the requirements")
    length = int(input("Enter a length"))
    upper = input("Uppercase? (y)(n): ").upper()
    lower = input("Lowercase? (y)(n): ").upper()
    numeric = input("Numbers? (y)(n): ").upper()
    special_characters = input("Special characters? (y)(n): ").upper()
    password = ""
    create_password(upper, lower, numeric, special_characters, length)
    while not is_password_valid(password, upper, lower, numeric, special_characters):
        password = create_password(upper, lower, numeric, special_characters, length)
    print("your {} character password is '{}'".format(length, password))


def create_password(upper, lower, numeric, special_characters, length):
    password = ""
    while len(password) < length:
        if upper == "Y":
            random_number = random.randint(0, length)
            password = password[:random_number] + random.choice(UPPER) + password[random_number + 1:]
        if lower == "Y":
            random_number = random.randint(0, length)
            password = password[:random_number] + random.choice(LOWER) + password[random_number + 1:]
        if numeric == "Y":
            random_number = random.randint(0, length)
            password = password[:random_number] + random.choice(NUMBERS) + password[random_number + 1:]
        if special_characters == "Y":
            random_number = random.randint(0, length)
            password = password[:random_number] + random.choice(SPECIAL_CHARACTERS) + password[random_number + 1:]
    return password


def is_password_valid(password, upper, lower, numeric, special_characters):
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for character in password:
        if character.isupper():
            count_upper += 1
        elif character.islower():
            count_lower += 1
        elif character.isdigit():
            count_digit += 1
        elif character in SPECIAL_CHARACTERS:
            count_special += 1
    if upper == "Y":
        if count_upper == 0:
            return False
    if lower == "Y":
        if count_lower == 0:
            return False
    if numeric == "Y":
        if count_digit == 0:
            return False
    if special_characters == "Y":
        if count_special == 0:
            return False
    return True


main()
