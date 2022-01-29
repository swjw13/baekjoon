N = int(input())
lst = [1 for _ in range(10)]

for _ in range(N - 1):
    for i in range(9, -1, -1):
        lst[i] = sum(lst[:(i + 1)])

print(sum(lst) % 10007)