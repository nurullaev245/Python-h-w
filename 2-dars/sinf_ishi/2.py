import random

son1 = random.randint(0, 10)
son2 = random.randint(0, 10)
amal = random.choice(["+", "-", "*", "/"])
print(f"a = {son1}, b = {son2}")
print(f"Amal: {amal}")




if amal == "+":
    natija = son1 + son2
    count = 0
    max_urinish = 3
    while count < max_urinish:
        foydalanuvchi = float(input("Natijani yozing: "))
        count += 1
        if foydalanuvchi == natija:
            print(f"Siz togri topdingiz Urinishlar soni: {count}")
            break
        else:
            print(f"Notog'ri! Qolgan urinishlar: {max_urinish - count}")
    else:
        print("Siz topa olmadingiz. Dastur tugadi.")
elif amal == "-":
    natija = son1 - son2
    count = 0
    max_urinish = 3
    while count < max_urinish:
        foydalanuvchi = float(input("Natijani yozing: "))
        count += 1
        if foydalanuvchi == natija:
            print(f"Siz togri topdingiz Urinishlar soni: {count}")
            break
        else:
            print(f"Notogri Qolgan urinishlar: {max_urinish - count}")
    else:
        print("Siz topa olmadingiz Dastur tugadi")
elif amal == "*":
    natija = son1 * son2
    count = 0
    max_urinish = 3
    while count < max_urinish:
        foydalanuvchi = float(input("Natijani yozing: "))
        count += 1
        if foydalanuvchi == natija:
            print(f"Siz togri topdingiz! Urinishlar soni: {count}")
            break
        else:
            print(f"Notogri Qolgan urinishlar: {max_urinish - count}")
    else:
        print("Siz topa olmadingiz Dastur tugadi")
elif amal == "/":
    if son2 == 0:
        print("Nolga bolish mumkin emas Dastur toxtadi")
    else:
        natija = son1 / son2
        count = 0
        max_urinish = 3
        while count < max_urinish:
            foydalanuvchi = float(input("Natijani yozing: "))
            count += 1
            if foydalanuvchi == natija:
                print(f"Siz togri topdingiz Urinishlar soni: {count}")
                break
            else:
                print(f"Notogri Qolgan urinishlar: {max_urinish - count}")
        else:
            print("Siz topa olmadingiz Dastur tugadi")
else:
    print("Noma'lum amal! Dastur toxtadi")

