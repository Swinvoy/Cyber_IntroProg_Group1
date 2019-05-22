# Write a function called 'InputNumber' that will keep asking the user to enter a value until the value is a valid number.

def inputNumber():
    noError = False
    while noError == False:
        try:
            validNumber = int(input("Insert a valid number:"))
            noError = True
            return validNumber
        except:
            print("That's not a valid number! Try again!")

print(inputNumber())