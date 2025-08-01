import random

guess = None
numberOfGuesses = 0

print('I am thinking of a number between 1 and 20')
chosenNumber = random.randint(1, 20)
print('For debug: ' + 'the number is ' + str(chosenNumber))

while guess != chosenNumber:
    print('Take a guess.')
    guess = int(input())
    numberOfGuesses += 1
    if guess < chosenNumber:
        print('Your guess is too low')
    elif guess > chosenNumber:
        print('Your guess is too high.')
    else:
        break
if guess == chosenNumber:
    print('Good job! You guessed my number in ' + str(numberOfGuesses) + ' guesses!')
else:
    print("You did not guess the number. The number was " + str(chosenNumber))
