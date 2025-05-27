mahsulotlar = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

n = len(mahsulotlar)

for i in range(n):
    for j in range(i + 1, n):
        if float(mahsulotlar[i][1]) < float(mahsulotlar[j][1]):
            mahsulotlar[i], mahsulotlar[j] = mahsulotlar[j], mahsulotlar[i]

print(mahsulotlar)
