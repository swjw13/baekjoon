N = int(input())
INF = 1e9
lst = [INF] * 5001

lst[3] = 1
lst[4] = INF
lst[5] = 1

for i in range(6, N + 1):
    lst[i] = min(lst[i - 3] + 1, lst[i - 5] + 1)

if lst[N] >= INF:
    print(-1)
else:
    print(lst[N])
