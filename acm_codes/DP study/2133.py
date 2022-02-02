n = int(input())
lst = [0 for _ in range(n + 1)]
lst[2] = 3

for i in range(2, n + 1, 2):
    for j in range(2, i, 2):
        lst[i] += lst[j] * lst[i - j]
        lst[i] += 1

print(lst[n])