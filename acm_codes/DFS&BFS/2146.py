# 서로 다른 대륙 연결하는 다리의 최소길이 구하기

import sys
from collections import deque

input = sys.stdin.readline
dydx = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N = int(input())
world = []
for _ in range(N):
    world.append(list(map(int, input().split())))

# 각 대륙마다 이름을 다르게 배정함
turn = 2
for i in range(N):
    for j in range(N):
        if world[i][j] == 1:
            queue = deque([(i, j)])
            world[i][j] = turn
            while queue:
                cur_row, cur_col = queue.popleft()
                for dx, dy in dydx:
                    x = cur_row + dx
                    y = cur_col + dy
                    if 0 <= x < N and 0 <= y < N and world[x][y] == 1:
                        queue.append((x, y))
                        world[x][y] = turn
            turn += 1

mn = sys.maxsize

# 각 점마다 바다와 붙어있으면 bfs로 다른 대륙까지의 최소 거리를 찾음.
# 다른 대륙을 만날 때마다 최소값과 비교하여 다리의 최소 길이를 찾아냄
for i in range(N):
    for j in range(N):
        if world[i][j] > 1:
            queue = deque([(i, j, 0, world[i][j])])
            while queue:
                current_row, current_col, distance, start_point = queue.popleft()
                for dx, dy in dydx:
                    x = current_row + dx
                    y = current_col + dy

                    if 0 <= x < N and 0 <= y < N:
                        if world[x][y] >= 1 and world[x][y] != start_point:
                            if -distance < mn:
                                mn = -distance
                        elif world[x][y] == 0 or (world[x][y] < distance - 1):
                            queue.append((x, y, distance - 1, start_point))
                            world[x][y] = distance - 1

print(mn)
