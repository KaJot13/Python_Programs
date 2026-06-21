import random

lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

print("Number Guessing Game")
print(f"Select number between {lowest_number} and {highest_number}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_number or guess > highest_number:
            print("That number is out of range")
            print(f"Please select a number between {lowest_number} and {highest_number}")
        elif guess < answer:
            print("To low! Try Again!")
        elif guess > answer:
            print("To high! Try Again")
        else:
            print(f"Well Done! The Answer Was: {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
            
    else:
        print("Invalid Guess")
        print(f"Please select a number between {lowest_number} and {highest_number}")

