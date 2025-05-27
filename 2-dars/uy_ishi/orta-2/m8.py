rows = 4
cols = 5

for i in range(rows):
    for j in range(cols):
        if (i + j) % 2 == 0:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()  