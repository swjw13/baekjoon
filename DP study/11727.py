n = int(input())

lst = [1 for _ in range(n + 1)]
for i in range(2, n + 1):
    if i % 2 == 0:
        lst[i] = (2 * lst[i - 1] + 1) % 10007
    else:
        lst[i] = (2 * lst[i - 1] - 1) % 10007

print(lst[n])
