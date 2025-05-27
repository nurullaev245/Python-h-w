import random

son = random.randint(0, 10)
son2 = random.randint(0, 10)
print(f"a={son} b={son2}")

fson = int(input("Ikkita tasodifiy son yigindisi yozing:"))

son += son2
if fson == son and son2:
    print("Siz tori topdingiz ")
else:
    print("siz notogri topdingiz")