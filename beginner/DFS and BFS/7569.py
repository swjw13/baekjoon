from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

M, N, H = list(map(int, input().split()))
mp = []
for i in range(H):
    tmp = []
    for _ in range(N):
        tmp.append(list(map(int, input().split())))
    mp.append(tmp)

dxdydz = [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

queue = deque()

for i in range(N):
    for j in range(M):
        for k in range(H):
            if mp[k][i][j] == 1:
                queue.append((i, j, k, 0))

day = 0
while queue:
    (a, b, c, depth) = queue.popleft()
    day = depth
    for dx, dy, dz in dxdydz:
        x = a + dx
        y = b + dy
        z = c + dz
        if 0 <= x < N and 0 <= y < M and 0 <= z < H and mp[z][x][y] == 0:
            queue.append((x, y, z, depth + 1))
            mp[z][x][y] = 1

tmp = False
for i in range(N):
    for j in range(M):
        for k in range(H):
            if mp[k][i][j] == 0:
                tmp = True

if tmp:
    print(-1)
else:
    print(day)
