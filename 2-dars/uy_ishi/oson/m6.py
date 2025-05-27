N = int(input("N ni kiriting: "))

yigindi = 0
for son in range(1, N + 1):
    if son % 2 == 0:
        yigindi += son

print("Juft sonlar yig'indisi:", yigindi)
