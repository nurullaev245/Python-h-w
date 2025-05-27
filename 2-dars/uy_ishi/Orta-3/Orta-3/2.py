n = int(input("N sonini kiriting: "))


yigindi = 0
temp = n
while temp > 0:
    yigindi += temp % 10
    temp //= 10


qoldiq = n % yigindi

print(qoldiq)
