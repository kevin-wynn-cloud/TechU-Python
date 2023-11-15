# Display a welcome message for the "Guess the Number" game
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# Import the 'random' module to generate a random number for the game
import random

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Initialize a variable to track whether the guess is correct
isGuessRight = False

# Start a loop to repeatedly prompt the user for guesses until they guess the correct number
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")  # Prompt the user for a guess
    if int(guess) == number:  # Check if the guess is correct
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True  # Set the flag to end the loop
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

# Display a message to count to 10 using a 'for' loop
print("Count to 10!")

# Iterate through numbers 0 to 10 (inclusive) and print each number
for x in range(0, 11):
    print(x)
