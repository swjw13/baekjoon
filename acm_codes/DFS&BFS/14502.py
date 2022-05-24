# 연구소
# https://www.acmicpc.net/problem/14502

from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline
points = []
mp = []
dydx = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, M = list(map(int, input().split()))
for i in range(N):
    for j in range(M):
        points.append((i, j))

for_indexing = [i for i in range(N * M)]
mp_for_bfs = [[0 for _ in range(M)] for _ in range(N)]

mx = -1

for _ in range(N):
    mp.append(list(map(int, input().split())))

for (one, two, three) in combinations(for_indexing, 3):

    point_one = points[one]
    point_two = points[two]
    point_three = points[three]

    if mp[point_one[0]][point_one[1]] != 0 or \
            mp[point_two[0]][point_two[1]] != 0 or \
            mp[point_three[0]][point_three[1]] != 0:
        continue
    else:
        mp[points[one][0]][points[one][1]] = 1
        mp[points[two][0]][points[two][1]] = 1
        mp[points[three][0]][points[three][1]] = 1

    for i in range(N):
        for j in range(M):
            mp_for_bfs[i][j] = mp[i][j]

    ans = 0
    for i in range(N):
        for j in range(M):
            if mp_for_bfs[i][j] == 2:
                queue = deque([(i, j)])
                ans += 1
                while queue:
                    current_row, current_col = queue.popleft()
                    for (dx, dy) in dydx:
                        new_x = current_row + dx
                        new_y = current_col + dy
                        if 0 <= new_x < N and 0 <= new_y < M and mp_for_bfs[new_x][new_y] == 0:
                            queue.append((new_x, new_y))
                            mp_for_bfs[new_x][new_y] = 3
                            ans += 1
            elif mp_for_bfs[i][j] == 1:
                ans += 1

    mx = max(mx, M * N - ans)

    mp[points[one][0]][points[one][1]] = 0
    mp[points[two][0]][points[two][1]] = 0
    mp[points[three][0]][points[three][1]] = 0

print(mx)
