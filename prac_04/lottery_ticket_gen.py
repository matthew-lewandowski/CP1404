import random


def main():
    quick_pick = int(input("Enter amount of quick picks: "))
    for picks in range(quick_pick):
        numbers = generates_picks()
        print(" ".join(numbers))


def generates_picks():
    numbers = []
    while len(numbers) < 5:
        random_number = random.randint(0, 46)
        if random_number in numbers:
            continue
        numbers.append(random_number)
    numbers.sort()
    fake_numbers = [str(number) for number in numbers]
    return fake_numbers


main()
