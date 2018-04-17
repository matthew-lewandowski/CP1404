YEAR = 2018


class Guitar:
    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:.2f} {}".format(self.name, self.year, self.cost, self.vintage_string())

    def get_age(self):
        age = YEAR - self.year
        return age

    def is_vintage(self):
        if self.get_age() > 50:
            return True
        else:
            return False

    def vintage_string(self):
        if self.is_vintage():
            return "(Vintage)"
        else:
            return ""
