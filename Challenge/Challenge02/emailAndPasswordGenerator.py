namesAndAges = open("people.txt","r")
emailsAndPasswords = open("userpass.txt","w")
fileLines = sum(1 for line in open('people.txt'))
count = 0

while count < fileLines:
    workingline = namesAndAges.readline().strip().split("|")
    try:
        x = 0
        while x < 3: 
            tester = workingline[x].lower()
            x = x + 1
        tester = int(workingline[2])
        if tester >= 100:
            raise ValueError("Too Old!")
        validDetails = True
    except:
        validDetails = False  
    if validDetails == True:
        firstName = workingline[0].lower()
        secondName = workingline[1].lower()
        year = str(2019 - int(workingline[2]))
        emailsAndPasswords.write(firstName[0]+secondName+"@Huawow.io|"+firstName+secondName[0].upper()+"_"+year)
        if count != (fileLines-1):
            emailsAndPasswords.write("\n")
    count = count + 1