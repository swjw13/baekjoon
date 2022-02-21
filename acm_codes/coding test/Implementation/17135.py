# 캐슬 디펜스
# https://www.acmicpc.net/problem/17135

import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
dxdy = [(-1, 0), (0, -1), (1, 0)]

N, M, D = list(map(int, input().split()))
mp_tmp = []
archers = [i for i in range(M)]

max_turn_tmp = 0
for line in range(N):
    lst = list(map(int, input().split()))
    if 1 in lst:
        max_turn_tmp = max(line, max_turn_tmp)
    mp_tmp.append(lst)

ans = 0
for i in combinations(archers, 3):
    mp = [deque() for _ in range(M)]
    for line in mp_tmp:
        for j in range(M):
            mp[j].append(line[j])

    total_enemies = 0
    max_turn = max_turn_tmp

    while max_turn >= 0:
        enemies_to_destroy = set()

        for points in i:
            visited = [[False for _ in range(N)] for _ in range(M)]
            queue = deque([(points, N - 1, 1)])
            visited[points][N - 1] = True
            while queue:
                row, col, turn = queue.popleft()
                if mp[row][col] == 1:
                    enemies_to_destroy.add((row, col))
                    break
                for dx, dy in dxdy:
                    new_row = row + dx
                    new_col = col + dy
                    if 0 <= new_row < M and 0 <= new_col < N and not visited[new_row][new_col] and turn + 1 <= D:
                        queue.append((new_row, new_col, turn + 1))

        total_enemies += len(enemies_to_destroy)
        for row, col in enemies_to_destroy:
            mp[row][col] = 0

        for line in mp:
            line.pop()
            line.appendleft(0)

        max_turn -= 1

    ans = max(ans, total_enemies)

print(ans)
