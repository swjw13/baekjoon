# https://www.acmicpc.net/problem/1956
# 운동
import sys
input = sys.stdin.readline
INF = sys.maxsize

V, E = list(map(int, input().split()))
lines = [[INF for _ in range(V + 1)] for _ in range(V + 1)]
for i in range(1, V + 1):
    lines[i][i] = 0

for _ in range(E):
    start, end, dist = list(map(int, input().split()))
    lines[start][end] = dist

for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            new_dist = lines[i][k] + lines[k][j]
            lines[i][j] = min(lines[i][j], new_dist)

mn = sys.maxsize
for k in range(1, V + 1):
    for i in range(1, V + 1):
        if k != i:
            mn = min(mn, lines[i][k] + lines[k][i])

if mn == sys.maxsize:
    print(-1)
else:
    print(mn)