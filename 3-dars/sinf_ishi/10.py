import random

sonlar = []
for i in range(20):
    son = random.randint(1, 100)
    sonlar.append(son)

print("Tasodifiy sonlar:", sonlar)
ortacha = sum(sonlar) / len(sonlar)
print("Ortalama qiymat:", ortacha)
