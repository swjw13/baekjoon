lst = [0 for i in range(1000001)]
lst[2] = 1
lst[3] = 1
for i in range(4, 1000001):
    tmp = lst[i - 1]
    if i % 2 == 0:
        tmp = min(tmp, lst[i // 2])
    if i % 3 == 0:
        tmp = min(tmp, lst[i // 3])
    lst[i] = tmp + 1

N = int(input())
print(lst[N])
