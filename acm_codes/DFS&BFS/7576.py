from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
mp = []

M, N = list(map(int, input().split()))
for _ in range(N):
    mp.append(list(map(int, input().split())))

dydx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

queue = deque()

for i in range(N):
    for j in range(M):
        if mp[i][j] == 1:
            queue.append((i, j, 0))

day = 0
while queue:
    row, col, depth = queue.popleft()
    day = depth
    for (dx, dy) in dydx:
        x = row + dy
        y = col + dx
        if 0 <= x < N and 0 <= y < M and mp[x][y] == 0:
            queue.append((x, y, depth + 1))
            mp[x][y] = 1

tmp = False
for i in range(N):
    for j in range(M):
        if mp[i][j] == 0:
            tmp = True
        if tmp:
            break
    if tmp:
        break

if tmp:
    print(-1)
else:
    print(day)
