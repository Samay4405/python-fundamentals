# Python number guessing game

import random

lowest_number = 1
highest_number = 100

answer=random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

print("Python number guessing game")
print(f"Select a number between {lowest_number} and {highest_number}")

while is_running:
    user_guess = (input("Enter your guess: "))
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
        guesses += 1
        
        if user_guess < lowest_number or user_guess > highest_number:
            print("Number out of range.")
        elif user_guess < answer:
            print("Too low. Try again.")
        elif user_guess > answer:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {answer} in {guesses} guesses.")
            is_running = False
        
    else:
        print("Invalid input.")
        print(f"Please select a number between {lowest_number} and {highest_number}")
        
       
    