from prac_07.date import Date
ADD = 12000

def main():
    date = Date(19, 4, 1993)
    expected = Date(25, 2, 2026)
    print(date)
    date.add_days(ADD)
    print("i added {} days".format(ADD))
    print("i got {}".format(date))
    print("i expected {}".format(expected))


main()
