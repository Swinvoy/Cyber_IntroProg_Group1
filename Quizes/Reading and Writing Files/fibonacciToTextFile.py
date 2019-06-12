# Write a Python script that can write the first 30 Fibonacci numbers on individual lines to a file called 'Fibonacci.txt'.
count = 1
f = open("Fibonacci.txt", "w")
f_contents = "1"
f.write(f_contents)
f.close()
f = open("Fibonacci.txt", "a")
a = 1
b = 1
c = 0
while count < 30:
    c = a + b
    f_contents = "\n" + str(b)
    f.write(f_contents)
    a = b
    b = c
    count += 1
f.close()