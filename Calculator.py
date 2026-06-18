import math

operator = input("Enter the operator (+,-,*,/) : ")
first_number = float(input("Enter first number: "))
second_number = float(input("Enter first number: "))

if operator == "+":
    result = first_number + second_number
    print(round(result, 3))
elif operator == "-":
    result = first_number - second_number
    print(round(result, 3))
elif operator == "*":
    result = first_number * second_number
    print(round(result, 3))
elif operator == "/":
    result = first_number / second_number
    print(round(result, 3))
else:
    print(f"{operator} is not valid operator")