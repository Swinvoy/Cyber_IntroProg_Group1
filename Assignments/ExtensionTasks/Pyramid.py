def pyramid(base):
    for y in range(0,base+1,2):
        space = int((((base)-y)/2))
        for z in range(space,0,-1):
            print(' ', end='')
        for x in range(y+1):
            print('x', end='')
        print("")

pyramid(int(input("How big do you want your triangles base? ")))