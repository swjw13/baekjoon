import sys
input = sys.stdin.readline
n, k = list(map(int, input().split()))
coins = []
tmp = [sys.maxsize for _ in range(k + 1)]
for _ in range(n):
    coins.append(int(input()))

for i in coins:
    if i < k + 1:
        tmp[i] = 1
    for s in range(1, k - i + 1):
        if tmp[s] != sys.maxsize:
            tmp[s + i] = min(tmp[s + i], tmp[s] + 1)

if tmp[k] >= sys.maxsize:
    print(-1)
else:
    print(tmp[k])
