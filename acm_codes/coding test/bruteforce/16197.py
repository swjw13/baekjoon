# 동전 떨어뜨리기
# https://www.acmicpc.net/problem/16197

import sys
from collections import deque

dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
input = sys.stdin.readline

N, M = list(map(int, input().split()))
mp = [['x' for _ in range(M + 2)]]
coins = []
for i in range(N):
    line = ["x"]
    line += list(input())[:-1]
    line += ['x']
    for j in range(1, M + 1):
        if line[j] == 'o':
            coins.append((i + 1, j))
    mp.append(line)
mp.append(['x' for _ in range(M + 2)])

visited = [[[[False for _ in range(M + 2)] for _ in range(N + 2)] for _ in range(M + 2)] for _ in range(N + 2)]

queue = deque([(coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0)])
visited[coins[0][0]][coins[0][1]][coins[1][0]][coins[1][1]] = True

ans = -1
while queue:
    first_row, first_col, second_row, second_col, turn = queue.popleft()

    if turn > 10:
        continue

    if mp[first_row][first_col] == 'x' or mp[second_row][second_col] == 'x':
        if mp[first_row][first_col] == mp[second_row][second_col]:
            continue
        else:
            ans = turn
            break

    for (dx, dy) in dxdy:
        x1 = first_row
        y1 = first_col
        x2 = second_row
        y2 = second_col
        if mp[first_row + dx][first_col + dy] != '#':
            x1 += dx
            y1 += dy
        if mp[second_row + dx][second_col + dy] != '#':
            x2 += dx
            y2 += dy

        if not visited[x1][y1][x2][y2] and (x1, y1) != (x2, y2):
            queue.append((x1, y1, x2, y2, turn + 1))
            visited[x1][y1][x2][y2] = True

print(ans)
