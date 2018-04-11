class ProgrammingLanguage:
    def __init__(self, language='', typing='', reflection='', year=0):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{},{} typing, reflection={}, First appeared in {}".format(self.language, self.typing, self.reflection,
                                                                          self.year)

    def is_dynamic(self):
        if self.reflection:
            return True
        else:
            return False
