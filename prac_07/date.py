DAYS31 = [1, 3, 5, 7, 8, 10, 12]
DAYS30 = [4, 6, 9, 11]
DAY28 = [2]


class Date:

    def __init__(self, day=0, month=00, year=0):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "the date is {},{},{}".format(self.day, self.month, self.year)

    def add_days(self, amount):
        while amount + self.day >= 28:
            if self.month in DAYS31:
                if self.month == 12:
                    self.year += 1
                    self.month = 1
                else:
                    self.month += 1
                amount -= 31
            elif self.month in DAYS30:
                if self.month == 12:
                    self.year += 1
                    self.month = 1
                else:
                    self.month += 1
                amount -= 30
            elif self.month in DAY28 and self.year % 4 == 0:
                if self.month == 12:
                    self.year += 1
                    self.month = 1
                else:
                    self.month += 1
                amount -= 29
            elif self.month in DAY28:
                if self.month == 12:
                    self.year += 1
                    self.month = 1
                else:
                    self.month += 1
                amount -= 28
        self.day += amount
