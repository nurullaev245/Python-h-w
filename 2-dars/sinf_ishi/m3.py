import random

son1 = 3
son2 = 4

amal = random.choice(["+", "-", "*", "/"])

if amal == "+":
    natija = son1 + son2
elif amal == '-':
    natija = son1 - son2
    
fson = input(f"{son1} {amal} {son2} =")