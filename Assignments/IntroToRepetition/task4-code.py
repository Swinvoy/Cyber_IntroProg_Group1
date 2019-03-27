rightorwrong = False

while rightorwrong == False:
    answer = input("What happens when you throw a yellow rock in the red sea? ")

    if answer == "It gets wet":
        print("You got it!")
        rightorwrong = True
    else:
        print("Try again!")