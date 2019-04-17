import subprocess
import time
then = time.time()

def runExe(username, pin):
    out = subprocess.check_output(["CrackMe.exe", username, str(pin)], shell=True)
    out = str(out, 'utf-8')
    out = out.strip()
    return out

usernameList = ['bob@asdf.com', 'ihencke0@about.me', 'kbrimblecombe1@deviantart.com', 'apurslow2@dyndns.org', 'hmacsharry3@answers.com', 'hdomleog@taobao.com', 'rperl5@youku.com', 'svany6@apple.com', 'bhewlings7@tiny.cc', 'wgounet8@ox.ac.uk', 'gwebley4@rediff.com', 'wcruxtona@apple.com', 'vburkittb@webeden.co.uk', 'iandrejsc@wordpress.com', 'ecockshutd@oakley.com', 'jpoinsette@macromedia.com', 'ghurlestonf@nydailynews.com', 'jreyner9@wiley.com', 'kcasserlyh@jugem.jp', 'awhickmani@networksolutions.com']
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