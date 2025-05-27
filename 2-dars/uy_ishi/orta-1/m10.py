
A = int(input("A = "))
B = int(input("B = "))


soni = 0
qoldiq = A

while qoldiq >= B:
    qoldiq -= B
    soni += 1


print("A kesmada", soni, "ta B bor")
print("Bosh qismi", qoldiq)
