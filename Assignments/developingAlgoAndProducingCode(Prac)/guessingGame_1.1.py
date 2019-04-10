import random

def valueRequest(requestText):
    while True:
        try:
            return int(input(requestText))
        except ValueError:
            print("Oops! That was not a valid number. Try again...")

print("Hey There! Lets play a little guessing game!")

maxGuesses = valueRequest("How many guesses do you want to make: ")
guessLeft = maxGuesses

lowerRange = valueRequest("What is the lower value you want to guess from: ")
upperRange = valueRequest("What is the upper value you want to guess from: ")

guessMe = random.randint(lowerRange,upperRange)
lowerBound = lowerRange
upperBound = upperRange
allGuesses = []
won = False

while won == False:
    print("Guess between " + str(lowerBound) + " and " + str(upperBound))
    userGuess = valueRequest("Enter Guess: ")
    allGuesses.append(userGuess)

    if userGuess == guessMe:
        won = True

    elif userGuess < guessMe:
        guessLeft = guessLeft - 1
        print("Nope, its greater than that!")
        print("You have " + str(guessLeft) + " guesses left!")
        if userGuess >= lowerBound:
            lowerBound = userGuess

    elif userGuess > guessMe:
        guessLeft = guessLeft - 1
        print("Nope, its less than that!")
        print("You have " + str(guessLeft) + " guesses left!")
        if userGuess <= upperBound:
            upperBound = userGuess
    
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
input()