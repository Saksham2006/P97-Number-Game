import random

# Taking the range

print('Welcome to the Number Guessing Game.')

lower = int(input('Enter the lowest possible number for your game:- '))
upper = int(input('Enter the highest possible number for your game:- '))

# Taking a random number from the range

n = random.randint(lower, upper)

print("\nYou will only get five chances to guess the correct number.")

# Setting the number of chances and the current number of guesses

chances = 5
count = 0

while count<chances:
    count = count+1
    guess = int(input('\nGuess a number:- '))

    if n == guess:
        print("\nCongratulations! You win!")
        break
    elif n > guess:
        print("\nYou guessed incorrectly! Your guess is too low!")
    elif n < guess:
        print("\nYou guessed incorrectly! Your guess is too high!")

if count>=chances:
    print("\nThe correct number was %d" % n)