i = int(input("Iltimos, 3 xonali son kiriting: "))

ikkihonali = (i >= 100 and i <= 10000)

print(i, "- bu 3 xonali son." if ikkihonali else i, "- bu 3 xonali son emas." if i-1 % 2 == 0 else  "Toq son")
