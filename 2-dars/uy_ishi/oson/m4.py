son = int(input("Sonni kiriting: "))

yigindi = 0
while son > 0:
    raqam = son % 10
    yigindi += raqam
    son //= 10

print("Raqamlar yig'indisi:", yigindi)
