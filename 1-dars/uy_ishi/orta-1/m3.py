son = int(input("Sonni kiriting: "))

teskari = 0
temp = son

while temp > 0:
    raqam = temp % 10        
    teskari = teskari * 10 + raqam  
    temp = temp // 10     

farq = son - teskari
print("Farq:", farq)
