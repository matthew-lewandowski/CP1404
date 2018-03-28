COLOURS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
           "aquamarine1": "	#7fffd4", "bisque2": "	#eed5b7"}

color = input("Enter a colour: ")
while color != "":
    if color in COLOURS:
        print(color, "is", COLOURS[color])
    else:
        print("Invalid colour name")
    color = input("Enter a colour: ").upper()
