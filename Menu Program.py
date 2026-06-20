
#dictionary key:valur pairs

menu = {"pizza": 3.00, "nachos": 4.50, "popcorn": 5.00, "fries": 1.43, "chips": 1.00, "soda": 2.00, "lemonade": 2.50}

cart = []
total = 0

print("------MENU------")
for key, value in menu.items():
    print(f"{key:8}: ${value:.2f}")

while True:
    food = input("Select item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your prize to pay is: ${total}")
print("----------------")