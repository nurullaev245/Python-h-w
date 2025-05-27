son = int(input())
for i in range(1, son + 1):
    yigindi = 0
    for j in range(1, i + 1):
        print(j, end="")
        yigindi += j
        if j != i:
            print("+", end="")
    print("=", yigindi)
