string = input("Enter a string: ")
word_to_count = {}
string = string.split()
string.sort()
longest_word = max(string)
for word in string:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

# for key, value in word_to_count.items():
#    print("{} : {}".format(key, value))    #works, not always ordered

i = 0
for string[i], value in word_to_count.items():  # always ordered
    print("{:{}} : {}".format(string[i], len(longest_word) + 2, value))
    i += 1
