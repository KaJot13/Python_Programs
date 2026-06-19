import  time

my_time = int(input("Enter number of seconds to countdown: "))

#for x in reversed(range(0, my_time + 1)):
for x in range(my_time, 0, -1):
    second = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{second:02}")

print("Times up")