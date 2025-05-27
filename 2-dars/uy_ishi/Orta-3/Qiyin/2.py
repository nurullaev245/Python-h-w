n = int(input("Input: "))
yigindi = 0

for i in range(1, n + 1):
    if n % i == 0:
        yigindi += i

if yigindi > 999:
    print("Ilojsiz")
else:
    birlik = ["", "bir", "ikki", "uch", "tort", "besh", "olti", "yetti", "sakkiz", "toqqiz"]
    onlik = ["", "on", "yigirma", "ottiz", "qirq", "ellik", "oltmish", "yetmish", "sakson", "toqson"]
    yuzlik = ["", "yuz", "ikki yuz", "uch yuz", "tort yuz", "besh yuz", "olti yuz", "yetti yuz", "sakkiz yuz", "toqqiz yuz"]

    yuz = yigindi // 100
    on = (yigindi % 100) // 10
    bir = yigindi % 10

    matn = ""
    if yuz:
        matn += yuzlik[yuz] + " "
    if on:
        matn += onlik[on] + " "
    if bir:
        matn += birlik[bir]

    print("Output:", matn)
