N = int(input("Boshlang'ich qiymat = "))
M = int(input("Oxirgi qiymat  = "))
K = int(input("Nechta Fibonachi soni kerak  = "))


a = 0
b = 1
count = 0

print("Natija:")
while count < K:
    if a >= N and a <= M:
        print(a)
        count += 1
    c = a + b
    a = b
    b = c

    if a > M and count < K:
        print("Berilgan oraliqda yetarli Fibonachi soni yo'q.")
        break
