n = int(input())

lst = [1 for i in range(n + 1)]
for i in range(2, n + 1):
    lst[i] = lst[i - 1] + lst[i - 2]
    lst[i] %= 10007

print(lst[n])