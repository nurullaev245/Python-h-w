son = 15 #int(input("Son: "))
import math
for i in range(0, son):
    for j in range(0, son):
        if i == 0 or i == son - 1 or j == 0 or j == son - 1 or (i == j or i == son - j - 1) and son/2>i :
            print("* ", end='')
        else:
            print("  ", end='')
    print()