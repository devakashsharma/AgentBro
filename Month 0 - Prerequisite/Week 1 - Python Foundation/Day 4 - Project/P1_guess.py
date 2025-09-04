"""
It is a guessing project, where an user will start game,
once the game is start, then user will have to guess the number.
if distance is too far, computer will say too far and if close
then it's close...
"""

"""
Guess Me
"""

# Import libraries
import random

# Generates a random integer between 1 and 100 (inclusive)
number = random.randint(1, 100)
user_guess = 0  # Initialize user_guess to enter the while loop

while user_guess != number:
    try:
        user_guess = int(input("Enter a Number between 1 and 100: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue  # Skip the rest of the loop and ask for input again

    if user_guess < number:
        if number - user_guess > 10:
            print("Your guess is too low (and far away).")
        else:
            print("Your guess is low, but you're getting close!")
    elif user_guess > number:
        if user_guess - number > 10:
            print("Your guess is too high (and far away).")
        else:
            print("Your guess is high, but you're getting close!")

print(f"Congratulations! The number was {number}. You guessed it right!")
