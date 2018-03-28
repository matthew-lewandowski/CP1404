def main():
    user_score = int(input("Enter score: "))
    calculated_score = calculate_score(user_score)
    print(calculated_score)


def calculate_score(score):
    if score > 90:
        return "you got an A"
    elif score > 80:
        return "you got a B"
    elif score > 70:
        return "you got a C"
    elif score > 60:
        return "you got a D"
    else:
        return "you Failed!"


main()
