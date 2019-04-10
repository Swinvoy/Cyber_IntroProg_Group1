import random

def valueRequest(requestText):
    while True:
        try:
            return int(input(requestText))
        except ValueError:
            print("Oops! That was not a valid number. Try again...")

print("Hey There! Lets play a little guessing game!")
print("Guess the number between 0 and 25")

maxGuesses = valueRequest("How many guesses do you want to make: ")
guessLeft = maxGuesses
guessMe = random.randint(0,25)
allGuesses = []
won = False

while won == False:
    userGuess = valueRequest("Enter Guess: ")
    allGuesses.append(userGuess)

    if userGuess == guessMe:
        won = True
    elif userGuess < guessMe:
        guessLeft = guessLeft - 1
        print("Nope, its greater than that!")
        print("You have " + str(guessLeft) + " guesses left!")
    else:
        guessLeft = guessLeft - 1
        print("Nope, its less than that!")
        print("You have " + str(guessLeft) + " guesses left!")
    
    if guessLeft < 1:
        break
    else:
        exit

if won == True:
    print("Damn you win!")
    print("The number was indeed " + str(userGuess))
    print("You guessed it in " + str(len(allGuesses)) + " guesses!")
else:
    print("AHAHAHA YOU LOOSE!")
    print("The number was " + str(guessMe) + " you fool!")

print("Your guess log:")
print(allGuesses)