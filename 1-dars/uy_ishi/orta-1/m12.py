son = input("Butun sonni kiriting: ")

for i in range(len(son) - 1):
    if son[i] == son[i + 1]:
        print("Bor.")
        break
else:
    print("Yo'q.")
