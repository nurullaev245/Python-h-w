lst = [1, 2, 33, 5, 6, 7, 7]
target = int(input())

n = len(lst)

for i in range(n - 1):
    for j in range(i + 1, n):
        if lst[i] + lst[j] == target:
            print(f"{i}, {j}")
