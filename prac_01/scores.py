score = float(input("Enter score: "))
while score < 0 or score > 100:
    score = float(input("invalid score. Enter score: "))
if score >= 90:
    print("Excellent!")
elif score >= 50:
    print("Passable!")
else:
    print("Bad!")
