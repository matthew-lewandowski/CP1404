total_items = int(input("Enter the amount of items: "))
while total_items <= 0:
    total_items = int(input("incorrect input. Enter the amount of items: "))
total_price = 0
for i in range(total_items):
    total_price = total_price+float(input("price of item: "))
if total_price > 100:
    total_price = total_price - ((total_price/100)*10)
print("Total price for {} items is ${:.2f}".format(total_items, total_price))