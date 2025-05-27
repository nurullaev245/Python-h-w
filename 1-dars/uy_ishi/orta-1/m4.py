N = int(input("Nechta Fibonachi soni kerak? N = "))


a = 0
b = 1

print("Fibonachi sonlari:")
for i in range(N):
    print(a)
    c = a + b
    a = b
    b = c
