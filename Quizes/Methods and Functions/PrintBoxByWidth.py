def PrintBoxByWidth(height,width):
    for y in range (0, height):
        for x in range (0, width):
            if y == 0 or y == (height - 1) or x == 0 or x == (width - 1):
                print("x", end='')
            elif y == ((height-1)/2):
                print("o", end='') 
            else:
                print(" ", end='')
        print("")

PrintBoxByWidth(11,100)