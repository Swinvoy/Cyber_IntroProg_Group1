# Write a function called 'GetElementAt' that takes a list and index as a parameter and returns the element at the index, or None if the index is out of bounds. 
# You can not use an if statement in your function (use a try except instead).

# eg: GetElementAt([1,2,3,4,5,6,7], 4) -> 5

# eg: GetElementAt([1, 2, 3], 3) -> None

# iAmList = [1,2,3]
# iAmIndex = 3

# try:
#     print(iAmList[iAmIndex])
# except:
#     print("None")

def getElementAt(iAmList,iAmIndex):
    try:
        return(iAmList[iAmIndex])
    except IndexError:
        print("None")
    except:
        print("Double check your inputs are right")

print(getElementAt([1,2,3,4],3))