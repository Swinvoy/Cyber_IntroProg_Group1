count = 2
pastNumber = 0
currentNumber = 1
nextNumber = 0

Print(pastNumber)
Print(CurrentNumber)

if count > 16:
    if false set Variable "NextNumber" to "PastNumber" plus "CurrentNumber"
        Print "NextNumber"
        Add 1 to "Count"
        Set "PastNumber" to "CurrentNumber" Value
        Set "CurrentNumber" to "NextNumber" Value
        Go back to line 14
    if true 
        Stop program