N = int(input("N ni kiriting: "))
M = int(input("M ni kiriting: "))
K = int(input("Nechta juft son kerak: "))

yigindi = 0
sana = 0

for son in range(N, M + 1):
    if son % 2 == 0:
        yigindi += son
        sana += 1
        if sana == K:
            break

print("Yig'indi:", yigindi)
