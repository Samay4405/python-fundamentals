import random

low = 1
high = 100

number = random.randint(low, high)

guess = int(input(f"Guess a number between {low} and {high}: "))
while guess != number:
    if guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input(f"Guess a number between {low} and {high}: "))

print("Congratulations! You guessed the correct number.")