n = int(input("Natural son kiriting: "))

print("Bo'luvchilari:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
