weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds?: (K or L) : ").upper()

if unit == "K":
    weight *= 2.205
    unit = "Lb"
    print(f"Your weight equal: {round(weight, 2)} {unit}")
elif unit == "L":
    weight /= 2.205
    unit = "Kg"
    print(f"Your weight equal: {round(weight, 2)} {unit}")
else:
    print(f"Unit was not valid")