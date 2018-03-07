import random

password = ""
length = int(input("enter length"))
random_number = random.randint(0, length)
password = password[:random_number] + 'z' + password[random_number+1:]
print(password)
print(len(password))
