from prac_07.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
made_up_language = ProgrammingLanguage("Made up Language", "Static", False, 1902)
languages = [ruby, python, visual_basic, made_up_language]

for language in languages:
    if ProgrammingLanguage.is_dynamic(language):
        print("{} is Dynamic".format(language.language))
