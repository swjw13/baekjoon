# https://www.acmicpc.net/problem/5427
# 불
import sys
from collections import deque

input = sys.stdin.readline
dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

T = int(input())
for _ in range(T):
    C, R = list(map(int, input().split()))
    board = []
    jihun_point = None
    fire_point = set()

    for i in range(R):
        tmp = list(input().strip())
        if "@" in tmp:
            jihun_point = (i, tmp.index("@"))
        idx = 0
        while "*" in tmp[idx:]:
            where = tmp[idx:].index("*")
            fire_point.add((i, idx + where))
            idx += where + 1
        board.append(tmp)

    visited = [[10000000 for _ in range(C)] for _ in range(R)]
    queue = deque()
    for x, y in fire_point:
        visited[x][y] = 0
        queue.append((x, y))

    while queue:
        fire_x, fire_y = queue.popleft()
        cur_point = visited[fire_x][fire_y]
        for dx, dy in dxdy:
            new_x, new_y = fire_x + dx, fire_y + dy
            if 0 <= new_x < R and 0 <= new_y < C:
                if board[new_x][new_y] != "#" and visited[new_x][new_y] > cur_point + 1:
                    visited[new_x][new_y] = cur_point + 1
                    queue.append((new_x, new_y))

    new_v = [[False for _ in range(C)] for _ in range(R)]
    new_v[jihun_point[0]][jihun_point[1]] = True
    queue = deque([(jihun_point[0], jihun_point[1], 0)])
    ans = False
    tot = -1

    while queue:
        cur_x, cur_y, turn = queue.popleft()
        if (cur_x == 0) or (cur_x == R - 1) or (cur_y == 0) or (cur_y == C - 1):
            tot = turn
            ans = True
            break
        else:
            for dx, dy in dxdy:
                new_x = cur_x + dx
                new_y = cur_y + dy
                if 0 <= new_x < R and 0 <= new_y < C and not new_v[new_x][new_y] and board[new_x][new_y] != "#":
                    if visited[new_x][new_y] > turn + 1:
                        new_v[new_x][new_y] = True
                        queue.append((new_x, new_y, turn + 1))

    if ans:
        print(tot + 1)
    else:
        print("IMPOSSIBLE")

