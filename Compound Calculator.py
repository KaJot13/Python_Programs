
principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter principle amount: "))
    if principle <= 0:
        print(f"Principle cant be less or equal to zero - and your principle equals: {principle}")

while rate <= 0:
    rate = float(input("Enter interest rate: "))
    if rate <= 0 :
        print(f"Interest rate cant be less or equal to zero - and your rate equals: {rate}")

while time <= 0:
    time = float(input("Enter time in years: "))
    if time <= 0 :
        print(f"Time cant be less or equal to zero - and your rate equals: {time}")

total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} years/s: ${total:.3f}")