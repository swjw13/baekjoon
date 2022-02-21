# 로봇 청소기
# https://www.acmicpc.net/problem/4991

import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline
dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while True:
    w, h = list(map(int, input().split()))
    if w == 0 and h == 0:
        break
    mp = []

    for _ in range(h):
        mp.append(list(input())[:-1])

    count = 0
    robot = 0
    for i in range(h):
        for j in range(w):
            if mp[i][j] == '*':
                mp[i][j] = str(count)
                count += 1
            elif mp[i][j] == 'o':
                robot = count
                mp[i][j] = str(count)
                count += 1

    line = [[-1 for _ in range(count)] for _ in range(count)]


    def bfs(start_row, start_col, point_num):
        visited = [[False for _ in range(w)] for _ in range(h)]
        queue = deque([(start_row, start_col, 0)])
        visited[start_row][start_col] = True
        while queue:
            cur_row, cur_col, turn = queue.popleft()
            if mp[cur_row][cur_col] not in ['x', '.']:
                line[point_num][int(mp[cur_row][cur_col])] = turn

            for dx, dy in dxdy:
                new_row = cur_row + dx
                new_col = cur_col + dy
                if 0 <= new_row < h and 0 <= new_col < w and not visited[new_row][new_col]:
                    if mp[new_row][new_col] != 'x':
                        queue.append((new_row, new_col, turn + 1))
                        visited[new_row][new_col] = True


    for i in range(h):
        for j in range(w):
            if mp[i][j] not in ['x', '.']:
                bfs(i, j, int(mp[i][j]))

    points = {i for i in range(count)} - {robot}
    mn = sys.maxsize
    is_reachable = True
    for i in line:
        if -1 in i:
            is_reachable = False
            break

    if not is_reachable:
        print(-1)
    else:
        for i in permutations(points):
            dist = 0
            start_index = robot
            for index in range(count - 1):
                dist += line[start_index][i[index]]
                start_index = i[index]
            mn = min(mn, dist)
        print(mn)
