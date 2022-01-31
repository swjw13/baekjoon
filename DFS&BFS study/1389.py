import sys
input = sys.stdin.readline
INF = 10**6

N, M = list(map(int, input().split()))
friend = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    start, end = list(map(int, input().split()))
    friend[start][end] = 1
    friend[end][start] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            friend[i][j] = min(friend[i][j], friend[i][k] + friend[k][j])

min = sys.maxsize
min_index = -1
for i in range(1, N + 1):
    lst = friend[i]
    tmp = sum(lst) - lst[0] - lst[i]
    if tmp < min:
        min_index = i
        min = tmp

print(min_index)
