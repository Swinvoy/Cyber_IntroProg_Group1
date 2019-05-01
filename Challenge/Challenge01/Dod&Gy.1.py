import subprocess
import time
import csv
then = time.time()

def runExe(username, pin):
    out = subprocess.check_output(["CrackMe.exe", username, str(pin)], shell=True)
    out = str(out, 'utf-8')
    out = out.strip()
    return out

usernameList = []
with open("usernames.csv",'r', encoding='utf-8-sig') as csvfile:
    reader=csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        usernameList.append(row[0])
usernamePassword = []

for usernameGuessValue in range(0,len(usernameList)-1,1):
    usernameGuess = usernameList[usernameGuessValue]
    usernameChecker = runExe(usernameGuess, 1000)
    if usernameChecker != "User not found":
        for pinGuess in range(0,999,1):
            output = runExe(usernameGuess, pinGuess)
            if output != "Incorrect Pin":
                usernamePassword.append(usernameGuess)
                usernamePassword.append(pinGuess)
                break

now = time.time()

print("Valid Username and Passwords: ", end="")
print(usernamePassword)
print("It took: ", now-then, " seconds")