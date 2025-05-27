print("Raqamlarida kamida bitta 3 bo'lgan uch xonali ilar:")

for i in range(100, 1000):
    birlik = i % 10
    onlik = (i // 10) % 10
    yuzlik = i // 100

    if birlik == 3 or onlik == 3 or yuzlik == 3:
        print(i)
