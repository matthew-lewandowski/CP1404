"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
WILDCARDS_01 = "67890()_+{}[]:;'/|?/"
WILDCARDS_02 = "12345!@#$%^&*<>,."
random_word_number = random.randint(0, 35)
word_format = ""
word = ""
count = 0
for letter in range(1, random_word_number):
    random_number = random.randint(0, 3)
    if random_number == 0:
        word_format += random.choice(VOWELS)
    if random_number == 1:
        word_format += random.choice(CONSONANTS)
    if random_number == 2:
        word_format += random.choice(WILDCARDS_01)
    if random_number == 3:
        word_format += random.choice(WILDCARDS_02)
for kind in word_format:
    if kind in WILDCARDS_01:
        word += random.choice(CONSONANTS)
    elif kind in WILDCARDS_02:
        word += random.choice(VOWELS)
    else:
        word += word_format[count]
    count += 1
print(word_format)
print(word)
