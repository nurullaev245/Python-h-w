data = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
natija = ()

for a, b, c in data:
    yengi = (a, b, 100)
    natija = natija + (yengi,)

print(natija)
