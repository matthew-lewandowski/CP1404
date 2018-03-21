def main():
    numbers = []
    for number in range(5):
        numbers.append(int(input("Number: ")))
    prints_numbers(numbers)


def prints_numbers(numbers):
    print("the first number is {}".format(numbers[0]))
    print("the last number is {}".format(numbers[4]))
    print("the smallest number is {}".format(min(numbers)))
    print("the largest number is {}".format(max(numbers)))
    print("the average of the numbers is {}".format(sum(numbers) / 5))


main()
