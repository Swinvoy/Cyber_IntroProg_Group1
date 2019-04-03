userWords = input("Let me tell you how many words you wrote: ").split()
userWordsNumber = len(userWords)
print(userWords[0])
if userWordsNumber >= 3:
    print(userWords[2])
else:
    print("No third word")
if userWordsNumber >=3:
    for x in range(1,len(userWords)-1,1): 
        print(userWords[x], end=" ")
else:
    print("Use more words!")