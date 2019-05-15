# Write the function between the START and END tags
# START

def SortWordsAlphabetically(hyphenSeperatedString):
    hyphenList = (hyphenSeperatedString.lower()).split("-")
    hyphenList.sort()
    hyphenSeperatedStringAlpha = '-'.join(hyphenList)
    return(hyphenSeperatedStringAlpha)

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(SortWordsAlphabetically("Bob-does-not-like-frank") == 'bob-does-frank-like-not'))
print("Test 2 Passed: " + str(SortWordsAlphabetically("why-am-i-doing-this-this-is-terrible") == "am-doing-i-is-terrible-this-this-why"))
print("Test 3 Passed: " + str(SortWordsAlphabetically("frank-kill-zoe-did") == "did-frank-kill-zoe"))