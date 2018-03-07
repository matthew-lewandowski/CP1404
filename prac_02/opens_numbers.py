numbers_file = open("numbers.txt", "r")
total = 0
for number in numbers_file:
    number = int(number)
    total += number
print(total)
numbers_file.close()