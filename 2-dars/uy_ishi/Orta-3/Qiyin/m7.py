n = int(input("Kvadrat tomonini kiriting: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or i <= j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
