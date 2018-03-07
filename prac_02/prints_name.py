name = open("names_file.txt", "r")
print("Your name is {}".format(name.read()))
name.close()
