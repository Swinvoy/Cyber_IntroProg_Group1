userNameStored = "John"
passwordStored = "1234"

userNameRequest = input("USERNAME: ")
passwordRequest = input("PASSWORD: ")

if ((userNameStored == userNameRequest) and (passwordStored == passwordRequest)):
    print("Login Successful")
else:
    print("Login Unseccessful")