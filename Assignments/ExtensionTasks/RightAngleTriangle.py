def rightAngleTriangle(base):
    for y in range(base-1,-1,-1):
        for x in range(y+1):
            print('x', end='')
        print("")

rightAngleTriangle(int(input("How big do you want your triangle? ")))