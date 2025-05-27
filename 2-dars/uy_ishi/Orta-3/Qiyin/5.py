a = input()

v1 = 0
v2 = 0
i = 0
while i < len(a):
    if a[i] == ',' and v1 == 0:
        v1 = i
    elif a[i] == ',' and v1 != 0:
        v2 = i
    i += 1

n = ""
i = 0
while i < v1:
    n += a[i]
    i += 1

m = ""
i = v1 + 1
while i < len(a):
    m += a[i]
    i += 1

raqamlar = ["0","1","2","3","4","5","6","7","8","9"]

N = 0
for c in n:
    i = 0
    while i < len(raqamlar):
        if raqamlar[i] == c:
            N = N * 10 + i
            break
        i += 1

M = 0
for c in m:
    i = 0
    while i < len(raqamlar):
        if raqamlar[i] == c:
            M = M * 10 + i
            break
        i += 1

if N > M:
    b = M
    e = N
else:
    b = N
    e = M

yig = 0
i = b
while i <= e:
    if i > 1:
        d = 2
        tub = 1
        while d * d <= i:
            if i % d == 0:
                tub = 0
                break
            d += 1
        if tub == 1:
            yig += i
    i += 1

print(yig)
