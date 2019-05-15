# Write the function between the START and END tags
# START

def IsPalindrome(entryString):
    testString = (entryString.lower()).replace(" ", "")
    testStringLength = len(testString)
    testStringLengthHalf = testStringLength/2
    palindromeChecker = False
    frontLetter = ""
    backLetter = ""
    for i in range(0, int(testStringLengthHalf)):
        frontLetter = testString[i]
        backLetter = testString[(testStringLength-1-i)]
        if frontLetter == backLetter:
            palindromeChecker = True
        else:
            palindromeChecker = False
            break
    return palindromeChecker

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(IsPalindrome("GlenElg") == True))
print("Test 2 Passed: " + str(IsPalindrome("Nurses Run") == True))
print("Test 3 Passed: " + str(IsPalindrome("Nurses") == False))
print("Test 4 Passed: " + str(IsPalindrome("frank") == False))