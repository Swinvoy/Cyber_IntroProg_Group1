# Write a Python Script that can output the following drawing, using only the provided `.write` methods to append to the text file named 'drawing.txt'.

# Expected output:

# *-------------------------------------*-------------------------------------*
# |                                     |                                     |
# |                                     |                                     |
# |                                     |                                     |
# |                                     |                                     |
# |                                     |                                     |
# |                                     |                                     |
# *-------------------------------------*-------------------------------------*
# Only 1 of each of these write methods are allowed:

# write("\n")
# write("-")
# write("*")
# write(" ")
# write("|")
# #Extension only writes:
# write("\\")
# write("/")
# Upload your python script once completed.

 

# Extension:

# 1. Can you make the boxes change width and height?

# 2. Allow the user to enter some text to be placed into each side of the box without changing the fundamental shape.

# 3. Replace the corners with slashes instead of stars. Example below:

# /-------------------------------------*-------------------------------------\
# |                                     |                                     |
# |                                     |                                     |
# |                                     |                                     |
# |                                     |                                     |
# |                                     |                                     |
# |                                     |                                     |
# \-------------------------------------*-------------------------------------/


def PrintBoxByWidth(height,width):
    yTotal = height - 1
    xTotal = width - 1
    for y in range (0, height):
        for x in range (0, width):
            if (y == 0 and x == 0) or (y == 0 and x == (xTotal/2)) or (y == 0 and x == xTotal) or (y == yTotal and x == 0) or (y == yTotal and x == (xTotal/2)) or (y == yTotal and x == xTotal):
                print("*", end='')
            elif x == 0 or x == (xTotal/2) or x == xTotal:
                print("|", end='')
            elif y == 0 or y == (height - 1):
                print("-", end='')
            else:
                print(" ", end='')
        print("")

PrintBoxByWidth(8,77)