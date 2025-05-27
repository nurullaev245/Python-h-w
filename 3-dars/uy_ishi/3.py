list1 = ['salom', 123, True, 'Hayr', 'world', 3.14, '7214']

TEXT = []
OTHER = []

for item in list1:
    if type(item) == str:
        TEXT.append(item)
    else:
        OTHER.append(item)

TEXT.sort()         
OTHER.sort(reverse=True) 

print("TEXT =", TEXT)
print("OTHER =", OTHER)
