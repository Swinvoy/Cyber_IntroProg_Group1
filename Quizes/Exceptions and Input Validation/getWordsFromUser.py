# Write a function called 'GetWordsFromUser' that takes a Min and Max as a parameter. 
# The function then takes an input from the user and ensures that the input has at least or at most the specified amount of words. 
# Keep on asking the user until the amount of words is within range, the function then returns all words as lower case in a list.

def getWordsFromUser(minPara,maxPara):
    noError = False
    while noError == False:
        try:
            minPara = int(minPara)
            maxPara = int(maxPara)
            userInput = str(input("Enter an input: ")).lower()
            userStringTemp = userInput.split()
            userStringTempLength = len(userStringTemp)
            if userStringTempLength >= minPara or userStringTempLength <= maxPara:
                raise InterruptedError
            print(userStringTemp)
            noError = True
        except ValueError:
            print("Your parameters are not a number!")
            noError = True
        except InterruptedError:
            print("Please input a string between " + str(minPara) + " to " + str(maxPara) + " words.")

getWordsFromUser(2,5)