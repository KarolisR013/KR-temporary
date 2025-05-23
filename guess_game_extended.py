# This will be a simple number guessing game
# The user will have to guess a number between 1 and 10
# if the user guessed number is incorrect, the program will tell the user if the number is too high or too low


# Problems:
# Does not handle invalid input (e.g. letters, special characters)
# Does not handle the case when the user enters a number outside the range of 1-10
# The user should be able to guess the number multiple times
# Solution:
# 1. Use a while loop to allow multiple guesses
# 2. Use try/except to handle invalid input
# 3. Check if the number is within the range of 1-10


print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 10.")

import random

parsed_guess = 0
# Initialize parsed_guess to 0 to avoid UnboundLocalError
number_to_guess = random.randint(1, 10)

while parsed_guess != number_to_guess:
    user_input = input("Please enter your guess: ")

    print("You guessed: " + user_input)
#print(f"You guessed: {user_input}")

    try:
        parsed_guess = int(user_input)
    except Exception:
        print("Invalid input. Please enter a number between 1 and 10.")
        exit()

    if parsed_guess < number_to_guess:
        print("Your guess is too low.") 

    if parsed_guess < 1 or parsed_guess > 10:
        print("Please enter a number between 1 and 10.")
    
    elif parsed_guess > number_to_guess:
        print("Your guess is too high.")
    else:   
        print("Congratulations! You guessed the number!")

print("The number was: " + str(number_to_guess))
# print(f"The number was: {number_to_guess}")



