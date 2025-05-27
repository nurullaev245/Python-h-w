
yigindi = 0
for son in range(1, 501):
    if son % 2 == 1:
        yigindi = yigindi + son

print("Toq sonlar yig'indisi:", yigindi)

matn = str(yigindi)
teskari = matn 

if matn == teskari:
    print("Bu son palindrom")
else:
    print("Bu son palindrom emas")
