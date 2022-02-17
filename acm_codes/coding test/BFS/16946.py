# 벽 부수고 이동하기
# https://www.acmicpc.net/problem/16946

import sys
from collections import deque

input = sys.stdin.readline
dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, M = list(map(int, input().split()))
mp = []
scale_per_bfs = {1: 0}

for _ in range(N):
    mp.append(list(map(int, list(input())[:-1])))

numbering = 2

for i in range(N):
    for j in range(M):
        if mp[i][j] == 0:
            count = 1
            queue = deque([(i, j)])
            mp[i][j] = numbering
            while queue:
                current_row, current_col = queue.popleft()
                for dx, dy in dxdy:
                    x = current_row + dx
                    y = current_col + dy
                    if 0 <= x < N and 0 <= y < M and mp[x][y] == 0:
                        queue.append((x, y))
                        mp[x][y] = numbering
                        count += 1
            scale_per_bfs[numbering] = count
            numbering += 1

for i in range(N):
    for j in range(M):
        count = 0
        if mp[i][j] == 1:
            tmp = set()
            for (dx, dy) in dxdy:
                x = i + dx
                y = j + dy
                if 0 <= x < N and 0 <= y < M:
                    tmp.add(mp[x][y])
            for s in tmp:
                count += scale_per_bfs[s]
            count += 1
        print(count % 10, end='')
    print()
