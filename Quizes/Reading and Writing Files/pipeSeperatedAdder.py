# Write a Python script that can sum all pipe ('|') separated numbers in a file called 'input.txt'. 
# input.txt:
# 1|2|3|4|55|1000|74564356|454878457515
# Console:
# Sum of all Numbers is: ‭454953022936‬

f = open("input.txt", "r")
f_contents = f.read().strip().split("|")
f.close()
adder = 0

for x in range(len(f_contents)):
    adder = adder + int(f_contents[x])
print("Sum of all Numbers is: " + str(adder))