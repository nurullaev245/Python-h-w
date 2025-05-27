a = int(input())
b = int(input())

sana = 0
for i in range(b - 1, a, -1):
    if i % 2 == 1:
        print(i, end=', ')
        sana = sana + 1
        if sana == 3:
            break
