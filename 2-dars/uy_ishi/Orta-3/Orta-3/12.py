son = 10
ustun = 5
qator = son // ustun

for i in range(1, qator + 1):
    for j in range(1, 11):
        for k in range(ustun):
            n = i + k * qator
            if n <= son:
                print(f"{n} * {j} = {n * j}", end="\t")
        print()
    print()
