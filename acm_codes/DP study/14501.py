N = int(input())
cost = []
for _ in range(N):
    cost.append(list(map(int, input().split())))

lst = [0 for _ in range(N + 1)]
for j in range(N - 1, -1, -1):
    tmp = lst[j + 1]
    if cost[j][0] + j <= N:
        tmp = max(tmp, cost[j][1] + lst[cost[j][0] + j])
    lst[j] = tmp

print(lst[0])