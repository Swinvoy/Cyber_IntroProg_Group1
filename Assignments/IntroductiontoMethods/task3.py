def helloUser(userName):
    if userName == ("Alice"):
        print("Hello " + userName)
    elif userName == "Bob":
        print("Hello " + userName)
    else:
        print("No chance buddy!")

helloUser(input("What is your name? "))
