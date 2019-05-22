# Write a function called 'GetIpAddress' that will keep asking the user to enter an IP Address until it is valid. The function will then return the IP address as a string.


# 255.255.255.255

def getIpAddress():
    noError = False
    while noError == False:
        try:
            ipAddress = input("What IP Address do you want to check: ")
            ipAddressList = ipAddress.split(".")
            if len(ipAddressList) != 4:
                raise ValueError
            for x in range (0,4):
                y = int(ipAddressList[x])
                if y > 265 or y < 0:
                    raise ValueError
            if ipAddressList[0] == "0":
                raise ValueError
            noError = True
            print("That is a valid IP Address!")
            return ipAddress
        except:
            print("That is not an IP Address!")

print(getIpAddress())