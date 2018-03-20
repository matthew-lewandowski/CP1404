def main():
    temperature = int(input("Enter temperature: "))
    what_degree = input("Enter (c) for celsius or (f) for fahrenheit").upper()
    if what_degree == "C":
        fahrenheit = convert_celsius(temperature)
        print("{} degrees celsius is {} degrees fahrenheit".format(temperature, fahrenheit))
    elif what_degree == "F":
        celsius = convert_fahrenheit(temperature)
        print("{} degrees fahrenheit is {} degrees celsius".format(temperature, celsius))


def convert_celsius(temperature):
    return (temperature * 9 / 5) + 32


def convert_fahrenheit(temperature):
    return (temperature - 32)/(9/5)


main()
