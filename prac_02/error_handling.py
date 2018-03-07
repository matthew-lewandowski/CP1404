"""error handling for entering in one letter, and then one number"""

LOWER = 33
UPPER = 127
user_character = str(input("Enter a character: "))
while not user_character.isalpha() or len(user_character) != 1:
    user_character = str(input("Invalid entry. Enter a character: "))
character_convert = ord(user_character)
print("The ASCII code for {} is {}".format(user_character, character_convert))
user_number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
while user_number > UPPER or user_number < LOWER:
    user_number = int(input("Invalid entry. Enter a number between {} and {}: ".format(LOWER, UPPER)))
number_convert = chr(user_number)
print("The character for {} is {}".format(user_number, number_convert))
