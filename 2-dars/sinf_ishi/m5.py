import random

daraja = 1

while daraja <= 2:
    if daraja == 1:
        boshi = 1
        ohiri = 5
        nomi = "Oson"
    elif daraja == 2:
        boshi = 5
        ohiri = 10
        nomi = "O rta"

    print(f"{nomi} darajasi boshlandi")
    togri_soni = 0

    for i in range(1, 6):
        son = random.randint(boshi, ohiri)
        son1 = random.randint(boshi, ohiri)
        amal = random.choice(["+", "-", "*", "//"])
        if amal == "+":
            natija = son + son1
        elif amal == "-":
            natija = son - son1
        elif amal == "*":
            natija = son * son1
        else:
            if son1 == 0:
                son1 = 1
            natija = son // son1
        fson = int(input(f"{son} {amal} {son1} = "))
        if natija == fson:
            print("togri")
            togri_soni += 1
        else:
            print("xato")

    if togri_soni == 5:
        if daraja < 2:
            print("Siz togri topdingiz, keyingi darajaga otdingiz")
            daraja += 1
        else:
            print("Tabriklaymiz Orta darajani ham muvaffaqiyatli bajardingiz")
            break
    else:
        print("Siz keyingi darajaga otolmadingiz")
        break

